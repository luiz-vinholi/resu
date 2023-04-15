from pydantic import BaseModel
from src.interfaces import app
from src.infra.repositories import AIRepository


class CreateTextSummaryBody(BaseModel):
    text: str


@app.post('/summaries')
def create_text_summary(body: CreateTextSummaryBody):
    ai = AIRepository()
    return ai.get_text_summary(body.text)