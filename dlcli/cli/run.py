from ..cli import *
from ..api import *
import sys
import click
import logging

from ..api import agents as agents_api
from ..api import rpc as rpc_api

logger = logging.getLogger(__name__)


@cli.group('run')
def run():
    """runs things"""


@click.command(short_help="run plugin")
@click.argument('plugin')
@click.option('--agent', help='Agent Name', type=str, default=None)
@click.option('--tag', help='Tag Name', type=str, default=None)
def plugin(plugin, agent, tag):
    try:
        if not agent and not tag:
            click.echo('Specify an agent or tag to run the plugin on')
            sys.exit(1)

        responses = []
        name_map = {}
        table_data = []
        agent_details = agents_api.get_agents(**context.settings)
        if agent:
            for a in agent_details:
                if a['name'] == agent:
                    name_map[a['id']] = a['name']
                    responses = rpc_api.run_local(plugin_path=plugin, agent_list=[a['id']], **context.settings)
        if tag:
            id_list = []
            for a in agent_details:
                if tag in a['tags']:
                    name_map[a['id']] = a['name']
                    id_list.append(a['id'])
            responses = rpc_api.run_local(plugin, id_list)
        for response in responses:
            table_data.append([
                name_map[response[0]], response[1]['returnCode'], response[1][
                    'result'].strip()
            ])

        print_run_table(table_data)
    except Exception, e:
        print 'Run plugin failed. %s' % e
        sys.exit(1)


@click.command(short_help="run command")
@click.argument('command')
@click.option('--agent', help='Agent Name', type=str, default=None)
@click.option('--tag', help='Tag Name', type=str, default=None)
def command(command, agent, tag):
    try:
        if not agent and not tag:
            click.echo('Specify an agent or tag to run the plugin on')
            sys.exit(1)

        responses = []
        name_map = {}
        table_data = []

        agent_details = agents_api.get_agents(**context.settings)
        if agent:
            for a in agent_details:
                if a['name'] == agent:
                    name_map[a['id']] = a['name']
                    responses = rpc_api.run_command(command=command, agent_list=[a['id']], **context.settings)
        if tag:
            id_list = []
            for a in agent_details:
                if tag in a['tags']:
                    name_map[a['id']] = a['name']
                    id_list.append(a['id'])
            responses = rpc_api.run_command(command=command, agent_list=id_list, **context.settings)
        for response in responses:
            table_data.append([
                name_map[response[0]], response[1]['returnCode'], response[1][
                    'result'].strip()
            ])

        print_command_output(table_data)
    except Exception, e:
        print 'Run command failed. %s' % e
        sys.exit(1)


run.add_command(plugin)
run.add_command(command)
