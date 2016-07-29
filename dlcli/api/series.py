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


def delete_agent_metric_paths(url='', org='', account='', key='', agent_id='', metric='', resolution='', period='', **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='metrics' + '/' + metric + '/series?source=' + agent_id + '&resolution=' + str(resolution) + '&period=' + str(period)),
        headers={'Authorization': "Bearer " + key}).json()

def delete_tag_metric_paths(url='', org='', account='', key='', tag='', metric='', resolution='', period='', **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='metrics' + '/' + metric + '/series?tag=' + tag + '&resolution=' + str(resolution) + '&period=' + str(period)),
        headers={'Authorization': "Bearer " + key}).json()


def update_agent_metric_paths(url='', org='', account='', key='', agent='', **kwargs):
    return requests.put(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='metrics/series?agent=' + agent),
        headers={'Authorization': "Bearer " + key},
        data={'status': 'valid'}).json()


def update_tag_metric_paths(url='', org='', account='', key='', tag='', **kwargs):
    return requests.put(
        utils.build_api_url(url,
                            org,
                            account,
                            endpoint='metrics/series?tag=' + tag),
        headers={'Authorization': "Bearer " + key},
        data={'status': 'valid'}).json()
