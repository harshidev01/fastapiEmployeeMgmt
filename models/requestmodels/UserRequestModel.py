from pydantic import BaseModel


class AddUserRequestModel(BaseModel):
    employeeId:str
    password:str
    reenterPassword:str
    loggedIn:bool = False
    

class FindOneuserRequestModel(BaseModel):
    id:str