import re
import demoji
from urban_dict_api import slang_words_def, get_slang_words
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Preprocessing:

    @staticmethod
    def remove_stopwords(text):
                
        # Download stopwords dataset if not already downloaded
        nltk.download('stopwords')
        nltk.download('punkt_tab')

        # Tokenize words
        words = word_tokenize(text)

        # Remove stop words
        filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]
        text = ' '.join(filtered_words)

        return text
    @staticmethod
    def to_lowercase(text):
        return text.lower()

    @staticmethod
    def convert_emojis(text):
        emoji_map = demoji.findall(text)
        for emoji, desc in emoji_map.items():
            text = text.replace(emoji, f" {desc} ")
        return text

    @staticmethod
    def add_slang_def(text,slang_words):
        slang_contained = get_slang_words(text,slang_words)
        word_defs = slang_words_def(slang_contained)
        for slang, definition in word_defs.items():
            text = re.sub(
                rf"\b{re.escape(slang)}\b", 
                f"{slang} (meaning: {definition})", 
                text, 
                flags=re.IGNORECASE
            )
        return text

    @staticmethod
    def clean_text(text,slang_words):
        text = Preprocessing.remove_stopwords(text)
        text = Preprocessing.to_lowercase(text)
        text = Preprocessing.convert_emojis(text)
        text = Preprocessing.add_slang_def(text,slang_words)
        return text
    
    @staticmethod
    def read_csv(file_path):
        df = pd.read_csv(file_path)

        # Extract the first column into a list
        slang_words = df.iloc[:, 0].tolist()

        return slang_words
    
