import urllib.parse
import urllib.request
import json
import ssl

base_url = 'https://maps.googleapis.com/maps/api/place/queryautocomplete/json'

# Create a dictionary containing the request parameters
values = dict()
values['input'] = 'North Quad'
values['key'] = 'AIzaSyB5H5fcIcZgHeayvhXGS3xbia6U32N64c4' # ENTER YOUR API KEY HERE

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Encode the dictionary into a Web-appropriate format
data = urllib.parse.urlencode(values)

# Attach the data to the URL
full_url = base_url + '?' + data

# Request the URL
req = urllib.request.Request(full_url)

# Read the response into a Python string
response_str = None
with urllib.request.urlopen(req, context=ctx) as response:
	response_str = response.read().decode()

# Parse the response into a json object
json_response = json.loads(response_str)

# Print the request status
print ('Request status:', json_response['status'])
print(json_response)

# If available, print the predicted places
predictions = json_response.get('predictions', None)
if predictions:
	print ('Predicted places:')
	for place in predictions:
		print (place['description'])
print(json_response['predictions'][0]['place_id'])

