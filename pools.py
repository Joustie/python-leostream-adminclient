from login import LeostreamSession
from webresource import WebResource

class LeostreamPools(WebResource):
    
    def __init__(self) -> None:
        self._api = LeostreamSession()
        self.resource = "pools"
        self._URL="https://"+str(self._api.broker)+"/rest/v1/pools?as+tree=0"
        self.data = self.list()
