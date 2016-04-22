from ..cli import *
from ..api import *
import sys
import click
import logging


logger = logging.getLogger(__name__)


@cli.group('backup')
def backup():
    """performs backups"""


@click.command(short_help="Backup an Account")
@click.argument('account')
def account(account):
    try:
        context.settings['account'] = account
        utils.backup_account(**context.settings)
    except Exception, e:
        print 'Backup account failed. %s' % e
        sys.exit(1)


@click.command(short_help="Backup an Organization")
@click.argument('org')
def org(org):
    try:
        context.settings['org'] = org
        utils.backup_org(**context.settings)
    except Exception, e:
        print 'Backup org failed. %s' % e
        sys.exit(1)


backup.add_command(account)
backup.add_command(org)
