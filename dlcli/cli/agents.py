from ..cli import *
import click

import logging
logger = logging.getLogger(__name__)

@cli.group('agents')
@click.pass_context
def agents(ctx):
    pass
