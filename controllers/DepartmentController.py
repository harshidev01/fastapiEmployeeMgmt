
from fastapi import APIRouter
from models.requestmodels.DepartmentRequestModel import (AddDepartmentRequestModel,
    DeleteDepartmentRequestModel, DeleteDesignationRequestModel, UpdateDepartmentRequestModel,
    UpdateDesignationRequestModel)
from services.DepartmentServices import DepartmentServices


depRouter = APIRouter()
depServices = DepartmentServices()


@depRouter.post("/adddepartment")
def AddDepartment(request:AddDepartmentRequestModel):
    response=  depServices.AddDepartment(request)
    return response

@depRouter.post("/adddesignation")
def AddDesignation(request:AddDepartmentRequestModel):
    response = depServices.AddDesgination(request)
    return response

@depRouter.get("/alldepartments")
def AllDepartments():
    response = depServices.AllDepartments()
    return response

@depRouter.get("/alldesignations")
def AllDesignations():
    response = depServices.AllDesignations()
    return response

@depRouter.post("/updatedepartment")
def UpdateDepartment(request:UpdateDepartmentRequestModel):
    response = depServices.UpdateDepartment(request)
    return response

@depRouter.post("/updatedesignation")
def UpdateDesignation(request:UpdateDesignationRequestModel):
    response = depServices.UpdateDesignation(request)
    return response
    
@depRouter.delete("/deletedepartment")
def DeleteDepartment(request:DeleteDepartmentRequestModel):
    response = depServices.DeleteDepartment(request)
    return response

@depRouter.delete("/deletedesignation")
def DeleteDepartment(request:DeleteDesignationRequestModel):
    response = depServices.DeleteDesignation(request)
    return response