import logging
import requests
from utils import build_api_url

logger = logging.getLogger(__name__)


class Orgs(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_orgs(self):
        return requests.get(build_api_url(self.ctx, orglevel=True), headers=self.headers).json()

    def delete_org(self, org):
        return requests.delete(build_api_url(self.ctx, orglevel=True) + '/' + org, headers=self.headers)