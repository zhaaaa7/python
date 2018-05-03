import wikipedia
from bs4 import BeautifulSoup
import re

def getsoup(pagename):
	hp=wikipedia.WikipediaPage(pagename)
	hphtml=hp.html()
	soup = BeautifulSoup(hphtml, 'html.parser')
	return soup


def print_section_titles(soup1):
	sect=soup1.find_all('span', class_='mw-headline')
	print('Section Titles')
	for i in sect:
		print(i.get_text())
	return None


def print_references(soup1):
	count=1
	ref=soup1.find_all(class_="reference-text")
	for lst in ref:
		print(count,lst.get_text())
		count+=1
	return None

usersoup=getsoup('Harry Potter')
print_section_titles(usersoup)
print_references(usersoup)	

def interactive_wiki():
	url = input('Enter page you want to see - ')
	allpage=wikipedia.search(url)
	count=0
	choicedic={}
	for i in allpage:
		print (count,' ',i)
		choicedic[str(count)]=i
		count+=1
	choice = input('Select the page you want - ')
	intersoup=getsoup(choicedic[choice])
	print_section_titles(intersoup)
	print_references(intersoup)

interactive_wiki()


