import os
import base64
import logging
import grequests
import utils

logger = logging.getLogger(__name__)


def set_meta(meta):
    def hook(r, **kwargs):
        r.meta = meta
        return r
    return hook


def run_local(url='', org='', account='', key='', plugin_path='', agent_list='', **kwargs):
    plugin_name = os.path.splitext(os.path.basename(plugin_path))
    plugin_content = utils.read_file_content(plugin_path)
    requests = (grequests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rpc' + '/run'),
        data={
            'name': plugin_name,
            'agent': agent_id,
            'content': base64.b64encode(plugin_content),
            'encoding': 'base64',
            'shell': '',
            'params': '',
            'type': 'INPROCESS'
        },
        callback=set_meta(agent_id),
        headers={'Authorization': "Bearer " + key}) for agent_id in agent_list)
    data = []
    for resp in grequests.imap(requests, size=10):
        data.append([resp.meta, resp.json()])
    return data


def run_command(url='', org='', account='', key='', command='', agent_list='', **kwargs):
    plugin_content = '#!/usr/bin/env bash \n' + command
    requests = (grequests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='rpc' + '/run'),
        data={
            'name': 'temp.sh',
            'agent': agent_id,
            'content': base64.b64encode(plugin_content),
            'encoding': 'base64',
            'params': '',
            'type': 'SCRIPT'
        },
        callback=set_meta(agent_id),
        headers={'Authorization': "Bearer " + key}) for agent_id in agent_list)
    data = []
    for resp in grequests.imap(requests, size=10):
        data.append([resp.meta, resp.json()])
    return data
