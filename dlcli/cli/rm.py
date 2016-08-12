from ..cli import *
import click
import sys
import logging

from tqdm import tqdm
from functools import partial
from multiprocessing import Pool
from requests.exceptions import ConnectionError

from ..api import accounts as accounts_api
from ..api import annotations as annotations_api
from ..api import agents as agents_api
from ..api import dashboards as dashboards_api
from ..api import links as links_api
from ..api import metrics as metrics_api
from ..api import orgs as orgs_api
from ..api import packs as packs_api
from ..api import plugins as plugins_api
from ..api import rules as rules_api
from ..api import series as series_api
from ..api import tags as tags_api
from ..api import templates as templates_api
from ..api import user as user_api


logger = logging.getLogger(__name__)


@cli.group('rm')
def rm():
    """deletes things"""

@click.command(short_help="rm account")
@click.argument('account')
@click.option('--yes', is_flag=True)
def account(account, yes):
    try:
        if not yes:
            click.confirm('Once you delete an account, there is no going back. Are you sure?', abort=True)
        context.settings['account'] = account
        resp = accounts_api.delete_account(**context.settings)
        if resp.status_code == 204:
            click.echo('Deleted account ' + account)
        else:
            click.echo('Error deleting ' + account + '. Status Code: ' + click.style(str(resp.status_code), fg='red'))
    except Exception, e:
        print 'Delete account failed. %s' % e
        sys.exit(1)

@click.command(short_help="rm agent")
@click.argument('agent')
def agent(agent):
    try:
        resp = agents_api.delete_agent(agent=agent, **context.settings)
        if resp.status_code == 204:
            click.echo('Deleted agent ' + agent)
        else:
            click.echo('Error deleting ' + agent + '. Status Code: ' + click.style(
                str(resp.status_code),
                fg='red'))
    except Exception, e:
        print 'Delete agent failed. %s' % e
        sys.exit(1)

@click.command(short_help="rm dashboard")
@click.argument('dashboard')
def dashboard(dashboard):
    try:
        resp = dashboards_api.delete_dashboard(dashboard=dashboard, **context.settings)
        if resp.status_code == 204:
            click.echo('Deleted dashboard ' + dashboard)
        else:
            click.echo('Error deleting ' + dashboard + '. Status Code: ' +
                       click.style(
                           str(resp.status_code),
                           fg='red'))
    except Exception, e:
        print 'Delete dashboard failed. %s' % e
        sys.exit(1)

@click.command(short_help="rm link")
@click.argument('link')
def link(link):
    try:
        resp = links_api.delete_link(link=link, **context.settings)
        if resp.status_code == 204:
            click.echo('Deleted link ' + link)
        else:
            click.echo('Error deleting ' + link + '. Status Code: ' + click.style(
                str(resp.status_code),
                fg='red'))
    except Exception, e:
        print 'Delete link failed. %s' % e
        sys.exit(1)

@click.command(short_help="rm org")
@click.argument('org')
@click.option('--yes', is_flag=True)
def org(org, yes):
    try:
        if not yes:
            click.confirm('Once you delete an organization, there is no going back. Are you sure?',abort=True)
        context.settings['org'] = org
        resp = orgs_api.delete_org(**context.settings)
        if resp.status_code == 204:
            click.echo('Deleted org ' + org)
        else:
            click.echo('Error deleting ' + org + '. Status Code: ' + click.style(
                str(resp.status_code),
                fg='red'))
    except Exception, e:
        print 'Delete org failed. %s' % e
        sys.exit(1)

@click.command(short_help="rm plugin")
@click.argument('plugin')
def plugin(plugin):
    try:
        resp = plugins_api.delete_plugin(plugin=plugin, **context.settings)
        if resp.status_code == 204:
            click.echo('Deleted plugin ' + plugin)
        else:
            click.echo('Error deleting ' + plugin + '. Status Code: ' +
                       click.style(
                           str(resp.status_code),
                           fg='red'))
    except Exception, e:
        print 'Delete plugin failed. %s' % e
        sys.exit(1)

@click.command(short_help="rm rule")
@click.argument('rule')
def rule(rule):
    try:
        resp = rules_api.delete_rule(rule=rule, **context.settings)
        if resp.status_code == 204:
            click.echo('Deleted rule ' + rule)
        else:
            click.echo('Error deleting ' + rule + '. Status Code: ' + click.style(
                str(resp.status_code),
                fg='red'))
    except Exception, e:
        print 'Delete rule failed. %s' % e
        sys.exit(1)

