from ..cli import *
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('create')
@click.pass_context
def create(ctx):
    """creates things"""


@click.command(short_help="Create token")
@click.argument('name')
@click.pass_context
def token(ctx, name):
    try:
        print User(ctx).create_user_token(name)['token']
    except:
        print "token creation failed. is the name already taken?"

create.add_command(token)


