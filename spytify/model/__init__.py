from .album import Album
from .artist import Artist
from .track import Track


def init():
    from . import album
    from . import track

    album.Artist = Artist
    album.Track = Track

    track.Album = Album
    track.Artist = Artist


init()

del init
