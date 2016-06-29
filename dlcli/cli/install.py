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
        click.confirm('This will uninstall and re-install the template as a pack. Are you sure?', abort=True)

        resp = packs.delete_pack(name=name, **context.settings)
        if resp.status_code == 204:
            click.echo('Deleted pack ' + name)
        else:
            click.echo('Error deleting ' + name + '. Status Code: ' + click.style(
                str(resp.status_code),
                fg='red'))

        resp = templates_api.install_template(name=name, **context.settings)
        if resp.status_code == 200:
            click.echo('Installed pack ' + name)
        else:
            click.echo('Error installing ' + name + '. Status Code: ' + click.style(
                str(resp.status_code),
                fg='red'))
    except Exception, e:
        print 'Install template failed. %s' % e
        sys.exit(1)


install.add_command(template)