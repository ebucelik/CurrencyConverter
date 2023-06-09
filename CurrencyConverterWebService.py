#!/usr/bin/env python

from spyne import Application, rpc, ServiceBase, Iterable, Unicode, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from Authentication import authenticate, AuthenticationError
from CurrencyConverterService import CurrencyConverterService
from InvalidInputError import InvalidInputError
from RequestHeader import RequestHeader


class CurrencyConverterWebService(ServiceBase):

    service = CurrencyConverterService()
    __in_header__ = RequestHeader

    @rpc(Unicode, _returns=Iterable(Unicode))
    def getCurrencyCodes(ctx, input):
        try:
            authenticate(ctx.in_header.authentication)
            return ctx.descriptor.service_class.service.getCurrencyCodes()
        except AuthenticationError as authentication_error:
            raise AuthenticationError(authentication_error.args[0])

    @rpc(Float(default=1), Unicode(default='EUR'), Unicode(default='USD'),
         _returns=float,
         _throws=InvalidInputError)
    def getConvertedValue(ctx,
                          current_value,
                          current_currency_code,
                          expected_currency_code):
        try:
            authenticate(ctx.in_header.authentication)
            try:
                return ctx.descriptor.service_class.service.getConvertedValue(
                    current_value,
                    current_currency_code,
                    expected_currency_code
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

    logging.info("listening to http://0.0.0.0:8501")
    logging.info("wsdl is at: http://0.0.0.0:8501/?wsdl")

    server = make_server('0.0.0.0', 8501, wsgi_application)
    server.serve_forever()
