from typing import Union
from fastapi import FastAPI
from login import LeostreamSession
from pools import LeostreamPools
from centers import LeostreamCenters
from pool import LeostreamPool
from center import LeostreamCenter
from gateways import LeostreamGateways
from gateway import LeostreamGateway
from policies import LeostreamPolicies
from policy import LeostreamPolicy
from poolassignments import LeostreamPoolAssignments
from poolassignment import LeostreamPoolAssignment
import jsonpickle

app = FastAPI()

@app.get("/")
def read_root():
    api = LeostreamSession()
    return {"Broker": api.broker}

@app.get("/pools")
def read_pools():
    pools = LeostreamPools()
    return {"Pools": pools.list()}

@app.get("/centers")
def read_centers():
    centers = LeostreamCenters()
    return {"Centers": centers.list()}

@app.get("/policies")
def read_policies():
    policies = LeostreamPolicies()
    return {"Policies": policies.list()}

@app.get("/pools/{item_id}")
def read_item(item_id: int):
    pool = LeostreamPool(item_id)
    leostreamObj = jsonpickle.encode(pool.get())
    return {"Poolid" : leostreamObj }

@app.get("/centers/{item_id}")
def read_item(item_id: int):
    center = LeostreamCenter(item_id)
    leostreamObj = jsonpickle.encode(center.get())
    return {"Centerid" : leostreamObj }

@app.get("/gateways")
def gateways():
    gateways = LeostreamGateways()
    return {"Gateways": gateways.list()}

@app.get("/gateways/{item_id}")
def read_item(item_id: int):
    gateway = LeostreamGateway(item_id)
    leostreamObj = jsonpickle.encode(gateway.get())
    return {"Gatewayid" : leostreamObj }

@app.get("/policies")
def gateways():
    policies = LeostreamPolicies()
    return {"Policies": policies.list()}

@app.get("/policy/{item_id}")
def read_item(item_id: int):
    policy = LeostreamPolicy(item_id)
    leostreamObj = jsonpickle.encode(policy.get())
    return {"PolicyID" : leostreamObj }

@app.get("/poolassignments/{item_id}")
def poolassignments(item_id: int):
    poolassignments = LeostreamPoolAssignments(item_id)
    return {"Pool assignments": poolassignments.list()}

@app.get("/poolassignment/{pool_id}/{item_id}")
def read_item(pool_id: int, item_id: int):
    policy = LeostreamPoolAssignment(pool_id, item_id)
    leostreamObj = jsonpickle.encode(policy.get())
    return {"Pool assignment:" : leostreamObj }
