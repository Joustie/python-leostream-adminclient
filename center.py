from login import LeostreamSession 
from webresource import WebResource
#---------------------------------------------------------
#   Get a specific center
#   Session id goes in header.   
#   Everything else goes in the PARAMS 
#---------------------------------------------------------

class LeostreamCenter(WebResource):
    
    def __init__(self,id) -> None:
        self._api = LeostreamSession()
        self.resource = "center"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/centers/"+ str(id)
