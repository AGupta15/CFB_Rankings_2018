#Abhimanyu Gupta All Rights Reserved. abhigupta.1600@gmail.com

dataset = []
import csv
with open('rankings_w14a.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in reader:
		if len(row) > 0:
			dataset.append(row)

# Collect ranking names
# rankings = []
# for row in dataset[3:87]:
# 	# print row[1]
# 	arr = []
# 	for i in range(3):
# 		if len(arr) <=1:
# 			if(len(row[i])>0):
# 				row[i] = row[i].replace(",","")
# 				arr.append(row[i])
# 	rankings.append(arr)

#Produce an array of all 130 FBS teams in readable format
for i in range(len(dataset)):
	if dataset[i][0] == 'Team,':
		startIndex = i
# print '========'

teams = []
for row in dataset[startIndex:]:
	# print row[0]
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

# print teams
# Collect each teams rankings
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
#Find indices
print teams[0]
scores = []
i = 0
for item in teams[0]:
	if 'SAG' in item:
		sagIndex = i+1
		print 'SAG ' + str(i)
	elif item in 'AND':
		andIndex = i+1
		print 'AND ' + str(i)
	elif item in 'HEN':
		henIndex = i+1
		print 'HEN ' + str(i)
	elif item in 'BIL':
		bilIndex = i+1
		print 'BIL ' + str(i)
	elif item in 'COL':
		colIndex = i+1
		print 'COL ' + str(i)
	elif item in 'MAS':
		masIndex = i+1
		print 'MAS ' + str(i)
	elif item in 'WOL':
		wolIndex = i+1
		print 'WOL ' + str(i)
	elif item in 'FPI':
		fpiIndex = i+1
		print 'FPI ' + str(i)
	elif item in 'USA':
		usaIndex = i+1
		print 'USA ' + str(i)
	elif item in 'AP':
		apIndex = i+1
		print 'AP ' + str(i)
	i = i + 1
	
	


for team in teams[1:]:
	#Computer Average
	print team[0]
	sag = max(26.0 - float(team[sagIndex]), 0.0)
	anh = max(26.0 - float(team[andIndex]), 0.0)
	bil = max(26.0 - float(team[bilIndex]), 0.0)
	col = max(26.0 - float(team[colIndex]), 0.0)
	mas = max(26.0 - float(team[masIndex]), 0.0)
	wol = max(26.0 - float(team[wolIndex]), 0.0)
	fpi = max(26.0 - float(team[fpiIndex]), 0.0)

	mx = max(sag, anh, bil, col, mas, wol, fpi)
	mn = min(sag, anh, bil, col, mas, wol, fpi)

	comp_avg = (sag+anh+bil+col+mas+wol+fpi)/175.0
	# comp_avg = (sag+anh+bil+col+mas+wol+fpi-mx-mn)/125.0

	# if team[0] == 'OhioSt':
	# 	print team
	# 	print team[andIndex], team[apIndex], team[bilIndex], team[colIndex], team[fpiIndex], team[masIndex], team[sagIndex], team[usaIndex], team[wolIndex]

	# if team[0] == 'Michigan':
	# 	print team
	# 	print team[andIndex], team[apIndex], team[bilIndex], team[colIndex], team[fpiIndex], team[masIndex], team[sagIndex], team[usaIndex], team[wolIndex]

	#Human Average
	if not isinstance(team[apIndex], int):
		ap = 0.0
	else:
		ap = max(26.0 - float(team[apIndex]), 0.0)

	if not isinstance(team[usaIndex], int):
		coa = 0.0
	else:
		coa = max(26.0 - float(team[usaIndex]), 0.0)

	hum_avg = (ap+coa)/50.0
	# print hum_avg

	#Your average 2/3 Comp, 1/3 Human
	my_avg = (comp_avg+comp_avg+hum_avg)/3.0

	# if not isinstance(team[26], int):
	# 	cfp = 0
	# else:
	# 	cfp = int(team[26])

	# arr = [team[0], team[1], comp_avg, hum_avg, my_avg, cfp]
	arr = [team[0], team[1], comp_avg, hum_avg, my_avg]
	scores.append(arr)
	# if 'Ala' in team[0]:
		# print team[0]
		# print sag, anh, bil, col, mas, wol, fpi


scores.sort(key=lambda x: x[3], reverse=True)
# print "========================================="
# print "            Human Rankings         "
# print "========================================="
for i in range(40):
	scores[i].append(i)
# 	print str(i+1)+" "+str(scores[i][0])
# 	# +" "+str(scores[i][3])

scores.sort(key=lambda x: x[2], reverse=True)
# print "========================================="
# print "            Computer Rankings         "
# print "========================================="
for i in range(40):
	scores[i].append(i)
# 	print str(i+1)+" "+str(scores[i][0])
# 	# " "+str(scores[i][2])

scores.sort(key=lambda x: x[4], reverse=True)
print "========================================="
print "            Abhi's Rankings         "
print "========================================="
for i in range(40):
	print str(i+1)+" "+str(scores[i][0])+" "+str(round(scores[i][4], 3))

for i in range(25):
	print '<tr>'
	print "<td>" + str(i+1)+"</td>"
	print "<td>" + str(scores[i][0]) + "</td>"
	print "<td>" + str(round(scores[i][4], 3)) + "</td>"
	print "<td>" + str(scores[i][-2])+ "</td>"
	print "<td>" + str(scores[i][-1])+ "</td>"
	print "<td>" + "</td>"
# 	print '</tr>'

