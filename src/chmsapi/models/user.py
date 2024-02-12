from datetime import datetime, timezone

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.chmsapi.models.base import Base
from src.chmsapi.models.base import id_key


class User(Base):
    __tablename__ = "user"

    id: Mapped[id_key] = mapped_column(init=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True, comment='Mail')
    password: Mapped[str] = mapped_column(String(255))
    is_superuser: Mapped[bool] = mapped_column(default=False, comment='Super authority')
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    join_time: Mapped[datetime] = mapped_column(
        init=False, default_factory=datetime.now(timezone.utc), comment='Registration time'
    )
    last_login_time: Mapped[datetime | None] = mapped_column(
        init=False, onupdate=datetime.now(timezone.utc), comment='Last login last time'
    )
