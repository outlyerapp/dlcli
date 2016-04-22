from ..cli import *
import click
import sys
import sparkline
import logging
import context

logger = logging.getLogger(__name__)


@cli.command('graph')
@click.argument('metric')
@click.option('--agent', help='Agent Name', type=str, default=None)
@click.option('--tag', help='Tag Name', type=str, default=None)
@click.option('--resolution', help='Time between points', type=int, default=30)
@click.option('--period', help='Length of time', type=int, default=600)
def graph(metric, agent, tag, resolution, period):
    """graphs things"""
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
                print "Min: %d Max: %d Avg: %d  %s " % (min(points), max(points), sum(points)/len(points), sparkline.sparkify(points).encode('utf-8'))
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
                print "Min: %d Max: %d Avg: %d  %s " % (min(points), max(points), sum(points)/len(points), sparkline.sparkify(points).encode('utf-8'))
    except Exception, e:
        print 'Graph failed. %s' % e
        sys.exit(1)
