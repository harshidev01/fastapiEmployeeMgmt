from enum import Enum
from pydantic import BaseModel



class EmployeeDesignationEnum(Enum):
    admin = "ADMIN"
    manager = "MANAGER"
    hr = "HR"
    employee = "EMPLOYEE"
    
    
    
class EmployeeDbModel(BaseModel):
    first_name:str
    last_name:str
    mobile_number:str
    email_id:str
    designation:EmployeeDesignationEnum 
    is_present:bool = False
    
 
    
    
    
    
    
    
    
    
    
    
    
   
        
        
        
        
        
