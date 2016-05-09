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


@click.command(short_help="Search for an Agent fingerprint")
@click.argument('fingerprint')
def fingerprint(fingerprint):
    try:
        utils.search_fingerprint(fingerprint=fingerprint, **context.settings)
    except Exception, e:
        print 'Search agent failed. %s' % e
        sys.exit(1)


@click.command(short_help="Search for an Agent metadata")
@click.argument('metadata')
def metadata(metadata):
    try:
        utils.search_metadata(metadata=metadata, **context.settings)
    except Exception, e:
        print 'Search agent metadata failed. %s' % e
        sys.exit(1)


search.add_command(agent)
search.add_command(fingerprint)
search.add_command(metadata)