import requests

from environment_api import token



def get_track(id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/tracks/{id}', headers=header)
    return response


def save_tracks(list_of_ids):
    header = {'Authorization': token}
    response = requests.put(f'https://api.spotify.com/v1/me/tracks?ids={list_of_ids}', headers=header)
    return response


def remove_saved_tracks(list_of_ids):
    header = {'Authorization': token}
    response = requests.delete(f'https://api.spotify.com/v1/me/tracks?ids={list_of_ids}', headers=header)
    return response