from requests_oauthlib import OAuth2Session


class Spotify:

    def __init__(self, session=None):
        self._session = session or OAuth2Session

    def test(self):
        return self.session.get('https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT')
