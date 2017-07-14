from ..cli import *
from ..api import *
import sys
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('set')
def set():
    """sets things"""


@click.command(short_help="Set url")
@click.argument('url')
def url(url):
    try:
        save_setting(setting='url', value=url, settings_file=context.settings['settings_file'])
    except Exception, e:
        print 'Save url failed. %s' % e
        sys.exit(1)


@click.command(short_help="Set organization")
@click.argument('org')
def org(org):
    try:
        save_setting(setting='org', value=org, settings_file=context.settings['settings_file'])
    except Exception, e:
        print 'Save org failed. %s' % e
        sys.exit(1)


@click.command(short_help="Set account")
@click.argument('account')
def account(account):
    try:
        save_setting(setting='account', value=account, settings_file=context.settings['settings_file'])
    except Exception, e:
        print 'Save account failed. %s' % e
        sys.exit(1)


@click.command(short_help="Set key")
@click.argument('key')
def key(key):
    try:
        save_setting(setting='key', value=key, settings_file=context.settings['settings_file'])
    except Exception, e:
        print 'Save key failed. %s' % e
        sys.exit(1)

set.add_command(url)
set.add_command(org)
set.add_command(account)
set.add_command(key)
