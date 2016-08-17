import logging
import requests

logger = logging.getLogger(__name__)


def get_user(url='', key='', timeout=60, **kwargs):
    return requests.get(url + '/user', headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def get_user_tokens(url='', key='', timeout=60, **kwargs):
    return requests.get(url + '/user/tokens',
                        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def create_user_token(url='', key='', token_name='', timeout=60, **kwargs):
    return requests.post(url + '/user/tokens',
                         headers={'Authorization': "Bearer " + key},
                         data={'name': token_name}, timeout=timeout).json()


def delete_user_token(url='', key='', token_name='', timeout=60, **kwargs):
    return requests.delete(url + '/user/tokens/' + token_name,
                           headers={'Authorization': "Bearer " + key}, timeout=timeout)
