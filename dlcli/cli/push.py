from ..cli import *
from ..api import *
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('push')
@click.pass_context
def push(ctx):
    """pushes things up to dataloop"""


@click.command(short_help="Push a dashboard")
@click.argument('dashboard')
@click.pass_context
def dashboard(ctx, dashboard):
    Dashboards(ctx).import_dashboard(dashboard)


@click.command(short_help="Push a plugin")
@click.argument('plugin')
@click.pass_context
def plugin(ctx, plugin):
    Plugins(ctx).import_plugin(plugin)


@click.command(short_help="Push a rule")
@click.argument('rule')
@click.pass_context
def rule(ctx, rule):
    Rules(ctx).import_rule(rule)


push.add_command(dashboard)
push.add_command(plugin)
push.add_command(rule)