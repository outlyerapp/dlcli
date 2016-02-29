import logging
import requests
import utils

logger = logging.getLogger(__name__)


class Agents(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_agents(self):
        return requests.get(utils.build_api_url(self.ctx, 'agents'), headers=self.headers).json()

    def delete_agent(self, agent):
        return requests.delete(utils.build_api_url(self.ctx, 'agents') + '/' + agent, headers=self.headers)