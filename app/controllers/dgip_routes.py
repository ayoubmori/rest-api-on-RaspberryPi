from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.constants.http_responces import *
from app.models.DGIP import DegitalInputs, DegitalInput


degitalinput = APIRouter(tags=["Digital Input"])


class DigitalInputState(BaseModel):
    state: str  # Assuming state can be either "ON" or "OFF"

@degitalinput.get(
    "/digital-inputs",
    responses={
        200: {"model": ExampleResponseOK, "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    },
)
async def get_all_digital_input():
    """Get status of all relays"""
    all_dgip_status = {}
    for dgip_id, dgip in DegitalInputs.items():
        all_dgip_status[dgip_id] = dgip.Get_State()
    return all_dgip_status







