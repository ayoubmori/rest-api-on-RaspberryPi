from fastapi import APIRouter, Body
from app.constants.http_responces import ExampleResponseServerError, ResponseOK
from app.models.calendar import Calendar
from app.services.calendar import *

calendar_route = APIRouter(tags=["Calendar"])

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
    add_calendar(calendar)
    
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
    Get_All_Calendar()
    
    
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
    Get_Calender_By_Id(calendar_id)
        
    
    
    
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
    Delete_Program(calendar_id)