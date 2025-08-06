from pydantic import BaseModel


class DespartmentDbModel(BaseModel):
    id:str
    departmentName:str