from ..cli import *
from ..api import *
import click

import logging
logger = logging.getLogger(__name__)


@cli.group('pull')
@click.pass_context
def pull(ctx):
    """pulls things down from dataloop"""


@click.command(short_help="Pull a dashboard")
@click.argument('dashboard')
@click.pass_context
def dashboard(ctx, dashboard):
    _dashboards = Dashboards(ctx)
    print _dashboards.export_dashboard(dashboard)


@click.command(short_help="Pull a plugin")
@click.argument('plugin')
@click.pass_context
def plugin(ctx, plugin):
    _plugins = Plugins(ctx)
    print _plugins.export_plugin(plugin)

pull.add_command(dashboard)
pull.add_command(plugin)