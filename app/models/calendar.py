from pydantic import BaseModel, Field, validator, root_validator
from typing import List, Optional, Union
from datetime import date
from typing_extensions import Literal  # Import from typing-extensions for Python 3.7 compatibility

class Lamp(BaseModel):
    id: str = Field(..., description="Relay ID")

class RuleDay(BaseModel):
    ctrProgId: int = Field(..., ge=0, description="Control program ID")
    timeConditiontype: Literal[1] = Field(..., description="Time condition type (1 for day)")
    start: Optional[str] = Field(..., description="Start day")
    end: Optional[str] = Field(None, description="End day (optional)")
    
    @validator('start', 'end', pre=True)
    def validate_weekday(cls, v):
        valid_weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        if v is not None and v not in valid_weekdays:
            raise ValueError(f"{v} is not a valid weekday. Valid weekdays are: {', '.join(valid_weekdays)}")
        return v

class RuleDate(BaseModel):
    ctrProgId: int = Field(..., ge=0, description="Control program ID")
    timeConditiontype: Literal[2] = Field(..., description="Time condition type (2 for date)")
    start: date = Field(..., description="Start date")
    end: Optional[date] = Field(None, description="End date (optional)")

# Union of the two Rule types
Rule = Union[RuleDay, RuleDate]

class Calendar(BaseModel):
    calendarId: int = Field(..., ge=0, description="Unique calendar ID")
    version: int = Field(..., ge=0, description="Version of the calendar")
    name: str = Field(..., description="Name of the calendar")
    defaultCtrProgId: int = Field(..., ge=0, description="Default control program ID")
    rules: Optional[List[Rule]] = Field(None, description="List of rules")
    lamp: List[Lamp] = Field(..., description="Array of relay IDs")
    
    @validator('rules', pre=True, each_item=True)
    def check_rules_consistency(cls, rule):
        if rule:
            time_condition_types = {type(rule).__name__ for rule in rule}
            if len(time_condition_types) > 1:
                raise ValueError('All rules must be of the same type (either all RuleDay or all RuleDate)')
        return rule

    class Config:
        json_encoders = {
            date: lambda v: v.isoformat() if isinstance(v, date) else v
        }