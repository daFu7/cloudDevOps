import requests
import json
import sys
from urllib.request import urlretrieve

page = 1755

def fetch_and_save_response_NeowsBrowse(apiKey, output_filename):

    # Set the API KEY and the page 1755
    URL_NeoBrowse = "https://api.nasa.gov/neo/rest/v1/neo/browse?"
    params = {
      'page':page,
      'api_key':apiKey
    }
    # Make the API request
    response = requests.get(URL_NeoBrowse,params=params)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Convert response to JSON
        response_json = response.json()
        
        # Save JSON response to a file
        with open(output_filename, 'w') as json_file:
            json.dump(response_json, json_file, indent=4)
        
        print(f"Response saved to {output_filename}")
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")

output_filename = "neowsResponse.json"
apiKey = sys.argv[1]
fetch_and_save_response_NeowsBrowse(apiKey, output_filename)
