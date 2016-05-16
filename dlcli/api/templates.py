import os
import logging
import requests
import utils
import yaml
import json
import base64

logger = logging.getLogger(__name__)


def get_public_templates(url='', org='', account='', key='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/public'),
        headers={'Authorization': "Bearer " + key}).json()


def get_private_templates(url='', org='', account='', key='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private'),
        headers={'Authorization': "Bearer " + key}).json()


def get_private_template(url='', org='', account='', key='', name='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private/%s' % name),
        headers={'Authorization': "Bearer " + key}).json()


def create_template(url='', org='', account='', key='', name='', **kwargs):
    return requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private'),
        data={"name": name},
        headers={'Authorization': "Bearer " + key}).json()


def delete_template(url='', org='', account='', key='', name='', **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private/%s' % name),
        headers={'Authorization': "Bearer " + key})


def put_manifest(url='', org='', account='', key='', name='', path='', **kwargs):
    content = yaml.safe_load(utils.read_file_content(os.path.join(path, 'package.yaml')))
    return requests.put(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='templates/private/%s' % name),
        headers={'Authorization': "Bearer " + key, "Content-Type": "application/json"},
        data=json.dumps(content))


def put_plugin(url='', org='', account='', key='', path='', name='', **kwargs):
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
                            endpoint='/templates/private/%s/plugins' % plugin_name),
        headers={'Authorization': "Bearer " + key},
        data=payload)
    return resp


def put_dashboard(url='', org='', account='', key='', path='', name='', **kwargs):
    dashboard_name = os.path.splitext(os.path.basename(path))[0]
    dashboard_yaml = utils.read_file_content(path)
    return requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='/templates/private/%s/dashboards' % dashboard_name),
        headers={'Authorization': "Bearer " + key, "Content-Type": "application/yaml"},
        data=dashboard_yaml)


def put_rule(url='', org='', account='', key='', path='', name='', **kwargs):
    rule_name = os.path.splitext(os.path.basename(path))[0]
    rule_content = utils.read_file_content(path)
    return requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='/templates/private/%s/rules' % rule_name),
        headers={'Authorization': "Bearer " + key, "Content-Type": "application/yaml"},
        data=rule_content)
