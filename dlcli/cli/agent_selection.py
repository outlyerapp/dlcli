from ..cli import *
from ..api import *
import click

import logging
logger = logging.getLogger(__name__)

@click.command(short_help="show agents")
@click.pass_context
def agents(ctx):
   print 'agents!'


@click.command(short_help="show status")
@click.pass_context
def status(ctx):
   print ctx.parent.parent.params