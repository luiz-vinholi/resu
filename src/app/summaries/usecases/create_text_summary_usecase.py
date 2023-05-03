import zlib
from base64 import b64decode, b64encode
from src.app import UseCase
from src.infra.repositories import AIRepository


class CreateTextSummaryUseCase(UseCase):
    def __init__(self, text: str):
        self._text = text


    def execute(self):
        text = b64decode(self._text)
        text = zlib.decompress(text).decode()
        print(text)
        ai = AIRepository()
        data = ai.get_text_summary(text)
        print(data)
        summary = next(iter(data['choices']))['text']
        self._summary = summary
        compressed_summary = b64encode(zlib.compress(summary.encode()))
        return compressed_summary