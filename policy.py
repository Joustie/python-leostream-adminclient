from login import LeostreamSession
from webresource import WebResource

class LeostreamPolicy(WebResource):
    
    def __init__(self,id) -> None:
        self._api = LeostreamSession()
        self.resource = "policy"
        self._id = id
        self._URL="https://"+str(self._api.broker)+"/rest/v1/policies/"+ str(self._id)
        self.data = self.get()
