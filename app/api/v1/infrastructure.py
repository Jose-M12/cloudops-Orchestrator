from fastapi import APIRouter, Header, HTTPException, Response, Depends
from pydantic import BaseModel, Field
from uuid import uuid4
from typing import Optional, Literal

router = APIRouter()

class RunRequest(BaseModel):
    action: Literal["plan", "apply", "destroy"]
    stack_path: str
    vars: dict = Field(default_factory=dict)
    workspace: str = "default"
    env_id: str

class Operation(BaseModel):
    id: str
    status: str # placeholder
    action: str
    stack_path: str
    workspace: str
    created_at: str
    updated_at: str

@router.post("/runs", status_code=202, response_model=Operation)
async def create_run(
    body: RunRequest,
    response: Response,
    idempotency_key: Optional[str] = Header(default=None, convert_underscores=False, alias="Idempotency-Key"),
    x_correlation_id: Optional[str] = Header(default=None, alias="X-Correlation-ID"),
):
    op_id = str(uuid4())
    op = {
        "id": op_id,
        "status": "pending",
        "action": body.action,
        "stack_path": body.stack_path,
        "workspace": body.workspace,
        "created_at": "2025-01-01T00:00:00Z",
        "updated_at": "2025-01-01T00:00:00Z",
    }
    response.headers["Location"] = f"/api/v1/infrastructure/operations/{op_id}"
    return op

@router.get("/operations/{op_id}", response_model=Operation)
async def get_operation(op_id: str):
    op = {
        "id": op_id,
        "status": "succeeded",
        "action": "apply",
        "stack_path": "/fake/path",
        "workspace": "default",
        "created_at": "2025-01-01T00:00:00Z",
        "updated_at": "2025-01-01T00:00:00Z",
    }
    return op
