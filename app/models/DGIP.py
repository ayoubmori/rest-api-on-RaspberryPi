from pydantic import BaseModel
from typing import Dict
from app.services.GPIO_state import dgip_pin_status

class DigitalInput(BaseModel):
    id: str
    state: str = None

    def __init__(self, id: str, **kwargs):
        super().__init__(id=id, **kwargs)
        self.state = dgip_pin_status(id)
    
    def Get_State(self):
        self.state = dgip_pin_status(self.id)  # Update state
        return {
            'id': self.id,
            'state': self.state
        }

DigitalInputs = {
    "DIGIN-1": DigitalInput(id="DIGIN-1"),
    "DIGIN-2": DigitalInput(id="DIGIN-2"),
    "DIGIN-3": DigitalInput(id="DIGIN-3"),
    "DIGIN-4": DigitalInput(id="DIGIN-4"),
    "DIGIN-5": DigitalInput(id="DIGIN-5"),
    "DIGIN-6": DigitalInput(id="DIGIN-6"),
    "DIGIN-7": DigitalInput(id="DIGIN-7"),
    "DIGIN-8": DigitalInput(id="DIGIN-8"),
    "DIGIN-9": DigitalInput(id="DIGIN-9"),
    "DIGIN-10": DigitalInput(id="DIGIN-10"),
}



class AllDGIPResponse(BaseModel):
    digital_inputs: Dict[str, DigitalInput]
