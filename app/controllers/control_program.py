from fastapi import APIRouter, HTTPException
from app.constants.http_responces import ExampleResponseServerError,ResponseOK



from pymongo import MongoClient
import os



client = MongoClient('mongodb://192.168.1.6:27017/')
db = client['test']
user = db['control_program']


control_prog= APIRouter(tags=["Control Program"])
    
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
        programs = list(user.find({}))
        
        # Convert ObjectId to string format
        for program in programs:
            program["_id"] = str(program["_id"])
        
        # Return the programs
        return programs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))