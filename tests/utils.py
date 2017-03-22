import sys
sys.path.append('..')

from spytify import Spotify
from spytify import AuthorizationCode, ClientCredentials


CLIENT_ID = '25de06ef6f834089becebb79784028e4'
CLIENT_SECRET = '2bf0aa15bd3d4691bf9406e0efb13909'


def create_spotify():
    return Spotify(auth=ClientCredentials(CLIENT_ID, CLIENT_SECRET))
