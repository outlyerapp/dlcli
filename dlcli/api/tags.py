import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_tags(url='', org='', account='', key='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='tags'),
        headers={'Authorization': "Bearer " + key}).json()


def delete_tag(url='', org='', account='', key='', tag_name='', **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='tags') + '/' + tag_name,
        headers={'Authorization': "Bearer " + key})
