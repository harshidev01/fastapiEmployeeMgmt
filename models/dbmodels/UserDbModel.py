from pydantic import BaseModel




class UserDBModel(BaseModel):
    emailId:str
    password:str
    otp:int
    loggedIn:bool
    employeeId:str