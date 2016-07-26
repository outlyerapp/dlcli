from ..cli import *
import sys
import click
from simplejson.scanner import JSONDecodeError

from ..api import agents as agents_api
from ..api import metrics as metrics_api
from ..api import series as series_api

@cli.group('cleanup')
def cleanup():
    """cleanup things"""

@click.command(short_help="Cleanup metric paths")
def metrics():
    try:
        # get every agent
        for a in agents_api.get_agents(**context.settings):
            # for every agent get every metric
            for m in metrics_api.get_agent_metrics(agent_id=a['id'], **context.settings):
                # for every metric get the series
                try:
                    for s in series_api.get_agent_series(agent_id=a['id'], metric=m['name'], **context.settings):
                        # if the series is empty expire the metric
                        if len(s['points']) == 0:
                            click.echo(click.style('Expired: %s.%s', fg='red') % (a['id'], m['name']))
                            #metrics_api.put_agent_metric_status(agent_id=a['id'], metric=m['id'], status='expired', **context.settings)
                        else:
                            click.echo(click.style('Active: %s.%s', fg='green') % (a['id'], m['name']))
                except JSONDecodeError:
                    continue

    except Exception, e:
        print 'Cleanup metrics failed. %s' % e
        sys.exit(1)

cleanup.add_command(metrics)
