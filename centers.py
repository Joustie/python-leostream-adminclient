from login import LeostreamSession
from webresource import WebResource

class LeostreamCenters(WebResource):
    
    def __init__(self) -> None:
        self._api = LeostreamSession()
        self.resource = "centers"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/centers?as+tree=0"
