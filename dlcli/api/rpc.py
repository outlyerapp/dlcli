import os
import base64
import logging
import grequests
import utils

logger = logging.getLogger(__name__)


class Rpc(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {'Authorization': "Bearer " + ctx.parent.parent.params['key']}

    def set_meta(self, meta):
        def hook(r, **kwargs):
            r.meta = meta
            return r

        return hook

    def run_local(self, plugin_path, agent_list):
        plugin_name = os.path.splitext(os.path.basename(plugin_path))
        plugin_content = utils.read_file_content(plugin_path)
        requests = (grequests.post(
            utils.build_api_url(self.ctx, 'rpc' + '/run'),
            data={
                'name': plugin_name,
                'agent': agent_id,
                'content': base64.b64encode(plugin_content),
                'encoding': 'base64',
                'shell': '',
                'params': '',
                'type': 'INPROCESS'
            },
            callback=self.set_meta(agent_id),
            headers=self.headers) for agent_id in agent_list)
        data = []
        for resp in grequests.imap(requests, size=10):
            data.append([resp.meta, resp.json()])
        return data

    def run_command(self, command, agent_list):
        plugin_content = '#!/usr/bin/env bash \n' + command
        requests = (grequests.post(
            utils.build_api_url(self.ctx, 'rpc' + '/run'),
            data={
                'name': 'temp.sh',
                'agent': agent_id,
                'content': base64.b64encode(plugin_content),
                'encoding': 'base64',
                'params': '',
                'type': 'SCRIPT'
            },
            callback=self.set_meta(agent_id),
            headers=self.headers) for agent_id in agent_list)
        data = []
        for resp in grequests.imap(requests, size=10):
            data.append([resp.meta, resp.json()])
        return data
