import csv
def get_data(csv_file):
	# Open CSV file and return a list of tuples.
	datalist=[]
	with open(csv_file,newline='') as f:
		datareader=csv.reader(f)
		for row in datareader:
			datalist.append(tuple(row))			
	return datalist
print(get_data('data.csv'))
