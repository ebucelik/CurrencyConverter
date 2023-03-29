#!/usr/bin/env python

from interface import implements

from BaseCurrencies import BaseCurrencies
from Converter import Converter
from Interfaces import CurrencyConverterServiceInterface


class CurrencyConverterService(implements(CurrencyConverterServiceInterface)):

    def getCurrencyCodes(self):
        base_currencies = BaseCurrencies()
        currency_codes = base_currencies.getCurrencyRateDictionary().keys()
        return list(currency_codes)

    def getConvertedValue(self, current_value, current_currency_code, expected_currency_code):
        converter = Converter()
        rate = converter.getConvertedValue(current_value, current_currency_code, expected_currency_code)
        return rate
