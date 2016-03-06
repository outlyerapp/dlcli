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
    resp = requests.get(str(ctx.parent.parent.params['url']) + '/orgs/' + str(ctx.parent.parent.params['org']), headers={"Token": ctx.parent.parent.params['key']})
    if resp.status_code == 200:
        click.echo('Authenticated: ' + click.style('True', fg='green'))
    else:
        click.echo('Authenticated: ' + click.style('False', fg='red') + ', Status Code: ' + click.style(str(resp.status_code), fg='red'))


@click.command(short_help="Show accounts")
@click.pass_context
def accounts(ctx):
    for account in Accounts(ctx).get_accounts():
        click.echo(account['name'])


@click.command(short_help="Show agents")
@click.pass_context
def agents(ctx):
    for agent in Agents(ctx).get_agents():
        if agent['presence_state'] == 'online':
            click.echo(click.style(agent['name'], fg='green'))
        else:
            click.echo(click.style(agent['name'], fg='red'))


@click.command(short_help="Show dashboards")
@click.pass_context
def dashboards(ctx):
    for dashboard in Dashboards(ctx).get_dashboards():
        click.echo(dashboard['name'])


@click.command(short_help="Show plugins")
@click.pass_context
def plugins(ctx):
    for plugin in Plugins(ctx).get_plugins():
        click.echo(plugin['name'])


@click.command(short_help="Show links")
@click.pass_context
def links(ctx):
    for link in Links(ctx).get_links():
        click.echo(link['id'])


@click.command(short_help="Show orgs")
@click.pass_context
def orgs(ctx):
    for org in Orgs(ctx).get_orgs():
        click.echo(org['name'])


@click.command(short_help="Show rules")
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


@click.command(short_help="Show alerts")
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


@click.command(short_help="Show tags")
@click.pass_context
def tags(ctx):
    for tag in Tags(ctx).get_tags():
        click.echo(tag['name'])


show.add_command(status)
show.add_command(accounts)
show.add_command(agents)
show.add_command(dashboards)
show.add_command(links)
show.add_command(orgs)
show.add_command(plugins)
show.add_command(rules)
show.add_command(alerts)
show.add_command(tags)
