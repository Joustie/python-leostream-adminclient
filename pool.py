from login import LeostreamSession
from webresource import WebResource

class LeostreamPool(WebResource):
    
    def __init__(self,id) -> None:
        self._api = LeostreamSession()
        self.resource = "pool"
        self._id = id
        self._URL="https://"+str(self._api.broker)+"/rest/v1/pools/"+ str(self._id)
