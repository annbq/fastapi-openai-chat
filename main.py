from fastapi import FastAPI
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel
from typing import AsyncGenerator
from chat import chat_with_gpt, chat_stream_gpt


app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(input: ChatInput):
    reply = await chat_with_gpt(input.message)
    return JSONResponse(
        content={"reply": reply},
        media_type="application/json; charset=utf-8"
    )

@app.post("/chat/stream")
async def chat_stream(input: ChatInput):
    async def stream_response() -> AsyncGenerator[bytes, None]:
        async for chunk in chat_stream_gpt(input.message):
            yield chunk.encode("utf-8")  # Encode UTF-8 để hỗ trợ tiếng Việt

    return StreamingResponse(
        stream_response(),
        media_type="text/plain; charset=utf-8"
    )
