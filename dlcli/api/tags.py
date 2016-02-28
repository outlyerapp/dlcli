import logging
import requests
from utils import build_api_url

logger = logging.getLogger(__name__)


class Tags(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_tags(self):
        return requests.get(build_api_url(self.ctx, 'tags'), headers=self.headers).json()

    def delete_tag(self, tag):
        return requests.delete(build_api_url(self.ctx, 'tags') + '/' + tag, headers=self.headers)