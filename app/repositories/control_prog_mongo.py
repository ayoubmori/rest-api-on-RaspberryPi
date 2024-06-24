from typing import List, Optional
from bson import ObjectId
from app.config.db import ControlProg
from app.models.control_program import ControlProgram
#from app.repositories.abstactm.control_prog_repo import ControlProgramRepository


class MongoControlProgramRepository():
    def add(self, program: ControlProgram) -> str:
        program_dict = program.dict(by_alias=True)
        result = ControlProg.insert_one(program_dict)
        return str(result.inserted_id)

    def get_all(self) -> List[ControlProgram]:
        program_items = list(ControlProg.find({}))
        return [ControlProgram(**item) for item in program_items]

    def get_by_id(self, program_id: str) -> Optional[ControlProgram]:
        program_item = ControlProg.find_one({"_id": ObjectId(program_id)})
        if program_item:
            return ControlProgram(**program_item)
        return None

    def delete(self, program_id: str) -> bool:
        result = ControlProg.delete_one({"_id": ObjectId(program_id)})
        return result.deleted_count == 1

    def update(self, program_id: str, program: ControlProgram) -> bool:
        program_dict = program.dict(by_alias=True)
        result = ControlProg.replace_one({"_id": ObjectId(program_id)}, program_dict)
        return result.modified_count == 1
