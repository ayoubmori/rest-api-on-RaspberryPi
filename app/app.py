from fastapi import FastAPI
from app.controllers.relay_routes import relay_route 
from app.controllers.dgip_routes import degitalinput

# from fastapi import HTTPException
# from fastapi.responses import JSONResponse
# from fastapi.requests import Request
# from datetime import datetime

# from fastapi import FastAPI, Response, HTTPException
# from datetime import datetime
# from typing import List, Optional
# from pydantic import BaseModel

app = FastAPI(
    title="rest api",
    disable_request_buffering=True,
    disable_response_buffering=True,
    debug=False
    )

app.include_router(relay_route, prefix="/api")
app.include_router(degitalinput, prefix="/api")

