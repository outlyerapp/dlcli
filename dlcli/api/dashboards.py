import logging
import requests
from utils import build_api_url

logger = logging.getLogger(__name__)


class Dashboards(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_dashboards(self):
        return requests.get(build_api_url(self.ctx, 'dashboards'), headers=self.headers).json()

    def export_dashboard(self, dashboard):
        self.headers.update({"Accept": "application/yaml"})
        return requests.get(build_api_url(self.ctx, 'dashboards') + '/' + dashboard, headers=self.headers).content

    def import_dashboard(self, dashboard):
        pass

    def delete_dashboard(self, dashboard):
        return requests.delete(build_api_url(self.ctx, 'dashboards') + '/' + dashboard, headers=self.headers)