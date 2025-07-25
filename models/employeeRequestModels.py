from pydantic import BaseModel


    
class AddEmployeeRequestModel(BaseModel):
    firstName:str
    lastName:str
    mobileNumber:str
    emailId:str
    employeeMentType:str
    isPresent:bool = False
    
    
class UpdateEmployee(BaseModel):
    emailId :str
    firstName:str  
    
    
class FindOneRequest(BaseModel):
    emailId:str    
    
class DeleteEmployee(BaseModel):
    employeeId:str