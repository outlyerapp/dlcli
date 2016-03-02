import os
import glob
import logging
import yaml
import json
import accounts
import agents
import plugins
import dashboards
import rules
import links

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
        yaml_file.write(yaml.safe_dump(data, default_flow_style=False, explicit_start=True))


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
    backupdir = ctx.parent.parent.params['backupdir']
    org = ctx.parent.parent.params['org']
    ctx.parent.parent.params['account'] = account

    backup_dir = create_dir(os.getcwd(), backupdir)
    org_dir = create_dir(backup_dir, org)
    account_dir = create_dir(org_dir, account)

    # backup agents
    agent_dir = create_dir(account_dir, 'agents')
    for agent_json in agents.Agents(ctx).get_agents():
        agent_path = os.path.join(agent_dir, str(agent_json['name']) + '.json')
        remove_keys = ['presence_state', 'created', 'modified', 'heartbeat']
        for key in remove_keys:
            if key in agent_json:
                del agent_json[key]
        with open(agent_path, 'w') as f:
            f.write(json.dumps(agent_json, indent=4))

    # backup dashboards
    dashboard_dir = create_dir(account_dir, 'dashboards')
    for d in dashboards.Dashboards(ctx).get_dashboards():
        dashboard_path = os.path.join(dashboard_dir, str(d['name']) + '.yaml')
        with open(dashboard_path, 'w') as f:
            f.write(yaml.safe_dump(d, default_flow_style=False, explicit_start=True))

    # backup plugins
    plugin_dir = create_dir(account_dir, 'plugins')
    _plugins = plugins.Plugins(ctx)
    for p in _plugins.get_plugins():
        plugin_path = os.path.join(plugin_dir, str(p['name']) + '.' + str(p['extension']))
        with open(plugin_path, 'w') as f:
            f.write(_plugins.export_plugin(p['name']))

    # backup rules
    rule_dir = create_dir(account_dir, 'rules')
    _rules = rules.Rules(ctx)
    for r in _rules.get_rules():
        rule_path = os.path.join(rule_dir, str(r['name']) + '.yaml')
        with open(rule_path, 'w') as f:
            rule_yaml = yaml.safe_load(_rules.export_rule(r['id']))
            remove_keys = ['timestamp']
            for key in remove_keys:
                if key in rule_yaml:
                    del rule_yaml[key]
            f.write(yaml.safe_dump(rule_yaml, default_flow_style=False, explicit_start=True))

    # backup links
    link_dir = create_dir(account_dir, 'links')
    for l in links.Links(ctx).get_links():
        link_path = os.path.join(link_dir, l['id'] + '.json')
        link_json = links.Links(ctx).export_link(l['id'])
        with open(link_path, 'w') as f:
            f.write(json.dumps(link_json, indent=4))


def backup_org(ctx, org):
    ctx.parent.parent.params['org'] = org
    _accounts = accounts.Accounts(ctx)
    for a in _accounts.get_accounts():
        backup_account(ctx, a['name'])


def read_file_content(file_path):
    try:
        with open(file_path) as f:
            return f.read()
    except IOError as exc:
        if exc.errno != os.errno.EISDIR:
            raise


def restore_account(ctx, account):
    ctx.parent.parent.params['account'] = account
    backup_dir = ctx.parent.parent.params['backupdir']
    org_dir = ctx.parent.parent.params['org']
    account_dir = ctx.parent.parent.params['account']

    agents_dir = os.path.join(backup_dir, org_dir, account_dir, 'agents')
    dashboards_dir = os.path.join(backup_dir, org_dir, account_dir, 'dashboards')
    plugins_dir = os.path.join(backup_dir, org_dir, account_dir, 'plugins')
    rules_dir = os.path.join(backup_dir, org_dir, account_dir, 'rules')
    links_dir = os.path.join(backup_dir, org_dir, account_dir, 'links')

    # restore agents
    agent_files = glob.glob(agents_dir + '/*.json')
    for agent_path in agent_files:
        agent_json = json.loads(read_file_content(agent_path))
        payload = {
            "fingerprint": agent_json['id'],
            "name": agent_json['name'],
            "hostname": agent_json['hostname'],
            "tag_names": ",".join(agent_json['tags']),
            "mac": agent_json['mac'],
            "os_name": agent_json['osName'],
            "container_name": agent_json['container_name'],
            "mode": agent_json['mode'],
            "status": agent_json['status']
        }
        agents.Agents(ctx).register_agent(payload)

    # restore dashboards
    dashboard_files = glob.glob(dashboards_dir + '/*.yaml')
    for dashboard_path in dashboard_files:
        dashboards.Dashboards(ctx).import_dashboard(dashboard_path)

    # restore plugins
    plugin_files = glob.glob(plugins_dir + '/*')
    for plugin_path in plugin_files:
        plugins.Plugins(ctx).import_plugin(plugin_path)

    # restore rules
    rule_files = glob.glob(rules_dir + '/*.yaml')
    for rule_path in rule_files:
        rules.Rules(ctx).import_rule(rule_path)

    # restore links
    link_files = glob.glob(links_dir + '/*.json')
    for link_path in link_files:
        links.Links(ctx).import_link(link_path)


def restore_org(ctx, org):
    ctx.parent.parent.params['org'] = org
    _accounts = accounts.Accounts(ctx)
    for a in _accounts.get_accounts():
        restore_account(ctx, a['name'])
