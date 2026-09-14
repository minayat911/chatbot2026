import os
from openai import OpenAI, RateLimitError
from dotenv import load_dotenv
import tiktoken

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Global variables for the chatbot
MAX_TOKENS = 500
TOKEN_BUDGET = 1000
SYSTEM_PROMPT = "You are a fed up and sassy assistant who hates answering questions."
TEMPERATURE = 0.7
MODEL = "gemini-3.5-flash-lite"

# To keep track of the conversation history
messages= [{"role": "system", "content": SYSTEM_PROMPT}]  

# Initialize AI client
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

# Token encoding for the model
def get_encoding(model):
    # If model is not found, use default encoding
    try:
        return tiktoken.encoding_for_model(model)
    except KeyError:
        print("Model not found. Using cl100k_base encoding.")
        return tiktoken.get_encoding("cl100k_base")

ENCODING = get_encoding(MODEL)

# Function to count tokens in a given text
def count_tokens(text):
    return len(ENCODING.encode(text))

# Function to count the total tokens used in the conversation history
def used_tokens(messages):
    try:
        return sum(count_tokens(message["content"]) for message in messages)
    except Exception as e:
        print(f"Error counting tokens: {e}")
        return 0

# Function to enforce the token budget by removing the older messages if needed
def enforce_token_budget(messages, budget = TOKEN_BUDGET):
    try: 
        while used_tokens(messages) > budget:
            # Remove the oldest user message (after the system prompt)
            if len(messages) > 1:
                break
            messages.pop(1)
    except Exception as e:
        print(f"Error enforcing token budget: {e}")

# The main CHAT function and AI response generation
def chat(user_input):
    # Message history is maintained in the global messages list
    messages.append({"role": "user", "content": user_input}) 

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )
        reply = response.choices[0].message.content

    except Exception as e:
        # Check if it's a 429 / Rate Limit error
        if "429" in str(e) or isinstance(e, RateLimitError):
            reply = "[System Notice: Whoa, slow down! You've hit the rate limit (Error 429). Wait a minute and try again.]"
        else:
            reply = f"[An error occurred: {e}]"

    # Save the AI's response to messages list
    messages.append({"role": "assistant", "content": reply})

    # Ensure we stay within the token budget
    enforce_token_budget(messages)  

    return reply    


# To keep the conversation going, unless quit or exit is typed
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        # If you want to get a SASSY final response before exiting, uncomment the below lines 
        # reply = chat(user_input)
        # print("Assistant: ", reply)
        print("Bye.")
        break
    reply = chat(user_input)
    print("Assistant: ", reply)
    print ("Current token usage: ", used_tokens(messages), "tokens.")