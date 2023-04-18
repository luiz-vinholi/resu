from fastapi import Request, HTTPException
from src.app.summaries import VerifyAccessToSummaryUseCase, SetAccessToSummaryUseCase
from starlette.middleware.base import BaseHTTPMiddleware


class VerifyRequesterAccessToResource(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        headers = dict(request.headers)
        print(headers)

        try:
            ip = self._sanitize_ip(headers['ip'])
        except KeyError:
            raise HTTPException(400, detail='The "ip" in header request is required.')


        VerifyAccessToSummaryUseCase(ip).execute()
        response = await call_next(request)
        SetAccessToSummaryUseCase(ip).execute()

        return response
    

    def _sanitize_ip(self, ip):
        ipSanitized = ''
        fragments = ip.split('.')
        for fragment in fragments:
            ipSanitized += fragment
        return ipSanitized

