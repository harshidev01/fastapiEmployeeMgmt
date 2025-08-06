from models.requestmodels.EmployeeRequestModel import (AddEmployeeRequestModel,
    DeleteEmployeeRequestModel, FindEmployeeRequestModel, UpdateEmployeeRequestModel)
from db.MongoDb import EmployeeMgmtDB
from models.dbmodels.EmployeeDBModel import EmployeeDesingationEnum
from utils.AppUtils import generateRandomId


class EmployeeServices:
    def AddEmployee(self, request: AddEmployeeRequestModel):
        addEmpTempObj = {
            "firstName": request.firstName,
            "lastName": request.lastName,
            "mobileNumber": request.mobileNumber,
            "emailId": request.emailId,
            "isPresent": request.isPresent,
            "designationId": request.designationId,
            "departmentId": request.departmentId,
            "id":generateRandomId()
        }
        data = {}

        empCollection = EmployeeMgmtDB.employees
        if request.designation == "HR":
            addEmpTempObj["designation"] = EmployeeDesingationEnum.HR.value
            data = empCollection.insert_one(document=addEmpTempObj)
        elif request.designation == "ADMIN":
            addEmpTempObj["designation"] = EmployeeDesingationEnum.ADMIN.value
            data = empCollection.insert_one(document=addEmpTempObj)
        elif request.designation == "MANAGER":
            addEmpTempObj["designation"] = EmployeeDesingationEnum.MANAGER.value
            data = empCollection.insert_one(document=addEmpTempObj)
        else:
            addEmpTempObj["designation"] = EmployeeDesingationEnum.EMPLOYEE.value
            data = empCollection.insert_one(document=addEmpTempObj)
        if data.inserted_id != 0:
            return {"data": "SUCESS"}
        else:
            return {"data": "ERROR"}

    def AllEmpl(self):
        empCollection = EmployeeMgmtDB.employees
        allEmp = empCollection.find()
        temp = []
        for emp in allEmp:
            allEmpTempObj = {
                "firstName": emp.get("firstName"),
                "lastName": emp.get("lastName"),
                "emailId": emp.get("emailId"),
                "mobileNumber": emp.get("mobileNumber"),
                "employeeId": emp.get("employeeId"),
                "designation": emp.get("designation"),
                "isPresent": emp.get("isPresent"),
                "id": emp.get("id"),
                "designationId": emp.get("designationId"),
                "departmentId": emp.get("departmentId")
            }
            temp.append(allEmpTempObj)
        return {"data": "SUCESS", "employeeData": temp}

    def UpdateEmployee(self,request: UpdateEmployeeRequestModel):
        empCollections = EmployeeMgmtDB.employees
        data = empCollections.update_one(
            {"id": request.id}, {"$set": {"firstName": request.firstName}}
        )
        if data.matched_count != 0:
            return {"data": "SUCESS"}
        else:
            return {"data": "ERROR"}
        
    def FindEmployee(self,request:FindEmployeeRequestModel):
        empCollection = EmployeeMgmtDB.employees
        emp = empCollection.find_one({"id":request.id})
        FindTempObj = {
            "firstName": emp.get("firstName"),
                "lastName": emp.get("lastName"),
                "emailId": emp.get("emailId"),
                "mobileNumber": emp.get("mobileNumber"),
                "employeeId": emp.get("employeeId"),
                "designation": emp.get("designation"),
                "isPresent": emp.get("isPresent"),
                "id": emp.get("id"),
                "designationId": emp.get("designationId"),
                "departmentId": emp.get("departmentId")
            
        }
        if emp.get("id") != None:
            return{"data":"SUCESS","employeeData":FindTempObj}
        else:
            return{"data":"ERROR"}
        
    def DeleteEmployee(self,request:DeleteEmployeeRequestModel):
        empCollection = EmployeeMgmtDB.employees
        data = empCollection.delete_one({"id":request.id})
        if data.deleted_count != 0:
            return{"data":"SUCESS"}
        else:
            return{"data":"ERROR"}
        
        
        
        
        
