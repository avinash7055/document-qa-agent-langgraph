from src.graph import build_qa_graph
from src.state import QAState

class DocumentQAAgent:
    def __init__(self):
        # Compile the graph only once during initialization
        self.graph = build_qa_graph()

    def run(self, file_path: str, question: str) -> str:
        # Create initial state with required fields
        initial_state = {
            "file_path": file_path,
            "question": question
        }
        
        # Use invoke method with config
        config = {"recursion_limit": 50}  # Optional: set recursion limit
        result = self.graph.invoke(initial_state, config)
        
        return result.get("answer", "No answer could be generated.")

if __name__ == "__main__":
    try:
        agent = DocumentQAAgent()
        answer = agent.run(
            file_path="data/uploaded_docs/sample.xlsx",  # Changed to .xlsx
            question="What is the total value in column X?"  # Example question for Excel
        )
        print(f"Answer: {answer}")
    except Exception as e:
        print(f"An error occurred: {e}")