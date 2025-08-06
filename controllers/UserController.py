from fastapi import APIRouter
from models.requestmodels.UserRequestModel import AddUserRequestModel, FindOneuserRequestModel
from services.UserServices import UserServices


userRouter = APIRouter()
userServices = UserServices()


@userRouter.post("/createuser")
def AddUser(request:AddUserRequestModel):
    response = userServices.AddUser(request)
    return response

@userRouter.post("/getuser")
def FindOneUser(request:FindOneuserRequestModel):
    response = userServices.FindOneUser(request)
    return response