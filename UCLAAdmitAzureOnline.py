import urllib.request
import json

data = {
    "Inputs": {
        "input":
        [
            {
                'admit': "1",
                'gre': "800",
                'gpa': "4",
                'rank': "1",
            }
        ],
    },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/d5139c79ba904e739c19633d41735af6/services/360a1d5a997f4829a1ed75974d96fce3/execute?api-version=2.0&format=swagger'
# Replace this with the API key for the web service
api_key = 'API_KEY'
headers = {'Content-Type': 'application/json',
           'Authorization': ('Bearer ' + api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
    
