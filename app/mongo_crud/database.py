import os
import certifi
from pymongo import MongoClient

tenant_id = os.environ['TENANT_ID']
connString = os.environ['MONGODB_CONNSTRING']

client = MongoClient(connString, tlsCAFile=certifi.where())

global_db = client["tenants"]
organisationColl = global_db["Organisation"]
r = organisationColl.find_one({"tenant_id":tenant_id})
tenant_db = r["db"]

db = client[tenant_db]
