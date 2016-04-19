from ..cli import *
import click
import logging
import uuid

from ..api import agents as agents_api

logger = logging.getLogger(__name__)


@cli.group('source')
def source():
    """work with sources"""


@click.command(short_help="Register source")
@click.argument('name')
def register(name):
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
    print agents_api.register_agent(payload=payload, finger=finger, **context.settings)


@click.command(short_help="Ping source")
@click.argument('name')
@click.argument('fingerprint')
def ping(name, fingerprint):
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
    print agents_api.ping_agent(payload=payload, finger=fingerprint, **context.settings)


source.add_command(register)
source.add_command(ping)
