import streamlit as st
import requests
import json

st.set_page_config(page_title="Doc Bot", page_icon="🤖", layout="centered")

st.title("🤖 Doc Bot - Your Health Assistant")
st.write("Ask me anything about your symptoms and I’ll give you doctor-style suggestions.")

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
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "gemma:2b", "prompt": user_input},
            stream=True,
        )

        bot_reply = ""
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode("utf-8"))
                        if "response" in data:
                            bot_reply += data["response"]
                        if data.get("done"):
                            break
                    except json.JSONDecodeError:
                        continue
        else:
            bot_reply = f"⚠️ Error {response.status_code}: {response.text}"

    except Exception as e:
        bot_reply = f"⚠️ Could not connect to Ollama: {str(e)}"

    # Add bot reply
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.markdown(f"**Doc Bot:** {bot_reply}")
