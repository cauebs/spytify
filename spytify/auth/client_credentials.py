from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

TOKEN_URL = 'https://accounts.spotify.com/api/token'


class ClientCredentials:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        client = BackendApplicationClient(client_id=self.client_id)
        self.session = OAuth2Session(client=client)

    def fetch_token(self):
        token = self.session.fetch_token(token_url=TOKEN_URL,
                                         client_id=self.client_id,
                                         client_secret=self.client_secret)
        return token
