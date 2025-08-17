# app/core/errors.py
from fastapi import Request
from fastapi.responses import JSONResponse

class Problem(Exception):
    def __init__(self, title, status=400, detail=None, type_="about:blank", instance=None):
        self.title = title
        self.status = status
        self.detail = detail
        self.type = type_
        self.instance = instance

async def problem_handler(request: Request, exc: Problem):
    body = {
        "type": exc.type,
        "title": exc.title,
        "status": exc.status,
        "detail": exc.detail,
        "instance": exc.instance or str(request.url)
    }
    return JSONResponse(content=body, status_code=exc.status)

class DomainError(Problem): ...
