from pydantic import BaseModel, Field, validator
from typing import List, Optional, Union
from typing_extensions import Literal  
from datetime import time, date

class AstroTimeControl(BaseModel):
    timeEvtType: Literal["Astro time"] = Field(..., description="Type of time event")
    dimmingLevel: int = Field(..., ge=0, le=100, description="Light brightness level")
    astroTypeEvt: str = Field(..., pattern="^(Sunrise|Sunset)$", description="Astro event type")
    offset: int = Field(..., ge=-720, le=720, description="Offset time in minutes")

class FixedTimeControl(BaseModel):
    timeEvtType: Literal["Fixed time"] = Field(..., description="Type of time event")
    dimmingLevel: int = Field(..., ge=0, le=100, description="Light brightness level")
    fixedTime: str = Field(..., pattern="^([01]\d|2[0-3]):([0-5]\d)$", description="Fixed time in HH:MM format")

TimeControlUnion = Union[AstroTimeControl, FixedTimeControl]

class ControlProgram(BaseModel):
    controlProgramId: int = Field(..., ge=0, description="Unique control program ID")
    version: int = Field(..., ge=0, description="Version of the control program")
    name: str = Field(..., description="Name of the control program")
    timeControls: List[TimeControlUnion] = Field(..., description="List of time control settings")