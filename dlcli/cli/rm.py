from ..cli import *
from ..api import *
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('rm')
@click.pass_context
def rm(ctx):
    """deletes things"""


@click.command(short_help="rm account")
@click.argument('account')
@click.pass_context
def account(ctx, account):
    click.confirm(
        'Once you delete an account, there is no going back. Are you sure?',
        abort=True)
    resp = Accounts(ctx).delete_account(account)
    if resp.status_code == 204:
        click.echo('Deleted account ' + account)
    else:
        click.echo('Error deleting ' + account + '. Status Code: ' +
                   click.style(
                       str(resp.status_code),
                       fg='red'))


@click.command(short_help="rm agent")
@click.argument('agent')
@click.pass_context
def agent(ctx, agent):
    resp = Agents(ctx).delete_agent(agent)
    if resp.status_code == 204:
        click.echo('Deleted agent ' + agent)
    else:
        click.echo('Error deleting ' + agent + '. Status Code: ' + click.style(
            str(resp.status_code),
            fg='red'))


@click.command(short_help="rm dashboard")
@click.argument('dashboard')
@click.pass_context
def dashboard(ctx, dashboard):
    resp = Dashboards(ctx).delete_dashboard(dashboard)
    if resp.status_code == 204:
        click.echo('Deleted dashboard ' + dashboard)
    else:
        click.echo('Error deleting ' + dashboard + '. Status Code: ' +
                   click.style(
                       str(resp.status_code),
                       fg='red'))


@click.command(short_help="rm link")
@click.argument('link')
@click.pass_context
def link(ctx, link):
    resp = Links(ctx).delete_link(link)
    if resp.status_code == 204:
        click.echo('Deleted link ' + link)
    else:
        click.echo('Error deleting ' + link + '. Status Code: ' + click.style(
            str(resp.status_code),
            fg='red'))


@click.command(short_help="rm org")
@click.argument('org')
@click.pass_context
def org(ctx, org):
    click.confirm(
        'Once you delete an organization, there is no going back. Are you sure?',
        abort=True)
    resp = Orgs(ctx).delete_org(org)
    if resp.status_code == 204:
        click.echo('Deleted org ' + org)
    else:
        click.echo('Error deleting ' + org + '. Status Code: ' + click.style(
            str(resp.status_code),
            fg='red'))


@click.command(short_help="rm plugin")
@click.argument('plugin')
@click.pass_context
def plugin(ctx, plugin):
    resp = Plugins(ctx).delete_plugin(plugin)
    if resp.status_code == 204:
        click.echo('Deleted plugin ' + plugin)
    else:
        click.echo('Error deleting ' + plugin + '. Status Code: ' +
                   click.style(
                       str(resp.status_code),
                       fg='red'))


@click.command(short_help="rm rule")
@click.argument('rule')
@click.pass_context
def rule(ctx, rule):
    resp = Rules(ctx).delete_rule(rule)
    if resp.status_code == 204:
        click.echo('Deleted rule ' + rule)
    else:
        click.echo('Error deleting ' + rule + '. Status Code: ' + click.style(
            str(resp.status_code),
            fg='red'))


@click.command(short_help="rm tag")
@click.argument('tag')
@click.pass_context
def tag(ctx, tag):
    resp = Tags(ctx).delete_tag(tag)
    if resp.status_code == 204:
        click.echo('Deleted tag ' + tag)
    else:
        click.echo('Error deleting ' + tag + '. Status Code: ' + click.style(
            str(resp.status_code),
            fg='red'))


rm.add_command(account)
rm.add_command(agent)
rm.add_command(dashboard)
rm.add_command(link)
rm.add_command(org)
rm.add_command(plugin)
rm.add_command(rule)
rm.add_command(tag)
