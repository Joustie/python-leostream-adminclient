from login import LeostreamSession
from webresource import WebResource
#---------------------------------------------------------
#   Get a specific pool
#   Session id goes in header.   
#   Everything else goes in the PARAMS 
#---------------------------------------------------------

class LeostreamPool(WebResource):
    
    def __init__(self,id) -> None:
        self._api = LeostreamSession()
        self.resource = "pool"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/pools/"+ str(id)
