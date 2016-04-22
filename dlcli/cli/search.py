from ..cli import *
from ..api import *
import sys
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('search')
def search():
    """performs searches"""


@click.command(short_help="Search for an Agent")
@click.argument('agent')
def agent(agent):
    try:
        utils.search_agent(agent=agent, **context.settings)
    except Exception, e:
        print 'Search agent failed. %s' % e
        sys.exit(1)


search.add_command(agent)
