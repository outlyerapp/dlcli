import os
import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_dashboards(url='', org='', account='', key='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='dashboards'),
        headers={'Authorization': "Bearer " + key}).json()


def export_dashboard(url='', org='', account='', key='', dashboard='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='dashboards') + '/' + dashboard,
        headers={'Authorization': "Bearer " + key, "Accept": "application/yaml"}).content


def import_dashboard(url='', org='', account='', key='', file_path='', **kwargs):
    dashboard_name = os.path.splitext(os.path.basename(file_path))[0]
    dashboard_yaml = utils.read_file_content(file_path)
    return requests.put(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='dashboards') + '/' + dashboard_name,
        headers={'Authorization': "Bearer " + key, "Content-Type": "application/yaml"},
        data=dashboard_yaml)


def delete_dashboard(url='', org='', account='', key='', dashboard='', **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='dashboards') + '/' + dashboard,
        headers={'Authorization': "Bearer " + key})
