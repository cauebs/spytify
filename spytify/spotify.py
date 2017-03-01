from .model import Artist, Track, Album
from oauthlib.oauth2 import TokenExpiredError

import re
import requests

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

    def __init__(self, auth=None):
        self.auth = auth

    def _get(self, *endpoint, params=None, **kwargs):
        print('CALLED', endpoint)

        kwargs.update(params or {})

        endpoint = '/'.join(endpoint)

        if self.auth:
            try:
                response = self.auth.session.get(self.API_URL + endpoint)
            except TokenExpiredError:
                self.auth.refresh_token()
                response = self.auth.session.get(self.API_URL + endpoint)

        else:
            response = requests.get(self.API_URL + endpoint)

        return response.json()

    def track(self, track_id):
        json = self._get('tracks', uri_id(track_id))
        return Track(json, spy=self)

    def artist(self, artist_id):
        json = self._get('artists', uri_id(artist_id))
        return Artist(json, spy=self)

    def album(self, album_id):
        json = self._get('albums', uri_id(album_id))
        return Album(json, spy=self)
