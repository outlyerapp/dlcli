import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_streams(url='', org='', account='', key='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='annotations'
                            ),
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def get_annotations(url='', org='', account='', key='', stream='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='annotations/%s' % stream
                            ),
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def delete_stream(url='', org='', account='', key='', stream='', timeout=60, **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='annotations/%s' % stream
                            ),
        headers={'Authorization': "Bearer " + key}, timeout=timeout)


def create_annotation(url='', org='', account='', key='', stream='', name='', description='', timeout=60, **kwargs):
    return requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='annotations/%s' % stream
                            ),
        headers={'Authorization': "Bearer " + key},
        json={"name": name, "description": description}, timeout=timeout)