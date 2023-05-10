import openai
from source.api_keys import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

def generate_chatgpt_response(history):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=500,
        temperature=1.2,
        messages=history,
    )
    return response.choices[0].message.content