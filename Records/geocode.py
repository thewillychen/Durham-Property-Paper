from geopy.geocoders import Bing
from geopy.distance import vincenty
import csv

southernBoundaries = ('southern boundaries', (35.95625302831242, -78.92609419345702), (2000,2500,3500))
sherwood = ('sherwood', (36.001420062411256, -78.87215723968244), (1000, 1500, 2500))
rockwood = ('rockwood',(35.972950743249214, -78.9218170838534), (1000, 1500, 2500))
cornwallis = ('cornwallis', (35.97845591554436,-78.95247102687885), (1200, 1700, 2700))
northgate = ('northgate', (36.0242222222222, -78.8996944444444), (1000, 1500, 2500))
lakeshoreG = ('lakeshoreG', (35.932350, -78.835439), (1500, 2000, 3000))
crossingG = ('crossingG', (35.980455, -78.806038), (1000, 1500, 2500))

parks = [southernBoundaries, sherwood, rockwood, cornwallis, northgate, lakeshoreG, crossingG]
#print parks[0][2][0]

#def checkAndWrite():


with open('testGeo.csv','rb') as houses:
	reader = csv.reader(houses)
	geolocator = Bing('')
	f = open('testGeoFill.csv','wb')
	mainWriter = csv.writer(f)
	firstRow = 1
	for house in reader:
		if firstRow == 1:
			mainWriter.writerow(house)
			firstRow = 0
		else:			
			address = house[1]
			print address
			location = geolocator.geocode(address)
			locationGeo = ((location.latitude), (location.longitude))
			house[14] = locationGeo
			column = 15
			for park in parks:		
				dist = vincenty(locationGeo, park[1]).feet	
				house[column] = dist
				column += 1
			mainWriter.writerow(house)
			# print (vincenty(locationGeo, park[1]).feet)
			# print ''


# Southern Boundaries Park - 100 THIRD FORK DRIVE -     (35.95625302831242, -78.92609419345702) + 1000 feet so within 2000, 2500, 3500

# Sherwood Park - 1720 CHEEK ROAD -     (36.001420062411256, -78.87215723968244) - standard 1000, 1500, 2500

# Rockwood Park - 2310 WHITLEY DRIVE - (35.972950743249214, -78.9218170838534) - standard 1000, 1500, 2500

# Cornwallis Road Park -  (35.97845591554436,-78.95247102687885) - 1200, 1700, 2700 

# Northgate - 300 WEST CLUB BOULEVARD - (36.0242222222222, -78.8996944444444)  - standard 1000, 1500, 2500


# Lakeshore Golf Course - (35.932350, -78.835439) 1500, 2000, 3000
#Crossing golf course - ( 35.980455, -78.806038) 1000, 1500, 2500


