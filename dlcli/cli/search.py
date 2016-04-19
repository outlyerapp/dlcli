from ..cli import *
from ..api import *
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('search')
def search():
    """performs searches"""


@click.command(short_help="Search for an Agent")
@click.argument('agent')
def agent(agent):
    utils.search_agent(agent=agent, **context.settings)


search.add_command(agent)
