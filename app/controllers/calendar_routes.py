from fastapi import APIRouter, Body
from app.constants.http_responces import ExampleResponseServerError, ResponseOK
from app.models.calendar import Calendar
from app.constants.BodyExmples import *
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
async def add_calendar(calendar: Calendar = Body(..., example=addCalendarBodyExmple)):
    return await add_calendar(calendar)
    
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
    return await Get_All_Calendar()
    
    
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
    return await Get_Calender_By_Id(calendar_id)
        
    
    
    
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
    return await Delete_Program(calendar_id)