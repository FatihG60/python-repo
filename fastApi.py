from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

message = Message(message="Hello world!")

@app.get("/")
def getMessage():
    return message

@app.post("/add-message")
def createMessage(message: Message):
    return message

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000) 