import os
import logging
import requests
import base64
import utils

logger = logging.getLogger(__name__)


def get_plugins(url='', org='', account='', key='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='plugins'),
        headers={'Authorization': "Bearer " + key}).json()


def export_plugin(url='', org='', account='', key='', plugin='', **kwargs):
    resp = requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='plugins') + '/' + plugin,
        headers={'Authorization': "Bearer " + key}).json()
    return base64.b64decode(resp['content'])


def import_plugin(url='', org='', account='', key='', plugin_path='', **kwargs):
    plugin_name = os.path.splitext(os.path.basename(plugin_path))[0]
    plugin_extension = os.path.splitext(os.path.basename(plugin_path))[1]
    plugin_content = utils.read_file_content(plugin_path)
    payload = {
        "name": plugin_name,
        "extension": plugin_extension.replace('.', ''),
        "content": base64.b64encode(plugin_content)
    }

    resp = requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='plugins'),
        headers={'Authorization': "Bearer " + key},
        data=payload)

    if resp.status_code == 422:
        resp = requests.patch(utils.build_api_url(url, org, account, endpoint='plugins' + '/' + plugin_name),
                              headers={'Authorization': "Bearer " + key},
                              data=payload)
    return resp


def delete_plugin(url='', org='', account='', key='', plugin_name='', **kwargs ):
    return requests.delete(
        utils.build_api_url(url, org, account, endpoint='plugins' + '/' + plugin_name),
        headers={'Authorization': "Bearer " + key})
