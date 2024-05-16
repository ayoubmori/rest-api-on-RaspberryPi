from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.constants.http_responces import *
from app.models.DGIP import DigitalInput, DigitalInputs, AllDGIPResponse


degitalinput = APIRouter(tags=["Digital Input"])


class DigitalInputState(BaseModel):
    state: str  # Assuming state can be either "ON" or "OFF"

@degitalinput.get(
    "/digital-inputs",
    responses={
        200: {"model": ResponseOK, "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    },
)
async def get_all_digital_input():
    """Get status of all relays"""
    all_dgip_status = []
    for dgip_id, dgip in DigitalInputs.items():
        all_dgip_status.append(dgip.Get_State())
    return all_dgip_status







