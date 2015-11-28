import csv
import urllib2
from bs4 import BeautifulSoup

webpage = urllib2.urlopen("http://property.spatialest.com/nc/durham/property/106653/card/1/building").read()

soup = BeautifulSoup(webpage, "html.parser")

for row in  soup.find_all(["strong","li"]):
	current = row.get_text()
	if "Year Built: " in current:
		print current[12:] #Get year
	if "Heated Area (S/F): "in current:
		print current[18:]
	#	print len(current)
	#	print current
	if "** Bathroom(s): "in current:
		print current[16:18]
		#print len(current)
		#print current
	if "** Bedroom(s): "in current:
		print current[15:]
		#print len(current)
		#print current			
	if "Attached Garage (Y/N): " in current:
		print current[23:]
	#	print len(current)
	#	print current


	# print 'here'
	# , 'Heated Area (S/F):', 'Bathrooms(s):','Bedroom(s):', 'Attached Garage']
	# print line




# with open('testSample.csv','rb') as houses:
# 	reader = csv.reader(houses)
# 	f = open('testSample1.csv','wb')
# 	writer = csv.writer(f)
# 	firstRow = 1
# 	for row in reader:
# 		if firstRow == 1:
# 			writer.writerow(row)
# 			firstRow = 0
# 		else:
# 			data = row
# 			data[10] = 1999
# 			print data
# 			writer.writerow(data)



#http://property.spatialest.com/nc/durham/property/208461/card/1/building
#row 9 = date built
#row 10 = sqft
#row11 = bathroom
#row12 = bedroom
#13 = attached garage