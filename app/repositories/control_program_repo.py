from abc import ABC, abstractmethod
from app.models.control_program import ControlProgram
from typing import List

class ControlProgramRepository(ABC):
    @abstractmethod
    def add(self, control_program: ControlProgram) -> str:
        pass

    @abstractmethod
    def get_all(self) -> List[ControlProgram]:
        pass

    @abstractmethod
    def get_by_id(self, control_program_id : str) -> ControlProgram:
        pass

    @abstractmethod
    def delete(self, control_program_id : str) -> bool:
        pass


