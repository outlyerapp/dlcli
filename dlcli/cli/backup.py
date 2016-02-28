import os
import json
import yaml
from ..cli import *
from ..api import *
import click


import logging
logger = logging.getLogger(__name__)

@cli.group('backup')
@click.pass_context
def backup(ctx):
    """performs backups"""


@click.command(short_help="Backup an Account")
@click.argument('account')
@click.pass_context
def account(ctx, account):
    #  create directory structure
    ctx.parent.parent.params['account'] = account
    org = ctx.parent.parent.params['org']
    backupdir = ctx.parent.parent.params['backupdir']

    backup_dir = create_dir(os.getcwd(), backupdir)
    org_dir = create_dir(backup_dir, org)
    account_dir = create_dir(org_dir, account)

    # backup agents
    agent_dir = create_dir(account_dir, 'agents')
    for a in Agents(ctx).get_agents():
        agent_path = os.path.join(agent_dir, str(a['name']) + '.json')
        with open(agent_path, 'w') as f:
            f.write(json.dumps(a, indent=4))

    # backup dashboards
    dashboard_dir = create_dir(account_dir, 'dashboards')
    for d in Dashboards(ctx).get_dashboards():
        dashboard_path = os.path.join(dashboard_dir, str(d['name']) + '.yaml')
        with open(dashboard_path, 'w') as f:
            f.write(yaml.safe_dump(d, default_flow_style=False))

    # backup plugins
    plugins_dir = create_dir(account_dir, 'plugins')
    _plugins = Plugins(ctx)
    for p in _plugins.get_plugins():
        plugin_path = os.path.join(plugins_dir, str(p['name']) + '.' + str(p['extension']))
        with open(plugin_path, 'w') as f:
            f.write(_plugins.export_plugin(p['name']))

    # backup rules
    rule_dir = create_dir(account_dir, 'rules')
    _rules = Rules(ctx)
    for r in _rules.get_rules():
        rule_path = os.path.join(rule_dir, str(r['name']) + '.yaml')
        with open(rule_path, 'w') as f:
            f.write(_rules.export_rule(r['id']))

    # backup tags
    tags_dir = create_dir(account_dir, 'tags')
    for t in Tags(ctx).get_tags():
        tag_path = os.path.join(tags_dir, str(t['name']) + '.json')
        with open(tag_path, 'w') as f:
            f.write(json.dumps(t, indent=4))


@click.command(short_help="Backup an Organization")
@click.argument('org')
@click.pass_context
def org(ctx, org):
    ctx.parent.parent.params['org'] = org
    for a in Accounts(ctx).get_accounts():
        ctx.invoke(account, account=a['name'])

backup.add_command(account)
backup.add_command(org)
