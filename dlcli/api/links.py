import logging
import requests
import utils
import json

logger = logging.getLogger(__name__)


class Links(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {'Authorization': "Bearer " + ctx.parent.parent.params['key']}

    def get_links(self):
        return requests.get(
            utils.build_api_url(self.ctx, 'links'),
            headers=self.headers).json()

    def delete_link(self, link):
        return requests.delete(
            utils.build_api_url(self.ctx, 'links') + '/' + link,
            headers=self.headers)

    def export_link(self, link):
        return requests.get(
            utils.build_api_url(self.ctx, 'links') + '/' + link,
            headers=self.headers).json()

    def import_link(self, link_path):
        link_json = json.loads(utils.read_file_content(link_path))
        return requests.post(
            utils.build_api_url(self.ctx, 'links'),
            headers=self.headers,
            data=link_json)
