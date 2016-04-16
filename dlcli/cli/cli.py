import sys
import context
from ..api import *
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


@click.group()
@click.option('--debug',
              is_flag=True,
              help='Debug mode',
              default=False)
@click.option('--loglevel',
              help='Log level',
              type=str,
              default='info')
@click.option('--settingsfile',
              help='Settings File',
              type=str,
              default=context.settings['settingsfile'])
@click.option('--backupdir',
              help='Backups Directory',
              type=str,
              required=False)
@click.option('--url', help='API URL', type=str)
@click.option('--org',
              help='Organization Name',
              type=str,
              required=False)
@click.option('--account',
              help='Account Name',
              type=str,
              required=False)
@click.option('--key',
              help='API Key',
              type=click.UUID,
              required=False)
@click.version_option(version=__version__)
def cli(settingsfile, url, org, account, key, backupdir, loglevel, debug):
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

    try:
        # load some settings from file over the top of the defaults
        stream = open(settingsfile, 'r')
        file_settings = yaml.load(stream)
        context.settings.update({k: v for k, v in file_settings.iteritems() if v})
    except IOError:
        pass

    # command line options override defaults and settings file
    args = {
        'settingsfile': settingsfile,
        'url': url,
        'org': org,
        'account': account,
        'key': key,
        'backupdir': backupdir
    }
    for arg, value in args.iteritems():
        if value:
            context.settings[arg] = value


@click.command(short_help="status")
def status():
    click.echo('URL: %s/orgs/%s/accounts ' % (context.settings['url'], context.settings['org']))
    click.echo('Organization: %s' % context.settings['org'])
    click.echo('Account: %s' % context.settings['account'])
    click.echo('Key: %s' % context.settings['key'])

    resp = requests.get(context.settings['url'] + '/orgs/' + context.settings['org'] + '/accounts',
                        headers={'Authorization': "Bearer " + context.settings['key']}).status_code
    if resp == 200:
        click.echo('Authenticated: %s' % click.style('True', fg='green'))
    else:
        click.echo('Authenticated: %s, Status Code: %s' % (click.style('False', fg='red'),
                                                           click.style(str(resp), fg='red'))
        )


cli.add_command(status)
