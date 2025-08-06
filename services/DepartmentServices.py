from models.requestmodels.DepartmentRequestModel import (AddDepartmentRequestModel,
    DeleteDepartmentRequestModel, DeleteDesignationRequestModel, UpdateDepartmentRequestModel,
    UpdateDesignationRequestModel)
from db.MongoDb import EmployeeMgmtDB
from utils.AppUtils import generateRandomId


class DepartmentServices:
    def AddDepartment(self, request: AddDepartmentRequestModel):
        depCollection = EmployeeMgmtDB.departments
        depTempObj = {"id": generateRandomId(), "departmentName": request.name}
        data = depCollection.insert_one(document=depTempObj)
        if data.inserted_id != 0:
            return {"data": "SUCESS"}
        else:
            return {"data": "ERROR"}

    def AddDesgination(self, request: AddDepartmentRequestModel):
        desCollection = EmployeeMgmtDB.designations
        desTempObj = {"id": generateRandomId(), "designationName": request.name}
        data = desCollection.insert_one(document=desTempObj)
        if data.inserted_id != 0:
            return {"data": "SUCESS"}
        else:
            return {"data": "ERROR"}

    def AllDepartments(self):
        depCollection = EmployeeMgmtDB.departments
        allDep = depCollection.find()
        temp = []
        for dep in allDep:
            AllDepTempObj = {
                "departmentId": dep.get("id"),
                "departmentName": dep.get("departmentName"),
            }
            temp.append(AllDepTempObj)
        return {"data": "SUCESS", "departmentsData": temp}

    def AllDesignations(self):
        desCollections = EmployeeMgmtDB.designations
        allDes = desCollections.find()
        temp = []
        for des in allDes:
            AllDesTempObj = {
                "designationId": des.get("id"),
                "designationName": des.get("designationName"),
            }
            temp.append(AllDesTempObj)
        return {"data": "SUCESS", "designationaData": temp}

    def UpdateDepartment(self, request: UpdateDepartmentRequestModel):
        depCollections = EmployeeMgmtDB.departments
        data = depCollections.update_one(
            {"id": request.id}, {"$set": {"departmentName": request.departmentName}}
        )
        if data.matched_count != 0:
            return {"data": "SUCESS"}
        else:
            return {"data": "ERROR"}

    def UpdateDesignation(self, request: UpdateDesignationRequestModel):
        desCollection = EmployeeMgmtDB.designations
        data = desCollection.update_one(
            {"id": request.id}, {"$set": {"designationName": request.designationName}}
        )
        if data.matched_count != 0:
            return{"data":"SUCESS"}
        else:
            return{"data":"ERROR"}
        
    def DeleteDepartment(self, request:DeleteDepartmentRequestModel):
        depCollection = EmployeeMgmtDB.departments
        data = depCollection.delete_one({"id":request.id})
        if data.deleted_count != 0:
            return{"data":"SUCESS"}
        else:
            return{"data":"ERROR"}
        
    def DeleteDesignation(self, request:DeleteDesignationRequestModel):
        desCollection = EmployeeMgmtDB.designations
        data = desCollection.delete_one({"id":request.id})
        if data.deleted_count != 0:
            return{"data":"SUCESS"}
        else:
            return{"data":"ERROR"}
        
