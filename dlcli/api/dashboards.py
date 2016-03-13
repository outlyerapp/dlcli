import os
import logging
import requests
import utils

logger = logging.getLogger(__name__)


class Dashboards(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {'Authorization': "Bearer " + ctx.parent.parent.params['key']}

    def get_dashboards(self):
        return requests.get(
            utils.build_api_url(self.ctx, 'dashboards'),
            headers=self.headers).json()

    def export_dashboard(self, dashboard_name):
        self.headers.update({"Accept": "application/yaml"})
        return requests.get(
            utils.build_api_url(self.ctx, 'dashboards') + '/' + dashboard_name,
            headers=self.headers).content

    def import_dashboard(self, file_path):
        dashboard_name = os.path.splitext(os.path.basename(file_path))[0]
        dashboard_yaml = utils.read_file_content(file_path)
        self.headers.update({"Content-Type": "application/yaml"})
        return requests.put(
            utils.build_api_url(self.ctx, 'dashboards') + '/' + dashboard_name,
            headers=self.headers,
            data=dashboard_yaml)

    def delete_dashboard(self, dashboard_name):
        return requests.delete(
            utils.build_api_url(self.ctx, 'dashboards') + '/' + dashboard_name,
            headers=self.headers)
