from login import LeostreamSession
from webresource import WebResource

class LeostreamPolicies(WebResource):
    
    def __init__(self) -> None:
        self._api = LeostreamSession()
        self.resource = "policies"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/policies?as+tree=0"
        self.data = self.list()
