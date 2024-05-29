from fastapi import APIRouter, HTTPException, Body
from typing import List
from app.models.control_program import ControlProgram
from app.constants.http_responces import ExampleResponseServerError, ResponseOK
from app.services.db_services.control_prog_mongo import MongoControlProgramRepository

control_prog= APIRouter(tags=["Control Program"])

control_program_repo = MongoControlProgramRepository()

def generate_unique_id():
    import random
    import string
    return int(''.join(random.choices(string.digits, k=10)))

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
    try:
        program.controlProgramId = generate_unique_id()
        program_id = control_program_repo.add(program)
        return {"message": "Control program added successfully", "program_id": program_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
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
    try:
        programs = control_program_repo.get_all()
        return programs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
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
    try:
        program = control_program_repo.get_by_id(control_program_id)
        if program:
            return program
        else:
            return {'status_code': 404, 'message': 'Control program does not exist'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
    
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
    try:
        success = control_program_repo.delete(control_program_id)
        if success:
            return {'status_code': 200, 'message': 'Control program deleted successfully'}
        else:
            return {'status_code': 404, 'message': 'Control program does not exist'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
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
    try:
        success = control_program_repo.update(control_program_id, new_control_program_item)
        if success:
            return {"status_code": 200, "message": "Control program updated successfully"}
        else:
            return {'status_code': 404, 'message': 'Control program does not exist'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

