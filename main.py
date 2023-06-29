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

app = FastAPI()

@app.get("/")
def read_root():
    api = LeostreamSession()
    return {"Broker": api.broker}

@app.get("/all")
def read_all():

    # Get all pools and individual pools
    pools = LeostreamPools()

    # Get all pool assignments
    for item in pools.data:
        pool = LeostreamPool(item['id'])

        # Get all pool assignments for this pool
        poolassignment = LeostreamPoolAssignments(item['id'])
        print("assignment: %s" % poolassignment.data)
        
        # Only get the specific pool assignment if it exists because getting pool assignments 
        # for a pool that has none will return a dict
        if type(poolassignment.data) is not dict:
            print("Pool assignment exists")
            for poolitem in poolassignment.data:
                print("Pool %s Pool assignment: %s" % (pool._id, poolitem['id']))
                poolassignment = LeostreamPoolAssignment(pool._id, poolitem['id'])
        else:
            print("No Pool assignments")
        
    # Get all centers and individual centers
    centers = LeostreamCenters()
    for item in centers.data:
       center = LeostreamCenter(item['id'])

    # Get all policies and individual policies
    policies = LeostreamPolicies()
    for item in policies.data:
       policy = LeostreamPolicy(item['id'])
    
    # Get all gateways and individual gateways
    gateways = LeostreamGateways()
    for item in gateways.data:
      gateway = LeostreamGateway(item['id'])

    return {"Leostream Configuration Saved"}

@app.get("/pools")
def read_pools():
    pools = LeostreamPools()
    return {"Pools": pools.data}

@app.get("/centers")
def read_centers():
    centers = LeostreamCenters()
    return {"Centers": centers.data}

@app.get("/policies")
def read_policies():
    policies = LeostreamPolicies()
    return {"Policies": policies.data}

@app.get("/pools/{item_id}")
def read_item(item_id: int):
    pool = LeostreamPool(item_id)
    return {"Pool" : pool.data }

@app.get("/centers/{item_id}")
def read_item(item_id: int):
    center = LeostreamCenter(item_id)
    return {"Center" : center.data }

@app.get("/gateways")
def gateways():
    gateways = LeostreamGateways()
    return {"Gateways": gateways.data}

@app.get("/gateways/{item_id}")
def read_item(item_id: int):
    gateway = LeostreamGateway(item_id)
    return {"Gateway" : gateway.data }

@app.get("/policies")
def gateways():
    policies = LeostreamPolicies()
    return {"Policies": policies.data}

@app.get("/policy/{item_id}")
def read_item(item_id: int):
    policy = LeostreamPolicy(item_id)
    return {"PolicyID" : policy.data }

@app.get("/poolassignments/{item_id}")
def poolassignments(item_id: int):
    poolassignments = LeostreamPoolAssignments(item_id)
    return {"Pool assignments": poolassignments.data}

@app.get("/poolassignment/{pool_id}/{item_id}")
def read_item(pool_id: int, item_id: int):
    policy = LeostreamPoolAssignment(pool_id, item_id)
    return {"Pool assignment:" : policy.data }
