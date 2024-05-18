from pydantic import BaseModel
from typing import List, Optional, Dict, Union
from typing_extensions import Literal

class TimeControl(BaseModel):
    timeEvtType: Literal["Fixed time", "Astro time"]
    dimmingLevel: int = 0
    fixedTime: Optional[str] = None
    astroTypeEvt: Optional[str] = "Sunrise"
    offset: int = 0
    
class AstroTimeControl(BaseModel):
    timeEvtType: str = "Astro time"
    dimmingLevel: int
    astroTypeEvt: str
    offset: int = 0

class FixedTimeControl(BaseModel):
    timeEvtType: str = "Fixed time"
    dimmingLevel: int
    fixedTime: str
    offset: int = 0

# Union of the two types of time controls
TimeControlUnion = Union[AstroTimeControl, FixedTimeControl]

class Program(BaseModel):
    _id: Dict[str, str]
    controlProgramId: Optional[int] = None
    version: int = 1
    name: str
    timeControls: List[TimeControlUnion]
    _class: str = "app.models.control_program.Program"

    def dict(self, *args, **kwargs):
        data = super().dict(*args, **kwargs)
        data['_class'] = self._class
        return data

