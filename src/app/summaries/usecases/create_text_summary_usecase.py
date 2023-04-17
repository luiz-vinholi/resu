import zlib
from base64 import b64decode
from src.app import UseCase
from src.infra.repositories import AIRepository


class CreateTextSummaryUseCase(UseCase):
    def __init__(self, text: str):
        self._text = text

    
    def execute(self):
        text = b64decode(self._text)
        text = zlib.decompress(text).decode()
        ai = AIRepository()
        return ai.get_text_summary(text)