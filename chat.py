import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def chat_with_gpt(message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",  # hoặc gpt-3.5-turbo nếu dùng bản miễn phí
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content
