from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Model Initialization
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=api_key,
        temperature=0.4
    )
    parser = StrOutputParser()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Respond to DSA questions clearly and concisely."),
        ("user", "{question}")
    ])
    chain = prompt | llm | parser
except Exception as e:
    st.error(f"Error initializing AI model. Please check your GOOGLE_API_KEY in the .env file. Details: {e}")
    llm = None
    chain = None

# UI
st.set_page_config(page_title="DSABuddy", page_icon="💡", layout="wide")

st.markdown("""
<style>
/* Main Content Centering and Max Width */
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 950px;
}

/* Header Styling */
header {
    visibility: hidden;
}

/* Chat Message Styling */
.msg-box {
    margin: 10px 0;
    padding: 14px 18px;
    border-radius: 18px;
    font-size: 17px;
    line-height: 1.6;
}
.user {
    background-color: #E6F3E0;
    text-align: right;
    box-shadow: 0 4px 8px rgba(0,0,0,0.08);
    border-top-right-radius: 0;
    margin-left: 10%;
}
.bot {
    background-color: #FFFFFF;
    text-align: left;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    border-top-left-radius: 0;
    margin-right: 10%;
    border: 1px solid #F0F0F0;
}
.name {
    font-weight: 700;
    margin-bottom: 7px;
    color: #4CAF50;
    font-size: 0.9em;
}
.user .name {
    color: #4CAF50;
}
.bot .name {
    color: #4A90E2;
}

/* Input box styling for better contrast and placement */
div[data-testid="stForm"] > div > div:nth-child(2) {
    padding-bottom: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# --- Application Header ---
st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
st.title("💡 DSABuddy")
st.markdown(
    '<hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.15), rgba(0, 0, 0, 0)); margin-bottom: 25px;">',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
# --- End Header ---

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        # User bubble: whole content is plain text, shown inside styled div
        st.markdown(
            f"<div class='msg-box user'><div class='name'>You</div>{msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        # Bot bubble: wrapper div via HTML, content via Markdown so **bold** works
        st.markdown("<div class='msg-box bot'><div class='name'>DSABuddy</div>", unsafe_allow_html=True)
        st.markdown(msg["content"])  # Markdown rendering for bold, lists, etc.
        st.markdown("</div>", unsafe_allow_html=True)

# Input at bottom
user_input = st.chat_input("Ask anything about DSA...")

if user_input:
    if not chain:
        st.error("Cannot process request: AI model is not initialized.")
    else:
        # Add user message to state
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Process and get bot reply
        with st.spinner("DSABuddy is thinking..."):
            try:
                bot_reply = chain.invoke({"question": user_input})
            except Exception as e:
                bot_reply = f"An error occurred while generating the response: {e}"

        # Add bot message to state
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        # Rerun to display the new messages
        st.rerun()
