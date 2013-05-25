import csv

def parse_data (constituencies, filename) :
	data = file (filename, "r")
	data_reader = csv.reader (data)

	for d in data_reader:
		constituencies [d[0]] = (int(d[1]), int(d[2]))
