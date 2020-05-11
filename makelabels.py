# open csv and read 'n' strings
import csv

with open('labels.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	s = []
	for row in spamreader:
		s.append(row[0])


#find n strings another csv
with open('annotation_df.csv', newline='') as csvfile:
	spamreader1 = csv.reader(csvfile, delimiter=',', quotechar='|')
	f = {}
	for idx, row1 in enumerate(spamreader1):
		if idx == 0:
			continue

		pid = row1[18]
		value = int(row1[16])
		if value > 3:
			malignancy = 1
		else:
			malignancy = 0
		f[pid] = malignancy


file = open("2dlabels.csv", "w")
for sid in s:
	print(sid, f[sid[:-4]], file=file, sep=",")


#pick its malignancy value
#write into first csv

