import requests
import json
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
        
        if response.status_code == 200:
            self.writefile(data)

        if response:
            return data
        else:
            return {"Broker": "Error"}
    
    def get(self):
        self._HEADERS = {
        'Content-Type':'application/json',
        'Authorization': self._api.authenticate()}

        print(f"URL is {self._URL}")
        response = requests.get(url=self._URL, headers=self._HEADERS, verify=False)
        data = response.json()
        pretty_json = json.dumps(data, indent=1)
        print(f"The brokers response is\n{pretty_json} \n\n")
        
        if response.status_code == 200:
            self.writefile(data)
        
        if response:
            return data
        else:
            return {"Broker": "Error"}

    def writefile(self, data):
        # Save the response to a file
        jsondir= os.getenv("LEOSTREAM_API_JSONDIR", ".")
              
        if hasattr(self, '_id') and hasattr(self, '_pool_id') :
            if not os.path.exists(jsondir + '/'+ self.resource):
                os.makedirs(jsondir + '/'+ self.resource)  

            if not os.path.exists(jsondir + '/'+ self.resource  + '/' + str(self._pool_id)):
                os.makedirs(jsondir + '/'+ self.resource + '/' + str(self._pool_id))  
            
            filename = jsondir + '/' + self.resource + '/' + str(self._pool_id) + '/' + str(self._id) + '.json'

        elif hasattr(self, '_id') and not hasattr(self, '_pool_id'):
            if not os.path.exists(jsondir + '/'+ self.resource):
                os.makedirs(jsondir + '/'+ self.resource) 
            filename = jsondir + '/' + self.resource + '/' + str(self._id) + '.json'

        elif hasattr(self, '_pool_id') and not hasattr(self, '_id'):
            if not os.path.exists(jsondir + '/'+ self.resource):
                os.makedirs(jsondir + '/'+ self.resource) 
            filename = jsondir + '/' + self.resource + '/' + str(self._pool_id) + '.json'

        else:    
            filename = jsondir + '/' + self.resource + '.json'

        with open(filename, 'w') as f:
            json.dump(data, f, indent=1)
