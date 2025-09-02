import streamlit as st
import requests

# -------------------------------
# SETTINGS
# Replace with your actual API key from Dify
API_KEY = "Bearer app-NCP7hdzl43aab5JPGYz5UmLy"
API_URL = "https://api.dify.ai/v1/chat-messages"
# -------------------------------

st.title("🩺 Doc Bot - AI Doctor Assistant")

# Input box for user question
user_input = st.text_input("Describe your symptoms or ask a medical question:")

if st.button("Ask Doc Bot"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        headers = {
            "Authorization": API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "inputs": {},
            "query": user_input,
            "response_mode": "blocking",
            "conversation_id": "",
            "user": "user123"
        }

        # Send request to Dify API
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            if response.status_code == 200:
                bot_reply = response.json()["answer"]
                st.success(bot_reply)
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")


