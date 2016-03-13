import os
import logging
import requests
import base64
import utils

logger = logging.getLogger(__name__)


class Plugins(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {'Authorization': "Bearer " + ctx.parent.parent.params['key']}

    def get_plugins(self):
        return requests.get(
            utils.build_api_url(self.ctx, 'plugins'),
            headers=self.headers).json()

    def export_plugin(self, plugin):
        resp = requests.get(
            utils.build_api_url(self.ctx, 'plugins') + '/' + plugin,
            headers=self.headers).json()
        return base64.b64decode(resp['content'])

    def import_plugin(self, plugin_path):
        plugin_name = os.path.splitext(os.path.basename(plugin_path))[0]
        plugin_extension = os.path.splitext(os.path.basename(plugin_path))[1]
        plugin_content = utils.read_file_content(plugin_path)
        payload = {
            "name": plugin_name,
            "extension": plugin_extension.replace('.', ''),
            "content": base64.b64encode(plugin_content)
        }

        resp = requests.post(
            utils.build_api_url(self.ctx, 'plugins'),
            headers=self.headers,
            data=payload)
        if resp.status_code == 422:
            resp = requests.patch(
                utils.build_api_url(self.ctx, 'plugins' + '/' + plugin_name),
                headers=self.headers,
                data=payload)
        return resp

    def delete_plugin(self, plugin):
        return requests.delete(
            utils.build_api_url(self.ctx, 'plugins' + '/' + plugin),
            headers=self.headers)
