from typing import TypedDict, Optional, List
from langchain_core.documents import Document

class QAState(TypedDict):
    file_path: str
    question: str
    processed_text: Optional[str] = None
    answer: Optional[str] = None
    documents: Optional[List[Document]] = None
