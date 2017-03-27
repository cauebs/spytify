from utils import create_spotify

spy = create_spotify()

dict_abba = {
    'genres': ['dance pop', 'europop', 'hollywood',
               'mellow gold', 'swedish pop'],
    'id': '0LcJLqbBmaGUft1e9Mm8HV',
    'name': 'ABBA',
    'uri': 'spotify:artist:0LcJLqbBmaGUft1e9Mm8HV',
    'url': 'https://open.spotify.com/artist/0LcJLqbBmaGUft1e9Mm8HV',
}

imgs_abba = [
    {'height': 640,
     'url': ('https://i.scdn.co/image/'
             '155610d632de75c11b61a46640c34f2196f25800'),
     'width': 640},

    {'height': 320,
     'url': ('https://i.scdn.co/image/'
             'b173fce5565965312cbd399be5ef971a41dacc87'),
     'width': 320},

    {'height': 160,
     'url': ('https://i.scdn.co/image/'
             '3d2867a1e457a1c2edec9bf5d320578308b8c1f9'),
     'width': 160},
]

dict_panic = {
    'genres': ['emo', 'pop punk', 'vegas indie'],
    'id': '20JZFwl6HVl6yg8a4H3ZqK',
    'name': 'Panic! At The Disco',
    'uri': 'spotify:artist:20JZFwl6HVl6yg8a4H3ZqK',
    'url': 'https://open.spotify.com/artist/20JZFwl6HVl6yg8a4H3ZqK',
}

imgs_panic = [
    {'height': 757,
     'url': 'https://i.scdn.co/image/13d0de938cc4d4d890ace6c3f3955803e9dd8ccd',
     'width': 1000},

    {'height': 484,
     'url': 'https://i.scdn.co/image/1d349f478ca67418cd09ca49a8c2aab883ef4306',
     'width': 640},

    {'height': 151,
     'url': 'https://i.scdn.co/image/6d314b0fb784ab9899f2113b6d5e19bc6cbb31ec',
     'width': 200},

    {'height': 48,
     'url': 'https://i.scdn.co/image/0f23a5fdfd9126f38540d6a07a60db445399baa6',
     'width': 63},
]


def test_abba():
    abba = spy.artist(dict_abba['uri'])

    for key, value in dict_abba.items():
        assert getattr(abba, key) == value

    for dict_img, obj_img in zip(imgs_abba, abba.images):
        assert obj_img.width == dict_img['width']
        assert obj_img.height == dict_img['height']
        assert obj_img.url == dict_img['url']


def test_panic():
    panic = spy.artist(dict_panic['uri'])

    for key, value in dict_panic.items():
        assert getattr(panic, key) == value

    for dict_img, obj_img in zip(imgs_panic, panic.images):
        assert obj_img.width == dict_img['width']
        assert obj_img.height == dict_img['height']
        assert obj_img.url == dict_img['url']
