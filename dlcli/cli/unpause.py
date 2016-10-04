from ..cli import *
from ..api import *
import sys
import click
import logging


logger = logging.getLogger(__name__)

from ..api import rules as rules_api

@cli.group('unpause')
def unpause():
    """unpauses things"""


@click.command(short_help="Pause all rules")
def all():
    for r in rules_api.get_rules(**context.settings):
        rules_api.unpause_rule(rule=r['name'], **context.settings)



@click.command(short_help="Backup an Organization")
@click.argument('name')
def rule(name):
    rules_api.unpause_rule(rule=name, **context.settings)


unpause.add_command(all)
unpause.add_command(rule)

