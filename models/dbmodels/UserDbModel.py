from pydantic import BaseModel




class UserDBModel(BaseModel):
    employeeId:str
    password:str
    loggedIn:bool
   