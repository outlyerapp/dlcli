from ..cli import *
from ..api import *
import click
import logging
import uuid

logger = logging.getLogger(__name__)


@cli.group('source')
@click.pass_context
def source(ctx):
    """work with sources"""


@click.command(short_help="Register source")
@click.argument('name')
@click.pass_context
def register(ctx, name):
    finger = uuid.uuid4()
    payload = {
        'mac': '',
        'hostname': name,
        'os_name': '',
        'os_version': '',
        'processes': [],
        'container': '',
        'interfaces': [],
        'mode': 'SOLO',
        'name': name
    }
    print Agents(ctx).register_agent(payload, finger)


@click.command(short_help="Ping source")
@click.argument('name')
@click.argument('fingerprint')
@click.pass_context
def ping(ctx, name, fingerprint):
    payload = {
        'mac': '',
        'hostname': name,
        'os_name': '',
        'os_version': '',
        'processes': [],
        'container': '',
        'interfaces': [],
        'mode': 'SOLO',
        'name': name
    }
    print Agents(ctx).ping_agent(payload, fingerprint)


source.add_command(register)
source.add_command(ping)