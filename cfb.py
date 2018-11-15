#Abhimanyu Gupta All Rights Reserved. abhigupta.1600@gmail.com

dataset = []
import csv
with open('rankings.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in reader:
		if len(row) > 0:
			dataset.append(row)

rankings = []
for row in dataset[3:107]:
	arr = []
	for i in range(3):
		if len(arr) <=1:
			if(len(row[i])>0):
				row[i] = row[i].replace(",","")
				arr.append(row[i])
	rankings.append(arr)

#Produce an array of all 130 FBS teams in readable format
teams = []
for row in dataset[108:]:
	arr = []
	if not row[1].isdigit():
		row[0] = row[0]+row[1]
		row[1] = ""
	for i in range(len(row)):
		if(len(row[i])>0):
			row[i] = row[i].replace(",","")
			if row[i].isdigit():
				arr.append(int(row[i]))
			else:
				arr.append(row[i])
	teams.append(arr)

#Collect each teams rankings
# Sagarin - SAG 97
# Anderson - AND 9
# Henderson -  HEN 46
# Billingsley - BIL 20
# Colley - COL 29
# Massey - MAS 71
# Wolfe - WOL 110
# Coaches - USA 104
# Associated Press - AP 10
# Committee - CFP 26
# FPI - FPI 42

#Compute your rankings
scores = []
for team in teams[1:]:

	#Computer Average
	sag = max(26.0 - float(team[97]), 0.0)
	anh = max(26.0 - float(team[9]), 0.0)
	bil = max(26.0 - float(team[20]), 0.0)
	col = max(26.0 - float(team[29]), 0.0)
	mas = max(26.0 - float(team[71]), 0.0)
	wol = max(26.0 - float(team[110]), 0.0)
	fpi = max(26.0 - float(team[42]), 0.0)

	mx = max(sag, anh, bil, col, mas, wol, fpi)
	mn = min(sag, anh, bil, col, mas, wol, fpi)

	comp_avg = (sag+anh+bil+col+mas+wol+fpi-mx-mn)/125.0

	#Human Average
	if not isinstance(team[10], int):
		ap = 0.0
	else:
		ap = max(26.0 - float(team[10]), 0.0)

	if not isinstance(team[104], int):
		coa = 0.0
	else:
		coa = max(26.0 - float(team[104]), 0.0)

	hum_avg = (ap+coa)/50.0

	#Your average 50% Comp, 50% Human
	my_avg = (comp_avg+hum_avg)/2.0

	if not isinstance(team[26], int):
		cfp = 0
	else:
		cfp = int(team[26])

	arr = [team[0], team[1], comp_avg, hum_avg, my_avg, cfp]
	scores.append(arr)

scores.sort(key=lambda x: x[2], reverse=True)
print "========================================="
print "            Computer Rankings         "
print "========================================="
for i in range(len(scores)):
	print str(i+1)+" "+str(scores[i][0])+" "+str(scores[i][2])


scores.sort(key=lambda x: x[3], reverse=True)
print "========================================="
print "            Human Rankings         "
print "========================================="
for i in range(len(scores)):
	print str(i+1)+" "+str(scores[i][0])+" "+str(scores[i][3])

scores.sort(key=lambda x: x[4], reverse=True)
print "========================================="
print "            Abhi's Rankings         "
print "========================================="
for i in range(len(scores)):
	print scores[i][5]
	print str(i+1)+" "+str(scores[i][0])+" "+str(scores[i][4])+" Diff: "+str(i+1-scores[i][5])



