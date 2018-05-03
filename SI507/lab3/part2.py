import re

f=open('littlebrother.txt',encoding='ISO-8859-1')
f_list=f.readlines()

count=[0,0,0,0]
for i in f_list:
	i_list=i.split()
	for j in i_list:
		if re.search('.*http:.*',j):
			count[0]+=1
		if re.search('[0-9]',j):
		    count[1]+=1
		if re.search('^[0-9]*$',j):
		    count[2]+=1	
		if re.search('[0-9]+[a-zA-Z]+|[a-zA-Z]+[0-9]',j):
		    count[3]+=1	    
print (count)


