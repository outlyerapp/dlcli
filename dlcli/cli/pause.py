from ..cli import *
from ..api import *
import sys
import click
import logging


logger = logging.getLogger(__name__)

from ..api import rules as rules_api

@cli.group('pause')
def pause():
    """pauses things"""


@click.command(short_help="Pause all rules")
def all():
    for r in rules_api.get_rules(**context.settings):
        rules_api.pause_rule(rule=r['name'], **context.settings)


@click.command(short_help="Backup an Organization")
@click.argument('name')
def rule(name):
    rules_api.pause_rule(rule=name, **context.settings)


pause.add_command(all)
pause.add_command(rule)

