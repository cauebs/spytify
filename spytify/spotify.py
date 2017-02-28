from oauthlib.oauth2 import TokenExpiredError
import requests
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

    def __init__(self, auth=None):
        self.auth = auth

    def _get(self, *endpoint, params=None, **kwargs):
        kwargs.update(params or {})

        if isinstance(endpoint, tuple):
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
        return self._get('tracks', clean_uri(track_id))

    def artist(self, artist_id):
        json = self._get('artists', clean_uri(artist_id))
        return Artist(json, spy=self)
