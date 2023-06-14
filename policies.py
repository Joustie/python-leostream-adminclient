from login import LeostreamSession
from webresource import WebResource
#---------------------------------------------------------
#   Get list of Policies
#   Session id goes in header.   
#   Everything else goes in the PARAMS 
#---------------------------------------------------------

class LeostreamPolicies(WebResource):
    
    def __init__(self) -> None:
        self._api = LeostreamSession()
        self.resource = "policies"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/policies?as+tree=0"
