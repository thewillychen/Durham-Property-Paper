import csv
import urllib2
from bs4 import BeautifulSoup

def parseData(url):
	print 'In url parsing'
	webpage = urllib2.urlopen(url).read()
	soup = BeautifulSoup(webpage, "html.parser")
	info = ['', '', '', '', '']
	first = [1,1,1,1,1]
	for row in  soup.find_all(["strong","li"]):
		current = row.get_text()
		if "Year Built: " in current and first[0] == 1:
			first[0] = 0
			#print current[12:]
			info[0] = current[12:] #Get year

		if "Heated Area (S/F): "in current and first[1] == 1:
			first[1] = 0
			info[1] = current[18:]
			#print len(current)
			#print current
		if "** Bathroom(s): "in current and first[2] == 1:
			first[2] = 0
			info[2] =  current[16:18]
			#print len(current)
			#print current
		if "** Bedroom(s): "in current and first[3] == 1:
			first[3] = 0
			info[3] =  current[15:]
			#print len(current)
			#print current			
		if "Attached Garage (Y/N): " in current and first[4] == 1:
			first[4] = 0
			info[4] =  current[23:]
		#	print len(current)
			#print current
#	print 'Done parsing'
#	print info
	return info

with open('testSample.csv','rb') as houses:
	reader = csv.reader(houses)
	f = open('testSample1.csv','wb')
	writer = csv.writer(f)
	firstRow = 1
	for row in reader:
		if firstRow == 1:
			writer.writerow(row)
			firstRow = 0
		elif row[0] == 'Parcel ID':
			print ''
			#Do nothing
		else:
			data = row
			url = data[8]
			if url != '':
				parsedData = parseData(url)
				data[9] = parsedData[0]
				data[10] = parsedData[1]
				data[11] = parsedData[2]
				data[12] = parsedData[3]
				data[13] = parsedData[4]
	#			print data
				writer.writerow(data)


#http://property.spatialest.com/nc/durham/property/208461/card/1/building
#row 9 = date built
#row 10 = sqft
#row11 = bathroom
#row12 = bedroom
#13 = attached garage