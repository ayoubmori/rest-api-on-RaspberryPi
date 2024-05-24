from fastapi import APIRouter, HTTPException, Body

from app.constants.http_responces import ExampleResponseServerError,ResponseOK
from app.config.db import Calendar_doc
from app.models.Calendar import Calendar

from bson import ObjectId
from bson.errors import InvalidId

from datetime import date
import random
import string
import json

calendar_route = APIRouter(tags=["Calendar"])

def generate_unique_id():
    return int(''.join(random.choices(string.digits, k=10)))

##POST 
@calendar_route.post('/calendar',
        responses={
        200: {"model": ResponseOK
              , "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    })
async def add_calendar(calendar: Calendar = Body(..., example={
    "calendarId": 587585,
    "version": 1,
    "name": "test1 Calendar",
    "defaultCtrProgId": 542274,
    "rules": [
        {
            "ctrProgId": 1001,
            "timeConditiontype": 1,
            "start": "2024-03-12",
            "end": "2024-10-20"
        },
        {
            "ctrProgId": 1002,
            "timeConditiontype": 2,
            "start": "2024-03-12",
            "end": "2024-10-20"
        }
    ],
    "lamp": [
        {"id": "relay1"}
    ]
})):
    try:
        # Convert string "_id" to ObjectId
        calendar_dict = calendar.dict()
        calendar_dict["calendarId"] = generate_unique_id()
        
        # Convert start and end dates to strings
        for rule in calendar_dict.get("rules", []):
            # Check if start and end are not None and not ObjectId
            if isinstance(rule.get("start"), date):
                rule["start"] = rule["start"].isoformat()
            if isinstance(rule.get("end"), date):
                rule["end"] = rule["end"].isoformat()

        # Insert document into MongoDB collection
        result = Calendar_doc.insert_one(calendar_dict)
        print(calendar_dict)
        print(result)

        # Check if document was inserted successfully
        if result.inserted_id:
            # Remove the '_id' field before returning the response
            calendar_dict.pop('_id', None)
            return {"message": "Calendar added successfully"}
        else:
            raise HTTPException(status_code=500, detail="Failed to add calendar")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
##GET 
@calendar_route.get(
    "/calendar",
        responses={
        200: {"model": ResponseOK
              , "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    }
)
async def get_all_calendar():
    try:
        # Retrieve all documents from the MongoDB collection
        calendar_items = list(Calendar_doc.find({}))
        
        # Convert ObjectId to string format
        for calendar_item in calendar_items:
            calendar_item["_id"] = str(calendar_item["_id"])
        
        # Return the programs
        return calendar_items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
#GET by id 
@calendar_route.get(
    "/calendar/{id}",
    summary="Get calendar by id ",
        responses={
        200: {"model": ResponseOK
              , "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    }
)
async def get_calender_by_id(calendar_id: str):
    try:
        calendar_id = ObjectId(calendar_id)
    except InvalidId:
        return {
            'status_code': 400,
            'message': 'Invalid calendar ID format'
        }

    calender_item = Calendar_doc.find_one({"_id": calendar_id})
    if calender_item :
        calender_item["_id"] = str(calender_item["_id"])
        return calender_item
    else :
        return {
            'status_code':404,
            'message': 'calendar does not exist'}
        
    
    
    
#DELETE by id    
@calendar_route.delete(
        "/calendar/{id}",
        summary="Delete calendar by id ",
        responses={
        200: {"model": ResponseOK
              , "description": "Successful response"},
        500: {
            "model": ExampleResponseServerError,
            "description": "Internal Server Error",
        },
    }
)
async def delete_program(calendar_id: str):
    try:
        calendar_id = ObjectId(calendar_id)
    except InvalidId:
        return {
            'status_code': 400,
            'message': 'Invalid program ID format'
        }
    # Query the collection for the document with the specified _id
    calender_item = Calendar_doc.find_one({"_id": calendar_id})
    if calender_item :
        result = Calendar_doc.delete_one({"_id": calendar_id})
        if result.deleted_count == 1 :
            return {
                'status_code':200,
                'message': 'calendar deleted successfully'}
        else : 
            return {
                'status_code':500,
                'message': 'failed to deleted calendar'}
    else :
        return {
            'status_code':404,
            'message': 'calendar does not exist'}
 