import os
import openai


class AIRepository:
    def  __init__(self): 
        openai.organization = os.getenv('CHAT_GPT_ORG_ID')
        openai.api_key = os.getenv('CHAT_GPT_APIKEY')
        self._client = openai
        self._summary_prefix = 'Resuma o texto a seguir:'
    

    def get_text_summary(self, text):
        content_message = f'{self._summary_prefix} {text}'
        data = self._client.Completion.create(
            engine='text-curie-001',
            prompt=content_message,
            stop=None,
            presence_penalty=-1,
            frequency_penalty=-1
        )
        return data