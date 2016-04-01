from ..cli import *
from ..api import *
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('search')
@click.pass_context
def search(ctx):
    """performs searches"""


@click.command(short_help="Search for an Agent")
@click.argument('agent')
@click.pass_context
def agent(ctx, agent):
    utils.search_agent(ctx, agent)

search.add_command(agent)
