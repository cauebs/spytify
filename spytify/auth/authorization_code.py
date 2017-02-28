from requests_oauthlib import OAuth2Session
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'


class AuthorizationCode:

    def __init__(self, client_id, client_secret, token=None,
                 auto_refresh=True, token_saver=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_saver = token_saver or (lambda *args: None)

        refresh_url = TOKEN_URL if auto_refresh else None
        extra = {'client_id': client_id,
                 'client_secret': client_secret}

        self.session = OAuth2Session(token=token,
                                     client_id=self.client_id,
                                     token_updater=self.token_saver,
                                     auto_refresh_url=refresh_url,
                                     auto_refresh_kwargs=extra)

    def auth_url(self, redirect_uri, scope=()):
        self.session.redirect_uri = redirect_uri
        self.session.scope = scope
        url, state = self.session.authorization_url(AUTH_URL)
        return url

    def fetch_token(self, code):
        token = self.session.fetch_token(TOKEN_URL,
                                         code=code,
                                         client_secret=self.client_secret)
        self.token_saver(token)
        return token

    def refresh_token(self):
        token = self.session.refresh_token(TOKEN_URL,
                                           client_id=self.client_id,
                                           client_secret=self.client_secret)
        return token

    def receive_code(self, port, final_redirect=None):
        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                try:
                    query = urlparse(self.path).query
                    query = parse_qs(query)
                    self.code = query['code'][0]
                except Exception as e:
                    self.send_response(500)
                    self.code = None
                else:
                    if final_redirect:
                        self.send_response(302)
                        self.send_header("Location", final_redirect)
                    else:
                        self.send_response(200)
                finally:
                    self.end_headers()

        address = ('localhost', port)
        server = HTTPServer(address, RequestHandler)
        request, client_address = server.get_request()
        code = RequestHandler(request, client_address, server).code

        return code
