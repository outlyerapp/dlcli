from ..cli import *
import sys
import click
import logging

from ..api import dashboards as dashboards_api
from ..api import plugins as plugins_api
from ..api import rules as rules_api
from ..api import templates as templates_api

logger = logging.getLogger(__name__)


@cli.group('push')
def push():
    """pushes things up to dataloop"""


@click.command(short_help="Push a dashboard")
@click.argument('dashboard')
def dashboard(dashboard):
    try:
        dashboards_api.import_dashboard(file_path=dashboard, **context.settings)
    except Exception, e:
        print 'Push dashboard failed. %s' % e
        sys.exit(1)


@click.command(short_help="Push a plugin")
@click.argument('plugin')
def plugin(plugin):
    try:
        plugins_api.import_plugin(plugin_path=plugin, **context.settings)
    except Exception, e:
        print 'Push plugin failed. %s' % e
        sys.exit(1)


@click.command(short_help="Push a rule")
@click.argument('rule')
def rule(rule):
    try:
        rules_api.import_rule(rule_path=rule, **context.settings)
    except Exception, e:
        print 'Push rule failed. %s' % e
        sys.exit(1)


@click.command(short_help="Push a template")
@click.argument('name')
@click.argument('path')
def template(name, path):
    try:
        click.confirm('This will delete and recreate the template. Are you sure?', abort=True)

        # delete old template
        templates_api.delete_template(name=name, **context.settings)

        # create new template
        templates_api.create_template(name=name, **context.settings)

        # upload package.yaml
        templates_api.put_manifest(name=name, path=path, **context.settings)

        # upload plugins
        for p in os.listdir(os.path.join(path, 'plugins')):
            if p.endswith(".py"):
                templates_api.put_plugin(path=os.path.join(path, 'plugins', p), name=name, **context.settings)

        # upload dashboards
        for p in os.listdir(os.path.join(path, 'dashboards')):
            if p.endswith(".yaml"):
                templates_api.put_dashboard(path=os.path.join(path, 'dashboards', p), name=name, **context.settings)

        # upload rules
        for p in os.listdir(os.path.join(path, 'rules')):
            if p.endswith(".yaml"):
                templates_api.put_rule(path=os.path.join(path, 'rules', p), name=name, **context.settings)

    except Exception, e:
        print 'Push template failed. %s' % e
        sys.exit(1)

push.add_command(dashboard)
push.add_command(plugin)
push.add_command(rule)
push.add_command(template)