import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_packs(url='', org='', account='', key='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='/packs'),
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def delete_pack(url='', org='', account='', key='', name='', timeout=60, **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='/packs/private/%s' % name),
        headers={'Authorization': "Bearer " + key}, timeout=timeout)