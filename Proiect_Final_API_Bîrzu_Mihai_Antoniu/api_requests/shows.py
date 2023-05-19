import requests

from environment_api import token



def get_show_episodes(id, limit):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/shows/{id}/episodes?limit={limit}', headers=header)
    return response

