import logging
import requests
import utils

logger = logging.getLogger(__name__)


class Tags(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {'Authorization': "Bearer " + ctx.parent.parent.params['key']}

    def get_tags(self):
        return requests.get(
            utils.build_api_url(self.ctx, 'tags'),
            headers=self.headers).json()

    def delete_tag(self, tag):
        return requests.delete(
            utils.build_api_url(self.ctx, 'tags') + '/' + tag,
            headers=self.headers)
