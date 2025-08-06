from models.requestmodels.UserRequestModel import AddUserRequestModel, FindOneuserRequestModel
from models.dbmodels.EmployeeDBModel import EmployeeDbModel
from db.MongoDb import EmployeeMgmtDB
from models.requestmodels.EmployeeRequestModel import FindEmployeeRequestModel
from utils.AppUtils import generateRandomId


class UserServices:
    def AddUser(self, request: AddUserRequestModel):
      if request.password != request.reenterPassword:
        return {"data":"PASSWORD DO NOT MATCHED"}
      
      empCollection = EmployeeMgmtDB.employees
      empData = empCollection.find_one({"employeeId": request.employeeId})
      if empData == None:
            return {"data": "NO EMPLOYEE FOUND"}
        
      if empData.get("employeeMentType") != "EMPLOYEE":
              userTempObj = {
                "employeeId":request.employeeId,
                "password": request.password,
                "loggedIn": request.loggedIn,
                "id":empData.get("id")
                }
              userCollection = EmployeeMgmtDB.users
              data = userCollection.insert_one(document=userTempObj)
              if data.inserted_id != 0:
                return {"data": "SUCESS"}
              else:
                return {"data": "ERROR"}
      else:
            return{"data":"EMPLOYEE IS NOT VALID TO CREATE ACCOUNT "}
          
          
    def FindOneUser(self,request:FindOneuserRequestModel):
      userCollection = EmployeeMgmtDB.users
      user = userCollection.find_one({"id":request.id})
      findTempObj = {
        "employeeId":user.get("employeeId"),
        "password":user.get("password"),
        "loggedIn":user.get("loggedIn")  
      }
      if user.get != None:
        return {"data":"SUCESS","userData":findTempObj}
      else:
        return{"data":"ERROR"}
            
            
        
              
            
