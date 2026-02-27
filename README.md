# Financial Document Analyzer

A FastAPI-based backend system that analyzes financial documents using CrewAI multi-agent AI and LLM models.

## Project Overview

This system processes corporate reports, financial statements, and investment documents using specialized AI agents that work together to provide comprehensive financial analysis.

## Features

- Upload financial documents (PDF format)
- AI-powered financial analysis using multi-agent CrewAI system
- Investment recommendations based on document data
- Risk assessment and market insights
- Secure API key management using `.env`
- Clean RESTful API with FastAPI

## Technologies Used

- **FastAPI** — Web framework and REST API
- **CrewAI** — Multi-agent AI orchestration
- **LiteLLM** — LLM provider abstraction
- **OpenAI GPT-4o-mini** — Primary LLM (requires paid account)
- **Google Gemini** — Alternative free LLM option
- **LangChain** — Document loading and processing
- **PyPDF** — PDF text extraction
- **Uvicorn** — ASGI server
- **Python 3.10+**

## Project Structure

financial-document-analyzer/
├── main.py          # FastAPI app and endpoints
├── agents.py        # CrewAI agent definitions
├── task.py          # CrewAI task definitions
├── tools.py         # PDF reader and analysis tools
├── requirements.txt # Python dependencies
├── .env             # API keys (not committed to git)
└── data/            # Uploaded documents (temporary)
|___database.py      # SQLite to store analysis      results
## Agents
    |  Agent |       :    | Role |
  *Financial Analyst: Extracts and analyzes key financial metrics 
 *Document Verifier: Validates document is a legitimate financial report 
 *Investment Advisor: Provides investment recommendations 
 *Risk Assessor: Identifies and quantifies risk factors 

## Getting Started

### 1. Install dependencies
pip install -r requirements.txt

### 2. Create `.env` file

# For OpenAI (paid)
OPENAI_API_KEY=sk-your-key-here
# OR for Gemini (free)
GEMINI_API_KEY=AIzaSy-your-key-here

### 3. Add sample document
Download Tesla Q2 2025 financial update:
https://www.tesla.com/sites/default/files/downloads/TSLA-Q2-2025-Update.pdf
Save as `data/sample.pdf`

### 4. Run the server
python -m uvicorn main:app --reload
### 5. Open API docs
http://localhost:8000/docs
## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health check |
| POST | `/analyze` | Upload PDF and analyze |
## Usage Example
1. Open `http://localhost:8000/docs`
2. Click **POST /analyze → Try it out**
3. Upload a financial PDF
4. Enter a query e.g. `"Summarize revenue and risk factors"`
5. Click **Execute**
6. View the AI-generated analysis
## Bugs Fixed

1) Incorrect API Key Error
    # Problem:
      litellm.AuthenticationError: Incorrect API key provided
      # Solution:
          *Added load_dotenv() at top of  main.py  
          *Ensured LLM loads API key using:
api_key=os.getenv("OPENAI_API_KEY")
3) # .env Not Detected
    # Problem:
      Application still used default API key:
      # Solution:
        *Verified working directory using pwd
        *Ensured .env is inside project root
        *Restarted server after changes
4) # Database Integration
       Improvement Added:
         *Implemented SQLite database
         *Created ORM models using SQLAlchemy
         *Auto-created tables on app startup
         *Added endpoint to retrieve stored results


## Notes
- OpenAI requires a paid account with credits
- Gemini free tier has daily quota limits — if you hit the limit, wait 24 hours
- Uploaded files are automatically deleted after analysis