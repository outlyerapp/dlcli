from ..cli import *
import sys
import yaml
import click
import logging

from ..api import accounts as accounts_api
from ..api import agents as agents_api
from ..api import dashboards as dashboards_api
from ..api import links as links_api
from ..api import orgs as orgs_api
from ..api import packs as packs_api
from ..api import plugins as plugins_api
from ..api import rules as rules_api
from ..api import tags as tags_api
from ..api import templates as templates_api
from ..api import metrics as metrics_api
from ..api import series as series_api
from ..api import user as user_api

logger = logging.getLogger(__name__)


@cli.group('get')
def get():
    """gets things"""


@click.command(short_help="Get accounts")
def accounts():
    try:
        for a in accounts_api.get_accounts(**context.settings):
            click.echo(a['name'])
    except Exception, e:
        print 'Get accounts failed. %s' % e


@click.command(short_help="Get agents")
@click.argument('status', type=click.Choice(['all', 'up', 'down']), default='all')
@click.option('--tag', help='Tag Name', type=str, default=None)
@click.option('--deregistered', help='Get deregistered agents', is_flag=True)
def agents(status, tag, deregistered):
    try:
        for a in agents_api.get_agents(**context.settings):
            if tag:
                if tag in a['tags']:
                    utils.agent_status_check(a, status)
            if deregistered:
                if a['status'] != 'REGISTERED':
                    print a['name']
            else:
                utils.agent_status_check(a, status)
    except Exception, e:
        print 'Get agents failed. %s' % e
        sys.exit(1)


@click.command(short_help="Get an agent")
@click.argument('name')
def agent(name):
    try:
        click.echo(json.dumps(agents_api.get_agent(agent_name=name, **context.settings), indent=4))
    except Exception, e:
        print 'Get agent failed. %s' % e
        sys.exit(1)

@click.command(short_help="Get dashboards")
def dashboards():
    try:
        for d in dashboards_api.get_dashboards(**context.settings):
            click.echo(d['name'])
    except Exception, e:
        print 'Get dashboards failed. %s' % e
        sys.exit(1)


@click.command(short_help="Get plugins")
def plugins():
    try:
        for p in plugins_api.get_plugins(**context.settings):
            click.echo(p['name'])
    except Exception, e:
        print 'Get plugins failed. %s' % e
        sys.exit(1)

@click.command(short_help="Get links")
def links():
    try:
        for l in links_api.get_links(**context.settings):
            click.echo(l['id'])
    except Exception, e:
        print 'Get links failed. %s' % e
        sys.exit(1)

@click.command(short_help="Get orgs")
def orgs():
    try:
        for o in orgs_api.get_orgs(**context.settings):
            click.echo(o['name'])
    except Exception, e:
        print 'Get orgs failed. %s' % e
        sys.exit(1)

@click.command(short_help="Get rules")
def rules():
    try:
        for r in rules_api.get_rules(**context.settings):
            print r['name']
    except Exception, e:
        print 'Get rules failed. %s' % e
        sys.exit(1)

@click.command(short_help="Get criterias")
def criterias():
    try:
        for r in rules_api.get_rules(**context.settings):
            for criteria in rules_api.get_criteria(rule=r['name'], **context.settings):
                on = 'unknown'
                if criteria['condition']['threshold']:
                    criteria_type = criteria['scopes'][0]['type']
                    if criteria_type == 'tag':
                        on = criteria['scopes'][0]['id']
                    if criteria_type == 'agent':
                        on = agents_api.get_agent_name_from_id(agent_id=criteria['scopes'][0]['id'], **context.settings)
                    message = "on %s %s %s %d for %d seconds" % (
                        criteria['scopes'][0]['type'],
                        on,
                        criteria['condition']['operator'],
                        criteria['condition']['threshold'],
                        criteria['condition']['timeout'])
                else:
                    criteria_type = criteria['scopes'][0]['type']
                    if criteria_type == 'tag':
                        on = criteria['scopes'][0]['id']
                    if criteria_type == 'agent':
                        on = agents_api.get_agent_name_from_id(agent_id=criteria['scopes'][0]['id'], **context.settings)
                    message = 'on %s %s for %d seconds' % (
                        criteria['scopes'][0]['type'],
                        on,
                        criteria['condition']['timeout'])

                if criteria['state'] == 'hit':
                    agent_names = []
                    triggered_by = criteria['triggered_by']
                    for agent_id in triggered_by:
                        agent_names.append(agents_api.get_agent_name_from_id(agent_id=agent_id, **context.settings))
                    click.echo(
                        click.style('%s %s %s triggered by %s', fg='red') % (r['name'], criteria['metric'], message, ','.join(map(str, agent_names)))
                    )
                else:
                    click.echo(click.style('%s %s %s', fg='green') % (r['name'], criteria['metric'], message))
    except Exception, e:
        print 'Get criterias failed. %s' % e
        sys.exit(1)

