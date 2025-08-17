from sqlalchemy import Column, Integer, String, JSON
from app.core.database import Base

class CloudResource(Base):
    __tablename__ = "cloud_resources"

    id = Column(Integer, primary_key=True, index=True)
    provider = Column(String)
    resource_type = Column(String)
    details = Column(JSON)
