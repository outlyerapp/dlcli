import logging
import utils
from wrapper import *

logger = logging.getLogger(__name__)


# noinspection PyUnusedLocal
def get_tags(url='', org='', account='', key='', timeout=60, **kwargs):
    return get(utils.build_api_url(url, org, account,
                                   endpoint='tags'),
               headers={'Authorization': "Bearer " + key}, timeout=timeout).json()


# noinspection PyUnusedLocal
def delete_tag(url='', org='', account='', key='', tag='', timeout=60, **kwargs):
    return delete(utils.build_api_url(url, org, account,
                                      endpoint='tags/%s' % tag),
                  headers={'Authorization': "Bearer " + key}, timeout=timeout)
