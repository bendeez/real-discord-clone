from pydantic import BaseModel, ConfigDict

class Schema(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)