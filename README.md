## Leostream API caller

This repos contains code to query the Leostream API. The code is written in Python and uses the FastAPI framework.

The following API endpoints are supported:
- centers
- center
- gateways
- gateway
- pools
- pool
- pool-assignments
- pool-assignment

See the Leostream API documentation for more information on these endpoints.

See [here](https://github.com/Joustie/leostream-client-go/blob/main/README.md) for a Golang implementation of a client for  the Leostream REST API.

## How to use

#### Add environment vars needed to access the Leostream API
```bash
export LEOSTREAM_API_HOSTNAME="192.168.178.79"  # required
export LEOSTREAM_API_USERNAME="api"             # required
export LEOSTREAM_API_PASSWORD="System@123"      # required
export LEOSTREAM_API_JSONDIR="json"             # optional
```

#### Create the directory to store the json output if you defined it in the environment vars
```bash
mkdir json
```

#### Install dependencies
```bash
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

## Start server
```
uvicorn main:app --reload
```

##  Browse to api
Go to http://localhost:8000/docs

All methods save the json response body to a file in the designated  json directory of the server.
The output is also written to the console of the server.
