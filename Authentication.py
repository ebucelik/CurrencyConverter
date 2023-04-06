#!/usr/bin/env python

from hashlib import sha256
from spyne.model.fault import Fault


def authenticate(basic_token):
    basic_auth = b'Currencyservice2023:fhcampus10!'

    if not basic_token.startswith('Basic '):
        raise AuthenticationError("Basic authentication required")

    token = basic_token.replace("Basic ", "")

    if token != sha256(basic_auth).hexdigest():
        raise AuthenticationError("Invalid authentication token")
    return True


class AuthenticationError(Fault):
    def __init__(self, msg):
        super(AuthenticationError, self).__init__(faultcode='Client.AuthenticationError', faultstring=msg)
