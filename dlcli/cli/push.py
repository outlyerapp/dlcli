from ..cli import *
import os
import sys
import click
import logging

from ..api import annotations as annotations_api
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
        resp = templates_api.create_template(name=name, **context.settings)
        if resp.status_code == 200:
            click.echo('Template created: ' + name)
        else:
            click.echo('Error creating template ' + name + '. Status Code: ' + click.style(str(resp.status_code), fg='red'))

        # upload package.yaml
        resp = templates_api.put_manifest(name=name, path=path, **context.settings)
        if resp.status_code == 200:
            click.echo('Uploaded package.yaml')
        else:
            click.echo('Error uploading package.yaml' + '. Status Code: ' + click.style(str(resp.status_code), fg='red'))

        # upload plugins
        for p in os.listdir(os.path.join(path, 'plugins')):
            if p.endswith(".py"):
                resp = templates_api.put_plugin(path=os.path.join(path, 'plugins', p), template=name, **context.settings)
                if resp.status_code == 200:
                    click.echo('Uploaded plugin ' + p)
                else:
                    click.echo('Error uploading plugin ' + p + '. Status Code: ' + click.style(str(resp.status_code), fg='red'))

        # upload dashboards
        for p in os.listdir(os.path.join(path, 'dashboards')):
            if p.endswith(".yaml"):
                resp = templates_api.put_dashboard(path=os.path.join(path, 'dashboards', p), template=name, **context.settings)
                if resp.status_code == 200:
                    click.echo('Uploaded dashboard ' + p)
                else:
                    click.echo('Error uploading dashboard ' + p + '. Status Code: ' + click.style(str(resp.status_code), fg='red'))

        # upload rules
        for p in os.listdir(os.path.join(path, 'rules')):
            if p.endswith(".yaml"):
                resp = templates_api.put_rule(path=os.path.join(path, 'rules', p), template=name, **context.settings)
                if resp.status_code == 200:
                    click.echo('Uploaded rule ' + p)
                else:
                    click.echo('Error uploading rule ' + p + '. Status Code: ' + click.style(str(resp.status_code), fg='red'))

    except Exception, e:
        print 'Push template failed. %s' % e
        sys.exit(1)

@click.command(short_help="Push an annotation")
@click.argument('stream')
@click.option('--name', help='annotation name', type=str, default=None)
@click.option('--description', help='annotation description', type=str, default=None)
def annotation(stream, name, description):
    try:
        annotations_api.create_annotation(stream=stream, name=name, description=description, **context.settings)
    except Exception, e:
        print 'Push annotation failed. %s' % e
        sys.exit(1)

push.add_command(dashboard)
push.add_command(plugin)
push.add_command(rule)
push.add_command(template)
push.add_command(annotation)