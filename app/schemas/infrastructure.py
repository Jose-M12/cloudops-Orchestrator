from pydantic import BaseModel
from typing import Literal, Dict

class RunRequest(BaseModel):
    action: Literal["plan", "apply", "destroy"]
    stack_path: str
    vars: Dict
    workspace: str = "default"
    env_id: str

class Operation(BaseModel):
    id: str
    status: str
    action: str
    stack_path: str
    workspace: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True
