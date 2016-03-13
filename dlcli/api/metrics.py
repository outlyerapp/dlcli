import logging
import requests
import utils

logger = logging.getLogger(__name__)


class Metrics(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {'Authorization': "Bearer " + ctx.parent.parent.params['key']}

    def get_agent_metrics(self, agent):
        return requests.get(
            utils.build_api_url(self.ctx, 'metrics'),
            headers=self.headers,
            params={"source": agent}).json()

    def get_tag_metrics(self, tag):
        return requests.get(
            utils.build_api_url(self.ctx, 'metrics'),
            headers=self.headers,
            params={"tag": tag}).json()
