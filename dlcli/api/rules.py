import logging
import requests
logger = logging.getLogger(__name__)


class Rules(object):
    def __init__(self, ctx):
        self.url = ctx.parent.parent.params['url']
        self.org = ctx.parent.parent.params['org']
        self.account = ctx.parent.parent.params['account']
        self.key = ctx.parent.parent.params['key']
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_rules(self):
        return requests.get(self.url + '/orgs/' + self.org + '/accounts/' + self.account + '/rules', headers=self.headers).json()

    def export_rule(self, rule):
        self.headers.update({"Accept": "application/yaml"})
        return requests.get(self.url + '/orgs/' + self.org + '/accounts/' + self.account + '/rules/56d0709e1b36dd8ef76e38fd', headers=self.headers).content