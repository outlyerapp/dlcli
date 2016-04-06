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
    for a in Accounts(ctx).get_accounts():
        click.echo(a['name'])


@click.command(short_help="Get agents")
@click.argument('status', type=click.Choice(['all', 'up', 'down']), default='all')
@click.option('--tag', help='Tag Name', type=str, default=None)
@click.pass_context
def agents(ctx, status, tag):
    for a in Agents(ctx).get_agents():
        if tag:
            if tag in a['tags']:
                utils.agent_status_check(a, status)
        else:
            utils.agent_status_check(a, status)


@click.command(short_help="Get an agent")
@click.argument('name')
@click.pass_context
def agent(ctx, name):
    click.echo(json.dumps(Agents(ctx).get_agent(name), indent=4))


@click.command(short_help="Get dashboards")
@click.pass_context
def dashboards(ctx):
    for dashboard in Dashboards(ctx).get_dashboards():
        click.echo(dashboard['name'])


@click.command(short_help="Get plugins")
@click.pass_context
def plugins(ctx):
    for p in Plugins(ctx).get_plugins():
        click.echo(p['name'])


@click.command(short_help="Get links")
@click.pass_context
def links(ctx):
    for l in Links(ctx).get_links():
        click.echo(l['id'])


@click.command(short_help="Get orgs")
@click.pass_context
def orgs(ctx):
    for o in Orgs(ctx).get_orgs():
        click.echo(o['name'])


@click.command(short_help="Get rules")
@click.pass_context
def rules(ctx):
    _rules = Rules(ctx)
    for r in _rules.get_rules():
        for criteria in _rules.get_criteria(r['name']):
            if criteria['condition']['threshold']:
                criteria_type = criteria['scopes'][0]['type']
                if criteria_type == 'tag':
                    scope_key = 'id'
                else:
                    scope_key = 'name'
                message = "on %s %s %s %d for %d seconds" % (
                    criteria['scopes'][0]['type'],
                    criteria['scopes'][0][scope_key],
                    criteria['condition']['operator'],
                    criteria['condition']['threshold'],
                    criteria['condition']['timeout'])
            else:
                criteria_type = criteria['scopes'][0]['type']
                if criteria_type == 'tag':
                    scope_key = 'id'
                else:
                    scope_key = 'name'
                message = 'on %s %s for %d seconds' % (
                    criteria['scopes'][0]['type'],
                    criteria['scopes'][0][scope_key],
                    criteria['condition']['timeout'])

            if criteria['state'] == 'hit':
                agent_names = []
                triggered_by = criteria['triggered_by']
                for agent_id in triggered_by:
                    agent_names.append(Agents(ctx).get_agent_name_from_id(
                        agent_id))
                click.echo(click.style('%s %s %s triggered by %s',
                                       fg='red') %
                           (r['name'], criteria['metric'], message,
                            ','.join(map(str, agent_names))))
            else:
                click.echo(click.style('%s %s %s',
                                       fg='green') %
                           (r['name'], criteria['metric'], message))


@click.command(short_help="Get alerts")
@click.pass_context
def alerts(ctx):
    _rules = Rules(ctx)
    for r in _rules.get_rules():
        for criteria in _rules.get_criteria(r['name']):
            if criteria['condition']['threshold']:
                criteria_type = criteria['scopes'][0]['type']
                if criteria_type == 'tag':
                    scope_key = 'id'
                else:
                    scope_key = 'name'
                message = "on %s %s %s %d for %d seconds" % (
                    criteria['scopes'][0]['type'],
                    criteria['scopes'][0][scope_key],
                    criteria['condition']['operator'],
                    criteria['condition']['threshold'],
                    criteria['condition']['timeout'])
            else:
                criteria_type = criteria['scopes'][0]['type']
                if criteria_type == 'tag':
                    scope_key = 'id'
                else:
                    scope_key = 'name'
                message = 'on %s %s for %d seconds' % (
                    criteria['scopes'][0]['type'],
                    criteria['scopes'][0][scope_key],
                    criteria['condition']['timeout'])

            if criteria['state'] == 'hit':
                agent_names = []
                triggered_by = criteria['triggered_by']
                for agent_id in triggered_by:
                    agent_names.append(Agents(ctx).get_agent_name_from_id(
                        agent_id))
                click.echo(click.style('%s %s %s triggered by %s',
                                       fg='red') %
                           (r['name'], criteria['metric'], message,
                            ','.join(map(str, agent_names))))


@click.command(short_help="Get tags")
@click.pass_context
def tags(ctx):
    for t in Tags(ctx).get_tags():
        click.echo(t['name'])


@click.command(short_help="Get metrics")
@click.option('--agent', help='Agent Name', type=str, default=None)
@click.option('--tag', help='Tag Name', type=str, default=None)
@click.pass_context
def metrics(ctx, agent, tag):
    if not agent and not tag:
        click.echo('Specify an agent or tag to get the metrics')
        sys.exit(1)
    if agent:
        agent_id = None
        agent_details = Agents(ctx).get_agents()
        for a in agent_details:
            if a['name'] == agent:
                agent_id = a['id']
        for metric in Metrics(ctx).get_agent_metrics(agent_id):
            print metric['name']
    if tag:
        for metric in Metrics(ctx).get_tag_metrics(tag):
            print metric['name']


@click.command(short_help="Get series")
@click.option('--agent', help='Agent Name', type=str, default=None)
@click.option('--tag', help='Tag Name', type=str, default=None)
@click.option('--resolution', help='Time between points', type=int, default=30)
@click.option('--period', help='Length of time', type=int, default=600)
@click.argument('metric')
@click.pass_context
def series(ctx, metric, agent, tag, resolution, period):
    if not agent and not tag:
        click.echo('Specify an agent or tag to get the metrics')
        sys.exit(1)

    if agent:
        agent_id = None
        agent_details = Agents(ctx).get_agents()
        for a in agent_details:
            if a['name'] == agent:
                agent_id = a['id']
        for s in Series(ctx).get_agent_series(agent_id, metric, resolution, period):
            points = []
            for point in s['points']:
                if point['type'] == 'boolean':
                    if point['all']:
                        points.append(0)
                    else:
                        points.append(2)
                else:
                    points.append(point['avg'])
            print ','.join(map(str, points))
    if tag:
        for s in Series(ctx).get_tag_series(tag, metric, resolution, period):
            points = []
            click.echo(click.style(s['source']['name'], fg='green'))
            for point in s['points']:
                if point['type'] == 'boolean':
                    if point['all']:
                        points.append(0)
                    else:
                        points.append(2)
                else:
                    points.append(point['avg'])
            print ','.join(map(str, points))


@click.command(short_help="Get user")
@click.argument('tokens', required=False)
@click.pass_context
def user(ctx, tokens):
    if tokens:
        token_list = User(ctx).get_user_tokens()
        for t in token_list:
            print t['name']
    else:
        print User(ctx).get_user()['name'].lower()


get.add_command(accounts)
get.add_command(agents)
get.add_command(agent)
get.add_command(dashboards)
get.add_command(links)
get.add_command(orgs)
get.add_command(plugins)
get.add_command(rules)
get.add_command(alerts)
get.add_command(tags)
get.add_command(metrics)
get.add_command(series)
get.add_command(user)

