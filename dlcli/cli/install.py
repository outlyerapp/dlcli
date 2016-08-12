from ..cli import *
import click
import sys
import logging
import context

from ..api import packs as packs_api
from ..api import templates as templates_api

logger = logging.getLogger(__name__)


@cli.group('install')
def install():
    """installs things"""


@click.command(short_help="Install template")
@click.argument('name')
@click.option('--yes', is_flag=True)
def template(name, yes):
    try:
        if not yes:
            click.confirm('This will uninstall and re-install the template as a pack. Are you sure?', abort=True)

        pack_list = []
        for pack in packs_api.get_packs(**context.settings):
            pack_list.append(pack['name'])

        if name in pack_list:
            resp = packs_api.delete_pack(name=name, **context.settings)
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