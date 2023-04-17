from fastapi import FastAPI
from .summary_router import set_summary_router


app = FastAPI()


@app.get('/')
async def get_hello_world():
    return { 'message': 'Hello World' }


set_summary_router(app)
