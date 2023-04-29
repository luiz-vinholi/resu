from fastapi import FastAPI
from .auth_router import set_auth_router
from .summary_router import set_summary_router


app = FastAPI()


@app.get('/')
async def get_hello_world():
    return { 'message': 'Hello World' }


set_auth_router(app)
set_summary_router(app)
