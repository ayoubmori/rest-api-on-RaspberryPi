from pydantic import BaseModel
from typing import Dict, List
import json
from app.services.GPIO_state import relay_pin_status

class Relay(BaseModel):
    id: str
    state: str = None

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


