from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from .auth_router import set_auth_router
from .summary_router import set_summary_router


app = FastAPI()

@app.get('/')
async def get_hello_world():
    return { 'message': 'Hello World' }


@app.exception_handler(Exception)
async def http_exception_handler(request, error):
    try:
        status_code = error.status_code
    except KeyError:
        status_code = 500
    print('vai se fude')
    repr(error)
    # return JSONResponse({'detail': error.code}, status_code=status_code)
    

set_auth_router(app)
set_summary_router(app)
