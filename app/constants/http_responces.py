
from pydantic import BaseModel


class ExampleResponseOK(BaseModel):
    id: str 
    state: str = "OFF"


class ExampleResponseBadRequest(BaseModel):
    status: int = 400
    message: str = 'Bad Request'


class ExampleResponseNotFound(BaseModel):
    status: int = 404
    message: str = "Not Found"


class ExampleResponseServerError(BaseModel):
    status: int = 500
    message: str = "Internal Server Erro"
