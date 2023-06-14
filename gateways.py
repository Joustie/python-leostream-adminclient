from login import LeostreamSession
from webresource import WebResource
#---------------------------------------------------------
#   Get list of Gateways
#   Session id goes in header.   
#   Everything else goes in the PARAMS 
#---------------------------------------------------------

class LeostreamGateways(WebResource):
    
    def __init__(self) -> None:
        self._api = LeostreamSession()
        self.resource = "gateways"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/gateways?as+tree=0"
