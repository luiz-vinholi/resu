from fastapi import Request


async def verify_requester_access_to_resource(request: Request, next_func):
        
    response = await next_func(request)
    return response