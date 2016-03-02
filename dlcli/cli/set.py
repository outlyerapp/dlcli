from ..cli import *
from ..api import *
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('set')
@click.pass_context
def set(ctx):
    """sets things"""


@click.command(short_help="Set url")
@click.argument('url')
@click.pass_context
def url(ctx, url):
    save_setting(ctx, {"url": str(url)})


@click.command(short_help="Set organization")
@click.argument('org')
@click.pass_context
def org(ctx, org):
    save_setting(ctx, {"org": str(org)})


@click.command(short_help="Set account")
@click.argument('account')
@click.pass_context
def account(ctx, account):
    save_setting(ctx, {"account": str(account)})


@click.command(short_help="Set key")
@click.argument('key')
@click.pass_context
def key(ctx, key):
    save_setting(ctx, {"key": str(key)})

set.add_command(url)
set.add_command(org)
set.add_command(account)
set.add_command(key)