from ..cli import *
import click

import logging
logger = logging.getLogger(__name__)


@cli.group('show')
@click.pass_context
def show(ctx):
    """shows things"""


@click.command(short_help="show agents")
@click.pass_context
def agents(ctx):
   print 'agents!'


@click.command(short_help="show status")
@click.pass_context
def status(ctx):
    click.echo('Organization: %s' % ctx.parent.parent.params['org'])
    click.echo('Account: %s' % ctx.parent.parent.params['account'])
    click.echo('Key: %s' % ctx.parent.parent.params['key'])


show.add_command(status)
show.add_command(agents)