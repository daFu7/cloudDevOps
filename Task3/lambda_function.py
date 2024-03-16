import requests
import json
import sys
import os
from urllib.request import urlretrieve

apiKey = os.environ.get('apiKey')

def lambda_handler(event, context):

    # Set the API KEY and the page 1755
    URL_NeoBrowse = "https://api.nasa.gov/neo/rest/v1/neo/browse?"
    params = {
      'page':event['page'],
      'api_key':apiKey
    }
    # Make the API request
    response = requests.get(URL_NeoBrowse,params=params)
    
    data = response.json()
    return {
         'statusCode' : 200,
         'body' : data
    }
