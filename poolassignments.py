from login import LeostreamSession
from webresource import WebResource
#---------------------------------------------------------
#   Get list of Policies
#   Session id goes in header.   
#   Everything else goes in the PARAMS 
#---------------------------------------------------------

class LeostreamPoolAssignments(WebResource):
    
    def __init__(self, pool_id) -> None:
        self._api = LeostreamSession()
        self.resource = "poolassignments"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/policies/"+ str(pool_id)+ "/pool-assignments"
