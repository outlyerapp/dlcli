from ..cli import *
import click
import requests

import logging
logger = logging.getLogger(__name__)



@cli.group('show')
@click.pass_context
def show(ctx):
    """shows things"""

@click.command(short_help="show status")
@click.pass_context
def status(ctx):
    click.echo('URL: %s' % ctx.parent.parent.params['url'])
    click.echo('Organization: %s' % ctx.parent.parent.params['org'])
    click.echo('Account: %s' % ctx.parent.parent.params['account'])
    click.echo('Key: %s' % ctx.parent.parent.params['key'])
    resp = requests.get(str(ctx.parent.parent.params['url']) + '/orgs/' + str(ctx.parent.parent.params['org']),
                        headers={"Token": ctx.parent.parent.params['key']})
    if resp.status_code == 200:
        click.echo('Authenticated: ' + click.style('True', fg='green'))
    else:
        click.echo('Authenticated: ' + click.style('False', fg='red') + ', Status Code: ' + click.style(str(resp.status_code), fg='red'))


@click.command(short_help="Show accounts")
@click.pass_context
def accounts(ctx):
    _accounts = Accounts(ctx)
    for account in _accounts.get_accounts():
        click.echo(account['name'])


@click.command(short_help="Show agents")
@click.pass_context
def agents(ctx):
    _agents = Agents(ctx)
    for agent in _agents.get_agents():
        click.echo(agent['name'])


@click.command(short_help="Show dashboards")
@click.pass_context
def dashboards(ctx):
    _dashboards = Dashboards(ctx)
    for dashboard in _dashboards.get_dashboards():
        click.echo(dashboard['name'])


@click.command(short_help="Show plugins")
@click.pass_context
def plugins(ctx):
    _plugins = Plugins(ctx)
    for plugin in _plugins.get_plugins():
        click.echo(plugin['name'])


@click.command(short_help="Show links")
@click.pass_context
def links(ctx):
    _links = Links(ctx)
    for link in _links.get_links():
        click.echo(link['id'])


@click.command(short_help="Show orgs")
@click.pass_context
def orgs(ctx):
    _orgs = Orgs(ctx)
    for org in _orgs.get_orgs():
        click.echo(org['name'])


@click.command(short_help="Show rules")
@click.pass_context
def rules(ctx):
    _rules = Rules(ctx)
    for rule in _rules.get_rules():
        click.echo(rule['name'])

@click.command(short_help="Show tags")
@click.pass_context
def tags(ctx):
    _tags = Tags(ctx)
    for tag in _tags.get_tags():
        click.echo(tag['name'])


show.add_command(status)
show.add_command(accounts)
show.add_command(agents)
show.add_command(dashboards)
show.add_command(links)
show.add_command(orgs)
show.add_command(plugins)
show.add_command(rules)
show.add_command(tags)