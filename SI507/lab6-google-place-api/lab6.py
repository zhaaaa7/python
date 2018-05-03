import urllib.parse
import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def getplaceid():
	base_url = 'https://maps.googleapis.com/maps/api/place/queryautocomplete/json'

	values = {}
	values['input'] = 'North Quad'
	values['key'] = 'AIzaSyB5H5fcIcZgHeayvhXGS3xbia6U32N64c4' 

	data = urllib.parse.urlencode(values)

	full_url = base_url + '?' + data

	req = urllib.request.Request(full_url)

	response_str = None
	with urllib.request.urlopen(req, context=ctx) as response:
		response_str = response.read().decode()

	json_response = json.loads(response_str)

	placeid=json_response['predictions'][0]['place_id']
	return placeid


def getgeometry():

	base_url = 'https://maps.googleapis.com/maps/api/place/details/json'
	values = {}
	values['placeid'] = getplaceid()
	values['key'] = 'AIzaSyB5H5fcIcZgHeayvhXGS3xbia6U32N64c4' # ENTER YOUR API KEY HERE

	data = urllib.parse.urlencode(values)
	full_url = base_url + '?' + data
	req = urllib.request.Request(full_url)

	response_str = None
	with urllib.request.urlopen(req, context=ctx) as response:
		response_str = response.read().decode()
	json_response = json.loads(response_str)

	lat=json_response['result']['geometry']['location']['lat']
	lng=json_response['result']['geometry']['location']['lng']

	#print(s)
	return (lat,lng)
s='latitude={}, longtitude={}'.format(getgeometry()[0],getgeometry()[1])
print(s)


def restaurantrate():
	base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
	geo=str(getgeometry()[0])+','+str(getgeometry()[1])
	values = {}
	values['location']=geo
	values['radius']=500
	values['types']='restaurant'
	values['key'] = 'AIzaSyB5H5fcIcZgHeayvhXGS3xbia6U32N64c4'
	data = urllib.parse.urlencode(values)
	full_url = base_url + '?' + data
	req = urllib.request.Request(full_url)

	response_str = None
	with urllib.request.urlopen(req, context=ctx) as response:
		response_str = response.read().decode()
	json_response = json.loads(response_str)
	#print(json_response)
	results=json_response.get('results')
	rest_dic={}
	for i in results:
		name=i['name']
		rate=i['rating']
		try:
			price=i['price_level']
		except:
			price=0
		print(name,rate)
		rest_dic[name]=[rate,price]
	return rest_dic
all_dic=restaurantrate()
#print(all_dic)


while True:
	criteria = input("sort by rating or price:")
	print(criteria)
	if criteria=='rating' or criteria=='price':
		break
	else:
		print('no validated criteria, please enter again')			

if criteria=='rating':
	sort_dic=sorted(all_dic,key=lambda x: all_dic[x][0])
elif criteria=='price':
	sort_dic=sorted(all_dic,key=lambda x: all_dic[x][1])

print('sorted one')
for i in sort_dic:
	print(i)







