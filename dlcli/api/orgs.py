import logging
import utils
from wrapper import *

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_orgs(url='', org='', account='', key='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account, org_level=True),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def delete_org(url='', org='', account='', key='', org_name='', timeout=60, **kwargs):
    return delete(utils.build_api_url(url, org, account,
                                      org_level=True) + '/' + org_name,
                  headers={'Authorization': "Bearer " + key}, timeout=timeout)
