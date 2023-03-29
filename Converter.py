#!/usr/bin/env python

from interface import implements

from BaseCurrencies import BaseCurrencies
from Interfaces import ConverterInterface


class Converter(implements(ConverterInterface)):

    def getCurrencyValue(self, currency_code):
        base_currencies = BaseCurrencies()
        currency_dict = base_currencies.getCurrencyRateDictionary()

        return float(currency_dict[currency_code])

    def getConvertedValue(self, current_value, current_currency_code, expected_currency_code):
        expected_currency_rate = self.getCurrencyValue(expected_currency_code)

        if current_currency_code != 'EUR':
            current_currency_rate = self.getCurrencyValue(current_currency_code)
        else:
            current_currency_rate = 1

        return current_value * expected_currency_rate / current_currency_rate
