from fastapi import APIRouter, HTTPException, Body
import json

from app.constants.http_responces import ExampleResponseServerError, ResponseOK
from app.models.calendar import Calendar
from app.services.db_services.calendar_mongo import MongoCalendarRepository


calendar_route = APIRouter(tags=["Calendar"])

calendar_repo = MongoCalendarRepository()

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
        inserted_id = calendar_repo.add(calendar)
        return {"state": 200 ,"message": "Calendar added successfully", "id": inserted_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
##GET 
@calendar_route.get(
    "/calendars",
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
        calendar_items = calendar_repo.get_all()
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
        calendar_item = calendar_repo.get_by_id(calendar_id)
        if calendar_item:
            return calendar_item
        else:
            return {
                'status_code': 404,
                'message': 'Calendar does not exist'
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
    
    
    
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
        success = calendar_repo.delete(calendar_id)
        if success:
            return {
                'status_code': 200,
                'message': 'Calendar deleted successfully'
            }
        else:
            return {
                'status_code': 404,
                'message': 'Calendar does not exist'
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))