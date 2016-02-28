import os
from ..cli import *
from ..api import *
import click


import logging
logger = logging.getLogger(__name__)

@cli.group('backup')
@click.pass_context
def backup(ctx):
    """performs backups"""


@click.command(short_help="Backup an Organization")
@click.argument('org')
@click.pass_context
def org(ctx, org):
    _orgs = Orgs(ctx)


@click.command(short_help="Backup an Account")
@click.argument('account')
@click.pass_context
def account(ctx, account):
    #  create directory structure
    org = ctx.parent.parent.params['org']
    account = ctx.parent.parent.params['account']
    backupdir = ctx.parent.parent.params['backupdir']

    backup_dir = create_dir(os.getcwd(), backupdir)
    org_dir = create_dir(backup_dir, org)
    account_dir = create_dir(org_dir, account)

    # backup agents
    agent_dir = create_dir(account_dir, 'agents')
    for agent in Agents(ctx).get_agents():
        agent_path = os.path.join(agent_dir, str(agent['name']))
        with open(agent_path, 'a') as f:
            f.write(str(agent))

    # backup tags
    tags_dir = create_dir(account_dir, 'tags')
    for tag in Tags(ctx).get_tags():
        tag_path = os.path.join(tags_dir, str(tag['name']))
        with open(tag_path, 'a') as f:
            f.write(str(tag))

backup.add_command(org)
backup.add_command(account)
