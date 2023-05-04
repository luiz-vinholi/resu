import os
import openai


class AIRepository:
    def  __init__(self): 
        openai.organization = os.getenv('CHAT_GPT_ORG_ID')
        openai.api_key = os.getenv('CHAT_GPT_APIKEY')
        self._client = openai
        self._summary_prefix = 'Resuma em português brasileiro:'
    

    def get_text_summary(self, text):
        content_message = f'{self._summary_prefix}\n\n{text}'
        data = self._client.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{ 'role': 'user', 'content': content_message}],
            max_tokens=1250
        )
        return data