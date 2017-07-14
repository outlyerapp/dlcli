import logging
import utils
from wrapper import *

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_packs(url='', org='', account='', key='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='/packs'),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def delete_pack(url='', org='', account='', key='', name='', timeout=60, **kwargs):
    return delete(utils.build_api_url(url, org, account,
                                      endpoint='/packs/private/%s' % name),
                  headers={'Authorization': "Bearer " + key}, timeout=timeout)
