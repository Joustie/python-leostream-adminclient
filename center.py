from login import LeostreamSession 
from webresource import WebResource

class LeostreamCenter(WebResource):
    
    def __init__(self,id) -> None:
        self._api = LeostreamSession()
        self.resource = "center"
        self._id = id
        self._URL="https://"+str(self._api.broker)+"/rest/v1/centers/"+ str(self._id)
