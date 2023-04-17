from fastapi import Request, HTTPException
from src.app.summaries import VerifyAccessToSummaryUseCase, SetAccessToSummaryUseCase


async def verify_requester_access_to_resource(request: Request, next_func):
    headers = dict(request.headers)
    if headers['ip']:
        HTTPException(400, detail='The "ip" in header request is required.')

    ip = _sanitize_ip(headers['ip'])

    VerifyAccessToSummaryUseCase(ip).execute()
    response = await next_func(request)
    SetAccessToSummaryUseCase(ip).execute()

    return response


def _sanitize_ip(ip):
    fragments = ip.split('.')
    for fragment in fragments:
        ipSanitized += fragment
    return ipSanitized