from requests_oauthlib import OAuth2Session
from .model import Artist, Track, Album

import re

URI_REGEX = re.compile(r'spotify:(.+):(.+)')


def clean_uri(uri):
    match = URI_REGEX.match(uri)

    try:
        return match.groups()
    except AttributeError:
        return uri


def uri_type(uri):
    return clean_uri(uri)[0]


def uri_id(uri):
    return clean_uri(uri)[1]


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
        print('CALLED', endpoint)

        kwargs.update(params or {})

        return self._session.get(
            self.API_URL + '/'.join(endpoint)).json()

    def test(self):
        return self._session.get(
            'https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT')

    def track(self, track_id):
        json = self._get('tracks', uri_id(track_id))
        return Track(json, spy=self)

    def artist(self, artist_id):
        json = self._get('artists', uri_id(artist_id))
        return Artist(json, spy=self)

    def album(self, album_id):
        json = self._get('albums', uri_id(album_id))
        return Album(json, spy=self)
