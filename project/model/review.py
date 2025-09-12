import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.db import db
from datetime import datetime
from model.user import User


#table: review(id: int, user_id: int (FK), review_text: str, created_at: timestamp)
class Review(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey("user.id"), nullable=False)
    review_text: Mapped[str] = mapped_column(sa.String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now())

    user: Mapped["User"] = relationship(back_populates="reviews")
    
    def __repr__(self) -> str:
        return f"Review(id={self.id}, user_id={self.user_id}, review_text={self.review_text}, created_at={self.created_at})"
