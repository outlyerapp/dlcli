import logging
import utils
import json
from wrapper import *

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_links(url='', org='', account='', key='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='links'),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def delete_link(url='', org='', account='', key='', link_id='', timeout=60, **kwargs):
    return delete(utils.build_api_url(url, org, account,
                                      endpoint='links/%s' % link_id),
                  headers={'Authorization': "Bearer " + key}, timeout=timeout)


# noinspection PyUnusedLocal
def export_link(url='', org='', account='', key='', link_id='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='links/%s' % link_id),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def import_link(url='', org='', account='', key='', link_path='', timeout=60, **kwargs):
    link_json = json.loads(utils.read_file_content(link_path))
    return post(utils.build_api_url(url, org, account,
                                    endpoint='links'),
                headers={'Authorization': "Bearer " + key},
                data=link_json, timeout=timeout)
