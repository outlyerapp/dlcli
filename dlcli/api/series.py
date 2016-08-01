import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_agent_series(url='', org='', account='', key='', agent_id='', metric='', resolution='', period='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='metrics' + '/' + metric + '/series?source=' + agent_id + '&resolution=' + str(resolution) + '&period=' + str(period)),
        headers={'Authorization': "Bearer " + key}).json()


def get_tag_series(url='', org='', account='', key='', tag='', metric='', resolution='', period='', **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='metrics' + '/' + metric + '/series?tag=' + tag + '&resolution=' + str(resolution) + '&period=' + str(period)),
        headers={'Authorization': "Bearer " + key}).json()


def update_agents_metric_paths(url='', org='', account='', key='', agents='',  metric='', status='', **kwargs):
    return requests.put(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='metrics' + '/' + metric + '/series'),
        headers={'Authorization': "Bearer " + key},
        params={"source": agents},
        data={'status': status}).json()


def update_tag_metrics(url='', org='', account='', key='', tag='', status='', **kwargs):
    return requests.put(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='metrics/series?tag=' + tag),
        headers={'Authorization': "Bearer " + key},
        data={'status': status}).json()
