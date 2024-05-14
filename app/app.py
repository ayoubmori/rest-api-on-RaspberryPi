from fastapi import FastAPI
from app.controllers.relay_routes import relay_route 
from app.controllers.dgip_routes import degitalinput


app = FastAPI(
    title="rest api",
    disable_request_buffering=True,
    disable_response_buffering=True,
    debug=False
    )

app.include_router(relay_route, prefix="/api")
app.include_router(degitalinput, prefix="/api")

