import streamlit as st
import requests
from langdetect import detect

API_KEY = st.secrets["API_KEY"]
API_URL = "https://api.dify.ai/v1/chat-messages"

st.title("🩺 Doc Bot - AI Doctor Assistant")

user_input = st.text_input("Describe your symptoms or ask a medical question:")

if st.button("Ask Doc Bot"):
    if not user_input.strip():
        st.warning("Please enter a question.")
    else:
        # 🔎 Detect language of input
        try:
            lang = detect(user_input)
        except:
            lang = "unknown"

        st.write(f"📝 Detected language: {lang}")

        headers = {
            "Authorization": f"Bearer {API_KEY}",  # ✅ correct format
            "Content-Type": "application/json"
        }

        # Pass language as input metadata to Dify
        payload = {
            "inputs": {"lang": lang},  
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
