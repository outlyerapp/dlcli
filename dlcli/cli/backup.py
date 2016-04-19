from ..cli import *
from ..api import *
import click
import logging


logger = logging.getLogger(__name__)


@cli.group('backup')
def backup():
    """performs backups"""


@click.command(short_help="Backup an Account")
@click.argument('account')
def account(account):
    context.settings['account'] = account
    utils.backup_account(**context.settings)


@click.command(short_help="Backup an Organization")
@click.argument('org')
def org(org):
    context.settings['org'] = org
    utils.backup_org(**context.settings)


backup.add_command(account)
backup.add_command(org)
