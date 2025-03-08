import preprocessing
import OpenAI
from dotenv import load_dotenv
import os

if __name__ == '__main__':

    preprocessing = preprocessing.Preprocessing()

    slang_words = preprocessing.read_csv("server/all_slangs.csv")

    example_phrase = "Slay girl you are so on fleek."

    processed_text = preprocessing.clean_text(example_phrase,slang_words)
    print("phrase:", example_phrase, '\n Meaning:',processed_text)

    load_dotenv()  # Load environment variables from .env
    api_key = os.getenv("OPENAI_API_KEY")

    connector = OpenAI.OpenAIConnector(api_key=api_key, model="gpt-4o")
    translation = connector.prompt(processed_text)
    print(translation)



