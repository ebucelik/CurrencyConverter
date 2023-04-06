#!/usr/bin/env python

from spyne import Application, rpc, ServiceBase, Iterable, Unicode, Float, srpc
from spyne.interface.xml_schema.defn import Element

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.model.primitive import UnsignedInteger32

import Authentication
from CurrencyConverterService import CurrencyConverterService
from InvalidInputError import InvalidInputError
from Authentication import check_authentication, authenticate, AuthenticationError


class CurrencyConverterWebService(ServiceBase):

    service = CurrencyConverterService()

    @rpc(Unicode, _returns=Iterable(Unicode))
    #@check_authentication
    def getCurrencyCodes(ctx, token):
        try:
            authenticate(token)
            return ctx.descriptor.service_class.service.getCurrencyCodes()
        except AuthenticationError as authentication_error:
            raise AuthenticationError(authentication_error.args[0])

    @rpc(Float(default=1), Unicode(default='EUR'), Unicode(default='USD'), Unicode,
          _returns=float,
          _throws=InvalidInputError)
    def getConvertedValue(ctx,
                          current_value,
                          current_currency_code,
                          expected_currency_code,
                          token):
        try:
            authenticate(token)
            try:
                return ctx.descriptor.service_class.service.getConvertedValue(
                    current_value,
                    current_currency_code,
                    expected_currency_code,
                    token
                )
            except ValueError as value_error:
                raise InvalidInputError(value_error.args[0])
        except AuthenticationError as authentication_error:
            raise AuthenticationError(authentication_error.args[0])



application = Application([CurrencyConverterWebService], 'currencyconverter.ac.at.fhcampuswien',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()
