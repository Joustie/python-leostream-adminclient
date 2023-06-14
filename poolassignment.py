from login import LeostreamSession
from webresource import WebResource
#---------------------------------------------------------
#   Get list of Policies
#   Session id goes in header.   
#   Everything else goes in the PARAMS 
#---------------------------------------------------------

class LeostreamPoolAssignment(WebResource):
    
    def __init__(self, pool_id, id) -> None:
        self._api = LeostreamSession()
        self.resource = "poolassignment"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/policies/"+ str(pool_id)+ "/pool-assignments" + str(id)
