from enum import Enum
from pydantic import BaseModel



class EmployeeDesignationEnum(Enum):
    admin = "ADMIN"
    manager = "MANAGER"
    hr = "HR"
    employee = "EMPLOYEE"
    
    
    
class AddEmployee(BaseModel):
    first_name:str
    last_name:str
    mobile_number:str
    email_id:str
    designation:EmployeeDesignationEnum 
    is_present:bool = False
    
    
    
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
    
    
    
    
    
    
    
    
    
    
    
   
        
        
        
        
        
