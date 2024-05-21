from pydantic import BaseModel, validator
from typing import List, Union
from datetime import date

class Rules(BaseModel):
    ctrProgId: int
    timeConditiontype: int = 1
    start: Union[str, date]
    end: Union[str, date]

    @validator('start', 'end')
    def validate_start_end(cls, v):
        if isinstance(v, date):
            # Convert date objects to ISO format strings
            return v.isoformat()
        return v

class Calendar(BaseModel):
    calendarId: int
    version: int = 2
    name: str
    defaultCtrProgId: int
    rules: List[Rules]
    lamp: int = 1
    class_name: str = "app.models.Calendar.Calendar"

    @validator('rules')
    def validate_rules(cls, v):
        for rule in v:
            rule.validate_start_end(rule.start)  # Pass 'start' value to validation method
            rule.validate_start_end(rule.end)    # Pass 'end' value to validation method
        return v