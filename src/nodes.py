from typing import Dict, Any
from src.state import QAState
import pandas as pd
from langchain_core.documents import Document
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Nodes:
    @staticmethod
    def process_document(state: QAState) -> Dict[str, Any]:
        """
        Process an Excel file and extract text
        """
        try:
            # Check if file is Excel
            if not state["file_path"].endswith(('.xlsx', '.xls')):
                raise ValueError("Only Excel files (.xlsx, .xls) are supported.")
            
            # Load Excel file (all sheets)
            xl = pd.read_excel(state["file_path"], sheet_name=None)
            
            # Extract text from all sheets
            docs = []
            processed_text = ""
            for sheet_name, df in xl.items():
                # Convert DataFrame to string with sheet name
                sheet_content = f"Sheet: {sheet_name}\n{df.to_string()}\n\n"
                processed_text += sheet_content
                # Create a Document object for each sheet (optional, for consistency with original)
                docs.append(Document(page_content=sheet_content))
            
            return {
                "documents": docs,
                "processed_text": processed_text
            }
        except Exception as e:
            print(f"Error processing Excel file: {e}")
            return {"documents": [], "processed_text": ""}

    @staticmethod
    def answer_question(state: QAState) -> Dict[str, Any]:
        """
        Generate an answer based on processed document and question
        """
        try:
            # Initialize Groq language model
            llm = ChatGroq(model="llama-3.1-8b-instant")  # Adjust model name as needed
            
            # Create prompt template
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful assistant that answers questions based on the given context."),
                ("human", "Context: {context}\n\nQuestion: {question}\n\nAnswer the question using only the provided context."),
            ])
            
            # Create chain
            chain = prompt | llm
            
            # Generate answer
            response = chain.invoke({
                "context": state.get("processed_text", ""),
                "question": state["question"]
            })
            
            return {"answer": response.content}
        except Exception as e:
            print(f"Error generating answer: {e}")
            return {"answer": "Could not generate an answer."}
