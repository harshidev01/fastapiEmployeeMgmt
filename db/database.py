from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017/")

db = cluster.employee_mgmt 

