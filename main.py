from fastapi import FastAPI
from models.userModels import (AddEmployee, EmployeeBankDetails, EmployeeFamilyDetails,
    UpdateEmployee)
from db.Db import database
import uvicorn
from bson import ObjectId


app = FastAPI()


@app.get("/health")
def healthCheck():
    return{"message":"sucessful"}


@app.post("/addemployee")
def addEmployee(employee:AddEmployee):
    employeeCollection = database.Employee
    employeeCollection.insert_one(document=employee.dict())
    return employee

@app.get("/getemployee")
def getEmployee():
    employeeCollection = database.Employee
    allemployee= employeeCollection.find()
    temp = []
    for employee in allemployee:
        employee["_id"] = str(employee["_id"])
        temp.append(employee)
    return {"data":temp} 

@app.get("/getEmployee/{userEmail}")
def getEmployee(userEmail:str):
    employeeCollection = database.Employee
    oneemployee = employeeCollection.find_one({"email":userEmail})
    oneemployee["_id"] = str(oneemployee["_id"])
    return {"data":oneemployee}

@app.post("/updateEmployee")
def updateEmployee(employee:UpdateEmployee):
    employeeCollection = database.Employee
    updateone = employeeCollection.update_one({"email":employee.email},{"$set":{"team":employee.team}})
    if updateone.matched_count == 0:
        return {"message":"not found"}
    else:
        return{"message":"sucessful"}
    
    
@app.delete("/deleteEmployee/{employee_id}")
def deleteEmployee(employee_id:str):
    employeeCollection = database.Employee
    status = employeeCollection.delete_one({"_id":ObjectId(employee_id)})
    if status.deleted_count == 0:
        return{"message":"employee not found"}
    else:
        return{"message":"deleted"}
    
    
@app.post("/addEmployeeFamilyDetails")
def addEmployeefamilyDetails(familyDetails:EmployeeFamilyDetails):
    employeeFamilyDetailsCollection = database.EmployeeFamilyDetails
    employeeFamilyDetailsCollection.insert_one(document=familyDetails.dict())
    return familyDetails
    
    
@app.delete("/deleteFamilyDetails/{employee_Name}")
def deleteFamilyDetails(employee_Name:str):
    employeeFamilyDetailsCollection = database.EmployeeFamilyDetails
    status = employeeFamilyDetailsCollection.delete_one({"employeeName":employee_Name})
    if status.deleted_count == 0:
        return{"message":"employee not found"}
    else:
        return{"message":"deleted"}
    
    
@app.post("/EmployeeBankDetails")
def employeeBankDetails(bankDetails: EmployeeBankDetails):
    employeeBankDetailsCollections = database.EmployeeBankDetails
    employeeBankDetailsCollections.insert_one(document=bankDetails.dict())
    return bankDetails

@app.delete("/deleteBankDetails/{employeeName}")
def deleteBankDetails(employeeName:str):
    employeeBankDetailsCollections = database.EmployeeBankDetails
    status = employeeBankDetailsCollections.delete_one({"name":employeeName})
    if status.deleted_count == 0:
        return{"message":"employee not found"}
    else:
        return{"message":"deleted"}
    


@app.get("/allEmployeeDetails/{employeeEmail}")
def allEmployeeDetails(employeeEmail:str):
    employeeCollection = database.Employee
    employeeFamilyDetailsCollection = database.EmployeeFamilyDetails
    employeeBankDetailsCollection = database.EmployeeBankDetailsCollection
    
    def clean(doc):
        if doc and "_id" in doc:
            doc["_id"]= str(doc["_id"])
        return doc   
    employee = employeeCollection.find_one({"email":employeeEmail})
    family = employeeCollection.find_one({"email":employeeEmail})
    bank = employeeCollection.find_one({"email":employeeEmail})
    return{"employee":clean(employee),"family":clean(family),"bank":clean(bank)}
    
        


if __name__ == "__main__":
    uvicorn.run("main:app",port = 8000, host="0.0.0.0")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    