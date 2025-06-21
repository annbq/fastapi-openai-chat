import os
from openai import OpenAI, AsyncOpenAI
from dotenv import load_dotenv
from fastapi.responses import StreamingResponse


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

clientAsync = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def chat_with_gpt(message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # hoặc gpt-3.5-turbo nếu dùng bản miễn phí
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content


async def chat_stream_gpt(message: str):
    stream = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ],
        stream=True  # Bật stream!
    )

    async for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta
