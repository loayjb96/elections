from typing import Optional
from datetime import date, datetime
from enum import Enum
from pydantic import BaseModel, Extra


class BaseDTO(BaseModel):
    class Config:
        extra = Extra.ignore


class ErrorRes(BaseDTO):
    error: Optional[str]
    error_description: Optional[str]


class BaseDTODict(BaseDTO):  # parser.skip
    def dict(self, *args, **kwargs) -> dict:
        dic = super().dict(*args, **kwargs)
        for key, value in dic.items():
            if isinstance(value, datetime):
                dic[key] = datetime.strftime(value, '%Y-%m-%d %H:%M:%S')
            elif isinstance(value, date):
                dic[key] = str(value)
            elif isinstance(value, Enum):
                dic[key] = value.value
        return dic
