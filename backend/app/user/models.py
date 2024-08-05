from app.tools.models.base_models import BaseMixin
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

DEFAULT_USER_PROFILE = "https://firebasestorage.googleapis.com/v0/b/discord-83cd2.appspot.com/o/default.png?alt=media&token=c27e7352-b75a-4468-b14b-d06b74839bd8"

class User(BaseMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    global_name: Mapped[str]
    avatar: Mapped[str] = mapped_column(default=DEFAULT_USER_PROFILE)
    bot: Mapped[bool] = mapped_column(default=False)
    verified: Mapped[str] = mapped_column(default=False)
    email: Mapped[str] = mapped_column(unique=True)
    created: Mapped[datetime] = mapped_column(default=datetime.now())


