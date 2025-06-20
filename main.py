from fastapi import FastAPI
from pydantic import BaseModel
from chat import chat_with_gpt

app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(input: ChatInput):
    reply = await chat_with_gpt(input.message)
    return {"reply": reply}
