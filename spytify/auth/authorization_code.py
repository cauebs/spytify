from requests_oauthlib import OAuth2Session

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'


class AuthorizationCode:

    def __init__(self, client_id, client_secret, redirect_uri, scope=[], token_saver=None):
        self.client_secret = client_secret
        self.session = OAuth2Session(client_id, redirect_uri, scope,
                                     auto_refresh_url=TOKEN_URL,
                                     auto_refresh_kwargs={'client_id': client_id,
                                                          'client_secret': client_secret},
                                     token_updater=token_saver)

    def fetch_auth_url(self):
        url, state = self._session.authorization_url(AUTH_URL)
        return url

    def fetch_token(self, code):
        token = self._session.fetch_token(TOKEN_URL,
                                          code=code,
                                          client_secret=self.client_secret)
        return token
