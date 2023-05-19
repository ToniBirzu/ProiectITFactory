import requests

from environment_api import token




def get_album_without_market(id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}', headers=header)
    return response


def get_album_tracks(id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}/tracks', headers=header)
    return response


def get_several_albums(list_of_ids):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums?ids={list_of_ids}', headers=header)
    return response


def get_album_with_country_and_limit(country, limit):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/browse/new-releases?country={country}&limit={limit}', headers=header)
    return response


def get_album_with_market(id,market):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}?market={market}', headers=header)
    return response


def save_albums(list_of_ids):
    header = {'Authorization': token}
    response = requests.put(f'https://api.spotify.com/v1/me/albums?ids={list_of_ids}', headers=header)
    return response


