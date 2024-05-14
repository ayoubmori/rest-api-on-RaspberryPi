from fastapi import APIRouter, HTTPException

from app.models.relay import Relay, relays, RelayRequest
from app.constants.http_responces import *
from app.services.GPIO_control import turn_relay_on,turn_relay_off

relay_route = APIRouter(tags=["Relay"])


@relay_route.get(
    "/relay",
    responses={
        200: {"model": ExampleResponseOK, "description": "Successful response"},
        404: {"model": ExampleResponseNotFound, "description": "Not Found"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    },
)
async def get_relay(relay_id: str):
    """Get the status of a relay"""
    if relay_id in relays:
        return relays[relay_id].Get_State()
    else:
        raise HTTPException(
            status_code=404, detail=f"Relay with id '{relay_id}' does not exist"
        )


@relay_route.post(
    "/relay/{relay_id}",
    response_description="Successful Response",
    response_model=Relay,
    responses={
        200: {"model": ExampleResponseOK, "description": "Successful response"},
        400: {"model": ExampleResponseBadRequest, "description": "Bad Request"},
        404: {"model": ExampleResponseNotFound, "description": "Not Found"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    },
)
async def change_relay_state(relay_stats: RelayRequest):
    """Change the state of a relay."""
    relay_id = relay_stats.id
    relay_state = relay_stats.state.upper()

    if relay_state not in {"ON", "OFF"}:
        raise HTTPException(
            status_code=400, detail="Invalid state. Must be either 'ON' or 'OFF'."
        )

    if relay_id in relays:
        if relay_state == "ON":
            relays[relay_id].state = "ON"
            turn_relay_on(relay_id)
        elif relay_state == "OFF":
            relays[relay_id].state = "OFF"
            turn_relay_off(relay_id)
        
        return relays[relay_id]
    else:
        raise HTTPException(
            status_code=404, detail=f"Relay with id '{relay_id}' does not exist"
        )



@relay_route.get(
    "/relays",
    responses={
        200: {"model": ExampleResponseOK, "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    },
)
async def get_all_relays():
    """Get status of all relays"""
    relay_status = {}
    for relay_id, relay in relays.items():
        relay_status[relay_id] = relay.Get_State()
    return relay_status
