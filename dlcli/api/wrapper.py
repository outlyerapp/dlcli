import requests
session = requests.session()


def get(url, **kwargs):
    r = session.get(url, **kwargs)
    r.raise_for_status()
    return r


def options(url, **kwargs):
    r = session.options(url, **kwargs)
    r.raise_for_status()
    return r


def head(url, **kwargs):
    r = session.head(url, **kwargs)
    r.raise_for_status()
    return r


def post(url, data=None, json=None, **kwargs):
    r = session.post(url, data, json, **kwargs)
    r.raise_for_status()
    return r


def put(url, data=None, **kwargs):
    r = session.put(url, data, **kwargs)
    r.raise_for_status()
    return r


def patch(url, data=None, **kwargs):
    r = session.patch(url, data, **kwargs)
    r.raise_for_status()
    return r


def delete(url, **kwargs):
    r = session.delete(url, **kwargs)
    r.raise_for_status()
    return r
