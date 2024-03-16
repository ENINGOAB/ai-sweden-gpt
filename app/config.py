import os
from mongo_crud.database import client

# ENV variables set during deployment
DEPLOYMENT_ENV = os.getenv("DEPLOYMENT_ENV", "development") # <-- PASS DURING DOCKER RUN

def load_tenant_configs(tenant_id:str):
    tenants_db_name = "tenants"
    tenant_db = client[tenants_db_name]
    config_collection = tenant_db["Config"]
    configs:dict = config_collection.find_one({"TENANT_ID":tenant_id})
    return configs