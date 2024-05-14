from pydantic import BaseModel
from typing import Dict
from app.services.GPIO_state import relay_pin_status
from app.services.GPIO_control import turn_relay_on, turn_relay_off

class Relay(BaseModel):
    id: str
    state: str = None

    def __init__(self, id: str, **kwargs):
        super().__init__(id=id, **kwargs)
        self.state = relay_pin_status(id)
        
    def Get_State(self):
        self.state = relay_pin_status(self.id)  # Update state
        return {
            'id': self.id,
            'state': self.state
        }
    
    
class RelayRequest(BaseModel):
    """
    Represents a request to change the state of a relay.

    :param id: The ID of the relay.
    :type id: str
    :param state: The state to set the relay to. Must be either 'ON' or 'OFF'.
    :type state: str
    """
    id: str = "relay1"
    state: str = "off"
        


relays = {
    'relay1': Relay(id="relay1"),
    'relay2': Relay(id="relay2"),
    'relay3': Relay(id="relay3")
}

class AllRelaysResponse(BaseModel):
    relays: Dict[str, Relay]
