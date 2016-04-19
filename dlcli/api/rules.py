import os
import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_rules(url='', org='', account='', key='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rules'),
        headers={'Authorization': "Bearer " + key}).json()


def get_criteria(url='', org='', account='', key='', rule='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rules' + '/' + rule + '/criteria'),
        headers={'Authorization': "Bearer " + key}).json()


def export_rule(url='', org='', account='', key='', rule='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rules') + '/' + rule,
        headers={'Authorization': "Bearer " + key, "Accept": "application/yaml"}).content


def delete_rule(url='', org='', account='', key='', rule='', **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rules') + '/' + rule,
        headers={'Authorization': "Bearer " + key})


def import_rule(url='', org='', account='', key='', rule_path='', **kwargs):
    rule_name = os.path.splitext(os.path.basename(rule_path))[0]
    rule_content = utils.read_file_content(rule_path)
    requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rules'),
        headers={'Authorization': "Bearer " + key},
        data={"name": rule_name})
    requests.put(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rules' + '/' + rule_name),
        headers={'Authorization': "Bearer " + key, "Content-Type": "application/yaml"},
        data=rule_content)
