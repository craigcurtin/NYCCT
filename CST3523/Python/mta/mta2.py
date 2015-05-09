# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:07:11 2015

@author: Craig
"""
# read subway/bus info from below, or drop in FF/IE
#http://web.mta.info/status/serviceStatus.txt

import urllib

from lxml import etree

class MTA():
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

class Subway(MTA):
    '''class to hold data about a NYC Subway line'''
    def __init__(self, name, status, text, date, time):
        '''data attributes are named same as XML attributes'''
        self.name = name
        self.status = status
        self.text = text
        self.date = date
        self.time = time

class Bus(MTA):
    '''class to hold data about a NYC Bus line'''
    def __init__(self, name, status, text, date, time):
        '''data attributes are named same as XML attributes'''
        self.name = name
        self.status = status
        self.text = text
        self.date = date
        self.time = time
        
class BT(MTA):
    '''class to hold data about a NYC Bridge and Tunnel line'''
    def __init__(self, name, status, text, date, time):
        '''data attributes are named same as XML attributes'''
        self.name = name
        self.status = status
        self.text = text
        self.date = date
        self.time = time

class LIRR(MTA):
    '''class to hold data about a NYC Bridge and Tunnel line'''
    def __init__(self, name, status, text, date, time):
        '''data attributes are named same as XML attributes'''
        self.name = name
        self.status = status
        self.text = text
        self.date = date
        self.time = time
        
class MetroNorth(MTA):
    '''class to hold data about a MetroNorth line'''
    def __init__(self, name, status, text, date, time):
        '''data attributes are named same as XML attributes'''
        self.name = name
        self.status = status
        self.text = text
        self.date = date
        self.time = time
    
    
class MTAStatus():
    '''Get data from MTA web site
       this mtaData() function returns a dictionary of k,v
       
        KEY-> value is Subway() instance
       '123' -> Subway('123', 'GOOD ...', 'Text', 'Date', 'Time')
       '456' -> Subway('456', 'GOOD ...', 'Text', 'Date', 'Time')
       
       NOTE: ... all MTA Subway lines are not availble
       
       Data is scraped from http://web.mta.info/status/serviceStatus.txt
       
       Drop above http, in your favorite browser to see the data
    
    '''
    def __init__(self):
        url='http://web.mta.info/status/serviceStatus.txt'
        self.subwayDataAsXML=urllib.urlopen(url).read()
        #open('subwayData.xml', "w").write(xmlData)
        self.root = etree.XML(self.subwayDataAsXML)
        # get MTA metadata
        self.responseCode = self.root.xpath('responsecode')[0].text
        self.timeStamp = self.root.xpath('timestamp')[0].text
        
    def getSubway(self):
        '''Subway data'''
        self.subwayDict = {}    
        # iterate through XML data, only care about Subway data for now
        for count in range(len(self.root.xpath('subway/line/name'))):
            subwayName = self.root.xpath('subway/line/name')[count].text
            subwayStatus = self.root.xpath('subway/line/status')[count].text
            subwayText = self.root.xpath('subway/line/text')[count].text
            subwayDate = self.root.xpath('subway/line/Date')[count].text    
            subwayTime = self.root.xpath('subway/line/Time')[count].text
            s = Subway(subwayName, subwayStatus, subwayText, subwayDate, subwayTime)
            # set the SubwayName = Subway() class data
            self.subwayDict[subwayName] = s
        return self.timeStamp, self.subwayDict

    def getBus(self):
        '''Bus data'''
        self.busDict = {}    
        # iterate through XML data, only care about Subway data for now
        for count in range(len(self.root.xpath('bus/line/name'))):
            busName = self.root.xpath('bus/line/name')[count].text
            busStatus = self.root.xpath('bus/line/status')[count].text
            busText = self.root.xpath('bus/line/text')[count].text
            busDate = self.root.xpath('bus/line/Date')[count].text    
            busTime = self.root.xpath('bus/line/Time')[count].text
            b = Bus(busName, busStatus, busText, busDate, busTime)
            # set the SubwayName = Subway() class data
            self.busDict[busName] = b
        return self.timeStamp, self.busDict

    def getBT(self):
        ''' Bridge and Tunnel data'''
        self.btDict = {}    
        # iterate through XML data, only care about Subway data for now
        for count in range(len(self.root.xpath('BT/line/name'))):
            btName = self.root.xpath('BT/line/name')[count].text
            btStatus = self.root.xpath('BT/line/status')[count].text
            btText = self.root.xpath('BT/line/text')[count].text
            btDate = self.root.xpath('BT/line/Date')[count].text    
            btTime = self.root.xpath('BT/line/Time')[count].text
            bt = BT(btName, btStatus, btText, btDate, btTime)
            # set the SubwayName = Subway() class data
            self.btDict[btName] = bt
        return self.timeStamp, self.btDict

    def getLIRR(self):
        ''' Bridge and Tunnel data'''
        self.lirrDict = {}    
        # iterate through XML data, only care about Subway data for now
        for count in range(len(self.root.xpath('LIRR/line/name'))):
            lirrName = self.root.xpath('LIRR/line/name')[count].text
            lirrStatus = self.root.xpath('LIRR/line/status')[count].text
            lirrText = self.root.xpath('LIRR/line/text')[count].text
            lirrDate = self.root.xpath('LIRR/line/Date')[count].text    
            lirrTime = self.root.xpath('LIRR/line/Time')[count].text
            lirr = LIRR(lirrName, lirrStatus, lirrText, lirrDate, lirrTime)
            # set the SubwayName = Subway() class data
            self.lirrDict[lirrName] = lirr
        return self.timeStamp, self.lirrDict

    def getMetroNorth(self):
        ''' Bridge and Tunnel data'''
        self.mnDict = {}    
        # iterate through XML data, only care about Subway data for now
        for count in range(len(self.root.xpath('MetroNorth/line/name'))):
            mnName = self.root.xpath('MetroNorth/line/name')[count].text
            mnStatus = self.root.xpath('MetroNorth/line/status')[count].text
            mnText = self.root.xpath('MetroNorth/line/text')[count].text
            mnDate = self.root.xpath('MetroNorth/line/Date')[count].text    
            mnTime = self.root.xpath('MetroNorth/line/Time')[count].text
            mn = MetroNorth(mnName, mnStatus, mnText, mnDate, mnTime)
            # set the SubwayName = Subway() class data
            self.mnDict[mnName] = mn
        return self.timeStamp, self.mnDict


if __name__ == '__main__':
    mtaStatus=MTAStatus()
    
    timeMTA_ReportedData, subwayDictionary=mtaStatus.getSubway()
    print 'Time MTA Reported Data: %s' % (timeMTA_ReportedData) # this is provided by MTA
    subwayNamesSorted = sorted(subwayDictionary.keys())
    for subwayName in subwayNamesSorted:
        print 'Subway Line: %5s has Status: %s' % (subwayDictionary[subwayName].getName(), subwayDictionary[subwayName].getStatus())
        
    timeMTA_ReportedData, busDictionary=mtaStatus.getBus()
    busNamesSorted = sorted(busDictionary.keys())
    for busName in busNamesSorted:
        print 'Bus Line: %5s has Status: %s' % (busDictionary[busName].getName(), busDictionary[busName].getStatus())

    timeMTA_ReportedData, btDictionary=mtaStatus.getBT()
    btNamesSorted = sorted(btDictionary.keys())
    for btName in btNamesSorted:
        print 'BT Line: %5s has Status: %s' % (btDictionary[btName].getName(), btDictionary[btName].getStatus())

    timeMTA_ReportedData, lirrDictionary=mtaStatus.getLIRR()
    lirrNamesSorted = sorted(lirrDictionary.keys())
    for lirrName in lirrNamesSorted:
        print 'LIRR Line: %5s has Status: %s' % (lirrDictionary[lirrName].getName(), lirrDictionary[lirrName].getStatus())
        
    timeMTA_ReportedData, mnDictionary=mtaStatus.getMetroNorth()
    mnNamesSorted = sorted(mnDictionary.keys())
    for mnName in mnNamesSorted:
        print 'MetroNorth Line: %5s has Status: %s' % (mnDictionary[mnName].getName(), mnDictionary[mnName].getStatus())