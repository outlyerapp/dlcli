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
    print 'coming soon'


push.add_command(dashboard)