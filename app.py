import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.dify.ai/v1/chat-messages"

st.title("🩺 Doc Bot - AI Doctor Assistant")

user_input = st.text_input("Describe your symptoms or ask a medical question:")

if st.button("Ask Doc Bot"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        headers = {
    "Authorization": f"Bearer {API_KEY}",  # ✅ correct format
    "Content-Type": "application/json"
}

        payload = {
            "inputs": {},
            "query": user_input,
            "response_mode": "blocking",
            "conversation_id": "",
            "user": "user123"
        }
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            if response.status_code == 200:
                bot_reply = response.json().get("answer", "No reply received.")
                st.success(bot_reply)
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")

