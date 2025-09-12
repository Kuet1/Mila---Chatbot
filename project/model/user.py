import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from model.db import db
from datetime import datetime


class User(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(sa.String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(sa.String(255), nullable=False)
    last_interaction: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now())

    reviews: Mapped[list["Review"]] = relationship("Review", back_populates="user", cascade="all, delete-orphan")
    summaries: Mapped[list["ConversationSummary"]] = relationship("ConversationSummary", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id}, email={self.email})"
