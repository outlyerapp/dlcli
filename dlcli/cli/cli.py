import sys
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
}

@click.group()
@click.option('--debug', is_flag=True, help='Debug mode', default=DEFAULT_ARGS['debug'])
@click.option('--loglevel', help='Log level', default=DEFAULT_ARGS['log_level'])
@click.option('--logfile', help='log file')
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx, debug, loglevel, logfile):
    if debug:
        numeric_log_level = logging.DEBUG or loglevel.upper() == 'DEBUG'
        format_string = '%(asctime)s %(levelname)-9s %(name)22s %(funcName)22s:%(lineno)-4d %(message)s'
    else:
        numeric_log_level = getattr(logging, loglevel.upper(), None)
        format_string = '%(asctime)s %(levelname)-9s %(message)s'
        if not isinstance(numeric_log_level, int):
            raise ValueError('Invalid log level: {0}'.format(loglevel))

    handler = logging.StreamHandler(
        open(logfile, 'a') if logfile else sys.stdout)

    handler.setFormatter(logging.Formatter(format_string))
    logging.root.addHandler(handler)
    logging.root.setLevel(numeric_log_level)
    logger = logging.getLogger('curator.cli')