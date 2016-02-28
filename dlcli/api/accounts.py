import logging
import requests
from agents import *
from utils import *

logger = logging.getLogger(__name__)


class Accounts(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_accounts(self):
        return requests.get(build_api_url(self.ctx, accountlevel=True), headers=self.headers).json()

    def delete_account(self, account):
        return requests.delete(build_api_url(self.ctx, accountlevel=True) + '/' + account, headers=self.headers)

    def backup_account(self, account):
        # create the backup dir structure
        create_backup_account_dir(self.ctx, account)

        # dump all agents to json files
        _agents = Agents(self.ctx)
        agents = _agents.get_agents()


