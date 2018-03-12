import re
import random

count=0
email_list=[]
tuple_ls=[]
flag=0
f=open('mbox.txt','r')
f_list=f.readlines()
for i in f_list:
	i_list=i.split()
	for j in i_list:
		j=j.lstrip('<')
		x = re.findall('^[a-zA-Z]\S+@\S+\.\S+[a-zA-Z]',j) 
		if len(x) > 0:
			if x[0] not in email_list:
				#print (x[0])
				count+=1
				email_list.append(x[0])
f.close()
print (count)
random_l=random.sample(range(10000,100000),count)
for i in email_list:
	tuple_ls.append((i,random_l[flag]))
	flag+=1
print (tuple_ls)

outfile=open('mbox-anon.txt','w')
for i in f_list:
	for j in tuple_ls:
		if j[0] in i:
			k=i.replace(j[0],'%%'+str(j[1])+'%%')
			i=k
	outfile.write(i)
outfile.close()

outfile=open('mbox-anon-key.txt','w')
for i in tuple_ls:
	l='{}={}\n'.format(i[1],i[0])
	outfile.write(l)
outfile.close()






		


