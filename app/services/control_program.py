from fastapi import APIRouter, HTTPException, Body
from typing import List
from app.models.control_program import ControlProgram
from app.constants.http_responces import ExampleResponseServerError, ResponseOK
from app.services.db_services.control_prog_mongo import MongoControlProgramRepository

control_program_repo = MongoControlProgramRepository()
   

def generate_unique_id():
    import random
    import string
    return int(''.join(random.choices(string.digits, k=10)))

#post : add control program
def Add_Program(program)
    try:
        program.controlProgramId = generate_unique_id()
        program_id = control_program_repo.add(program)
        return {"message": "Control program added successfully", "program_id": program_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#get : get all control program
def Get_All_Programs()    
    try:
        programs = control_program_repo.get_all()
        return programs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
#get : get by id
def	Get_Program(control_program_id):
    try:
        program = control_program_repo.get_by_id(control_program_id)
        if program:
            return program
        else:
            return {'status_code': 404, 'message': 'Control program does not exist'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
#delete : delete by id
def Delete_Program(control_program_id):
    try:
        success = control_program_repo.delete(control_program_id)
        if success:
            return {'status_code': 200, 'message': 'Control program deleted successfully'}
        else:
            return {'status_code': 404, 'message': 'Control program does not exist'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
    
#put : put by id
def Update_Control_Program(control_program_id, new_control_program_item):
    try:
        success = control_program_repo.update(control_program_id, new_control_program_item)
        if success:
            return {"status_code": 200, "message": "Control program updated successfully"}
        else:
            return {'status_code': 404, 'message': 'Control program does not exist'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


    