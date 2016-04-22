import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_packs(url='', org='', account='', key='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='packs'),
        headers={'Authorization': "Bearer " + key}).json()


