from fastapi import FastAPI
app = FastAPI()
import src.interfaces.summaries.summary_router


@app.get('/')
async def get_hello_world():
    return { 'message': 'Hello World' }
