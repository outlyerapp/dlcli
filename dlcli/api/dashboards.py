import logging
import requests
import utils

logger = logging.getLogger(__name__)


class Dashboards(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_dashboards(self):
        return requests.get(utils.build_api_url(self.ctx, 'dashboards'), headers=self.headers).json()

    def export_dashboard(self, dashboard):
        self.headers.update({"Accept": "application/yaml"})
        return requests.get(utils.build_api_url(self.ctx, 'dashboards') + '/' + dashboard, headers=self.headers).content

    def import_dashboard(self, dashboard):
        pass

    def delete_dashboard(self, dashboard):
        return requests.delete(utils.build_api_url(self.ctx, 'dashboards') + '/' + dashboard, headers=self.headers)