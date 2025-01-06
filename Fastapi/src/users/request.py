from datetime import date

from pydantic import BaseModel, field_validator

class UserCreateUserRequestBody(BaseModel):
    name: str
    date_of_birth: date    # 생일

    @field_validator("date_of_birth")
    def validate_date_of_birth(cls, v):
        age_delta = date.today() - v
        if age_delta.days < 5 * 365:
            raise ValueError("만 6세 이상만 가입할 수 있습니다.")
        return v
    