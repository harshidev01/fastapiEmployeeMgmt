from fastapi import FastAPI
from controllers.DepartmentController import depRouter
from controllers.EmployeeController import empRouter
from controllers.UserController import userRouter


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=depRouter, prefix="/dep")
app.include_router(router=empRouter, prefix="/emp")
app.include_router(router=userRouter, prefix="/user")



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=8000, host="127.0.0.1")
