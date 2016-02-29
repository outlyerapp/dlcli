import logging
import requests
import utils

logger = logging.getLogger(__name__)


class Rules(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_rules(self):
        return requests.get(utils.build_api_url(self.ctx, 'rules'), headers=self.headers).json()

    def export_rule(self, rule):
        self.headers.update({"Accept": "application/yaml"})
        return requests.get(utils.build_api_url(self.ctx, 'rules') + '/' + rule, headers=self.headers).content

    def delete_rule(self, rule):
        return requests.delete(utils.build_api_url(self.ctx, 'rules') + '/' + rule, headers=self.headers)