from fastapi import APIRouter, HTTPException, Body
from typing import List
from app.models.control_program import ControlProgram
from app.constants.http_responces import ExampleResponseServerError, ResponseOK
from app.services.db_services.control_prog_mongo import MongoControlProgramRepository

control_prog= APIRouter(tags=["Control Program"])

control_program_repo = MongoControlProgramRepository()



##POST 
@control_prog.post('/control-program',
        responses={
        200: {"model": ResponseOK
              , "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    })
async def add_program(program: ControlProgram = Body(..., example={
    "controlProgramId": 2456468648,
    "version": 1,
    "name": "Sample Control Program",
    "timeControls": [
        {
            "timeEvtType": "Fixed time",
            "dimmingLevel": 50,
            "fixedTime": "12:00",
            "offset": 30
        }
    ]})):
    Add_Program(program)
 
##GET 
@control_prog.get(
    "/control-programs",
        responses={
        200: {"model": ResponseOK
              , "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    }
)
async def get_all_programs():
    Get_All_Programs()
    
    
#GET by id 
@control_prog.get(
    "/control-program/{id}",
    summary="Get Control Program by id ",
        responses={
        200: {"model": ResponseOK
              , "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    }
)
async def get_program(control_program_id: str):
    Get_Program(control_program_id)
        
    
#DELETE by id    
@control_prog.delete(
        "/control-program/{id}",
        summary="Delete Control Program by id ",
        responses={
        200: {"model": ResponseOK
              , "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    }
)
async def delete_program(control_program_id: str):
    Delete_Program(control_program_id)
    
    
@control_prog.put("/control-program/{id}",
        summary="update control Program by id ",
        responses={
        200: {"model": ResponseOK
              , "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    }
)
async def update_control_program(control_program_id: str, new_control_program_item: ControlProgram):
    Update_Control_Program(control_program_id, new_control_program_item)

