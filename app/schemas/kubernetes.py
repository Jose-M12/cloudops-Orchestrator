from pydantic import BaseModel

class KubernetesResourceBase(BaseModel):
    cluster: str
    resource_type: str

class KubernetesResourceCreate(KubernetesResourceBase):
    details: dict

class KubernetesResource(KubernetesResourceBase):
    id: int
    details: dict

    class Config:
        from_attributes = True
