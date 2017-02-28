from requests_oauthlib import OAuth2Session
from .model import Artist

import re

URI_REGEX = re.compile(r'spotify:(.+):(.+)')


def clean_uri(uri):
    match = URI_REGEX.match(uri)

    try:
        return match.group(2)
    except AttributeError:
        return uri


class Spotify:

    API_URL = 'https://api.spotify.com/v1/'

    def __init__(self, authorization_code=None,
                 client_credentials=None, session=None):
        if authorization_code:
            pass
        elif client_credentials:
            client_credentials.fetch_token()
            self._session = client_credentials.session
        else:
            self._session = session or OAuth2Session()

    def _get(self, *endpoint, params=None, **kwargs):
        kwargs.update(params or {})

        if isinstance(endpoint, tuple):
            endpoint = '/'.join(endpoint)

        return self._session.get(self.API_URL + endpoint).json()

    def test(self):
        return self._session.get(
            'https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT')

    def track(self, track_id):
        return self._get('tracks', clean_uri(track_id))

    def artist(self, artist_id):
        json = self._get('artists', clean_uri(artist_id))
        return Artist(json, spy=self)
