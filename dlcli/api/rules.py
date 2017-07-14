import os
import logging
import utils
import click
from wrapper import *

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_rules(url='', org='', account='', key='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='rules'),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def get_rule(url='', org='', account='', key='', rule='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='rules/%s' % rule),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def get_criteria(url='', org='', account='', key='', rule='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='rules/%s/criteria' % rule),
               headers={'Authorization': "Bearer " + key}, timeout=timeout)


# noinspection PyUnusedLocal
def export_rule(url='', org='', account='', key='', rule='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='rules/%s' % rule),
               headers={'Authorization': "Bearer " + key, "Accept": "application/yaml"}, timeout=timeout).content


# noinspection PyUnusedLocal
def delete_rule(url='', org='', account='', key='', rule='', timeout=60, **kwargs):
    return delete(utils.build_api_url(url, org, account,
                                      endpoint='rules/%s' % rule),
                  headers={'Authorization': "Bearer " + key}, timeout=timeout)


# noinspection PyUnusedLocal
def import_rule(url='', org='', account='', key='', rule_path='', timeout=60, **kwargs):
    rule_name = os.path.splitext(os.path.basename(rule_path))[0]
    rule_content = utils.read_file_content(rule_path)
    click.echo("restoring rule %s" % rule_name)
    post(utils.build_api_url(url, org, account,
                             endpoint='rules'),
         headers={'Authorization': "Bearer " + key},
         data={"name": rule_name}, timeout=timeout)
    return requests.put(
        utils.build_api_url(url, org, account,
                            endpoint='rules/%s' % rule_name),
        headers={'Authorization': "Bearer " + key, "Content-Type": "application/yaml"},
        data=rule_content, timeout=timeout)


# noinspection PyUnusedLocal
def mute_rule(url='', org='', account='', key='', rule='', timeout=60, **kwargs):
    click.echo("muting rule %s" % rule)
    return patch(utils.build_api_url(url, org, account,
                                     endpoint='rules/%s' % rule),
                 headers={'Authorization': "Bearer " + key}, data={'mute': True}, timeout=timeout)


# noinspection PyUnusedLocal
def unmute_rule(url='', org='', account='', key='', rule='', timeout=60, **kwargs):
    click.echo("unmuting rule %s" % rule)
    return patch(utils.build_api_url(url, org, account,
                                     endpoint='rules/%s' % rule),
                 headers={'Authorization': "Bearer " + key}, data={'mute': False}, timeout=timeout)
