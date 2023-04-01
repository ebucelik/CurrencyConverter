#!/usr/bin/env python

import unittest

from Converter import Converter
from BaseCurrencies import BaseCurrencies


class TestBaseCurrenciesMethods(unittest.TestCase):

    def test_getCurrencyCodes_containsKeyValuePairs(self):
        base_currencies = BaseCurrencies()
        currency_codes = base_currencies.getCurrencyRateDictionary()
        self.assertGreater(len(currency_codes), 0,
                           msg="Currencies have not been read correctly")


class TestConverterMethods(unittest.TestCase):

    def test_getConvertedValue_isPositive(self):
        converter = Converter()
        self.assertGreater(converter.getConvertedValue(1, 'EUR', 'USD'), 0,
                           msg="Value to be converted must be higher than 0")

    def test_getConvertedValue_isConvertable(self):
        converter = Converter()
        expected_value = 3.14
        rate_one = converter.getConvertedValue(expected_value, 'EUR', 'USD')
        rate_two = converter.getConvertedValue(rate_one, 'USD', 'EUR')
        self.assertEqual(expected_value, rate_two,
                         msg="Re-converting value is not valid")

    def test_getConvertedValue_invalidCurrentCurrency(self):
        converter = Converter()
        with self.assertRaises(ValueError):
            converter.getConvertedValue(1, 'LISA', 'EUR')
        with self.assertRaises(ValueError):
            converter.getConvertedValue(1, 'EUR', 'MARIE')
        with self.assertRaises(ValueError):
            converter.getConvertedValue(1, 'LISA', 'MARIE')

    def test_getConvertedValue_invalidValue(self):
        converter = Converter()
        self.assertIsNone(converter.getConvertedValue('INVALID', 'EUR', 'USD'),
                          msg="Value to be converted is not valid")
        self.assertIsNone(converter.getConvertedValue(False, 'EUR', 'USD'),
                          msg="Value to be converted is not valid")

    def test_getConvertedValue_invalidParameter(self):
        converter = Converter()
        with self.assertRaises(TypeError, msg="A parameter is missing"):
            converter.getConvertedValue('EUR', 'USD')
        with self.assertRaises(TypeError, msg="A parameter is missing"):
            converter.getConvertedValue(1, 'USD')
        with self.assertRaises(TypeError, msg="A parameter is missing"):
            converter.getConvertedValue()


if __name__ == '__main__':
    unittest.main()
