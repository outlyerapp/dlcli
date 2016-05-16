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


def create_template(url='', org='', account='', key='', name='', **kwargs):
    return requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private'),
        data={"name": name},
        headers={'Authorization': "Bearer " + key}).json()


def delete_template(url='', org='', account='', key='', name='', **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private/%s' % name),
        headers={'Authorization': "Bearer " + key})