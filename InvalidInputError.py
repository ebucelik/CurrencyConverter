#!/usr/bin/env python

from spyne.model.fault import Fault


class InvalidInputError(Fault):
    def __init__(self, msg):
        print(msg)
        super(InvalidInputError, self).__init__(faultcode='Client.InvalidInputError', faultstring=msg)
