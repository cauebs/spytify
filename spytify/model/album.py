from .utils import Image

Artist = None
Track = None


class Album:
    def __init__(self, json, spy=None):
        self._spy = spy

        self._load_json(json)

    def _load_json(self, json):
        self._name = json['name']
        self._id = json['id']
        self._uri = json['uri']
        self._url = json['external_urls']['spotify']
        self._album_type = json['album_type']
        self._available_markets = json['available_markets']
        self._artists = tuple(Artist(artist, spy=self._spy)
                              for artist in json['artists'])

        self._images = tuple(Image(**image) for image in json['images'])

        try:
            self._tracks = tuple(Track(track, spy=self._spy)
                                 for track in json['tracks']['items'])
        except KeyError:
            self._followers = None

        self._popularity = json.get('popularity')
        self._label = json.get('label')
        self._genres = json.get('genres')
        self._release_date = json.get('release_date')

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
    def album_type(self):
        return self._album_type

    @property
    def available_markets(self):
        return self._available_markets

    @property
    def artists(self):
        return self._artists

    @property
    def artist(self):
        return self._artists[0]

    @property
    def images(self):
        return self._images

    @property
    def tracks(self):
        if self._tracks is None:
            self._load()

        return self._tracks

    @property
    def popularity(self):
        if self._popularity is None:
            self._load()

        return self._popularity

    @property
    def labels(self):
        if self._labels is None:
            self._load()

        return self._labels

    @property
    def genres(self):
        if self._genres is None:
            self._load()

        return self._genres

    @property
    def release_date(self):
        if self._release_date is None:
            self._load()

        return self._release_date

    def __str__(self):
        return '<{} object: name={}, uri={}>'.format(
            self.__class__.__name__, self.name, self.uri)
