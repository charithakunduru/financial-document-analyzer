import os
from dotenv import load_dotenv
load_dotenv()
from crewai.tools import tool
from langchain_community.document_loaders import PyPDFLoader

@tool
def read_data_tool(path: str = 'data/sample.pdf') -> str:
    """Tool to read data from a pdf file from a path.

    Args:
        path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

    Returns:
        str: Full Financial Document file
    """
    try:
        docs = PyPDFLoader(file_path=path).load()
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

    full_report = ""
    for data in docs:
        content = data.page_content
        while "\n\n" in content:
            content = content.replace("\n\n", "\n")
        full_report += content + "\n"

    return full_report


@tool
def analyze_investment_tool(financial_document_data: str) -> str:
    """Tool to analyze investment data from financial document text.

    Args:
        financial_document_data (str): Raw text from financial document.

    Returns:
        str: Processed investment analysis data
    """
    processed_data = financial_document_data
    i = 0
    while i < len(processed_data):
        if processed_data[i:i+2] == "  ":
            processed_data = processed_data[:i] + processed_data[i+1:]
        else:
            i += 1
    return processed_data


@tool
def create_risk_assessment_tool(financial_document_data: str) -> str:
    """Tool to create risk assessment from financial document text.

    Args:
        financial_document_data (str): Raw text from financial document.

    Returns:
        str: Risk assessment data
    """
    return financial_document_data
