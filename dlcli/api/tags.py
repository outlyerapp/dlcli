import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_tags(url='', org='', account='', key='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='tags'),
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def delete_tag(url='', org='', account='', key='', tag='', timeout=60, **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='tags') + '/' + tag,
        headers={'Authorization': "Bearer " + key}, timeout=timeout)
