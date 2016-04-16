import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_agents(url='', org='', account='', key='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='agents'
                            ),
        headers={'Authorization': "Bearer " + key}).json()


def get_agent(url='', org='', account='', key='', agent_name='', **kwargs):
    agent_map = get_agents(url=url, org=org, account=account, key=key)
    for agent in agent_map:
        if agent['name'] == agent_name:
            return requests.get(
                utils.build_api_url(url,
                                    org,
                                    account,
                                    endpoint='agents') + '/' + agent['id'],
                headers={'Authorization': "Bearer " + key}).json()


def register_agent(url='', org='', account='', key='', payload='', finger='', **kwargs):
    return requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='agents/%s/ping' % finger),
        headers={'Authorization': "Bearer " + key},
        data=payload)


def ping_agent(url='', org='', account='', key='', payload='', finger='', **kwargs):
    return requests.post(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='agents/%s/ping' % finger),
        headers={'Authorization': "Bearer " + key},
        data=payload)


def delete_agent(url='', org='', account='', key='', agent_name='', **kwargs):
    agent_map = get_agents(url, key, org, account)
    for agent in agent_map:
        if agent['name'] == agent_name:
            return requests.delete(
                utils.build_api_url(url,
                                    org,
                                    account,
                                    endpoint='agents') + '/' + agent['id'],
                headers={'Authorization': "Bearer " + key})


def get_agent_name_from_id(url='', org='', account='', key='', agent_id='', **kwargs):
    agents = requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='agents'),
        headers={'Authorization': "Bearer " + key}).json()
    for a in agents:
        if a['id'] == agent_id:
            return a['name']
