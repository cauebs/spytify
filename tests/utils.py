import json
import sys
sys.path.append('..')

from spytify import Spotify
from spytify import AuthorizationCode, ClientCredentials


def load_config():
    with open('config.json') as config_file:
        return json.loads(config_file.read())


def create_spotify():
    config = load_config()
    auth = ClientCredentials(config['client_id'], config['client_secret'])
    return Spotify(auth=auth)


print(load_config())
