from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from preprocessing import Preprocessing
from sentiment_analysis import analyze_sentiment
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
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.put("/translations")
async def set_sentence(sentence: Sentence):
    pre = Preprocessing()

    # add API key here
    connector = OpenAI.OpenAIConnector(api_key=api_key, model="gpt-4o", temperature=0.0)
    slang_words = pre.read_csv("all_slangs.csv")
    processed_text = pre.clean_text(sentence.text, slang_words)
    prompt = "Message:" + sentence.text + "\n Meaning:" + processed_text
    translation = connector.prompt(prompt)
    print(translation)

    sentiment = analyze_sentiment(translation)

    response = {
        "sentence_text": sentence.text,
        "translation": translation.replace("Message: ", ""),
        "sentiment": sentiment,
    }
    return response
