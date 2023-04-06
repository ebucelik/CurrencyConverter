#!/usr/bin/env python

from spyne.model.complex import ComplexModel
from spyne.model.primitive import Mandatory


class RequestHeader(ComplexModel):
    __namespace__ = 'currencyconverter.ac.at.fhcampuswien'
    authentication = Mandatory.String
