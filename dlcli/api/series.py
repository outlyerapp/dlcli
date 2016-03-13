import logging
import requests
import utils

logger = logging.getLogger(__name__)


class Series(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {'Authorization': "Bearer " + ctx.parent.parent.params['key']}

    def get_agent_series(self, agent, metric, resolution, period):
        return requests.get(
            utils.build_api_url(
                self.ctx, 'metrics' + '/' + metric + '/series?source=' + agent
                + '&resolution=' + str(resolution) + '&period=' + str(period)),
            headers=self.headers).json()

    def get_tag_series(self, tag, metric, resolution, period):
        return requests.get(
            utils.build_api_url(
                self.ctx, 'metrics' + '/' + metric + '/series?tag=' + tag +
                '&resolution=' + str(resolution) + '&period=' + str(period)),
            headers=self.headers).json()
