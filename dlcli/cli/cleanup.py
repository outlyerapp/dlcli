from ..cli import *
import sys
import click

from ..api import agents as agents_api
from ..api import metrics as metrics_api


@cli.group('cleanup')
def cleanup():
    """cleanup things"""

@click.command(short_help="Cleanup metric paths")
def metrics():
    try:
        for a in agents_api.get_agents(**context.settings):
            for m in metrics_api.get_agent_metrics(agent_id=a['id'], **context.settings):
                metrics_api.put_agent_metric_status(agent_id=a['id'], metric=m['id'], status='expired', **context.settings)
    except Exception, e:
        print 'Cleanup metrics failed. %s' % e
        sys.exit(1)

cleanup.add_command(metrics)
