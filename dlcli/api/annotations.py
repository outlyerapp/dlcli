import logging
import utils
from wrapper import *

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_streams(url='', org='', account='', key='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='annotations'),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def get_annotations(url='', org='', account='', key='', stream='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='annotations/%s' % stream),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def delete_stream(url='', org='', account='', key='', stream='', timeout=60, **kwargs):
    return delete(utils.build_api_url(url, org, account,
                                      endpoint='annotations/%s' % stream),
                  headers={'Authorization': "Bearer " + key}, timeout=timeout)


# noinspection PyUnusedLocal
def create_annotation(url='', org='', account='', key='', stream='', name='', description='', timeout=60, **kwargs):
    return post(utils.build_api_url(url, org, account,
                                    endpoint='annotations/%s' % stream),
                headers={'Authorization': "Bearer " + key},
                json={"name": name, "description": description}, timeout=timeout)
