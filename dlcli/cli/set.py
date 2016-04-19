from ..cli import *
from ..api import *
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('set')
def set():
    """sets things"""


@click.command(short_help="Set url")
@click.argument('url')
def url(url):
    save_setting(setting={"url": str(url)}, **context.settings)


@click.command(short_help="Set organization")
@click.argument('org')
def org(org):
    save_setting(setting={"org": str(org)}, **context.settings)


@click.command(short_help="Set account")
@click.argument('account')
def account(account):
    save_setting(setting={"account": str(account)}, **context.settings)


@click.command(short_help="Set key")
@click.argument('key')
def key(key):
    save_setting(setting={"key": str(key)}, **context.settings)


set.add_command(url)
set.add_command(org)
set.add_command(account)
set.add_command(key)
