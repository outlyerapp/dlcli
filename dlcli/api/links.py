import logging
import requests
import utils

logger = logging.getLogger(__name__)


class Links(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_links(self):
        return requests.get(utils.build_api_url(self.ctx, 'links'), headers=self.headers).json()

    def delete_link(self, link):
        return requests.delete(utils.build_api_url(self.ctx, 'links') + '/' + link, headers=self.headers)