from openai import OpenAI

class OpenAIConnector:
    def __init__(self, api_key, model="gpt-4o", temperature=0.0):
        """
        Initialize the OpenAI connector.
        :param api_key: OpenAI API key.
        :param model: The model to use 
        :param temperature: The sampling temperature
        """
        self.api_key = api_key
        self.model = model
        self.client = OpenAI(api_key=self.api_key)
        self.temperature = temperature

    def prompt(self, prompt):
        """
        Sent the phrase to OpenAI to get the translation.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[ 
                    {"role": "system", "content": "You are an intergenerational slang translator. Your task is to take a given phrase, which may contain slang, abbreviations, or generational expressions, and translate it into clear, standard English. You should only return the translated sentence."},
                    {"role": "user", "content": prompt
                }],
                temperature=self.temperature,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return None