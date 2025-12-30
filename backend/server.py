from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import Optional, List, Dict
import json
import uuid
from pathlib import Path

load_dotenv(override=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def load_personality():
    try:
        with open("me.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return "You are a helpful digital twin."

model = genai.GenerativeModel(
    model_name='gemini-2.5-flash-lite',
    system_instruction=load_personality()
)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MEMORY_DIR = Path("../memory")
MEMORY_DIR.mkdir(exist_ok=True)

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    session_id: str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        session_id = request.session_id or str(uuid.uuid4())
        
        # load history
        file_path = MEMORY_DIR / f"{session_id}.json"
        history = []
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                history = json.load(f)

        gemini_history = []
        for msg in history:
            role = "model" if msg["role"] == "assistant" else "user"
            gemini_history.append({"role": role, "parts": [msg["content"]]})

        # create chat session
        chat_session = model.start_chat(history=gemini_history)
        
        # send response message 
        response = chat_session.send_message(request.message)
        ai_text = response.text
        
        # save history
        history.append({"role": "user", "content": request.message})
        history.append({"role": "assistant", "content": ai_text})
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
            
        return ChatResponse(response=ai_text, session_id=session_id)

    except Exception as e:
        print(f"Error details: {str(e)}") 
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)