from datetime import datetime

from fastapi import Response, Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from src.chmsapi.common.logs import log


class AccessMiddleware(BaseHTTPMiddleware):
    """Record the intermediate part of the request log"""

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        start_time = datetime.now()
        response = await call_next(request)
        end_time = datetime.now()
        log.info(f'{response.status_code} {request.client.host} {request.method} {request.url} {end_time - start_time}')
        return response
