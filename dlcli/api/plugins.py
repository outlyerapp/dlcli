import os
import logging
import base64
import utils
from wrapper import *

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_plugins(url='', org='', account='', key='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='plugins'),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def export_plugin(url='', org='', account='', key='', plugin='', timeout=60, **kwargs):
    resp = get(utils.build_api_url(url, org, account,
                                   endpoint='plugins/%s' % plugin),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()
    return base64.b64decode(resp['content'])


# noinspection PyUnusedLocal
def import_plugin(url='', org='', account='', key='', plugin_path='', timeout=60, **kwargs):
    plugin_name = os.path.splitext(os.path.basename(plugin_path))[0]
    plugin_extension = os.path.splitext(os.path.basename(plugin_path))[1]
    plugin_content = utils.read_file_content(plugin_path)
    payload = {
        "name": plugin_name,
        "extension": plugin_extension.replace('.', ''),
        "content": base64.b64encode(plugin_content)
    }
    print "restoring plugin %s" % plugin_name
    resp = requests.post(utils.build_api_url(url, org, account,
                                             endpoint='plugins'),
                         headers={'Authorization': "Bearer " + key},
                         data=payload, timeout=timeout)

    if resp.status_code == 422:
        resp = requests.patch(utils.build_api_url(url, org, account,
                                                  endpoint='plugins/%s' % plugin_name),
                              headers={'Authorization': "Bearer " + key},
                              data=payload, timeout=timeout)
    return resp


# noinspection PyUnusedLocal
def delete_plugin(url='', org='', account='', key='', plugin='', timeout=60, **kwargs):
    return delete(utils.build_api_url(url, org, account,
                                      endpoint='plugins/%s' % plugin),
                  headers={'Authorization': "Bearer " + key}, timeout=timeout)
