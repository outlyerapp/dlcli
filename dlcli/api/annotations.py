import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_streams(url='', org='', account='', key='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='annotations'
                            ),
        headers={'Authorization': "Bearer " + key}).json()


def get_annotations(url='', org='', account='', key='', stream='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='annotations/%s' % stream
                            ),
        headers={'Authorization': "Bearer " + key}).json()


def delete_stream(url='', org='', account='', key='', stream='', **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='annotations/%s' % stream
                            ),
        headers={'Authorization': "Bearer " + key})


def create_annotation(url='', org='', account='', key='', stream='', name='', description='', **kwargs):
    return requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='annotations/%s' % stream
                            ),
        headers={'Authorization': "Bearer " + key},
        json={"name": name, "description": description})