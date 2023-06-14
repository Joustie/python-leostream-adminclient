import requests # restful API support
import json     # supports json formatting
import os

class WebResource(object):

    
    
    def list(self):
        self._HEADERS = {
        'Content-Type':'application/json',
        'Authorization': self._api.authenticate()}

        response = requests.get(url=self._URL, headers=self._HEADERS, verify=False)
        data = response.json()
        pretty_json = json.dumps(data, indent=1)
        print(f"The brokers response is\n{pretty_json} \n\n")
        
        self.writefile(data)

        if response:
            return data
        else:
            return {"Broker": "Error"}
    
    def get(self):
        self._HEADERS = {
        'Content-Type':'application/json',
        'Authorization': self._api.authenticate()}

        response = requests.get(url=self._URL, headers=self._HEADERS, verify=False)
        data = response.json()
        pretty_json = json.dumps(data, indent=1)
        print(f"The brokers response is\n{pretty_json} \n\n")
        
        self.writefile(data)
        
        if response:
            return data
        else:
            return {"Broker": "Error"}

    def writefile(self, data):
        # Save the response to a file
        jsondir= os.getenv("LEOSTREAM_API_JSONDIR", ".")
        filename = jsondir + '/' + self.resource + '.json'
        with open(filename, 'w') as f:
            json.dump(data, f, indent=1)
        
