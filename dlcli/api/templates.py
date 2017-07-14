import os
import logging
import utils
import yaml
import json
import base64
from wrapper import *

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_public_templates(url='', org='', account='', key='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='templates/public'),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def get_private_templates(url='', org='', account='', key='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='templates/private'),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def get_private_template(url='', org='', account='', key='', name='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='templates/private/%s' % name),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def create_template(url='', org='', account='', key='', name='', timeout=60, **kwargs):
    return post(utils.build_api_url(url, org, account,
                                    endpoint='templates/private'),
                data={"name": name},
                headers={'Authorization': "Bearer " + key}, timeout=timeout)


# noinspection PyUnusedLocal
def delete_template(url='', org='', account='', key='', name='', timeout=60, **kwargs):
    return delete(utils.build_api_url(url, org, account,
                                      endpoint='templates/private/%s' % name),
                  headers={'Authorization': "Bearer " + key}, timeout=timeout)


# noinspection PyUnusedLocal
def put_manifest(url='', org='', account='', key='', name='', path='', timeout=60, **kwargs):
    content = yaml.safe_load(utils.read_file_content(os.path.join(path, 'package.yaml')))
    return put(utils.build_api_url(url, org, account,
                                   endpoint='templates/private/%s' % name),
               headers={'Authorization': "Bearer " + key, "Content-Type": "application/json"},
               data=json.dumps(content), timeout=timeout)


# noinspection PyUnusedLocal
def put_plugin(url='', org='', account='', key='', path='', template='', timeout=60, type='INPROCESS', **kwargs):
    plugin_name = os.path.splitext(os.path.basename(path))[0]
    plugin_extension = os.path.splitext(os.path.basename(path))[1]
    plugin_content = utils.read_file_content(path)
    payload = {
        "name": plugin_name,
        "extension": plugin_extension.replace('.', ''),
        "content": base64.b64encode(plugin_content),
        "type": type
    }
    resp = post(utils.build_api_url(url, org, account,
                                    endpoint='/templates/private/%s/plugins' % template),
                headers={'Authorization': "Bearer " + key},
                data=payload, timeout=timeout)
    return resp


# noinspection PyUnusedLocal
def put_dashboard(url='', org='', account='', key='', path='', template='', timeout=60, **kwargs):
    dashboard_name = os.path.splitext(os.path.basename(path))[0]
    dashboard_yaml = utils.read_file_content(path)
    return put(utils.build_api_url(url, org, account,
                                   endpoint='/templates/private/%s/dashboards/%s' % (template, dashboard_name)),
               headers={'Authorization': "Bearer " + key, "Content-Type": "application/yaml"},
               data=dashboard_yaml, timeout=timeout)


# noinspection PyUnusedLocal
def put_rule(url='', org='', account='', key='', path='', template='', timeout=60, **kwargs):
    rule_name = os.path.splitext(os.path.basename(path))[0]
    rule_content = utils.read_file_content(path)
    return post(utils.build_api_url(url, org, account,
                                    endpoint='/templates/private/%s/rules' % template),
                headers={'Authorization': "Bearer " + key, "Content-Type": "application/yaml"},
                data=rule_content, timeout=timeout)


# noinspection PyUnusedLocal
def install_template(url='', org='', account='', key='', name='', timeout=60, **kwargs):
    return post(utils.build_api_url(url, org, account,
                                    endpoint='/packs'),
                headers={'Authorization': "Bearer " + key},
                json={"name": name, "force": True, "email": "", "repo": "private"}, timeout=timeout)
