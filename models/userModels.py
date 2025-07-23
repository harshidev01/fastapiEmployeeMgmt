from pydantic import BaseModel,Field


class AddEmployee(BaseModel):
    firstName:str
    lastName:str
    email:str
    age:int
    desig:str
    team:str
    
    
class UpdateEmployee(BaseModel):
    email:str
    team:str
    
    
class EmployeeFamilyDetails(BaseModel):
    employeeName:str
    fatherName:str
    motherName:str
    email:str
    address:str
    phNo:int
    
    
class EmployeeBankDetails(BaseModel):
    name:str
    acNo:int
    ifscCode:str
    branch:str
    email:str
    
    


