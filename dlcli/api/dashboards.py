import os
import logging
from wrapper import *
import utils

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_dashboards(url='', org='', account='', key='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='dashboards'),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def export_dashboard(url='', org='', account='', key='', dashboard='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='dashboards/%s' % dashboard),
               headers={'Authorization': "Bearer " + key, "Accept": "application/yaml"}, timeout=timeout).content


# noinspection PyUnusedLocal
def import_dashboard(url='', org='', account='', key='', file_path='', timeout=60, **kwargs):
    dashboard_name = os.path.splitext(os.path.basename(file_path))[0]
    dashboard_yaml = utils.read_file_content(file_path)
    print "restoring dashboard %s" % dashboard_name
    return put(utils.build_api_url(url, org, account,
                                   endpoint='dashboards/%s' % dashboard_name),
               headers={'Authorization': "Bearer " + key, "Content-Type": "application/yaml",
                        "Accept-Encoding": "identity"},
               data=dashboard_yaml, timeout=timeout)


# noinspection PyUnusedLocal
def delete_dashboard(url='', org='', account='', key='', dashboard='', timeout=60, **kwargs):
    return delete(utils.build_api_url(url, org, account,
                                      endpoint='dashboards/%s' % dashboard),
                  headers={'Authorization': "Bearer " + key}, timeout=timeout)
