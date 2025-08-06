from pydantic import BaseModel


class DesignatioNDbModel(BaseModel):
    id:str
    designationName:str