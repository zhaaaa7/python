#proj2.py
import requests
from bs4 import BeautifulSoup
import re

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"html.parser")
count=1
 
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
    count+=1
    if count>10:
    	break



#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url = 'https://www.michigandaily.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"html.parser")
 

top=soup.find(class_="view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-99658157999dd0ac5aa62c2b284dd266")
print(top.get_text())



#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url = 'http://newmantaylor.com/gallery.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"html.parser")

for story_heading in soup.find_all('img'): 
	try:
		print(story_heading.attrs['alt'])
	except:
		print('No alternative text provided!!')




#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
def gethtml(url):
	r = requests.get(url,headers={'User-Agent': 'SI_CLASS'})
	soup = BeautifulSoup(r.text,"html.parser")
	return soup

firl = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
url_list=[firl]
def newpage(first_url):
	basesoup=gethtml(first_url)
	nextpage=basesoup.find(title='Go to next page')
	newurl=nextpage['href']
	#print(newurl)
	first_url='https://www.si.umich.edu/'+newurl
	url_list.append(first_url)
	try:
		newpage(first_url)
	except:
		pass
	return url_list

allpageurl_lst=newpage(firl)

emai_lst=[]
def getcontact(eachsoup):
	emaillink=eachsoup.find_all(class_="field field-name-contact-details field-type-ds field-label-hidden")
	for i in emaillink:
		emai_lst.append(i.a['href'])
	return None

for i in allpageurl_lst:
	isoup=gethtml(i)
	getcontact(isoup)
#print(emai_lst)

#newpage=gethtml('https://www.si.umich.edu/'+newurl)


allemail=[]

for i in emai_lst:
	profilepagesoup=gethtml('https://www.si.umich.edu/'+i)
	perlink=profilepagesoup.find(text=re.compile("@umich"))
	allemail.append(perlink)

count=1
for i in allemail:
	print(count,i)
	count+=1
