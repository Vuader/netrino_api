from tachyonic.client import Client
from tachyonic.client.middleware import Token as BaseToken
from tachyonic.client.exceptions import ClientError
from tachyonic.neutrino import constants as const

class Token(BaseToken):
     def __init__(self):
         self.interface = "api"

     def init(self, req, resp):
         resp.headers['Content-Type'] = const.APPLICATION_JSON