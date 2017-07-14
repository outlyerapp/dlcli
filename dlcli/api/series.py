import logging
import utils
from wrapper import *

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_agent_series(url='', org='', account='', key='', agent_id='', metric='',
                     resolution='', period='', timeout=60, **kwargs):
    return get(
        utils.build_api_url(url, org, account,
                            endpoint='metrics/%s/series?source=%s&resolution=%s&period=%s' % (
                                metric, agent_id, resolution, period)),
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def get_tag_series(url='', org='', account='', key='', tag='', metric='',
                   resolution='', period='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='metrics/%s/series?tag=%s&resolution=%s&period=%s' % (
                                       metric, tag, resolution, period)),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def update_agents_metric_paths(url='', org='', account='', key='', agents='', metric='',
                               status='', timeout=60, **kwargs):
    return put(utils.build_api_url(url, org, account,
                                   endpoint='metrics/%s/series' % metric),
               headers={'Authorization': "Bearer " + key},
               params={"source": agents},
               data={'status': status}, timeout=timeout).json()


# noinspection PyUnusedLocal
def update_tag_metrics(url='', org='', account='', key='', tag='',
                       status='', timeout=60, **kwargs):
    return put(utils.build_api_url(url, org, account,
                                   endpoint='metrics/series?tag=%s' % tag),
               headers={'Authorization': "Bearer " + key},
               data={'status': status}, timeout=timeout).json()
