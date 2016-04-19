from ..cli import *
from ..api import *
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('restore')
def restore():
    """restores backups"""


@click.command(short_help="Restore an Account")
@click.argument('account')
def account(account):
    context.settings['account'] = account
    utils.restore_account(**context.settings)


@click.command(short_help="Restore an Organization")
@click.argument('org')
def org(org):
    context.settings['org'] = org
    utils.restore_org(**context.settings)


restore.add_command(account)
restore.add_command(org)
