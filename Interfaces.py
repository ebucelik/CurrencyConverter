#!/usr/bin/env python

from interface import Interface


class BaseCurrenciesInterface(Interface):
    def getCurrencyRateDictionary(self):
        pass


class ConverterInterface(Interface):
    def getConvertedValue(self, current_value, current_currency_code, expected_currency_code):
        pass

    def getCurrencyValue(self, currency_code):
        pass

    def currencyIsValid(self, currency_code):
        pass

    def valueIsValid(self, current_value):
        pass


class CurrencyConverterServiceInterface(Interface):
    def getCurrencyCodes(self):
        pass

    def getConvertedValue(self, current_value, current_currency_code, expected_currency_code, token):
        pass

