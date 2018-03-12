import json
import requests
import wikipedia
import unittest
import webbrowser
import unittest

class Picture():
	def __init__(self,countryname):
		self.title=countryname

	def getpicture(self):         
		base_url = "https://api.flickr.com/services/rest/"
		params_d = {}
		params_d['method'] = 'flickr.photos.search'
		params_d['api_key'] = "e000708b861dce5e414251b565994ada"
		params_d['format'] = 'json'
		params_d['tags'] = [self.title+',symbol']
		params_d['tag_mode'] = 'all'
		params_d['per_page'] = 1
		r = requests.get(base_url, params=params_d)
		return r

	def saveindic(self):
		resp_text = self.getpicture().text
		search_result_diction = json.loads(resp_text[14:-1])
		each_photo = search_result_diction['photos']['photo']
		return each_photo

	def imageurl(self):
		picturedic=self.saveindic()
		url = 'https://www.flickr.com/photos/{}/{}'.format(picturedic[0]['owner'],picturedic[0]['id']) 
		return url

	def openinbrowser(self): 
		webbrowser.open(self.imageurl())

	def __str__(self):
		return 'See a image of *{}* in your broswer.'.format(self.title)

class Wiki():
	def __init__(self,query):
		self.query=query
	def wsummary(self):
		try:		
			return wikipedia.summary(self.query)
		except:		
			return wikipedia.summary(self.query+'(country)')
	def __str__(self):
		return 'The page is {}'.format(self.query)	
		
class Facebook():
	access_token = 'EAACEdEose0cBAAsdSsI3cNKiawqrnXAf8JmLHSh5ynLsdVP5pKskeEHZCAtqgdNqFjMMHJtZC6ENgZARUrhxFZCgx2PhrYZAQIjPOYPdvDOZALWittz0ZBld1I4PnEw5UW1ZCZCZC9HQePwAH9sxfn3bMKV2gVFT5IDYRJ0MhCSBsZBawZDZD'
	if access_token == None:
		access_token = raw_input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ") 

	def __init__(self,fb_class_id):
		self.id=fb_class_id

	def getmessage(self):
		baseurl = "https://graph.facebook.com/v2.3/{}/feed"  
		url_params = {}
		url_params["access_token"] = self.access_token
		url_params["fields"] = "message,created_time"
		url_params["limit"]=250
		r = requests.get(baseurl.format(self.id),params=url_params)
		feed = json.loads(r.text)
		return feed

    # cahce data from Facebook
	def getdic(self):
		try:
			f = open("cnn.txt", 'r')
			cnn= json.loads(f.read())
			f.close()
		except:
			f = open("cnn.txt", 'w')
			f.write(json.dumps(self.getmessage()))
			f.close()
			cnn=self.getmessage()
		return cnn

cnn_dic=Facebook('18793419640').getdic() # create an instance of Facebook class, and also call getdic method


def readfile(filename):
	f=open(filename,'r')
	lines=f.readlines()
	outputlist=[]
	for i in lines:
		outputlist.append(i.strip())
	return outputlist

country_name=readfile('country.txt')

#accumulation
word_countdic={}
for each_massage in cnn_dic['data']:
	if 'message' in each_massage:
		message_list=each_massage['message'].split()
		#print message_list
		for i in message_list:
			if i in country_name:
				if i not in word_countdic:
					word_countdic[i]=0
				word_countdic[i]+=1
#sort
country_common=sorted(word_countdic,key=lambda x: word_countdic[x],reverse=True)[:5]

#list comprehension
name_times=[(i,word_countdic[i]) for i in country_common]
print "\nThe most mentioned five countries are:"
print name_times
print '\n'

#cache url of flicke images
try:
	f = open("imageurl.txt", 'r')
	url_dic= json.loads(f.read())
	f.close()
	#print "use url from cache\n"
except:	
	url_dic={}
	for i in country_common:
		url_dic[i]=Picture(i).imageurl() #create instance of Picture class, and also call imageurl method on all instance of class Picture 
	f=open("imageurl.txt","w")
	f.write(json.dumps(url_dic))
	f.close()

outfile = open("cnn_word.csv","w")
outfile.write("word, counts, imageurl\n")
for i in country_common:	
	outfile.write("{},{},{}\n".format(i.encode('utf-8'),word_countdic[i],url_dic[i]))
outfile.close()


def writefile(countryname):
	f = open(countryname+'.txt', 'w')
	s=Wiki(countryname).wsummary() #create instance of Wiki class, and also call wsummary method on all instance of class Wiki 
	f.write(json.dumps(s))
	f.close()


for i in country_common:
	print i
	#cache data from Wikipedia
	try:
		writefile(i)
	except:
		print "No connection to Internet, please read the data from Wikipedia in cached txt files"

	p=Picture(i) #create instances of Picture class
	try:
		p.openinbrowser() #Calling openinbrowser method on all instance of class Picture
		print p
	except:
		print "No connection to Internet, go to the cvs file and find the url of all images"
	print '\n'


class Fb(unittest.TestCase):       
    def test1(self):   
        self.assertEqual(type(cnn_dic),type({}))

class countrylist(unittest.TestCase):  
    def test2(self): 
    	for i in word_countdic:
    		self.assertEqual(type(word_countdic[i]),type(1))     
    def test3(self): 
    	self.assertEqual(len(country_common),5)
    def test4(self): 
    	self.assertEqual(name_times[1][1]>=name_times[2][1],True)

class readcountry(unittest.TestCase):  
    def test5(self): 
    	self.assertEqual(type(country_name),type([]))     
    def test6(self): 
    	self.assertEqual(type(country_name[1]),type(''))

class urllist(unittest.TestCase):       
    def test7(self): 
    	self.assertEqual(len(url_dic),5)
    def test8(self):   
        self.assertEqual(type(url_dic),type({}))



unittest.main(verbosity=2)