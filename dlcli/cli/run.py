from ..cli import *
from ..api import *
import click
import logging

logger = logging.getLogger(__name__)


@cli.group('run')
@click.pass_context
def run(ctx):
    """runs things"""


@click.command(short_help="run plugin")
@click.argument('plugin')
@click.option('--agent', help='Agent Name', type=str, default=None)
@click.option('--tag', help='Tag Name', type=str, default=None)
@click.pass_context
def plugin(ctx, plugin, agent, tag):
    if not agent and not tag:
        click.echo('Specify an agent or tag to run the plugin on')
        sys.exit(1)

    responses = []
    name_map = {}
    table_data = []
    agent_details = agents.Agents(ctx).get_agents()
    if agent:
        for a in agent_details:
            if a['name'] == agent:
                name_map[a['id']] = a['name']
                responses = rpc.Rpc(ctx).run_local(plugin, [a['id']])
    if tag:
        id_list = []
        for a in agent_details:
            if tag in a['tags']:
                name_map[a['id']] = a['name']
                id_list.append(a['id'])
        responses = rpc.Rpc(ctx).run_local(plugin, id_list)
    for response in responses:
        table_data.append([
            name_map[response[0]], response[1]['returnCode'], response[1][
                'result'].strip()
        ])

    print_run_table(table_data)


@click.command(short_help="run command")
@click.argument('command')
@click.option('--agent', help='Agent Name', type=str, default=None)
@click.option('--tag', help='Tag Name', type=str, default=None)
@click.pass_context
def command(ctx, command, agent, tag):
    if not agent and not tag:
        click.echo('Specify an agent or tag to run the plugin on')
        sys.exit(1)

    responses = []
    name_map = {}
    table_data = []

    agent_details = agents.Agents(ctx).get_agents()
    if agent:
        for a in agent_details:
            if a['name'] == agent:
                name_map[a['id']] = a['name']
                responses = rpc.Rpc(ctx).run_command(command, [a['id']])
    if tag:
        id_list = []
        for a in agent_details:
            if tag in a['tags']:
                name_map[a['id']] = a['name']
                id_list.append(a['id'])
        responses = rpc.Rpc(ctx).run_command(command, id_list)
    for response in responses:
        table_data.append([
            name_map[response[0]], response[1]['returnCode'], response[1][
                'result'].strip()
        ])

    print_command_output(table_data)


run.add_command(plugin)
run.add_command(command)
