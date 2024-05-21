from fastapi import APIRouter, HTTPException

from app.constants.http_responces import ExampleResponseServerError,ResponseOK
from app.config.db import ControlProgram
from app.models.control_program import Program

from bson import ObjectId
from bson.errors import InvalidId


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
async def add_program(program: Program):
    try:
        # Convert string "_id" to ObjectId
        program_dict = program.dict()
        
        # Insert document into MongoDB collection
        result = ControlProgram.insert_one(program_dict)
        print(program_dict)
        print(result)
        # Check if document was inserted successfully
        if result.inserted_id:
            return {"message": "Contole program added successfully"}
        else:
            raise HTTPException(status_code=500, detail="Failed to add contole program")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
##GET 
@control_prog.get(
    "/control-program",
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
        # Retrieve all documents from the MongoDB collection
        programs = list(ControlProgram.find({}))
        
        # Convert ObjectId to string format
        for program in programs:
            program["_id"] = str(program["_id"])
        
        # Return the programs
        return programs
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
        control_program_id = ObjectId(control_program_id)
    except InvalidId:
        return {
            'status_code': 400,
            'message': 'Invalid contole program ID format'
        }

    program = ControlProgram.find_one({"_id": control_program_id})
    if program :
        program["_id"] = str(program["_id"])
        return program
    else :
        return {
            'status_code':404,
            'message': 'Contole program does not exist'}
        
    
    
    
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
        control_program_id = ObjectId(control_program_id)
    except InvalidId:
        return {
            'status_code': 400,
            'message': 'Invalid contole program ID format'
        }
    # Query the collection for the document with the specified _id
    program = ControlProgram.find_one({"_id": control_program_id})
    if program :
        result = ControlProgram.delete_one({"_id": control_program_id})
        if result.deleted_count == 1 :
            return {
                'status_code':200,
                'message': 'Contole program deleted successfully'}
        else : 
            return {
                'status_code':500,
                'message': 'failed to deleted contole program'}
    else :
        return {
            'status_code':404,
            'message': 'Contole program does not exist'}
    
    
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
async def update_control_program(control_program_id: str, new_control_program_item: Program):
    try:
        control_program_id = ObjectId(control_program_id)
    except InvalidId:
        return {
            'status_code': 400,
            'message': 'Invalid program ID format'
        }

    new_control_program_data = new_control_program_item.dict()

    modified_count = ControlProgram.replace_one({"_id": ObjectId(control_program_id)}, new_control_program_data)

    if modified_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"status_code" : 200 ,
        "message": "Control program replaced successfully"}

