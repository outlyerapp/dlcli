from ..cli import *
from ..api import *
import sys
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('restore')
def restore():
    """restores backups and metric paths"""


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


@click.command(short_help="Restore metric paths")
def metrics():
    try:
        resp = series.update_tag_metrics(tag="all", status='valid', **context.settings)
        click.echo(click.style('Recovered: %s paths', fg='green') % (resp))
    except Exception, e:
        print 'Cleanup metrics failed. %s' % e
        sys.exit(1)


restore.add_command(account)
restore.add_command(org)
restore.add_command(metrics)
