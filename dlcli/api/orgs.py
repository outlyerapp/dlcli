import logging
import requests
import utils

logger = logging.getLogger(__name__)


def get_orgs(url='', org='', account='', key='', timeout=60, **kwargs):
    return requests.get(
        utils.build_api_url(url,
                            org,
                            account,
                            orglevel=True),
        headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


def delete_org(url='', org='', account='', key='', org_name='', timeout=60, **kwargs):
    return requests.delete(
        utils.build_api_url(url,
                            org,
                            account,
                            orglevel=True) + '/' + org_name,
        headers={'Authorization': "Bearer " + key}, timeout=timeout)
