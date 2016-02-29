from ..cli import *
from ..api import *
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('restore')
@click.pass_context
def restore(ctx):
    """restores backups"""


@click.command(short_help="Restore an Organization")
@click.argument('org')
@click.pass_context
def org(ctx, org):
    _orgs = Orgs(ctx)


@click.command(short_help="Restore an Account")
@click.argument('account')
@click.pass_context
def account(ctx, account):
    _accounts = Accounts(ctx)


restore.add_command(org)
restore.add_command(account)
