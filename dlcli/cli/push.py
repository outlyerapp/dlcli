from ..cli import *
import click
import logging

from ..api import dashboards as dashboards_api
from ..api import plugins as plugins_api
from ..api import rules as rules_api

logger = logging.getLogger(__name__)


@cli.group('push')
def push():
    """pushes things up to dataloop"""


@click.command(short_help="Push a dashboard")
@click.argument('dashboard')
def dashboard(dashboard):
    dashboards_api.import_dashboard(file_path=dashboard, **context.settings)


@click.command(short_help="Push a plugin")
@click.argument('plugin')
def plugin(plugin):
    plugins_api.import_plugin(plugin_path=plugin, **context.settings)


@click.command(short_help="Push a rule")
@click.argument('rule')
def rule(rule):
    rules_api.import_rule(rule_path=rule, **context.settings)


push.add_command(dashboard)
push.add_command(plugin)
push.add_command(rule)
