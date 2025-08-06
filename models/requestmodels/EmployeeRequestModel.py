from pydantic import BaseModel

class AddEmployeeRequestModel(BaseModel):
    firstName:str
    lastName:str
    emailId:str
    mobileNumber:str
    employeeId:str
    employeeMentType: str
    isPresent:bool = False
    designationId:str
    departmentId:str
    
class UpdateEmployeeRequestModel(BaseModel):
    id:str
    firstName:str
    
class FindEmployeeRequestModel(BaseModel):
    id:str
    
class DeleteEmployeeRequestModel(BaseModel):
    id:str
    