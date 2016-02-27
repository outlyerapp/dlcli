import sys
import yaml
import click
from .. import __version__

import logging
logger = logging.getLogger(__name__)

try:
    from logging import NullHandler
except ImportError:
    from logging import Handler

    class NullHandler(Handler):
        def emit(self, record):
            pass

DEFAULT_ARGS = {
    'debug': False,
    'log_level': 'INFO',
    'url': 'https://api.dataloop.io/v1',
    'org': None,
    'account': None,
    'key': None
}

settings_file = "/tmp/.dlcli.yaml"
try:
    stream = open(settings_file, 'r')
    settings = yaml.load(stream)
    DEFAULT_ARGS.update({k: v for k, v in settings.iteritems() if v})
except IOError:
    pass


@click.group()
@click.option('--debug', is_flag=True, help='Debug mode', default=DEFAULT_ARGS['debug'])
@click.option('--loglevel', help='Log level', type=str, default=DEFAULT_ARGS['log_level'])
@click.option('--url', help='API URL', type=str, default=DEFAULT_ARGS['url'])
@click.option('--org', help='Organization Name', type=str, default=DEFAULT_ARGS['org'])
@click.option('--account', help='Account Name', type=str, default=DEFAULT_ARGS['account'])
@click.option('--key', help='API Key', type=str, default=DEFAULT_ARGS['key'])
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx, debug, loglevel, url, org, account, key):
    if debug:
        numeric_log_level = logging.DEBUG or loglevel.upper() == 'DEBUG'
        format_string = '%(asctime)s %(levelname)-9s %(name)22s %(funcName)22s:%(lineno)-4d %(message)s'
    else:
        numeric_log_level = getattr(logging, loglevel.upper(), None)
        format_string = '%(asctime)s %(levelname)-9s %(message)s'
        if not isinstance(numeric_log_level, int):
            raise ValueError('Invalid log level: {0}'.format(loglevel))

    handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(logging.Formatter(format_string))
    logging.root.addHandler(handler)
    logging.root.setLevel(numeric_log_level)
    logger = logging.getLogger('dlcli.cli')
    logging.getLogger("requests").setLevel(logging.WARNING)