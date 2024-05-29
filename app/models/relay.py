from pydantic import BaseModel, Field, validator
from typing import Dict, List
import json
from app.services.GPIO_state import relay_pin_status

class Relay(BaseModel):
    id: str
    state: str = None
    #mode: str = "AUTOMATIC"  # default to automatic mode
    #timeout: int = 0  # default timeout to 0, meaning no timeout

    def __init__(self, **data):
        super().__init__(**data)
        if self.state is None:
            self.state = relay_pin_status(self.id)
        
    def Get_State(self):
        self.state = relay_pin_status(self.id)  # Update state
        return {
            'id': self.id,
            'state': self.state
        }
    

relays = {
    'relay1': Relay(id="relay1"),
    'relay2': Relay(id="relay2"),
    'relay3': Relay(id="relay3")
}

class ModeRequest(BaseModel):
    mode: str = Field(..., pattern="^(AUTOMATIC|MANUAL)$", description="Control mode: must be 'AUTOMATIC' or 'MANUAL'")

class TimeoutRequest(BaseModel):
    timeout: int = Field(..., ge=0, description="Timeout period in seconds, must be a non-negative integer")


    
class RelayConfig(BaseModel):
    mode: str = "AUTOMATIC"
    timeout: int = 0
    