@click.command(short_help="Get alerts")
def alerts():
    try:
        triggered = False
        for r in rules_api.get_rules(**context.settings):
            for criteria in rules_api.get_criteria(rule=r['name'], **context.settings):
                if criteria['condition']['threshold']:
                    criteria_type = criteria['scopes'][0]['type']
                    if criteria_type == 'tag' or criteria_type == 'agent':
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
                    if criteria_type == 'tag' or criteria_type == 'agent':
                        scope_key = 'id'
                    else:
                        scope_key = 'name'
                    message = 'on %s %s for %d seconds' % (
                        criteria['scopes'][0]['type'],
                        criteria['scopes'][0][scope_key],
                        criteria['condition']['timeout'])

                if criteria['state'] == 'hit':
                    triggered = True
                    agent_names = []
                    triggered_by = criteria['triggered_by']
                    for agent_id in triggered_by:
                        agent_names.append(agents_api.get_agent_name_from_id(agent_id=agent_id, **context.settings))
                    click.echo(click.style('%s %s %s triggered by %s',
                                           fg='red') %
                               (r['name'], criteria['metric'], message,
                                ','.join(map(str, agent_names))))
        if not triggered:
            print "all clear! no alert rule criteria are triggered"
            sys.exit(0)
        else:
            sys.exit(2)
    except Exception, e:
        print 'Get alerts failed. %s' % e
        sys.exit(1)

@click.command(short_help="Get tags")
def tags():
    try:
        for t in tags_api.get_tags(**context.settings):
            click.echo(t['name'])
    except Exception, e:
        print 'Get tags failed. %s' % e
        sys.exit(1)


@click.command(short_help="Get metrics")
@click.option('--agent', help='Agent Name', type=str, default=None)
@click.option('--tag', help='Tag Name', type=str, default=None)
def metrics(agent, tag):
    try:
        if not agent and not tag:
            click.echo('Specify an agent or tag to get the metrics')
            sys.exit(1)
        if agent:
            agent_id = None
            agent_details = agents_api.get_agents(**context.settings)
            for a in agent_details:
                if a['name'] == agent:
                    agent_id = a['id']
            for metric in metrics_api.get_agent_metrics(agent_id=agent_id, **context.settings):
                print metric['name']
        if tag:
            for metric in metrics_api.get_tag_metrics(tag_name=tag, **context.settings):
                print metric['name']
    except Exception, e:
        print 'Get metrics failed. %s' % e
        sys.exit(1)


@click.command(short_help="Get series")
@click.option('--agent', help='Agent Name', type=str, default=None)
@click.option('--tag', help='Tag Name', type=str, default=None)
@click.option('--resolution', help='Time between points', type=int, default=30)
@click.option('--period', help='Length of time', type=int, default=600)
@click.option('--lastvalue', is_flag=True, help='Gets the last value only')
@click.argument('metric')
def series(metric, agent, tag, resolution, period, lastvalue):
    try:
        if not agent and not tag:
            click.echo('Specify an agent or tag to get the metrics')
            sys.exit(1)

        if agent:
            agent_id = None
            agent_details = agents_api.get_agents(**context.settings)
            for a in agent_details:
                if a['name'] == agent:
                    agent_id = a['id']
            for s in series_api.get_agent_series(agent_id=agent_id, metric=metric, resolution=resolution, period=period, **context.settings):
                points = []
                for point in s['points']:
                    if point['type'] == 'boolean':
                        if point['all']:
                            points.append(0)
                        else:
                            points.append(2)
                    else:
                        points.append(point['avg'])
                if lastvalue:
                    print points[-1]
                else:
                    print ','.join(map(str, points))
        if tag:
            for s in series_api.get_tag_series(tag=tag, metric=metric, resolution=resolution, period=period, **context.settings):
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
                if lastvalue:
                    print points[-1]
                else:
                    print ','.join(map(str, points))
    except Exception, e:
        print 'Get series failed. %s' % e
        sys.exit(1)

@click.command(short_help="Get user")
@click.argument('tokens', required=False)
def user(tokens):
    try:
        if tokens:
            token_list = user_api.get_user_tokens(**context.settings)
            for t in token_list:
                print t['name']
        else:
            print user_api.get_user(**context.settings)['name'].lower()
    except Exception, e:
        print 'Get user failed. %s' % e
        sys.exit(1)

@click.command(short_help="Get pack")
def packs():
    try:
        for p in packs_api.get_packs(**context.settings):
            click.echo(p['name'])
    except Exception, e:
        print 'Get packs failed. %s' % e
        sys.exit(1)


@click.command(short_help="Get templates")
@click.argument('type', type=click.Choice(['all', 'public', 'private']), default='private')
def templates(type):
    try:
        if type == 'all':
            for t in templates_api.get_public_templates(**context.settings):
                click.echo(t['name'])
            for t in templates_api.get_private_templates(**context.settings):
                click.echo(t['name'])
        if type == 'public':
            for t in templates_api.get_public_templates(**context.settings):
                click.echo(t['name'])
        if type == 'private':
            for t in templates_api.get_private_templates(**context.settings):
                click.echo(t['name'])
    except Exception, e:
        print 'Get templates failed. %s' % e
        sys.exit(1)


@click.command(short_help="Get template")
@click.argument('name')
def template(name):
    try:
        print yaml.safe_dump(templates_api.get_private_template(name=name, **context.settings), default_flow_style=False, explicit_start=True)
    except Exception, e:
        print 'Get template failed. %s' % e
        sys.exit(1)


get.add_command(accounts)
get.add_command(agents)
get.add_command(agent)
get.add_command(dashboards)
get.add_command(links)
get.add_command(orgs)
get.add_command(packs)
get.add_command(plugins)
get.add_command(criterias)
get.add_command(rules)
get.add_command(alerts)
get.add_command(tags)
get.add_command(template)
get.add_command(templates)
get.add_command(metrics)
get.add_command(series)
get.add_command(user)
