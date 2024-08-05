from pydantic import Field, EmailStr, model_validator
from app.tools.base_schemas import Schema
from typing import Optional
import re


class UserIn(Schema):
    email: EmailStr
    username: str = Field(min_length=2, max_length=32)
    global_name: Optional[str] = None
    password: str = Field(min_length=8, max_length=32)

    @model_validator(mode="after")
    def validate_username_characters(self):
        invalid_characters = re.compile(r"(@|#|:|`|discord|\s)")
        if invalid_characters.search(self.username):
            raise ValueError("Username contains invalid characters")
        return self

    @model_validator(mode="after")
    def validate_password_characters(self):
        necessary_characters = re.compile(r"(?=.*[A-Z])(?=.*[!@#$%^&*()])(?=.*\d)")
        if not necessary_characters.search(self.password):
            raise ValueError("Password must contain numbers, symbols, lowercase, and uppercase letters")
        return self

    @model_validator(mode="after")
    def set_global_name(self) -> str:
        self.global_name = self.username
        return self

