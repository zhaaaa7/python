import csv
biglist=[]
dic={}
mdic={}
fdic={}
with open('gradebook.csv') as csvfile:
	reader=csv.reader(csvfile)
	for row in reader:
		biglist.append(row)
#print(biglist)

print('PART 1')
for i in range(1,len(biglist)-2):
	dic={biglist[0][1]:biglist[i][1], biglist[0][2]:biglist[i][2], biglist[0][3]:biglist[i][3], biglist[0][4]:biglist[i][4]}
	mdic[biglist[i][0]]=dic
print(mdic,'\n')

print('PART 2')
for i in range(1,len(biglist[0])):
	dic={biglist[-2][0]:biglist[-2][i],biglist[-1][0]:biglist[-1][i]}
	fdic[biglist[0][i]]=dic
print(fdic,'\n')


print('PART 3')
def student_average(student_name):
	sum=0
	for i in mdic[student_name]:
		sum+=int(mdic[student_name][i])/float(fdic[i]['max_points'])*float(fdic[i]['weight'])*100
	print(sum)
	return sum
for i in mdic:
	student_average(i)

print('\n')
print('PART 4')
def assn_average(assn_name):
	sum=0
	for i in mdic:
		sum+=int(mdic[i][assn_name])/float(fdic[assn_name]['max_points'])
		aver=sum/6*100
	return aver
for i in fdic:
	print(assn_average(i))

print('\n')



print('PART 5')
def student(name):
	student_grade=[]
	newls=[]
	sum=0
	for i in mdic[name]:
		student_grade.append(int(mdic[name][i])/float(fdic[i]['max_points'])*100)	
		sum+=int(mdic[name][i])/float(fdic[i]['max_points'])*float(fdic[i]['weight'])*100
	student_grade.append(sum)
	for i in student_grade:
		newls.append(str(i)[:4]+'%')
	return (newls,sum)

h=0
for i in mdic:
	h+=student(i)[1]
su=h/6

aver_ls=[]
new_aver_ls=[]
for i in fdic:
	aver_ls.append(assn_average(i))
aver_ls.append(su)
for i in aver_ls:
	new_aver_ls.append(str(i)[:4]+'%')


def format_gradebook():
	k=biglist[0]
	k.append('Grade')
	print ('{:<10}{:>9}{:>9}{:>9}{:>14}{:>9}'.format(k[0],k[1],k[2],k[3],k[4],k[5]))
	print('{:-^60}'.format(''))
	for i in mdic:
		k=student(i)[0]
		print('{:<10}{:>9}{:>9}{:>9}{:>14}{:>9}'.format(i,k[0],k[1],k[2],k[3],k[4]))
	print('{:-^60}'.format(''))
	k=new_aver_ls
	print('{:<10}{:>9}{:>9}{:>9}{:>14}{:>9}'.format('Average',k[0],k[1],k[2],k[3],k[4]))
	return None
format_gradebook()
























