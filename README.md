🤖 Doc Bot – Your Health Assistant

Doc Bot is an AI-powered chatbot that provides doctor-style suggestions based on user-described symptoms.
It is built using Streamlit for the frontend and integrated with the Dify.ai API for natural language generation.

⚠️ Disclaimer: This bot does not provide medical advice. It is for educational and informational purposes only. Always consult a licensed healthcare professional for real medical concerns.

🚀 Features

🗨️ Interactive chat interface powered by Streamlit

💬 Maintains chat history during the session

⚡ Connects with Dify.ai API for AI-generated responses

🛑 Handles errors gracefully (e.g., API issues, connection problems)

🛠️ Tech Stack

Python 3.7+

Streamlit – UI framework

Dify.ai – AI model hosting & inference

Requests & JSON – API communication

📦 Installation & Setup
1️⃣ Clone the Repository
git clone https://gitlab.com/your-username/doc-bot.git
cd doc-bot

2️⃣ Install Dependencies
pip install streamlit requests

3️⃣ Set Up Dify.ai API Key

Create an app in Dify.ai

Get your API key from the app’s "API Key" section

You can either:

Store it securely in a .env file as:

DIFY_API_KEY=app-xxxxxxxxxxxxxxxx


Or paste it directly in your app.py (not recommended for production).

4️⃣ Run the App
streamlit run app.py


Open the app in your browser at http://localhost:8501

🖼️ Usage

Start the app with:

streamlit run app.py


Enter your symptoms in the chat box.

Doc Bot will reply with suggestions in a doctor-style conversational tone.

The session maintains history so you can continue the conversation.

🔍 Example Interaction

You: I have a headache and fever.
Doc Bot: Based on your symptoms, it may indicate a common infection or flu. Stay hydrated, rest well, and if symptoms persist, consult a doctor.

📌 Future Improvements

✅ Deploy online (e.g., Streamlit Cloud, Hugging Face Spaces)
✅ Add speech-to-text and text-to-speech support
✅ Enhance medical knowledge with domain-specific datasets
✅ Support multi-language interactions

👨‍💻 Author

Developed as part of an internship at Summer of AI Internship at Viswam.ai.
