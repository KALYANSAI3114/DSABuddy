# 💡 DSABuddy

A clean and modern chatbot assistant built with Streamlit and LangChain to help you with Data Structures and Algorithms (DSA) questions.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)

## 📋 Features

- **Interactive Chat Interface**: Clean, WhatsApp-style chat bubbles for easy conversation
- **AI-Powered Responses**: Uses Google's Gemini 2.5 Flash model for intelligent DSA explanations
- **Modern UI**: Responsive design with custom styling and smooth user experience
- **Real-time Responses**: Get instant answers to your DSA questions

## 🚀 Getting Started

### Prerequisites

- Python3
- Google API Key (for Gemini AI)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/KALYANSAI3114/DSABuddy.git
   cd dsabuddy
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   To get your Google API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy and paste it into your `.env` file

### Running the Application

```bash
streamlit run chatbot.py
```

The application will open in your default browser at `http://localhost:8501`

## 📦 Requirements

Create a `requirements.txt` file with the following dependencies:

```txtstreamlit
python-dotenv
langchain
langchain-core
langchain-google-genai
google-generativeai

```

## 🎨 Features Breakdown

### Chat Interface
- **User Messages**: Displayed on the right with green background
- **Bot Responses**: Displayed on the left with white background and subtle border
- **Message Styling**: Rounded corners, shadows, and proper spacing for readability

### AI Model
- **Model**: Google Gemini 2.5 Flash
- **Temperature**: 0.4 (balanced between creativity and consistency)
- **System Prompt**: Optimized for clear and concise DSA explanations

## 🛠️ Project Structure

```
dsabuddy/
│
├── app.py                 # Main application file
├── .env                   # Environment variables (not in git)
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 💻 Usage

1. Launch the application using `streamlit run chatbot.py`
2. Type your DSA question in the chat input at the bottom
3. Press Enter or click the send icon
4. Wait for DSABuddy to generate a response
5. Continue the conversation as needed

### Example Questions

- "Explain binary search algorithm"
- "What's the time complexity of quicksort?"
- "How do I implement a linked list in Python?"
- "Difference between stack and queue?"

## 👨‍💻 Author

Your Name
- GitHub: [KALYANSAI-3114](https://github.com/KALYANSAI3114)

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [LangChain](https://langchain.com/) for LLM integration
- [Google Gemini](https://deepmind.google/technologies/gemini/) for the AI model
