from langgraph.graph import StateGraph, END
from src.nodes import Nodes
from src.state import QAState

def build_qa_graph():
    workflow = StateGraph(QAState)
    
    # Define nodes
    workflow.add_node("process_doc", Nodes.process_document)
    workflow.add_node("answer_q", Nodes.answer_question)
    
    # Define edges
    workflow.add_edge("process_doc", "answer_q")
    workflow.add_edge("answer_q", END)
    
    # Set entry point
    workflow.set_entry_point("process_doc")
    
    # Compile the graph
    return workflow.compile()