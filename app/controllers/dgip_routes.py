from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.models.DGIP import DegitalInputs, DegitalInput


degitalinput = APIRouter(tags=["Digital Input"])


class DigitalInputState(BaseModel):
    state: str  # Assuming state can be either "ON" or "OFF"


@degitalinput.get("/digital-inputs", response_description="Successful Response", response_model=DegitalInput)
async def get_digital_input(dgip_id: str):
    """Get the status of a digital input."""
    if dgip_id in DegitalInputs:
        dgip = DegitalInputs[dgip_id]
        return  dgip.get_status()
    else:
        raise HTTPException(
            status_code=404, detail=f"Relay with id '{dgip_id}' does not exist"
        )







