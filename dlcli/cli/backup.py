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
    _accounts = Accounts(ctx)


backup.add_command(org)
backup.add_command(account)
