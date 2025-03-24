# import streamlit as st
# from src.main import DocumentQAAgent
# import os

# # Initialize the agent
# agent = DocumentQAAgent()

# # Streamlit UI
# st.title("Document QA Agent")
# st.write("Upload an Excel file (.xlsx) and ask a question about its content.")

# # File upload section
# uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

# # Question input
# question = st.text_input("Enter your question", "What is it about?")

# # Process and display results
# if uploaded_file is not None and question:
#     # Save the uploaded file temporarily
#     file_path = os.path.join("data/uploaded_docs", uploaded_file.name)
#     os.makedirs("data/uploaded_docs", exist_ok=True)  # Ensure directory exists
    
#     with open(file_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())
    
#     # Display uploaded file details
#     st.write(f"Uploaded file: {uploaded_file.name}")
    
#     # Run the agent
#     with st.spinner("Processing document and generating answer..."):
#         try:
#             answer = agent.run(file_path, question)
#             st.success("Answer generated successfully!")
#             st.write("**Question:**", question)
#             st.write("**Answer:**", answer)
#         except Exception as e:
#             st.error(f"An error occurred: {e}")
# else:
#     st.info("Please upload a file and enter a question to get started.")
# app.py
import streamlit as st
from src.main import DocumentQAAgent  # Assuming this is where your agent is defined
import os

# Initialize the agent
if "agent" not in st.session_state:
    st.session_state.agent = DocumentQAAgent()

# Streamlit UI
st.title("Document QA Chatbot")
st.write("Upload an Excel file (.xlsx) and chat with the agent about its content.")

# File upload section (in sidebar for cleaner UI)
with st.sidebar:
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"], key="file_uploader")
    if uploaded_file:
        # Save the uploaded file temporarily
        file_path = os.path.join("data/uploaded_docs", uploaded_file.name)
        os.makedirs("data/uploaded_docs", exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Uploaded: {uploaded_file.name}")
        st.session_state.file_path = file_path
    else:
        st.info("Upload a file to start chatting.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if "file_path" in st.session_state:
    prompt = st.chat_input("Ask a question about the document...")
    if prompt:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message immediately
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Run the agent and get the answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    answer = st.session_state.agent.run(st.session_state.file_path, prompt)
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})
else:
    with st.chat_message("assistant"):
        st.markdown("Please upload an Excel file to start chatting.")

# Optional: Clear chat history button
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()