import logging
import yaml

logger = logging.getLogger(__name__)


def save_setting(ctx, setting):
    settings_file = ctx.parent.parent.params['settingsfile']
    try:
        stream = open(settings_file, 'r')
        data = yaml.load(stream)
    except IOError:
        data = {}
    data.update({k: v for k, v in setting.iteritems() if v})
    with open(settings_file, 'w') as yaml_file:
        yaml_file.write(yaml.safe_dump(data, default_flow_style=False))


def build_api_url(ctx, endpoint='', orglevel=False, accountlevel=False):
    url = ctx.parent.parent.params['url']
    org = ctx.parent.parent.params['org']
    account = ctx.parent.parent.params['account']
    if orglevel:
        return url + '/orgs'
    if accountlevel:
        return url + '/orgs/' + org + '/accounts'
    return url + '/orgs/' + org + '/accounts/' + account + '/' + endpoint