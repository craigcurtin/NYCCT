# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:32:11 2015

@author: Craig
"""

import Citibike as cb
client = cb.Citibike()
stations = client.stations() #Retrieve a list of stations

print "Data was collected %s" % (client.asOfTime())

for station in stations:
    print "%s has %d/%d bikes available" % (station['stationName'], station['availableDocks'], station['totalDocks'])
    if station['stationName'] == 'Jay St & Tech Pl':
        print station

#http://blog.visual.ly/data-sources/
#https://nycopendata.socrata.com/data?cat=NYC%20BigApps