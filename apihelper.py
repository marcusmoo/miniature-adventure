import requests


def callApi(url):
    return requests.get(url).json()


def callStarwarsApi(endpoint, search):
    return callApi("https://swapi.dev/api/" + endpoint + "/?search=" + search)
