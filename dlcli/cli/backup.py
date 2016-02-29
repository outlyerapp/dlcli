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
    utils.backup_account(ctx, account)


@click.command(short_help="Backup an Organization")
@click.argument('org')
@click.pass_context
def org(ctx, org):
    utils.backup_org(ctx, org)


backup.add_command(account)
backup.add_command(org)
