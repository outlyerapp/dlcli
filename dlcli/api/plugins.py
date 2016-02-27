import logging
import requests
import base64
logger = logging.getLogger(__name__)


class Plugins(object):
    def __init__(self, ctx):
        self.url = ctx.parent.parent.params['url']
        self.org = ctx.parent.parent.params['org']
        self.account = ctx.parent.parent.params['account']
        self.key = ctx.parent.parent.params['key']
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_plugins(self):
        return requests.get(self.url + '/orgs/' + self.org + '/accounts/' + self.account + '/plugins', headers=self.headers).json()

    def export_plugin(self, plugin):
        resp = requests.get(self.url + '/orgs/' + self.org + '/accounts/' + self.account + '/plugins/' + plugin, headers=self.headers).json()
        return base64.b64decode(resp['content'])