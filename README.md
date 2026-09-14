# 💬 AI Conversational Chatbot

A lightweight AI-powered conversational chatbot built with **Python and Google's Gemini API**. The project explores practical **LLM application development**, including API integration, conversational context management, prompt engineering, token management, error handling, and secure API credential management.

## ✨ Features

### 🤖 LLM-Powered Conversations

* Integrates Google's **Gemini model** into a Python application using the OpenAI Python SDK and Google's OpenAI-compatible API endpoint.
* Processes user input and generates AI-powered conversational responses.
* Maintains conversation context throughout a session.

### 🧠 Conversation & Token Management

* Maintains conversation history to provide context across interactions.
* Tracks token usage using **tiktoken**.
* Enforces a configurable token budget to manage conversation length.
* Automatically removes older conversation messages when the token budget is exceeded.

### 🎯 Prompt Engineering & Persona Control

* Uses a system prompt to define the chatbot's behaviour, tone, and personality.
* Demonstrates how system instructions can influence LLM-generated responses.
* Includes a deliberately playful and sassy assistant persona.

### 🔐 Secure Credential Management

* Loads the Gemini API key from environment variables using **python-dotenv**.
* Keeps API credentials separate from application code.
* Supports secure local configuration through a `.env` file.

### ⚠️ API Error Handling

* Handles API exceptions during chatbot interactions.
* Detects rate-limit (HTTP 429) errors and provides a user-friendly system message.
* Provides fallback error messages when API requests fail.

### ⚙️ Configurable AI Behaviour

* Configurable model, temperature, maximum response tokens, and conversation token budget.
* Keeps chatbot configuration separate from the core conversation logic for easier experimentation.

## 🛠️ Technologies Used

* **Python**
* **Google Gemini API**
* **OpenAI Python SDK**
* **tiktoken**
* **python-dotenv**
* **OpenAI-compatible API**

## 🏗️ How It Works

The chatbot follows a simple request-and-response workflow:

```text
User Input
    ↓
Python Application
    ↓
System Prompt + Conversation History
    ↓
Token Budget Management
    ↓
Gemini API
    ↓
Generated Response
    ↓
Conversation History Updated
```

The application maintains the conversation history and checks token usage after each interaction. When the configured token budget is exceeded, older conversation messages are removed while preserving the system prompt.

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* A Google Gemini API key

### Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
python chatbot.py
```

## 🔒 Security

API credentials are loaded through environment variables rather than being stored directly in the source code.

Make sure your `.env` file is included in `.gitignore`:

```text
.env
```

Never commit API keys or other sensitive credentials to the repository.

## 📚 What I Learned

This project provided hands-on experience with:

* Integrating an LLM API into a Python application
* Working with an OpenAI-compatible API interface
* Designing system prompts and controlling LLM behaviour
* Managing conversational context
* Tracking and managing token usage
* Handling API errors and rate limits
* Managing API credentials through environment variables
* Building an application around a generative AI model

## 🔮 Future Improvements

* Add a web-based user interface
* Support multiple chatbot personalities
* Improve conversation-memory management
* Add automated testing
* Improve response validation and error handling
* Explore additional LLM application patterns

## 📄 License

This project is a personal learning project exploring **LLM application development, generative AI, and API integration**.
