from sqlalchemy import Column, Integer, String, Text
from database import Base

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String, nullable=False)
    result = Column(Text, nullable=False)