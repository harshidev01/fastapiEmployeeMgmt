from fastapi import FastAPI
from controllers.DepartmentController import depRouter
from controllers.EmployeeController import empRouter


app = FastAPI()


app.include_router(router=depRouter, prefix="/dep")
app.include_router(router=empRouter, prefix="/emp")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=8000, host="127.0.0.1")
