from ..cli import *
from ..api import *
import sys
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('restore')
def restore():
    """restores backups"""


@click.command(short_help="Restore an Account")
@click.argument('account')
def account(account):
    try:
        context.settings['account'] = account
        utils.restore_account(**context.settings)
    except Exception, e:
        print 'Restore account failed. %s' % e
        sys.exit(1)


@click.command(short_help="Restore an Organization")
@click.argument('org')
def org(org):
    try:
        context.settings['org'] = org
        utils.restore_org(**context.settings)
    except Exception, e:
        print 'Restore org failed. %s' % e
        sys.exit(1)


restore.add_command(account)
restore.add_command(org)
