from ..cli import *
import click
import sys
import logging
import context

from ..api import user as user_api
from ..api import templates as templates_api

logger = logging.getLogger(__name__)


@cli.group('create')
def create():
    """creates things"""


@click.command(short_help="Create token")
@click.argument('name')
def token(name):
    try:
        print user_api.create_user_token(token_name=name, **context.settings)['token']
    except Exception, e:
        print 'Create token failed. %s' % e
        sys.exit(1)

@click.command(short_help="Create pack")
@click.argument('name')
def pack(name):
    try:
        home = os.path.join(os.getcwd(), name)
        create_tree(home, {})

        content = {
            '': ['package.yaml', 'README.md'],
            'plugins': [name + '.py'],
            'dashboards': [name + '.yaml'],
            'rules': [name + '.yaml']
        }
        create_tree(home, content)

        package_desc = {
            "title": name,
            "author": user_api.get_user(**context.settings)['name'],
            "version": "0.0.1",
            "description": "",
            "instructions_required": False,
            "icon": {
                "name": "",
                "background": "blue",
                "foreground": "white"
            }
        }
        with open(os.path.join(home, 'package.yaml'), 'w') as package_file:
            package_file.write(yaml.safe_dump(package_desc, default_flow_style=False, explicit_start=True))

    except Exception, e:
        print 'Create pack failed. %s' % e
        sys.exit(1)

@click.command(short_help="Create template")
@click.argument('name')
def template(name):
    try:
        print yaml.safe_dump(templates_api.create_template(name=name, **context.settings), default_flow_style=False, explicit_start=True)
    except Exception, e:
        print 'Create template failed. %s' % e
        sys.exit(1)

create.add_command(token)
create.add_command(pack)
create.add_command(template)