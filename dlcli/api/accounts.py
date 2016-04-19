import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_accounts(url='', org='', key='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account='',
                            accountlevel=True),
        headers={'Authorization': "Bearer " + key}).json()


def delete_account(url='', org='', account='', key='', **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            accountlevel=True) + '/' + account,
        headers={'Authorization': "Bearer " + key})
