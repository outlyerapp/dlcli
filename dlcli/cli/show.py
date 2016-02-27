import click
from .agent_selection import *

import logging
logger = logging.getLogger(__name__)

@cli.group('show')
@click.pass_context
def show(ctx):
    """shows things"""
show.add_command(status)
show.add_command(agents)