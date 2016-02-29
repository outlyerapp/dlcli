import os
import logging
import yaml
import json
import accounts
import agents
import plugins
import dashboards
import rules
import tags

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


def create_dir(path, directory):
    new_directory = os.path.join(path, directory)
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    return new_directory


def backup_account(ctx, account):
    #  create directory structure
    ctx.parent.parent.params['account'] = account
    org = ctx.parent.parent.params['org']
    backupdir = ctx.parent.parent.params['backupdir']

    backup_dir = create_dir(os.getcwd(), backupdir)
    org_dir = create_dir(backup_dir, org)
    account_dir = create_dir(org_dir, account)

    # backup agents
    agent_dir = create_dir(account_dir, 'agents')
    for a in agents.Agents(ctx).get_agents():
        agent_path = os.path.join(agent_dir, str(a['name']) + '.json')
        with open(agent_path, 'w') as f:
            f.write(json.dumps(a, indent=4))

    # backup dashboards
    dashboard_dir = create_dir(account_dir, 'dashboards')
    for d in dashboards.Dashboards(ctx).get_dashboards():
        dashboard_path = os.path.join(dashboard_dir, str(d['name']) + '.yaml')
        with open(dashboard_path, 'w') as f:
            f.write(yaml.safe_dump(d, default_flow_style=False))

    # backup plugins
    plugins_dir = create_dir(account_dir, 'plugins')
    _plugins = plugins.Plugins(ctx)
    for p in _plugins.get_plugins():
        plugin_path = os.path.join(plugins_dir, str(p['name']) + '.' + str(p['extension']))
        with open(plugin_path, 'w') as f:
            f.write(_plugins.export_plugin(p['name']))

    # backup rules
    rule_dir = create_dir(account_dir, 'rules')
    _rules = rules.Rules(ctx)
    for r in _rules.get_rules():
        rule_path = os.path.join(rule_dir, str(r['name']) + '.yaml')
        with open(rule_path, 'w') as f:
            f.write(_rules.export_rule(r['id']))

    # backup tags
    tags_dir = create_dir(account_dir, 'tags')
    for t in tags.Tags(ctx).get_tags():
        tag_path = os.path.join(tags_dir, str(t['name']) + '.json')
        with open(tag_path, 'w') as f:
            f.write(json.dumps(t, indent=4))


def backup_org(ctx, org):
    ctx.parent.parent.params['org'] = org
    _accounts =accounts.Accounts(ctx)
    for a in _accounts.get_accounts():
        backup_account(ctx, a['name'])
