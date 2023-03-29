#!/usr/bin/env python

import requests
from xml.etree import ElementTree
from bs4 import BeautifulSoup
from interface import implements

from Interfaces import BaseCurrenciesInterface


class BaseCurrencies(implements(BaseCurrenciesInterface)):
    referenceRatesUrl = 'http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'

    def getCurrencyRateDictionary(self):
        currency_rate_dict = dict()

        response = requests.get(self.referenceRatesUrl)
        
        xml = BeautifulSoup(response.text, 'xml')
        
        # Find all Cube tags with currency attribute
        cube_array = xml.findAll('Cube', {"currency": True})
        
        for cube in cube_array:
            currency_rate_dict[cube['currency']] = cube['rate']
        
        return currency_rate_dict
