from app.base_models import BaseMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import CheckConstraint


class User(BaseMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    global_name: Mapped[str]
    avatar: Mapped[str]
    bot: Mapped[bool] = mapped_column(default=False)
    verified: Mapped[str]
    email: Mapped[str]
    CheckConstraint('username !~ (@|#|:|```|discord|\s) AND global_name (@|#|:|```|discord|\s)', name="check_valid_characters_constraint")
    CheckConstraint("length(username) BETWEEN 2 AND 32",name="check_username_length")
    CheckConstraint("length(global_name) BETWEEN 1 AND 32", name="check_global_name_length")





