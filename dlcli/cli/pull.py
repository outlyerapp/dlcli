from ..cli import *
import sys
import click
import logging

from ..api import dashboards as dashboards_api
from ..api import plugins as plugins_api
from ..api import rules as rules_api


logger = logging.getLogger(__name__)


@cli.group('pull')
def pull():
    """pulls things down from dataloop"""


@click.command(short_help="Pull a dashboard")
@click.argument('dashboard')
def dashboard(dashboard):
    try:
        print dashboards_api.export_dashboard(dashboard=dashboard, **context.settings)
    except Exception, e:
        print 'Pull dashboard failed. %s' % e
        sys.exit(1)


@click.command(short_help="Pull a plugin")
@click.argument('plugin')
def plugin(plugin):
    try:
        print plugins_api.export_plugin(plugin=plugin, **context.settings)
    except Exception, e:
        print 'Pull plugin failed. %s' % e
        sys.exit(1)


@click.command(short_help="Pull a rule")
@click.argument('rule')
def rule(rule):
    try:
        print rules_api.export_rule(rule=rule, **context.settings)
    except Exception, e:
        print 'Pull rule failed. %s' % e
        sys.exit(1)


pull.add_command(dashboard)
pull.add_command(plugin)
pull.add_command(rule)
