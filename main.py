from fastapi import FastAPI

from db.database import db
from models.employeeRequestModels import AddEmployeeRequestModel, DeleteEmployee, FindOneRequest,UpdateEmployee
from models.employeeDbModels import EmployeeDesignationEnum

app = FastAPI()


@app.post("/addemployee")
def addEmployee(request: AddEmployeeRequestModel):
    employeeCollection = db.employees
    data = {}
    tempEmpObj = {
        "first_name": request.firstName,
        "last_name": request.lastName,
        "mobile_number": request.mobileNumber,
        "email_id": request.emailId,
        "is_present": request.isPresent,
    }
    if request.employeeMentType == "admin":
        tempEmpObj["designation"] = EmployeeDesignationEnum.admin.value
        data = employeeCollection.insert_one(document=tempEmpObj)
    elif request.employeeMentType == "manager":
        tempEmpObj["designation"] = EmployeeDesignationEnum.manager.value
        data = employeeCollection.insert_one(document=tempEmpObj)
    elif request.employeeMentType == "hr":
        tempEmpObj["designation"] = EmployeeDesignationEnum.hr.value
        data = employeeCollection.insert_one(document=tempEmpObj)
    else:
        tempEmpObj["designation"] = EmployeeDesignationEnum.employee.value
        data = employeeCollection.insert_one(document=tempEmpObj)

    if data.inserted_id != None:
        return {"data": "data inserted"}
    else:
        return {"data": "not inserted"}


@app.post("/findemployee")
def findEmployee(request: FindOneRequest):
    employeeCollection = db.employees
    data = employeeCollection.find_one({"email_id": request.emailId})
    tempFindEmp = {
        "firstName": data.get("first_name"),
        "lastName": data.get("last_name"),
        "mobileNumber": data.get("mobile_number"),
        "emailId": data.get("email_id"),
        "employeeMentType":data.get("designation"),
        "isPresent":data.get("is_present"),
        "emplId":str(data.get("_id"))
    }
    
    if data["_id"] != None:
        return{"data":"found","empldata":tempFindEmp}
    else:
        return{"data":"Not Found"}
    
@app.post("/updateemployee")
def UpdateEmployee(request:UpdateEmployee):
    employeeCollection = db.employees
    data =  employeeCollection.update_one({"email_id":request.emailId},{"$set":{"first_name":request.firstName}})
    if data.matched_count != 0:
        return{"data":"Updated sucessfully"}
    else:
        return{"data":"Not Updated"}
    
@app.delete("/deleteemployee")
def deleteEmployee(request:DeleteEmployee):
    employeeCollection = db.employees
    data = employeeCollection.delete_one({"_id":request.employeeId})
    if data.deleted_count != 0:
        return {"data":"Deleted"}
    else:
        return {"data":"Not Deleted"}
    
@app.get("/getallemployees")
def getAllEmployees():
    employeeCollection = db.employees
    allempl = employeeCollection.find()
    
    temp = []
    for empl in allempl:
        tempGetObj = {
            "firstName": empl.get("first_name"),
            "lastName":empl.get("last_name"),
            "mobileNumber":empl.get("mobile_number"),
            "emailId":empl.get("email_id"),
            "employeeMentType":empl.get("designation"),
            "isPresent":empl.get("is_present")
        }
        temp.append(tempGetObj)
    return {"data":temp}   
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1", port = 8000)