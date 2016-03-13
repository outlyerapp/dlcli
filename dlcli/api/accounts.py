import logging
import requests
import utils

logger = logging.getLogger(__name__)


class Accounts(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {'Authorization': "Bearer " + ctx.parent.parent.params['key']}

    def get_accounts(self):
        return requests.get(
            utils.build_api_url(self.ctx,
                                accountlevel=True),
            headers=self.headers).json()

    def delete_account(self, account):
        return requests.delete(
            utils.build_api_url(self.ctx,
                                accountlevel=True) + '/' + account,
            headers=self.headers)
