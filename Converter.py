#!/usr/bin/env python

from interface import implements

from BaseCurrencies import BaseCurrencies
from Interfaces import ConverterInterface


class Converter(implements(ConverterInterface)):

    def currencyIsValid(self, currency_code):
        base_currencies = BaseCurrencies()
        valid_currencies = base_currencies.getCurrencyRateDictionary().keys()

        if (currency_code in valid_currencies) or currency_code == 'EUR':
            return True

        raise ValueError("Invalid currency code")

    def valueIsValid(self, current_value):

        if type(current_value) == int or type(current_value) == float:
            if current_value > 0:
                return True
            else:
                raise ValueError("Value must be greater than zero")

    def getCurrencyValue(self, currency_code):
        base_currencies = BaseCurrencies()
        currency_dict = base_currencies.getCurrencyRateDictionary()

        if currency_code == 'EUR':
            return float(1)
        else:
            return float(currency_dict[currency_code])

    def getConvertedValue(self, current_value, current_currency_code, expected_currency_code):

        if (self.currencyIsValid(current_currency_code)) and \
                (self.currencyIsValid(expected_currency_code)) and \
                (self.valueIsValid(current_value)):

            current_currency_rate = self.getCurrencyValue(current_currency_code)
            expected_currency_rate = self.getCurrencyValue(expected_currency_code)

            return current_value * expected_currency_rate / current_currency_rate
