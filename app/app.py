from fastapi import FastAPI
from app.controllers.relay_routes import relay_route 
from app.controllers.dgip_routes import degitalinput
from app.controllers.control_program_routes import control_prog

app = FastAPI(
    title="rest api",
    disable_request_buffering=True,
    disable_response_buffering=True,
    debug=False
    )


app.include_router(relay_route, prefix="/api")
app.include_router(degitalinput, prefix="/api")
app.include_router(control_prog, prefix="/api")