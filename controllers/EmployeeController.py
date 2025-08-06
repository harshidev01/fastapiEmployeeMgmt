from fastapi import APIRouter
from models.requestmodels.EmployeeRequestModel import (AddEmployeeRequestModel,
    DeleteEmployeeRequestModel, FindEmployeeRequestModel, UpdateEmployeeRequestModel)
from services.EmployeeServices import EmployeeServices


empRouter = APIRouter()
empServices = EmployeeServices()





@empRouter.post("/addemployee")
def AddEmployee(request:AddEmployeeRequestModel):
    response = empServices.AddEmployee(request)
    return response

@empRouter.get("/allemployees")
def AllEmpl():
    response = empServices.AllEmpl()
    return response

@empRouter.post("/updateemployee")
def UpdateEmployee(request:UpdateEmployeeRequestModel):
    response = empServices.UpdateEmployee(request)
    return response

@empRouter.post("/findemployee")
def FindEmployee(request:FindEmployeeRequestModel):
    response = empServices.FindEmployee(request)
    return response

@empRouter.delete("/deleteemployee")
def DeletEmployee(request:DeleteEmployeeRequestModel):
    response = empServices.DeleteEmployee(request)
    return response
    
    
    
