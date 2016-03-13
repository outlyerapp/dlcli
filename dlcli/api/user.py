import logging
import requests

logger = logging.getLogger(__name__)


class User(object):
    def __init__(self, ctx):
        self.ctx = ctx
        self.url = ctx.parent.parent.params['url']
        self.headers = {'Authorization': "Bearer " + ctx.parent.parent.params['key']}

    def get_user(self):
        return requests.get(
            self.url + '/user',
            headers=self.headers).json()

    def get_user_tokens(self):
        return requests.get(
            self.url + '/user/tokens',
            headers=self.headers).json()

    def create_user_token(self, name):
        return requests.post(
            self.url + '/user/tokens',
            headers=self.headers,
            data={'name': name}).json()

    def delete_user_token(self, name):
        return requests.delete(
            self.url + '/user/tokens/' + name,
            headers=self.headers)
