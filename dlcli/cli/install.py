from ..cli import *
import click
import sys
import logging
import context

from ..api import templates as templates_api

logger = logging.getLogger(__name__)


@cli.group('install')
def install():
    """installs things"""


@click.command(short_help="Install template")
@click.argument('name')
def template(name):
    try:
        print templates_api.install_template(name=name, **context.settings)
    except Exception, e:
        print 'Create template failed. %s' % e
        sys.exit(1)


install.add_command(template)