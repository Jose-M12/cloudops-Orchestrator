from sqlalchemy import Column, Integer, String, JSON
from app.core.database import Base

class KubernetesResource(Base):
    __tablename__ = "kubernetes_resources"

    id = Column(Integer, primary_key=True, index=True)
    cluster = Column(String)
    resource_type = Column(String)
    details = Column(JSON)
