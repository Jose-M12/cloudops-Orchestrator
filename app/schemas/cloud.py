from pydantic import BaseModel

class CloudResourceBase(BaseModel):
    provider: str
    resource_type: str

class CloudResourceCreate(CloudResourceBase):
    details: dict

class CloudResource(CloudResourceBase):
    id: int
    details: dict

    class Config:
        from_attributes = True
