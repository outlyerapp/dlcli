from ..cli import *
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('get')
@click.pass_context
def get(ctx):
    """gets things"""


@click.command(short_help="Get accounts")
@click.pass_context
def accounts(ctx):
    for account in Accounts(ctx).get_accounts():
        click.echo(account['name'])


@click.command(short_help="Get agents")
@click.pass_context
def agents(ctx):
    for agent in Agents(ctx).get_agents():
        if agent['presence_state'] == 'online':
            click.echo(click.style(agent['name'], fg='green'))
        else:
            click.echo(click.style(agent['name'], fg='red'))


@click.command(short_help="Get dashboards")
@click.pass_context
def dashboards(ctx):
    for dashboard in Dashboards(ctx).get_dashboards():
        click.echo(dashboard['name'])


@click.command(short_help="Get plugins")
@click.pass_context
def plugins(ctx):
    for plugin in Plugins(ctx).get_plugins():
        click.echo(plugin['name'])


@click.command(short_help="Get links")
@click.pass_context
def links(ctx):
    for link in Links(ctx).get_links():
        click.echo(link['id'])


@click.command(short_help="Get orgs")
@click.pass_context
def orgs(ctx):
    for org in Orgs(ctx).get_orgs():
        click.echo(org['name'])


@click.command(short_help="Get rules")
@click.pass_context
def rules(ctx):
    _rules = Rules(ctx)
    for rule in _rules.get_rules():
        for criteria in _rules.get_criteria(rule['name']):
            if criteria['condition']['threshold']:
                message = "on %s %s %s %d for %d seconds" % (
                    criteria['scopes'][0]['type'],
                    criteria['scopes'][0]['name'],
                    criteria['condition']['operator'],
                    criteria['condition']['threshold'],
                    criteria['condition']['timeout'])
            else:
                message = 'on %s %s for %d seconds' % (
                    criteria['scopes'][0]['type'],
                    criteria['scopes'][0]['name'],
                    criteria['condition']['timeout'])

            if criteria['state'] == 'hit':
                agent_names = []
                triggered_by = criteria['triggered_by']
                for agent_id in triggered_by:
                    agent_names.append(Agents(ctx).get_agent_name_from_id(agent_id))
                click.echo(click.style('%s %s %s triggered by %s', fg='red') % (
                    rule['name'],
                    criteria['metric'],
                    message,
                    ','.join(map(str, agent_names))))
            else:
                click.echo(click.style('%s %s %s', fg='green') % (
                    rule['name'],
                    criteria['metric'],
                    message))


@click.command(short_help="Get alerts")
@click.pass_context
def alerts(ctx):
    _rules = Rules(ctx)
    for rule in _rules.get_rules():
        for criteria in _rules.get_criteria(rule['name']):
            if criteria['condition']['threshold']:
                message = "on %s %s %s %d for %d seconds" % (
                    criteria['scopes'][0]['type'],
                    criteria['scopes'][0]['name'],
                    criteria['condition']['operator'],
                    criteria['condition']['threshold'],
                    criteria['condition']['timeout'])
            else:
                message = 'on %s %s for %d seconds' % (
                    criteria['scopes'][0]['type'],
                    criteria['scopes'][0]['name'],
                    criteria['condition']['timeout'])

            if criteria['state'] == 'hit':
                agent_names = []
                triggered_by = criteria['triggered_by']
                for agent_id in triggered_by:
                    agent_names.append(Agents(ctx).get_agent_name_from_id(agent_id))
                click.echo(click.style('%s %s %s triggered by %s', fg='red') % (
                    rule['name'],
                    criteria['metric'],
                    message,
                    ','.join(map(str, agent_names))))


@click.command(short_help="Get tags")
@click.pass_context
def tags(ctx):
    for tag in Tags(ctx).get_tags():
        click.echo(tag['name'])


get.add_command(accounts)
get.add_command(agents)
get.add_command(dashboards)
get.add_command(links)
get.add_command(orgs)
get.add_command(plugins)
get.add_command(rules)
get.add_command(alerts)
get.add_command(tags)
