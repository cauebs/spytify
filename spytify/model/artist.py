from .utils import Image


class Artist:
    def __init__(self, json, spy=None):
        self._spy = spy

        self._load_json(json)

    def _load_json(self, json):
        self._name = json['name']
        self._id = json['id']
        self._uri = json['uri']
        self._url = json['external_urls']['spotify']

        self._genres = json.get('genres')
        self._popularity = json.get('popularity')

        try:
            self._followers = json['followers']['total']
        except KeyError:
            self._followers = None

        try:
            self._images = tuple(Image(**image) for image in json['images'])
        except KeyError:
            self._images = None

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
    def genres(self):
        if self._genres is None:
            self._load()

        return self._genres

    @property
    def popularity(self):
        if self._popularity is None:
            self._load()

        return self._popularity

    @property
    def followers(self):
        if self._followers is None:
            self._load()

        return self._followers

    @property
    def images(self):
        if self._images is None:
            self._load()

        return self._images

    def __str__(self):
        return '<{} object: name={}, uri={}>'.format(
            self.__class__.__name__, self.name, self.uri)

    def __eq__(self, other):
        if isinstance(other, Artist):
            return self.uri == other.uri
        return NotImplemented
