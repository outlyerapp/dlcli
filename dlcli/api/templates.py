import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_public_templates(url='', org='', account='', key='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/public'),
        headers={'Authorization': "Bearer " + key}).json()


def get_private_templates(url='', org='', account='', key='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private'),
        headers={'Authorization': "Bearer " + key}).json()


