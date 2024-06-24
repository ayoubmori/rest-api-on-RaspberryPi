from fastapi import APIRouter, Body
from app.models.control_program import ControlProgram
from app.constants.http_responces import ExampleResponseServerError, ResponseOK
from app.constants.BodyExmples import *
from app.services.control_program import *

control_prog= APIRouter(tags=["Control Program"])




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
async def add_program(program: ControlProgram = Body(..., example=addProgramBodyExmple)):
    return await Add_Program(program)
 
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
    return await Get_All_Programs()
    
    
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
    return await Get_Program(control_program_id)
        
    
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
    return await Delete_Program(control_program_id)
    
    
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
    return await Update_Control_Program(control_program_id, new_control_program_item)

