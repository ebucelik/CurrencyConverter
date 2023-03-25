#!/usr/bin/env python

import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup

class BaseCurrencies:
    referenceRatesUrl = 'http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'

    def getCurrencyRateDictionary(self):
        currencyRateDict = dict()

        response = requests.get(self.referenceRatesUrl)
        
        xml = BeautifulSoup(response.text, 'xml')
        
        # Find all Cube tags with currency attribute
        cubeArray = xml.findAll('Cube', {"currency": True})
        
        for cube in cubeArray:
            currencyRateDict[cube['currency']] = cube['rate']
        
        return currencyRateDict