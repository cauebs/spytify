from requests_oauthlib import OAuth2Session
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'


class AuthorizationCode:

    def __init__(self, client_id, client_secret, token=None, token_saver=None):
        self.client_secret = client_secret
        self.token_saver = token_saver or (lambda *args: None)

        auto_refresh_kwargs = {'client_id': client_id,
                               'client_secret': client_secret}

        self.session = OAuth2Session(client_id=client_id,
                                     auto_refresh_url=TOKEN_URL,
                                     auto_refresh_kwargs=auto_refresh_kwargs,
                                     token=token,
                                     token_updater=self.token_saver)

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
