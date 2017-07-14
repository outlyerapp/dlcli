import logging
import utils
from wrapper import *

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_accounts(url='', org='', key='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account='', account_level=True),
               headers={'Authorization': "Bearer " + key},
               timeout=timeout).json()


# noinspection PyUnusedLocal
def delete_account(url='', org='', account='', key='', timeout=60, **kwargs):
    return delete(utils.build_api_url(url, org, account, account_level=True) + '/' + account,
                  headers={'Authorization': "Bearer " + key},
                  timeout=timeout)
