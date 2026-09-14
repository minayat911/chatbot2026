import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

MAX_TOKENS = 500
TOKEN_BUDGET = 1000
SYSTEM_PROMPT = "You are a fed up and sassy assistant who hates answering questions."
TEMPERATURE = 0.7
MODEL = "gemini-3.6-flash"

api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )


def chat(user_input):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )
    return response.choices[0].message.content


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