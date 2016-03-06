import os
import logging
import requests
import utils

logger = logging.getLogger(__name__)


class Rules(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.headers = {"Token": ctx.parent.parent.params['key']}

    def get_rules(self):
        return requests.get(
            utils.build_api_url(self.ctx, 'rules'),
            headers=self.headers).json()

    def get_criteria(self, rule):
        return requests.get(
            utils.build_api_url(self.ctx, 'rules' + '/' + rule + '/criteria'),
            headers=self.headers).json()

    def export_rule(self, rule):
        self.headers.update({"Accept": "application/yaml"})
        return requests.get(
            utils.build_api_url(self.ctx, 'rules') + '/' + rule,
            headers=self.headers).content

    def delete_rule(self, rule):
        return requests.delete(
            utils.build_api_url(self.ctx, 'rules') + '/' + rule,
            headers=self.headers)

    def import_rule(self, rule_path):
        rule_name = os.path.splitext(os.path.basename(rule_path))[0]
        rule_content = utils.read_file_content(rule_path)
        requests.post(
            utils.build_api_url(self.ctx, 'rules'),
            headers=self.headers,
            data={"name": rule_name})
        self.headers.update({"Content-Type": "application/yaml"})
        requests.put(
            utils.build_api_url(self.ctx, 'rules' + '/' + rule_name),
            headers=self.headers,
            data=rule_content)
