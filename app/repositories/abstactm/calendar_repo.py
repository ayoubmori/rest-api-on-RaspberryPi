from abc import ABC, abstractmethod
from app.models.calendar import Calendar
from typing import List

class CalendarRepository(ABC):
    @abstractmethod
    def add(self, calendar: Calendar) -> str:
        pass

    @abstractmethod
    def get_all(self) -> List[Calendar]:
        pass

    @abstractmethod
    def get_by_id(self, calendar_id: str) -> Calendar:
        pass

    @abstractmethod
    def delete(self, calendar_id: str) -> bool:
        pass



