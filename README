# AI Digital Twin - Production-Ready Conversational AI

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-623CE4?style=for-the-badge&logo=terraform&logoColor=white)

Welcome to the **AI Digital Twin** project! This repository provides production-ready source code and Infrastructure-as-Code (IaC) for building a personalized conversational AI digital twin, deployed with a secure, serverless, cloud-native architecture on AWS.

## 🎥 Project Demonstration

Check out the AI Digital Twin in action: [Link to Video Demo](https://example.com) — replace with your video link (YouTube, Loom, Google Drive, etc.).

### Show the demo video and system image locally
- Place your demo video as `demo.mp4` and a poster image `image.svg` into the `frontend/public/` folder.
- The Next.js frontend serves `public/` files at the site root, so the video will be accessible at `/demo.mp4` and the image at `/image.svg`.
- If the UI supports embedding media in messages, reference those URLs (for example, `<video src="/demo.mp4" poster="/image.svg" controls />`).

## 🏗️ System Architecture

The architecture evolves from a local FastAPI development setup to a fully automated, secure, and serverless AWS deployment.

🛠️ Tech Stack

- Frontend
	- Next.js (App Router): Modern React framework for the chat interface.
	- Tailwind CSS: Utility-first CSS for responsive, beautiful UI.

- Backend
	- FastAPI: High-performance Python framework for AI logic.
	- AWS Lambda & API Gateway: Serverless execution and API management.
	- Pydantic: Data validation and settings management.

- AI & Data
	- AWS Bedrock with Amazon Nova Models: Enterprise-grade LLMs for conversational responses (e.g., Nova 2 Lite/Pro).
	- S3 Persistence: JSON-based conversation history storage.

- DevOps & Infrastructure
	- Terraform: IaC for multi-environment (dev/test/prod) management.
	- GitHub Actions: CI/CD pipeline with OIDC authentication.
	- LocalStack: Local AWS emulation for development and testing.

🚀 Getting Started

### Prerequisites

- Python 3.9+ (or newer)
- Node.js 18+
- Terraform ≥ 1.5
- Docker (for LocalStack testing)
- AWS account with appropriate permissions

### Local Development

Clone the repository:

```bash
git clone <your-repo-url>
cd twin
```

Backend setup (example):

```bash
cd backend
pip install -r requirements.txt
# Run the FastAPI dev server (adjust module:path if different):
uvicorn server:app --reload
```

Frontend setup:

```bash
cd frontend
npm install
npm run dev
# Visit http://localhost:3000 to view the app
```

### Deployment with Terraform

```bash
cd terraform
terraform workspace select dev   # or test/prod
terraform apply -var-file="dev.tfvars"
```

🛡️ Security Features

- OIDC Authentication: No long-lived AWS keys in GitHub secrets.
- Bedrock Guardrails: Built-in content filtering for safe interactions.
- KMS Encryption: All data at rest encrypted with customer-managed keys.
- Least-Privilege IAM: Strict role policies.
- WAF & Rate Limiting: Protection against common web attacks.
- CloudTrail & CloudWatch: Full monitoring and auditing.

🤝 Contributing

Contributions are welcome! Please open an issue first to discuss major changes.