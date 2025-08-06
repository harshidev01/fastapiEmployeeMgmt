from pydantic import BaseModel
from enum import Enum


class EmployeeDesingationEnum(Enum):
    HR = "HR"
    EMPLOYEE = "EMPLOYEE"
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"


class EmployeeDbModel(BaseModel):
    firstName: str
    lastName: str
    emailId: str
    mobileNumber: str
    employeeId: str
    employeeMentType: EmployeeDesingationEnum
    isPresent: bool
    id: str
    designationId: str
    departmentId: str
