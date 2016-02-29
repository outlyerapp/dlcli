import os
import logging
import requests
import base64
import utils

logger = logging.getLogger(__name__)


class Plugins(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_plugins(self):
        return requests.get(utils.build_api_url(self.ctx, 'plugins'), headers=self.headers).json()

    def export_plugin(self, plugin):
        resp = requests.get(utils.build_api_url(self.ctx, 'plugins') + '/' + plugin, headers=self.headers).json()
        return base64.b64decode(resp['content'])

    def import_plugin(self, plugin):
        filename, file_extension = os.path.splitext(plugin)
        with open(plugin, 'r') as f:
            content = f.read()
        base64_content = base64.b64encode(content)
        payload = {
            "name": filename,
            "extension": file_extension.replace('.', ''),
            "content": base64_content
        }
        return requests.post(utils.build_api_url(self.ctx, 'plugins'), headers=self.headers, data=payload)

    def delete_plugin(self, plugin):
        filename, file_extension = os.path.splitext(plugin)
        return requests.delete(utils.build_api_url(self.ctx, 'plugins' + '/' + filename), headers=self.headers)
