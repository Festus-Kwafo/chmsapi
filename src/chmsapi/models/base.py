from datetime import datetime

from sqlalchemy.orm import MappedAsDataclass, Mapped, mapped_column


class DateTimeMixin(MappedAsDataclass):
    created_date: Mapped[datetime] = mapped_column(init=False, )
