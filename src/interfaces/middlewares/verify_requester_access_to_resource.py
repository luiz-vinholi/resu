from fastapi import HTTPException
from src.app.summaries import VerifyAccessToSummaryUseCase, SetAccessToSummaryUseCase
from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from src.app.summaries.errors import ExpiredResourceAccessError


class VerifyRequesterAccessToResource(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            ip = request.headers.get('X-Forwarded-For').split(', ')[0]
            ip = self._sanitize_ip(ip)
        except KeyError:
            raise HTTPException(400, detail='The "ip" in request is required.')

        try:
            VerifyAccessToSummaryUseCase(ip).execute()
            response = await call_next(request)
            SetAccessToSummaryUseCase(ip).execute()
        except ExpiredResourceAccessError as err:
            raise HTTPException(status_code=403, detail=err.to_dict())

        return response
    

    def _sanitize_ip(self, ip):
        ipSanitized = ''
        fragments = ip.split('.')
        for fragment in fragments:
            ipSanitized += fragment
        return ipSanitized

