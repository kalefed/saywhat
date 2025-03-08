from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from preprocessing import Preprocessing
import OpenAI
import os


class Sentence(BaseModel):
    text: str


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.put("/translations")
async def set_sentence(sentence: Sentence):
    try:
        pre = Preprocessing()

        connector = OpenAI.OpenAIConnector(api_key=api_key, model="gpt-4o")

        slang_words = pre.read_csv("all_slangs.csv")
        processed_text = pre.clean_text(sentence.text, slang_words)
        prompt = "Message:" + sentence.text + "\n Meaning:" + processed_text

        # Make API call and capture any issues
        translation = connector.prompt(prompt)
        print(translation)

        return {"message": f"Received sentence: {sentence.text}"}

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {"error": "Internal Server Error", "details": str(e)}, 500
