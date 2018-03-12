
import csv

data_is_loaded = False

def load_data():
	readcsv=[]
	with open('US_County_Level_Presidential_Results_12-16.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			if row[0]!='':
				if row[9]!='AK':
					readcsv.append(row)
	return readcsv

def get_data(party='dem', raw=True, sort_ascending=True, year=2016):
	if not data_is_loaded:
		load_data()
	loaded=load_data()
	raw_data_ls={}
	state_total={}
	vote_each_state_ls=[]
	vote_each_state_total_ls=[]
	percent=0
	vote_percent=[]
	for row in loaded:
		if row[9] not in raw_data_ls:
			raw_data_ls[row[9]]=[]
			state_total[row[9]]=[]
		state_total[row[9]].append(row[4])

		if party=='dem':
			raw_data_ls[row[9]].append(row[2])

		if party=='gop':
				raw_data_ls[row[9]].append(row[3])

	for i in raw_data_ls:
		sum=0
		for j in raw_data_ls[i]:
			sum+=float(j)
		vote_each_state_ls.append((i,sum))

	for i in state_total:
		sum_total=0
		for j in state_total[i]:
			sum_total+=float(j)		
		vote_each_state_total_ls.append((i,sum_total))

	for i in vote_each_state_total_ls:
		for j in vote_each_state_ls:
			if i[0]==j[0]:
				percent=j[1]/i[1]
				vote_percent.append((i[0],percent))

	if raw==True:
		sorted_ls_as=sorted(vote_each_state_ls,key=lambda x: x[1], reverse=False)
		sorted_ls_des=sorted(vote_each_state_ls,key=lambda x: x[1], reverse=True)		
	else:
		sorted_ls_as=sorted(vote_percent,key=lambda x: x[1], reverse=False)
		sorted_ls_des=sorted(vote_percent,key=lambda x: x[1], reverse=True)

	if sort_ascending==True:
		return sorted_ls_as
	else:
		return sorted_ls_des

if __name__ == "__main__":

	points = 0

	data = get_data()
	if data[0] == ('WY', 55949.0) and data[-1] == ('CA', 7362490.0):
		points += 3.33

	data = get_data(party='gop', raw=False)
	if data [0][0] == 'DC' and int(data[0][1] * 100) == 4 and \
		data[-1][0] == 'WY' and int(data[-1][1] * 100) == 70:
		points += 3.33

	data = get_data(party='dem', raw=True, sort_ascending=False)
	if data[0] == ('CA', 7362490.0) and data[-1] == ('WY', 55949.0):
		points += 3.34

	print("points :", points)

