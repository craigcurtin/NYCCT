# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:42:26 2015

@author: Craig, not really ....
"""
#https://raw.githubusercontent.com/codingjester/pycitibike/master/pycitibike/__init__.py
#!/usr/bin/env python

import requests

class Citibike(object):
    """
    A tiny API client for the citibike API
    """
    def __init__(self, host='www.citibikenyc.com'):
      self.host = host

    def stations(self, **kwargs):
        """
        Request a full list of stations for citibike

        :param kwargs: a dict of key values for the API.
            I'm actually not fully sure what this supports yet
        """
        self.stationList = self._get('stations/json', kwargs)
        return self.stationList
        
    def asOfTime(self):
        """
        return the date/time the data was aggregated by Divi
        """
        return self.executionTime
        
    def _get(self, uri, options):
        """
        Quick and dirty wrapper around the requests object to do
        some simple data catching

        :params uri: a string, the uri you want to request
        :params options: a dict, the list of parameters you want to use
        """
        url = "http://%s/%s" % (self.host, uri)
        r = requests.get(url, params=options)
        if r.status_code == 200:
            data = r.json()
            self.executionTime = data['executionTime']
            return  data['stationBeanList']
        else:
            # Throws anything not 200 error
            r.raise_for_status()