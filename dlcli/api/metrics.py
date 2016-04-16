import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_agent_metrics(url='', org='', account='', key='', agent_id='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='metrics'),
        headers={'Authorization': "Bearer " + key},
        params={"source": agent_id}).json()


def get_tag_metrics(url='', org='', account='', key='', tag_name='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='metrics'),
        headers={'Authorization': "Bearer " + key},
        params={"tag": tag_name}).json()
