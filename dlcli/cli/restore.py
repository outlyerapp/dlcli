from ..cli import *
from ..api import *
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('restore')
@click.pass_context
def restore(ctx):
    """restores backups"""


@click.command(short_help="Restore an Account")
@click.argument('account')
@click.pass_context
def account(ctx, account):
    utils.restore_account(ctx, account)


@click.command(short_help="Restore an Organization")
@click.argument('org')
@click.pass_context
def org(ctx, org):
    utils.restore_org(ctx, org)


restore.add_command(account)
restore.add_command(org)

