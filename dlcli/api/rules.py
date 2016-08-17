import os
import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_rules(url='', org='', account='', key='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rules'),
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def get_criteria(url='', org='', account='', key='', rule='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rules' + '/' + rule + '/criteria'),
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def export_rule(url='', org='', account='', key='', rule='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rules') + '/' + rule,
        headers={'Authorization': "Bearer " + key, "Accept": "application/yaml"}, timeout=timeout).content


def delete_rule(url='', org='', account='', key='', rule='', timeout=60, **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rules') + '/' + rule,
        headers={'Authorization': "Bearer " + key}, timeout=timeout)


def import_rule(url='', org='', account='', key='', rule_path='', timeout=60, **kwargs):
    rule_name = os.path.splitext(os.path.basename(rule_path))[0]
    rule_content = utils.read_file_content(rule_path)
    requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rules'),
        headers={'Authorization': "Bearer " + key},
        data={"name": rule_name}, timeout=timeout)
    return requests.put(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rules' + '/' + rule_name),
        headers={'Authorization': "Bearer " + key, "Content-Type": "application/yaml"},
        data=rule_content, timeout=timeout)
