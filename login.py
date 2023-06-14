# restful api required libraries, use the following commands to install
# python -m pip install requests
# python -m pip install --upgrade pip
import requests # restful API support
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os

class LeostreamSession:

  def __init__(self) -> None:
    self._broker = os.getenv("LEOSTREAM_API_HOSTNAME")
    self._login = os.getenv("LEOSTREAM_API_USERNAME")
    self._password= os.getenv("LEOSTREAM_API_PASSWORD")

  def get_broker(self):
      return self._broker
    
  def set_broker(self, a):
      self._broker = a
 
  broker = property(get_broker, set_broker)

  def authenticate(self):
    #---------------------------------------------------------
    #   Login
    #---------------------------------------------------------
    #print(f"Logging into broker {self._broker} as {self._login}\n\n")
    URL="https://"+str(self._broker)+"/rest/v1/session/login"
    PARAMS = {
    'user_login':self._login,
    'password':self._password
    }
    response = requests.post(url=URL,json=PARAMS, verify=False)

    data = json.loads(response.text)

    sessionID= "Bearer " + data["sid"]
    return sessionID
