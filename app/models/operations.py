import enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import String, Enum, ForeignKey, text
from app.core.database import Base

class OperationStatus(str, enum.Enum):
    pending = "pending"
    running = "running"
    succeeded = "succeeded"
    failed = "failed"
    cancelled = "cancelled"

class Operation(Base):
    __tablename__ = "operations"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    env_id: Mapped[str] = mapped_column(String, index=True)
    action: Mapped[str] = mapped_column(String)
    status: Mapped[OperationStatus] = mapped_column(Enum(OperationStatus), index=True)
    stack_path: Mapped[str] = mapped_column(String)
    workspace: Mapped[str] = mapped_column(String, default="default")
    task_id: Mapped[str | None] = mapped_column(String, nullable=True)
    idem_key: Mapped[str | None] = mapped_column(String, index=True, nullable=True, unique=False)
    correlation_id: Mapped[str | None] = mapped_column(String, index=True)
    meta: Mapped[dict] = mapped_column(JSONB, default=dict)
    created_at: Mapped[str] = mapped_column(server_default=text("NOW() AT TIME ZONE 'utc'"))

    async def save(self, db): db.add(self); await db.commit(); await db.refresh(self)
    @classmethod
    async def get(cls, db, op_id: str): return await db.get(cls, op_id)
    @classmethod
    async def get_by_idem_key(cls, db, key: str):
        q = await db.execute(text("SELECT * FROM operations WHERE idem_key=:k ORDER BY created_at DESC LIMIT 1"), {"k": key})
        row = q.mappings().first()
        return db.merge(cls(**row)) if row else None
    async def attach_task(self, db, task_id: str): self.task_id = task_id; await self.save(db)
    def to_dict(self): return {k: getattr(self, k) for k in ("id","env_id","action","status","stack_path","workspace","created_at")}
