import zlib
import os
from base64 import b64decode, b64encode
from src.app import UseCase
from src.app.summaries.errors import SummaryWordLimitExceededError
from src.infra.repositories import AIRepository


class CreateTextSummaryUseCase(UseCase):
    def __init__(self, text: str):
        self._text = text
        self._word_quantity_limit = int(os.getenv('SUMMARY_WORD_QUANTITY_LIMIT'))
        self._ai_respository = AIRepository()


    def execute(self):
        text = self._decompress_text()
        text = text.strip()

        self._verify_word_quantity(text)

        data = self._ai_respository.get_text_summary(text)
        summary = next(iter(data['choices']))['message']['content']
        summary = summary.strip()
        self._summary = summary

        compressed_summary = self._compress_summary()
        return compressed_summary


    def _decompress_text(self):
        text = b64decode(self._text)
        decompressed_text = zlib.decompress(text).decode()
        return decompressed_text


    def _compress_summary(self):
        compressed_summary = b64encode(zlib.compress(self._summary.encode()))
        return compressed_summary


    def _verify_word_quantity(self, text):
        word_quantity = len(text.split())
        print(word_quantity)
        if word_quantity > self._word_quantity_limit:
            raise SummaryWordLimitExceededError()