@click.command(short_help="rm tag")
@click.argument('tag')
def tag(tag):
    try:
        resp = tags_api.delete_tag(tag=tag, **context.settings)
        if resp.status_code == 204:
            click.echo('Deleted tag ' + tag)
        else:
            click.echo('Error deleting ' + tag + '. Status Code: ' + click.style(
                str(resp.status_code),
                fg='red'))
    except Exception, e:
        print 'Delete tag failed. %s' % e
        sys.exit(1)

@click.command(short_help="rm token")
@click.argument('name')
def token(name):
    try:
        resp = user_api.delete_user_token(token_name=name, **context.settings)
        if resp.status_code == 204:
            click.echo('Deleted token ' + name)
        else:
            click.echo('Error deleting ' + name + '. Status Code: ' + click.style(
                str(resp.status_code),
                fg='red'))
    except Exception, e:
        print 'Delete token failed. %s' % e
        sys.exit(1)

@click.command(short_help="rm pack")
@click.argument('name')
def pack(name):
    try:
        resp = packs_api.delete_pack(name=name, **context.settings)
        if resp.status_code == 204:
            click.echo('Deleted pack ' + name)
        else:
            click.echo('Error deleting ' + name + '. Status Code: ' + click.style(
                str(resp.status_code),
                fg='red'))
    except Exception, e:
        print 'Delete pack failed. %s' % e
        sys.exit(1)

@click.command(short_help="rm template")
@click.argument('name')
def template(name):
    try:
        resp = templates_api.delete_template(name=name, **context.settings)
        if resp.status_code == 204:
            click.echo('Deleted template ' + name)
        else:
            click.echo('Error deleting ' + name + '. Status Code: ' + click.style(
                str(resp.status_code),
                fg='red'))
    except Exception, e:
        print 'Delete template failed. %s' % e
        sys.exit(1)

@click.command(short_help="rm stream")
@click.argument('name')
def stream(name):
    try:
        resp = annotations_api.delete_stream(stream=name, **context.settings)
        if resp.status_code == 204:
            click.echo('Deleted stream ' + name)
        else:
            click.echo('Error deleting ' + name + '. Status Code: ' + click.style(
                str(resp.status_code),
                fg='red'))
    except Exception, e:
        print 'Delete stream failed. %s' % e
        sys.exit(1)

def _find_expired_metric_path(period_seconds, resolution_seconds, tag, m):
    if period_seconds > 3600:
        # check if there is something to expire from the last 5 minutes first
        if len(_find_expired_metric_path(300, 2, tag, m)) == 0:
            return []
    metric_series = series_api.get_tag_series(tag=tag,
                                              metric=m['name'],
                                              period=period_seconds,
                                              resolution=resolution_seconds,
                                              **context.settings)
    # find the expired series: no points means no confidence
    # empty points array means expired metric path
    expired_series = filter((lambda s: False if 'points' not in s else not len(s['points'])), metric_series)
    return expired_series

def _expire_metric_path(period_seconds, resolution_seconds, tag, m):
    try:
        expired_series = _find_expired_metric_path(period_seconds, resolution_seconds, tag, m)
        if len(expired_series) == 0:
            return None
        # expires metric paths, only for the right sources
        expired_source_ids = [series['source']['id'] for series in expired_series]
        return series_api.update_agents_metric_paths(agents=expired_source_ids,
                                                     metric=m['name'],
                                                     status='expired',
                                                     **context.settings)
    except (KeyboardInterrupt, ValueError, ConnectionError), e:
        return None

@click.command(short_help="rm metric paths")
@click.option('--period', help='check back this number of hours', type=int, default=48)
@click.option('--resolution', help='number of hours distance between points', type=int, default=1)
@click.option('--tag', help='name of the tag where metric paths should be cleaned up', type=str, default="all")
@click.option('--threads', help='number of threads to start', type=int, default=1)
def metrics(period, resolution, tag, threads):
    try:
        pool = Pool(processes=threads)
        period_seconds = period * 3600
        resolution_seconds = resolution * 3600
        m = metrics_api.get_tag_metrics(tag_name=tag, **context.settings)
        click.echo(click.style('Found: %s metrics', fg='green') % (len(m)))

        expire = partial(_expire_metric_path, period_seconds, resolution_seconds, tag)
        expired_paths = tqdm(pool.imap_unordered(expire, m))
        expired_paths = sum(filter(None, expired_paths))
        click.echo(click.style('Expired: %s metric paths', fg='green') % (expired_paths))

    except Exception, e:
        print 'Cleanup metrics failed. %s' % e

    finally:
        pool.terminate()
        pool.join()


rm.add_command(account)
rm.add_command(agent)
rm.add_command(dashboard)
rm.add_command(link)
rm.add_command(org)
rm.add_command(plugin)
rm.add_command(rule)
rm.add_command(tag)
rm.add_command(pack)
rm.add_command(template)
rm.add_command(token)
rm.add_command(stream)
rm.add_command(metrics)
