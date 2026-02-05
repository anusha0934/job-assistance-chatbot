import streamlit as st
import os
from chatbot import get_response


# Train model if not already trained (for cloud deployment)
if not os.path.exists("model.pkl"):
    os.system("python train.py")

st.set_page_config(page_title="Job Assistance Chatbot", page_icon="🤖")

st.title("🤖 Job Assistance Chatbot")
st.write("Ask me about resumes, interviews, skills, and jobs!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)