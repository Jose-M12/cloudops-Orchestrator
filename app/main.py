from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from app.core.config import settings
from app.core.middleware import CorrelationIdMiddleware
from app.core.errors import problem_handler, Problem
from app.core.logging import setup_logging
# Routers will be created later
# from app.api.v1 import cloud, kubernetes, infrastructure

# Setup logging
setup_logging()

# Initialize Limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="CloudOps Orchestrator",
    description="Multi-cloud infrastructure management platform",
    version="1.0.0"
)

# Add state and middleware
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(CorrelationIdMiddleware)

# Add exception handlers
app.add_exception_handler(Problem, problem_handler)

@app.exception_handler(RateLimitExceeded)
async def ratelimit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        {"type": "about:blank", "title": "Rate limit exceeded", "detail": str(exc.detail), "status": 429},
        status_code=429,
        headers={"Retry-After": str(int(exc.detail)) if hasattr(exc, "detail") and exc.detail is not None else "60"},
    )

app.include_router(cloud.router, prefix="/api/v1/cloud", tags=["cloud"])
app.include_router(kubernetes.router, prefix="/api/v1/kubernetes", tags=["kubernetes"])
app.include_router(infrastructure.router, prefix="/api/v1/infrastructure", tags=["infrastructure"])
app.include_router(monitoring.router, prefix="/api/v1/monitoring", tags=["monitoring"])

@app.get("/")
def read_root():
    return {"message": "CloudOps Orchestrator is running"}
