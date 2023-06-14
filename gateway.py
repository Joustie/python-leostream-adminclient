from login import LeostreamSession
from webresource import WebResource
#---------------------------------------------------------
#   Get a specific Gateways
#   Session id goes in header.   
#   Everything else goes in the PARAMS 
#---------------------------------------------------------

class LeostreamGateway(WebResource):
    
    def __init__(self,id) -> None:
        self._api = LeostreamSession()
        self.resource = "gateway"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/gateways/"+ str(id)
