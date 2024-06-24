from fastapi import HTTPException
import random
import string
from app.repositories.calendar_mongo import MongoCalendarRepository

calendar_repo = MongoCalendarRepository()

def generate_unique_id():
    return int(''.join(random.choices(string.digits, k=10)))

async def Add_Calendar(calendar):
    try:
        inserted_id = calendar_repo.add(calendar)
        return {"state": 200 ,"message": "Calendar added successfully", "id": inserted_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
async def Get_All_Calendar():
    try:
        calendar_items = calendar_repo.get_all()
        return calendar_items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

async def Get_Calender_By_Id(calendar_id):
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
    
    
async def Delete_Program(calendar_id):
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
   
    