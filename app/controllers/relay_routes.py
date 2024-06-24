from fastapi import APIRouter, HTTPException
from typing import List
from app.models.relay import Relay, relays, RelayConfig, TimeoutRequest, ModeRequest
from app.constants.http_responces import *
from app.services.gpio.GPIO_control import configure_relay

relay_route = APIRouter(tags=["Relay"])

relay_config = RelayConfig()

@relay_route.get(
    "/relays/{relay_id}",
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
    "/relays",
    responses={
        200: {"model": ResponseOK, "description": "Successful response"},
        400: {"model": ExampleResponseBadRequest, "description": "Bad Request"},
        404: {"model": ExampleResponseNotFound, "description": "Not Found"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    },
)
async def change_relay_state(request_body: List[Relay]):
    """Change the state of relays."""
    response = []
    print(request_body)
    for relay_request in request_body:

        relay_id = relay_request.id
        relay_state = relay_request.state.upper()

        if relay_state not in ["ON", "OFF"]:
            error_dict = {"id": relay_id ,"status_code": 400, "responce": "Invalid state. Must be either 'ON' or 'OFF'"}
            response.append(error_dict)
            continue

        if relay_id in relays:
            configure_relay(relay_id, relay_state)
            relays[relay_id].state = relay_state
            response.append({"id": relay_id, "state": relay_state, "status_code": 200, "responce": "Change state of relay successfully"})
        else:
            error_dict = {"id": relay_id,"status_code": 404, "responce": f"Relay with id '{relay_id}' does not exist"}
            response.append(error_dict)

    return response



@relay_route.get(
    "/relays",
    responses={
        200: {"model": ResponseOK, "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    },
)
async def get_all_relays():
    """Get status of all relays"""
    relay_list = []
    for relay_id, relay in relays.items():
        relay_list.append({"id": relay_id, "state": relay.state})
    return relay_list








# Control mode endpoints
@relay_route.get(
    "/relays/config/control_mode",
    responses={
        200: {"description": "Successful response"},
        500: {"description": "Internal Server Error"},
    },
)
async def get_control_mode():
    """Get the control mode for all relays"""
    return {"mode": relay_config.mode}

@relay_route.post(
    "/relays/config/control_mode",
    responses={
        200: {"description": "Successful response"},
        400: {"description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
)
async def set_control_mode(request_body: ModeRequest):
    """Set the control mode for all relays"""
    mode = request_body.mode
    relay_config.mode = mode
    return {"message": "Control mode updated successfully"}

# Timeout configuration endpoints
@relay_route.get(
    "/relays/config/timeout",
    responses={
        200: {"description": "Successful response"},
        500: {"description": "Internal Server Error"},
    },
)
async def get_timeout():
    """Get the timeout configuration for all relays"""
    return {"timeout": relay_config.timeout}

@relay_route.post(
    "/relays/config/timeout",
    responses={
        200: {"description": "Successful response"},
        400: {"description": "Bad Request"},
        500: {"description": "Internal Server Error"},
    },
)
async def set_timeout(request_body: TimeoutRequest):
    """Set the timeout configuration for all relays"""
    timeout = request_body.timeout
    relay_config.timeout = timeout
    return {"message": "Timeout configuration updated successfully"}