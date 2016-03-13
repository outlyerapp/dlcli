import logging
import requests
import utils

logger = logging.getLogger(__name__)


class Orgs(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {'Authorization': "Bearer " + ctx.parent.parent.params['key']}

    def get_orgs(self):
        return requests.get(
            utils.build_api_url(self.ctx,
                                orglevel=True),
            headers=self.headers).json()

    def delete_org(self, org):
        return requests.delete(
            utils.build_api_url(self.ctx,
                                orglevel=True) + '/' + org,
            headers=self.headers)
