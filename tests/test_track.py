from utils import create_spotify
from datetime import timedelta

spy = create_spotify()

dict_sos = {
    'disc_number': 1,
    'duration': timedelta(milliseconds=205466),
    'explicit': False,
    'id': '2c6BNK8IQjsFdUznUBDe4N',
    'name': 'S.O.S.',
    'preview_url': ('https://p.scdn.co/mp3-preview/'
                    '4a6e1456e04690cac4cafe1687f45bef82757d4a?'
                    'cid=25de06ef6f834089becebb79784028e4'),
    'track_number': 4,
    'uri': 'spotify:track:2c6BNK8IQjsFdUznUBDe4N',
    'url': 'https://open.spotify.com/track/2c6BNK8IQjsFdUznUBDe4N',
}

dict_cola = {
    'disc_number': 1,
    'duration': timedelta(milliseconds=260893),
    'explicit': True,
    'id': '29ryZ3PkPU9SKe3ZAIwnrJ',
    'name': 'Cola',
    'preview_url': ('https://p.scdn.co/mp3-preview/'
                    '218ad874f3b20f343c10cc44e0ae2765c3968b4a?'
                    'cid=25de06ef6f834089becebb79784028e4'),
    'track_number': 3,
    'uri': 'spotify:track:29ryZ3PkPU9SKe3ZAIwnrJ',
    'url': 'https://open.spotify.com/track/29ryZ3PkPU9SKe3ZAIwnrJ',
}

dict_telephone = {
    'disc_number': 1,
    'duration': timedelta(milliseconds=220626),
    'explicit': False,
    'id': '00BuKLSAFkaEkaVAgIMbeA',
    'name': 'Telephone',
    'preview_url': ('https://p.scdn.co/mp3-preview/'
                    'b440f5b990275459fdad0a3fc726046100cdf365?'
                    'cid=25de06ef6f834089becebb79784028e4'),
    'track_number': 6,
    'uri': 'spotify:track:00BuKLSAFkaEkaVAgIMbeA',
    'url': 'https://open.spotify.com/track/00BuKLSAFkaEkaVAgIMbeA',
}

track_uris = [
    'spotify:track:5cY8y2XgOfkAh4kSWLFKkz',
    'spotify:track:4zjFqN9fXAw91GNgJOCYX6',
    'spotify:track:6SpLc7EXZIPpy0sVko0aoU',
    'spotify:track:3WotBmwJH3eVPf1Wy2Y2IC',
    'spotify:track:0pKrMTlDlW54abYkdBsgxj',
]


def test_sos():
    sos = spy.track(dict_sos['uri'])

    for key, value in dict_sos.items():
        assert getattr(sos, key) == value

    assert str(sos) == ('<Track object: name=S.O.S., '
                        'uri=spotify:track:2c6BNK8IQjsFdUznUBDe4N>')

    assert sos.artist == spy.artist('spotify:artist:0LcJLqbBmaGUft1e9Mm8HV')


def test_cola():
    cola = spy.track(dict_cola['uri'])

    for key, value in dict_cola.items():
        assert getattr(cola, key) == value

    assert str(cola) == ('<Track object: name=Cola, '
                         'uri=spotify:track:29ryZ3PkPU9SKe3ZAIwnrJ>')

    assert cola.artist == spy.artist('spotify:artist:00FQb4jTyendYWaN8pK0wa')


def test_telephone():
    telephone = spy.track(dict_telephone['uri'])

    for key, value in dict_telephone.items():
        assert getattr(telephone, key) == value

    assert str(telephone) == ('<Track object: name=Telephone, '
                              'uri=spotify:track:00BuKLSAFkaEkaVAgIMbeA>')

    lady_gaga = spy.artist('1HY2Jd0NmPuamShAr6KMms')
    beyonce = spy.artist('6vWDO969PvNqNYHIOW5v0m')

    assert telephone.artist == lady_gaga
    assert telephone.artists == (lady_gaga, beyonce)


def test_tracks():
    assert spy.tracks(track_uris) == [spy.track(uri) for uri in track_uris]
