from login import LeostreamSession
from webresource import WebResource

class LeostreamGateway(WebResource):
    
    def __init__(self,id) -> None:
        self._api = LeostreamSession()
        self.resource = "gateway"
        self._id = id
        self._URL="https://"+str(self._api.broker)+"/rest/v1/gateways/"+ str(self._id)
