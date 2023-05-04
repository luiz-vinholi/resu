import zlib
from base64 import b64encode
from fastapi import HTTPException
from pydantic import BaseModel
from src.app.summaries import CreateTextSummaryUseCase
from src.app.summaries.errors import SummaryWordLimitExceededError
from src.interfaces.middlewares.verify_requester_access_to_resource import VerifyRequesterAccessToResource


def set_summary_router(app):
    class CreateTextSummaryBody(BaseModel):
        text: str

    app.add_middleware(VerifyRequesterAccessToResource)

    @app.post('/summaries')
    def create_text_summary(body: CreateTextSummaryBody):
        try:
            usecase = CreateTextSummaryUseCase(body.text)
            summary = usecase.execute()
            return { 'summary': summary }
        except SummaryWordLimitExceededError as err:
            raise HTTPException(status_code=400, detail=err.to_dict())

