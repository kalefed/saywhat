import re
import demoji
from api.urban_dict import slang_words_def, get_slang_words

class Preprocessing:
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
    def add_slang_def(text):
        slang_contained = get_slang_words(text)
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
    def clean_text(text):
        text = Preprocessing.to_lowercase(text)
        text = Preprocessing.convert_emojis(text)
        text = Preprocessing.add_slang_def(text)
        return text