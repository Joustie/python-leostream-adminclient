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

To access the Leostream API, you *need* to set the following environment variables:
- LEOSTREAM_API_URL
- LEOSTREAM_API_USERNAME
- LEOSTREAM_API_PASSWORD

#### Example
```bash
export LEOSTREAM_API_HOSTNAME="192.168.178.79"
export LEOSTREAM_API_USERNAME="api"
export LEOSTREAM_API_PASSWORD="System@123"
```

## Start server
```
uvicorn main:app --reload
```

##  Browse to api
Go to http://localhost:8000/docs

All methods save the json response body to a file in the json directory of the server.
The output is also written to the console of the server.
