import os
import logging
import requests
import utils
import yaml
import json
import base64

logger = logging.getLogger(__name__)


def get_public_templates(url='', org='', account='', key='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/public'),
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def get_private_templates(url='', org='', account='', key='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private'),
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def get_private_template(url='', org='', account='', key='', name='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private/%s' % name),
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def create_template(url='', org='', account='', key='', name='', timeout=60, **kwargs):
    return requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private'),
        data={"name": name},
        headers={'Authorization': "Bearer " + key}, timeout=timeout)


def delete_template(url='', org='', account='', key='', name='', timeout=60, **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private/%s' % name),
        headers={'Authorization': "Bearer " + key}, timeout=timeout)


def put_manifest(url='', org='', account='', key='', name='', path='', timeout=60, **kwargs):
    content = yaml.safe_load(utils.read_file_content(os.path.join(path, 'package.yaml')))
    return requests.put(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private/%s' % name),
        headers={'Authorization': "Bearer " + key, "Content-Type": "application/json"},
        data=json.dumps(content), timeout=timeout)


def put_plugin(url='', org='', account='', key='', path='', template='', timeout=60, **kwargs):
    plugin_name = os.path.splitext(os.path.basename(path))[0]
    plugin_extension = os.path.splitext(os.path.basename(path))[1]
    plugin_content = utils.read_file_content(path)
    payload = {
        "name": plugin_name,
        "extension": plugin_extension.replace('.', ''),
        "content": base64.b64encode(plugin_content)
    }
    resp = requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='/templates/private/%s/plugins' % template),
        headers={'Authorization': "Bearer " + key},
        data=payload, timeout=timeout)
    return resp


def put_dashboard(url='', org='', account='', key='', path='', template='', timeout=60, **kwargs):
    dashboard_name = os.path.splitext(os.path.basename(path))[0]
    dashboard_yaml = utils.read_file_content(path)
    return requests.put(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='/templates/private/%s/dashboards/%s' % (template, dashboard_name)),
        headers={'Authorization': "Bearer " + key, "Content-Type": "application/yaml"},
        data=dashboard_yaml, timeout=timeout)


def put_rule(url='', org='', account='', key='', path='', template='', timeout=60, **kwargs):
    rule_name = os.path.splitext(os.path.basename(path))[0]
    rule_content = utils.read_file_content(path)
    return requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='/templates/private/%s/rules' % template),
        headers={'Authorization': "Bearer " + key, "Content-Type": "application/yaml"},
        data=rule_content, timeout=timeout)


def install_template(url='', org='', account='', key='', name='', timeout=60, **kwargs):
    return requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='/packs'),
        headers={'Authorization': "Bearer " + key},
        json={"name": name, "force": True, "email": "", "repo": "private"}, timeout=timeout)