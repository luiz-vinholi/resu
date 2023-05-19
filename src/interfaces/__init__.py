from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .auth_router import set_auth_router
from .summary_router import set_summary_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def get_hello_world():
    return { 'message': 'Hello World' }


@app.exception_handler(Exception)
async def http_exception_handler(_, error):
    try:
        status_code = error.status_code
    except AttributeError:
        status_code = 500

    print(error)
    try:
        detail = error.detail
    except AttributeError:
        detail = error.message

    return JSONResponse({'detail': detail}, status_code=status_code)
    

set_auth_router(app)
set_summary_router(app)
