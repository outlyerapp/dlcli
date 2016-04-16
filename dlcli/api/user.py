import logging
import requests

logger = logging.getLogger(__name__)


def get_user(url='', key='', **kwargs):
    return requests.get(url + '/user', headers={'Authorization': "Bearer " + key}).json()


def get_user_tokens(url='', key='', **kwargs):
    return requests.get(url + '/user/tokens',
                        headers={'Authorization': "Bearer " + key}).json()


def create_user_token(url='', key='', token_name='', **kwargs):
    return requests.post(url + '/user/tokens',
                         headers={'Authorization': "Bearer " + key},
                         data={'name': token_name}).json()


def delete_user_token(url='', key='', token_name='', **kwargs):
    return requests.delete(url + '/user/tokens/' + token_name,
                           headers={'Authorization': "Bearer " + key})
