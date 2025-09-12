import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.db import db
from model.user import User
from datetime import datetime

#table: conversation_summary(id: int, user_id: int (FK), summary: str, created_at: timestamp)
class ConversationSummary(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey("user.id"), nullable=False)
    summary: Mapped[str] = mapped_column(sa.String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now())

    user: Mapped["User"] = relationship(back_populates="summaries")

    def __repr__(self) -> str:
        return f"ConversationSummary(id={self.id}, user_id={self.user_id}, created_at={self.created_at})"
