from pydantic import BaseModel


class AddDepartmentRequestModel(BaseModel):
    name: str

class AddDesignationRequestModel(BaseModel):
    name:str
    
class UpdateDepartmentRequestModel(BaseModel):
    id :str
    departmentName:str
    
class UpdateDesignationRequestModel(BaseModel):
    id :str
    designationName:str
    
class DeleteDepartmentRequestModel(BaseModel):
    id:str
    
class DeleteDesignationRequestModel(BaseModel):
    id:str