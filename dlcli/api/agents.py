import logging
import utils
from wrapper import *

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_agents(url='', org='', account='', key='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='agents'),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def get_agent(url='', org='', account='', key='', agent_name='', timeout=60, **kwargs):
    agent_map = get_agents(url=url, org=org, account=account, key=key)
    for agent in agent_map:
        if agent['name'] == agent_name:
            return get(utils.build_api_url(url, org, account,
                                           endpoint='agents/%s' % agent['id']),
                       headers={'Authorization': "Bearer " + key}, timeout=timeout)


# noinspection PyUnusedLocal
def register_agent(url='', org='', account='', key='', payload='', finger='', timeout=60, **kwargs):
    return post(utils.build_api_url(url, org, account,
                                    endpoint='agents/%s/ping' % finger),
                headers={'Authorization': "Bearer " + key},
                data=payload, timeout=timeout)


# noinspection PyUnusedLocal
def ping_agent(url='', org='', account='', key='', payload='', finger='', timeout=60, **kwargs):
    return post(utils.build_api_url(url, org, account,
                                    endpoint='agents/%s/ping' % finger),
                headers={'Authorization': "Bearer " + key},
                data=payload, timeout=timeout)


# noinspection PyUnusedLocal
def delete_agent(url='', org='', account='', key='', agent_name='', timeout=60, **kwargs):
    agent_map = get_agents(url, org, account, key)
    for agent in agent_map:
        if agent['name'] == agent_name:
            return requests.delete(utils.build_api_url(url, org, account,
                                                       endpoint='agents/%s' % agent['id']),
                                   headers={'Authorization': "Bearer " + key}, timeout=timeout)


# noinspection PyUnusedLocal
def get_agent_name_from_id(url='', org='', account='', key='', agent_id='', timeout=60, **kwargs):
    agents = get(utils.build_api_url(url, org, account,
                                     endpoint='agents'),
                 headers={'Authorization': "Bearer " + key}, timeout=timeout).json()
    for a in agents:
        if a['id'] == agent_id:
            return a['name']
