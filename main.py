from dotenv import load_dotenv
import os
load_dotenv()
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import uuid
from crewai import Crew, Process,LLM,Agent
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from task import analyze_financial_document, investment_analysis, risk_assessment, verification
from database import engine
from models import Base

Base.metadata.create_all(bind=engine)
llm = LLM(
    model="gpt-4o-mini",
    api_key=os.environ.get("OPENAI_API_KEY")
)
os.environ["CREWAI_TELEMETRY"] = "false"
app = FastAPI(title="Financial Document Analyzer")

def run_crew(query: str, file_path: str):
    financial_crew = Crew(
        agents=[financial_analyst, verifier, investment_advisor, risk_assessor],
        tasks=[verification, analyze_financial_document, investment_analysis, risk_assessment],
        process=Process.sequential,
    )
    result = financial_crew.kickoff(inputs={"query": query, "file_path": file_path})
    return result

@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}

@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"
    try:
        os.makedirs("data", exist_ok=True)
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        if not query.strip():
            query = "Analyze this financial document for investment insights"
        result = run_crew(query=query.strip(), file_path=file_path)
        return {"status": "success", "query": query, "analysis": str(result), "file_processed": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing financial document: {str(e)}")
    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
