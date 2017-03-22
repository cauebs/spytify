from datetime import timedelta

Artist = None
Album = None


class Track:
    def __init__(self, json, spy=None):
        self._spy = spy

        self._load_json(json)

    def _load_json(self, json):
        self._name = json['name']
        self._id = json['id']
        self._uri = json['uri']
        self._url = json['external_urls']['spotify']
        self._preview_url = json['preview_url']
        self._explicit = json['explicit']
        self._available_markets = json['available_markets']
        self._track_number = json['track_number']
        self._disc_number = json['disc_number']
        self._duration = timedelta(milliseconds=json['duration_ms'])
        self._artists = tuple(Artist(artist, spy=self._spy)
                              for artist in json['artists'])

        self._album = Album(json['album'], spy=self)

        self._popularity = json.get('popularity')

    def _load(self):
        json = self._spy._get('artists', self.id)

        self._load_json(json)

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def uri(self):
        return self._uri

    @property
    def url(self):
        return self._url

    @property
    def preview_url(self):
        return self._preview_url

    @property
    def explicit(self):
        return self._explicit

    @property
    def available_markets(self):
        return self._available_markets

    @property
    def track_number(self):
        return self._track_number

    @property
    def disc_number(self):
        return self._disc_number

    @property
    def duration(self):
        return self._duration

    @property
    def artists(self):
        return self._artists

    @property
    def artist(self):
        return self._artists[0]

    @property
    def popularity(self):
        if self._popularity is None:
            self._load()

        return self._popularity

    def __str__(self):
        return '<{} object: name={}, uri={}>'.format(
            self.__class__.__name__, self.name, self.uri)

    def __eq__(self, other):
        if isinstance(other, Track):
            return self.uri == other.uri
        return NotImplemented
