import logging
import requests
import utils
import json

logger = logging.getLogger(__name__)


def get_links(url='', org='', account='', key='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='links'),
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def delete_link(url='', org='', account='', key='', link='', timeout=60, **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='links') + '/' + link,
        headers={'Authorization': "Bearer " + key}, timeout=timeout)


def export_link(url='', org='', account='', key='', link='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='links') + '/' + link,
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def import_link(url='', org='', account='', key='', link_path='', timeout=60, **kwargs):
    link_json = json.loads(utils.read_file_content(link_path))
    return requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='links'),
        headers={'Authorization': "Bearer " + key},
        data=link_json, timeout=timeout)
