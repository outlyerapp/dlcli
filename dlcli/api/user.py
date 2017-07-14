import logging
from wrapper import *

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_user(url='', key='', timeout=60, **kwargs):
    return get(url + '/user', headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def get_user_tokens(url='', key='', timeout=60, **kwargs):
    return get(url + '/user/tokens',
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def create_user_token(url='', key='', token_name='', timeout=60, **kwargs):
    return post(url + '/user/tokens',
                headers={'Authorization': "Bearer " + key},
                data={'name': token_name}, timeout=timeout).json()


# noinspection PyUnusedLocal
def delete_user_token(url='', key='', token_name='', timeout=60, **kwargs):
    return delete(url + '/user/tokens/' + token_name,
                  headers={'Authorization': "Bearer " + key}, timeout=timeout)
