from login import LeostreamSession
from webresource import WebResource
#---------------------------------------------------------
#   Get list of Centers
#   Session id goes in header.   
#   Everything else goes in the PARAMS 
#---------------------------------------------------------

class LeostreamCenters(WebResource):
    
    def __init__(self) -> None:
        self._api = LeostreamSession()
        self.resource = "centers"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/centers?as+tree=0"

        
