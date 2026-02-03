# policy_ragchatbot
Internal policy rag chatbot
An internal **Policy Question-Answering chatbot** built using **Retrieval-Augmented Generation (RAG)**.  
The system allows employees to ask questions about company policies (leave, WFH, holidays, reimbursements, etc.) and get accurate answers grounded in internal documents.
## Features
- Ask natural language questions about internal policies
- Uses RAG to avoid hallucinations
- FastAPI backend with Swagger UI
- FAISS-based vector search
- Modular and scalable architecture
## Tech Stack
Backend: FastAPI
LLM Orchestration: LangChain
Vector Store: FAISS
Embeddings: HuggingFace / Google GenAI
Language Model: Gemini
API Docs: Swagger (OpenAPI)
## Architecture (RAG Flow)
1. Policy documents are loaded from text files
2. Documents are chunked and embedded
3. Embeddings are stored in FAISS
4. User query is embedded
5. Relevant chunks are retrieved
6. LLM generates an answer grounded in retrieved content
## clone the code using the:  git clone https://github.com/rajeswariC2697/policy_ragchatbot.git

## Create an Virtual  environment:
python -m venv .venv
.venv\Scripts\activate   # Windows

python -m venv .venv
source .venv/bin/activate #macos

## Install the dependencies 
pip install -r requirements.txt
## start the server
 python main.py
##  I bind to `127.0.0.1` for local development. 
 For deployment or Docker, I bind to `0.0.0.0` so the service is reachable externally.
 

