#!/usr/bin/env python

from hashlib import sha256
from decorator import decorator
from spyne.model.fault import Fault


class AuthenticationError(Fault):
    def __init__(self, msg):
        print(msg)
        super(AuthenticationError, self).__init__(faultcode='Client.AuthenticationError', faultstring=msg)


#class AuthenticationError(Exception):
#    pass


#def _check_authentication(func, *args, **kwargs):
#    print("before call")
#    ctx = args[0]
#
#    token = ctx.transport.req.get("HTTP_TOKEN")
#    if token is None or token != "the_token_needed":
#        return "Authentication failed"
#
#    result = func(*args, **kwargs)
#
#    print("after call")
#    return result
#
#
#def check_authentication(f):
#    return decorator(_check_authentication, f)


#def _check_authentication(func, *args, **kw):
#    print("before call")
#    result = func(*args, **kw)
#    print("after call")
#    return result
#
#def check_authentication(f):
#    return decorator(_check_authentication, f)

def authenticate(token):
    if token != sha256(b"lisa123").hexdigest():
        raise AuthenticationError("Invalid authentication token")
    return True


def check_authentication(func):
    def wrapper(ctx, token, *args, **kwargs):
        print(*args)
        print(**kwargs)
        print(token)
        if token != 'mysecrettoken':
            raise AuthenticationError("Invalid authentication token")
        return func(ctx, *args, **kwargs)
    return wrapper

#m = sha256()
#m.update(b"Nobody inspects")
#m.update(b" the spammish repetition")
#print(m.digest())
#print(m.hexdigest())
#
#x = sha256(b"lisa123").hexdigest()
#print(x)