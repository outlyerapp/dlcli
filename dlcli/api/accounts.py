import logging
import requests
logger = logging.getLogger(__name__)


class Accounts(object):
    def __init__(self, ctx):
        self.url = ctx.parent.parent.params['url']
        self.org = ctx.parent.parent.params['org']
        self.account = ctx.parent.parent.params['account']
        self.key = ctx.parent.parent.params['key']
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_accounts(self):
        return requests.get(self.url + '/orgs/' + self.org + '/accounts', headers=self.headers).json()