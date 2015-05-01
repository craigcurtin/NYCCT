# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:10:43 2015

@author: Craig
"""

import urllib2
import json

# use vehicles
uri="https://www.car2go.com/api/v2.1/vehicles?loc=hamburg&oauth_consumer_key=car2gowebsite&format=json"
raw_data = urllib2.urlopen(uri)
json_data = json.load(raw_data)
cars = json_data['placemarks']

#
# get all Location names .... why isn't there a Brooklyn?
#
uri="http://www.car2go.com/api/v2.1/locations?&oauth_consumer_key=car2gowebsite&format=json"
raw_data = urllib2.urlopen(uri)
json_data = json.load(raw_data)
locations = json_data['location']
for loc in locations:
    print loc['locationName']
    if loc['locationName'] == 'New York City':
        loc
#
# now we know ... its not Brooklyn, its 'New York City'
#
        
uri="https://www.car2go.com/api/v2.1/vehicles?loc=New%20York%20City&oauth_consumer_key=car2gowebsite&format=json"
raw_data = urllib2.urlopen(uri)
json_data = json.load(raw_data)
cars = json_data['placemarks']
print cars[0]

print """We have %d cars in 'New York City' """ % ( len(cars) )

#
# lets find all the cars in myZipCode
#
# if the car is in my zipCode, display some informatoin about it
#
myZipCode='11231'
for car in cars:
    if myZipCode in car['address']:
        print 'Interior: %s, Exterior: %s, Address: %s' % (car['interior'], car['exterior'], car['address'])



#
# lets get a count of cars in each zip code
#
# we'll create a python dictionary to hold zipCode-->car count
#
from collections import defaultdict
zipCodeToNumberOfCars=defaultdict(lambda:0)

for car in cars:
    streetAddr, zipAndCity = car['address'].split(',')
    zipCode, city = zipAndCity.lstrip().split(' ')
    
    zipCodeToNumberOfCars[zipCode] = zipCodeToNumberOfCars[zipCode] + 1
    print 'Zip %s, City: %s' % (zipCode, city)

#
# print the ZipCode-->car Count
#
for zipCode in zipCodeToNumberOfCars:
    print "Zip code %s has %d cars" % (zipCode, zipCodeToNumberOfCars[zipCode])

#https://www.car2go.com/en/newyorkcity/car2go-apps/
#https://code.google.com/p/car2go/wiki/index_v2_1
