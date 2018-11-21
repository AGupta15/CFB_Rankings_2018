import urllib2
from bs4 import BeautifulSoup
import re
from selenium import webdriver

#================
#    Sagarin
#================
# sagarin = "https://www.usatoday.com/sports/ncaaf/sagarin/"
# page = urllib2.urlopen(sagarin)
# soup = BeautifulSoup(page, "html.parser")

# sag = []
# item_arr = soup.find_all("font")
# for i in range(len(item_arr)):
# 	item = str(item_arr[i].get_text().encode('utf-8'))
# 	item = item.replace("&nbsp", "").replace("AA =", "").replace("A  =", "").strip()
# 	if any(c.isalpha() for c in item):
# 		if any(c.isdigit() for c in item):
# 			if len(item) > 0 and len(item) < 100:
# 				if not item[0].isalpha():
# 					for j in range(len(item)):
# 						if item[j].isalpha():
# 							sag.append(item[j:])
# 							break
#================
#   Anderson
#================
anderson = "http://www.andersonsports.com/football/ACF_frnk.html"
page = urllib2.urlopen(anderson)
soup = BeautifulSoup(page, "html.parser")

ander = []
mid = soup.find_all("table", class_="midrank")
for table in mid:
	items = table.find_all("tr")
	for item in items:
		tds = item.find_all("td")[1]
		if 'height' in tds.attrs:
			ander.append(tds.get_text().encode('ascii', 'ignore').replace(' ', ''))
print ander


#================
#  Billingsley
#================

#================
#    Colley
#================
# colley_url = "http://www.colleyrankings.com/currank.html"
# page = urllib2.urlopen(colley_url)
# soup = BeautifulSoup(page, "html.parser")
# item_arr = soup.find_all("frame")
# colley_url = "http://www.colleyrankings.com" + item_arr[1]['src']
# page = urllib2.urlopen(colley_url)
# soup = BeautifulSoup(page, "html.parser")

# col = []
# for item in soup.find_all("tr"):
# 	tds = item.find_all("td")
# 	if len(tds) > 6:
# 		col.append(tds[1].find("a").get_text())

# col = col[1:]

#================
#    Massey
#================

# browser = webdriver.Chrome()

# url = "https://www.masseyratings.com/cf/ncaa-d1/ratings"
# browser.get(url) #navigate to the page
# soup = BeautifulSoup(browser.page_source, 'html.parser')

# mas = []
# for tr in soup.find_all("tr", class_="bodyrow"):
# 	for td in tr.find_all("td")[0]:
# 		text = td.get_text().replace("FBS", "").replace("NCAA D1", "").replace("FCS", "").replace("HBCU", "")
# 		if len(text)>0:
# 			mas.append(text)

#================
#     Wolfe
#================
# wolfe = "http://prwolfe.bol.ucla.edu/cfootball/ratings.htm"
# page = urllib2.urlopen(wolfe)
# soup = BeautifulSoup(page, "html.parser")
# browser.get(wolfe) #navigate to the page
# soup = BeautifulSoup(browser.page_source, 'html.parser')

# wol = []
# print soup.body
# item_arr = soup.find_all("a")
# for item in item_arr[1:3]:
# 	print item.get_text()

#================
#    ESPN FPI
#================
# espn_fpi = "http://www.espn.com/college-football/statistics/teamratings"
# page = urllib2.urlopen(espn_fpi)
# soup = BeautifulSoup(page, "html.parser")

# fpi = []
# for item in soup.find_all("tr"):
# 	team = item.find("a")
# 	if team is not None:
# 		if "W-L" not in team.get_text():
# 			fpi.append(team.get_text())

#================
#    Coaches
#================
# espn_url = "http://www.espn.com/college-football/rankings"
# page = urllib2.urlopen(espn_url)
# soup = BeautifulSoup(page, "html.parser")

# coaches = []
# for item in soup.find_all("div", class_="column-split"):
# 	if "Coaches Poll" in item.find("h2").get_text():
# 		rows = item.find_all("tr")
# 		for row in rows:
# 			# print row
# 			tds = row.find_all("td")
# 			if len(tds) > 3:
# 				team = tds[1].find("span", class_="team-names").get_text()
# 				points = tds[3].get_text()
# 				coaches.append([team, int(points)])

# others = soup.find_all("div", class_="ranking-details")
# for blob in others[1].find_all("p"):
# 	if "Others receiving votes" in blob.get_text():
# 		text = blob.get_text()
# 		text = text.replace("Others receiving votes: ", "")
# 		text = text.split(",")
# 		for item in text:
# 			for j in range(len(item)):
# 				if item[j].isalpha():
# 					splits = item[j:]
# 					for k in range(len(item)):
# 						if splits[k].isdigit():
# 							team = splits[:k-1]
# 							points = splits[k:]
# 							coaches.append([team, points])
# 							break
# 					break
#================
#   AP Poll
#================
# ap = []
# for item in soup.find_all("div", class_="column-split"):
# 	if "AP Top 25" in item.find("h2").get_text():
# 		rows = item.find_all("tr")
# 		for row in rows:
# 			# print row
# 			tds = row.find_all("td")
# 			if len(tds) > 3:
# 				team = tds[1].find("span", class_="team-names").get_text()
# 				points = tds[3].get_text()
# 				ap.append([team, int(points)])

# others = soup.find_all("div", class_="ranking-details")
# for blob in others[0].find_all("p"):
# 	if "Others receiving votes" in blob.get_text():
# 		text = blob.get_text()
# 		text = text.replace("Others receiving votes: ", "")
# 		text = text.split(",")
# 		for item in text:
# 			for j in range(len(item)):
# 				if item[j].isalpha():
# 					splits = item[j:]
# 					for k in range(len(item)):
# 						if splits[k].isdigit():
# 							team = splits[:k-1]
# 							points = splits[k:]
# 							ap.append([team, points])
# 							break
# 					break

#Compute rankings

#comp = sag + and + bil + col + mas + wol + fpi
#hum = ap + coaches

