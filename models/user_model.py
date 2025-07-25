from pydantic import BaseModel

class AddUser(BaseModel):
    employee_id = str
    logged_in:bool
    email_id:str
    password:str