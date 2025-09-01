import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Dify API Endpoint (adjust if needed)
API_URL = "https://api.dify.ai/v1/chat-messages"

# Streamlit UI
st.set_page_config(page_title="Dify AI Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Dify AI Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Prepare request
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": {},
        "query": user_input,
        "response_mode": "blocking",
        "conversation_id": "",
        "user": "user1"
    }

    try:
        # Send request to Dify API
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()

        # Extract bot reply
        bot_reply = response.json().get("answer", "⚠️ No reply from API")
        st.chat_message("assistant").markdown(bot_reply)

        # Save bot reply to session
        st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

    except requests.exceptions.RequestException as e:
        st.error(f"❌ API Error: {e}")
