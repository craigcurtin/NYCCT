# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:07:11 2015

@author: Craig
"""
# read subway/bus info from below, or drop in FF/IE
#http://web.mta.info/status/serviceStatus.txt

import urllib

from lxml import etree

class Subway():
    '''class to hold data about a NYC subway line'''
    def __init__(self, name, status, text, date, time):
        '''data attributes are named same as XML attributes'''
        self.name = name
        self.status = status
        self.text = text
        self.date = date
        self.time = time
    def getName(self):
        return self.name
    def getStatus(self):
        return self.status
    def getText(self):
        return self.text
    def getDate(self):
        return self.date
    def getTime(self):
        return self.time
    
def mtaData():
    '''Get data from MTA web site
       this mtaData() function returns a dictionary of k,v
       
        KEY-> value is Subway() instance
       '123' -> Subway('123', 'GOOD ...', 'Text', 'Date', 'Time')
       '456' -> Subway('456', 'GOOD ...', 'Text', 'Date', 'Time')
       
       NOTE: ... all MTA Subway lines are not availble
       
       Data is scraped from http://web.mta.info/status/serviceStatus.txt
       
       Drop above http, in your favorite browser to see the data
    
    '''
    url='http://web.mta.info/status/serviceStatus.txt'
    subwayDataAsXML=urllib.urlopen(url).read()
    #open('subwayData.xml', "w").write(xmlData)
    root = etree.XML(subwayDataAsXML)
    # get MTA metadata
    responseCode = root.xpath('responsecode')[0].text
    timeStamp = root.xpath('timestamp')[0].text

    subwayDict = {}    
    # iterate through XML data, only care about Subway data for now
    for count in range(len(root.xpath('subway/line/name'))):
        subwayName = root.xpath('subway/line/name')[count].text
        subwayStatus = root.xpath('subway/line/status')[count].text
        subwayText = root.xpath('subway/line/text')[count].text
        subwayDate = root.xpath('subway/line/Date')[count].text    
        subwayTime = root.xpath('subway/line/Time')[count].text
        s = Subway(subwayName, subwayStatus, subwayText, subwayDate, subwayTime)
        # set the SubwayName = Subway() class data
        subwayDict[subwayName] = s
    return timeStamp, subwayDict

if __name__ == '__main__':
    timeMTA_ReportedData, subwayDictionary=mtaData()
    print 'Time MTA Reported Data: %s' % (timeMTA_ReportedData) # this is provided by MTA
    
    #subwayNamesSorted = sorted(subwayDictionary, key=lambda key: subwayDictionary[key])
    subwayNamesSorted = sorted(subwayDictionary.keys())
    
    for subwayName in subwayNamesSorted:
        print 'Subway Line: %5s has Status: %s' % (subwayDictionary[subwayName].getName(), subwayDictionary[subwayName].getStatus())