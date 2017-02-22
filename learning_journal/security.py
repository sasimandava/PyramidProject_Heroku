from pyramid.security import Allow, Everyone, Authenticated

from passlib.context import CryptContext
password_context = CryptContext(schemes=['pbkdf2_sha512'])
hashed = password_context.encrypt('password')
if password_context.verify('password', hashed):
    print("It matched")

class EntryFactory(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'create'),
        (Allow, Authenticated, 'edit'),
    ]
    def __init__(self, request):
        pass