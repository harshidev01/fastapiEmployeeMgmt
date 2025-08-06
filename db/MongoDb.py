from pymongo import MongoClient


cluster = MongoClient("mongodb://localhost:27017/")






EmployeeMgmtDB = cluster.EmployeeMgmt