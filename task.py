from crewai import Task
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import read_data_tool


analyze_financial_document = Task(
    description=(
        "Thoroughly read and analyze the financial document located at the provided file path: {file_path}. "
        "Focus on answering the user's specific query: {query}\n"
        "Extract and summarize key financial metrics including revenue, net income, EPS, "
        "cash flow, debt levels, and any forward-looking guidance. "
        "Identify major business segments, geographic performance, and year-over-year trends. "
        "Use only data directly sourced from the document — do not fabricate any figures."
    ),
    expected_output=(
        "A structured financial summary containing:\n"
        "1. Key financial metrics with exact figures from the document\n"
        "2. Year-over-year performance comparison\n"
        "3. Business segment breakdown\n"
        "4. Management commentary highlights\n"
        "5. A direct answer to the user's query: {query}\n"
        "All figures must be cited directly from the financial document."
    ),
    agent=financial_analyst,
    tools=[read_data_tool],
    async_execution=False,
)

investment_analysis = Task(
    description=(
        "Based on the verified financial data extracted from the document at {file_path}, conduct a thorough "
        "investment analysis in response to the user query: {query}\n"
        "Evaluate valuation metrics (P/E, P/S, EV/EBITDA if available), growth trajectory, "
        "competitive positioning, and capital allocation strategy. "
        "Provide investment recommendations grounded strictly in the document data. "
        "Clearly state assumptions and distinguish between facts and interpretations."
    ),
    expected_output=(
        "A professional investment analysis report including:\n"
        "1. Valuation assessment based on reported financials\n"
        "2. Growth outlook supported by documented figures\n"
        "3. Bull case and bear case scenarios with factual backing\n"
        "4. Specific investment recommendations for different risk profiles\n"
        "5. Key metrics to monitor going forward\n"
        "All recommendations must reference specific data points from the financial document."
    ),
    agent=investment_advisor,
    tools=[read_data_tool],
    async_execution=False,
)

risk_assessment = Task(
    description=(
        "Conduct a balanced and evidence-based risk assessment of the company based on the "
        "financial document at {file_path}, in the context of the user query: {query}\n"
        "Identify genuine risk factors including liquidity risk, market risk, operational risk, "
        "and regulatory risk as evidenced by the financial data. "
        "Use standard risk frameworks and base all findings strictly on documented figures."
    ),
    expected_output=(
        "A comprehensive risk assessment report including:\n"
        "1. Key risk factors identified from the financial statements\n"
        "2. Quantified risk exposure where data is available\n"
        "3. Risk mitigation strategies currently employed by the company\n"
        "4. Overall risk rating (Low / Medium / High) with justification\n"
        "5. Recommendations for risk-aware investors\n"
        "All risk factors must be supported by specific data from the financial document."
    ),
    agent=risk_assessor,
    tools=[read_data_tool],
    async_execution=False,
)

verification = Task(
    description=(
        "Verify that the uploaded file at {file_path} is a legitimate financial document. "
        "Check for the presence of standard financial statement components: "
        "income statement, balance sheet, cash flow statement, and notes/disclosures. "
        "Confirm that the document contains real numerical financial data and is not "
        "a non-financial file (e.g., marketing material, grocery list, unrelated report)."
    ),
    expected_output=(
        "A verification report stating:\n"
        "1. Document type confirmed (e.g., quarterly earnings report, annual report)\n"
        "2. Financial statements present: Yes/No for each (Income, Balance Sheet, Cash Flow)\n"
        "3. Reporting period and company name identified\n"
        "4. Data quality assessment (complete / partial / insufficient)\n"
        "5. Verified: Yes/No — with clear reasoning\n"
        "Base all conclusions strictly on the actual content of the document."
    ),
    agent=verifier,
    tools=[read_data_tool],
    async_execution=False
)
