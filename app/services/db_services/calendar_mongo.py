from typing import List
from app.models.calendar import Calendar
from app.config.db import Calendar_doc
from bson import ObjectId
from app.repositories.calendar_repo import CalendarRepository

class MongoCalendarRepository(CalendarRepository):
    def add(self, calendar: Calendar) -> str:
        calendar_dict = calendar.dict(by_alias=True)
        result = Calendar_doc.insert_one(calendar_dict)
        return str(result.inserted_id)

    def get_all(self) -> List[Calendar]:
        calendar_items = list(Calendar_doc.find({}))
        return [Calendar(**item) for item in calendar_items]

    def get_by_id(self, calendar_id: str) -> Calendar:
        calendar_item = Calendar_doc.find_one({"_id": ObjectId(calendar_id)})
        if calendar_item:
            return Calendar(**calendar_item)
        return None

    def delete(self, calendar_id: str) -> bool:
        result = Calendar_doc.delete_one({"_id": ObjectId(calendar_id)})
        return result.deleted_count == 1



