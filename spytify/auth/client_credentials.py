from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

TOKEN_URL = 'https://accounts.spotify.com/api/token'


def client_credentials(client_id, client_secret):
    client = BackendApplicationClient(client_id=client_id)
    session = OAuth2Session(client=client)
    token = session.fetch_token(token_url=TOKEN_URL,
                                client_id=client_id,
                                client_secret=client_secret)
    return session
