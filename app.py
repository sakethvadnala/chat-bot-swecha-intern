import streamlit as st
import requests

st.set_page_config(page_title="Doc Bot", page_icon="🤖", layout="centered")

st.title("🤖 Doc Bot - Your Health Assistant")
st.write("Ask me anything about your symptoms and I’ll give you doctor-style suggestions.")

# Your Dify API key and URL
API_KEY = "Authorization: Bearer {API_KEY}"  # <-- Replace with your Dify App API Key
API_URL = "https://api.dify.ai/v1"

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Doc Bot:** {msg['content']}")

# Input field
user_input = st.text_input("💬 Ask Doc Bot anything:", key="input")

if st.button("Send") and user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f"**You:** {user_input}")

    try:
        payload = {
            "inputs": {},
            "query": user_input,
            "response_mode": "blocking",
            "conversation_id": "",
            "user": "streamlit-user"
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(API_URL, json=payload, headers=headers)
        
        if response.status_code == 200:
            bot_reply = response.json().get("answer", "")
        else:
            bot_reply = f"⚠️ Error {response.status_code}: {response.text}"

    except Exception as e:
        bot_reply = f"⚠️ Could not connect to Dify: {str(e)}"

    # Add bot reply
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.markdown(f"**Doc Bot:** {bot_reply}")

