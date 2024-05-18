from pydantic import BaseModel
from typing import List, Optional, Dict
from typing_extensions import Literal

class TimeControl(BaseModel):
    timeEvtType: Literal["Fixed time", "Astro time"]
    dimmingLevel: int
    fixedTime: Optional[str] = None
    astroTypeEvt: Optional[str] = None
    offset: int

class Program(BaseModel):
    _id: Dict[str, str]
    controlProgramId: int
    version: int
    name: str
    timeControls: List[TimeControl]
    _class: str = "app.models.control_program.Program"

    def dict(self, *args, **kwargs):
        data = super().dict(*args, **kwargs)
        data['_class'] = self._class
        return data

