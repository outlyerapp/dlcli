.. _readme:

`Quick Example`_
----------------------------

install dlcli using pip

.. code-block:: none

    pip install dlcli

set your org, account and api key

.. code-block:: none

    dlcli set org acme-ltd

.. code-block:: none

    dlcli set account staging

.. code-block:: none

    dlcli set key xxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

these get stored in ~/dlcli.yaml so the details only need to be changed when you are switching orgs or accounts

now verify you have a successful connection

.. code-block:: none

    dlcli show status

then get a list of all of your agents

.. code-block:: none

    dlcli show agents

fun! this is a work in progress so if you want to collaborate please raise PR's



`Dataloop CLI Tool`_
----------------------------

dlcli commands can be thought of as a series of nested commands, with each stage having its own options and flags.

.. code-block:: none

    dlcli [FLAGS] COMMAND [FLAGS] SUBCOMMAND [FLAGS]


The square braces indicate optional elements. Some commands have flags, some do not. Some of those flags are optional, some are mandatory per the command. See the list of commands and flags for more information.

The first thing to know is that help is never far away. You can use the ``--help`` flag at any stage to discover which flags are available:

.. code-block:: none

    dlcli --help

.. code-block:: none

    dlcli COMMAND --help

.. code-block:: none

    dlcli COMMAND SUBCOMMAND --help


Understand that using the ``--help`` flag in between two nested commands will result in the previous level ``--help`` output being shown.


``dlcli --help`` COMMAND will have the same output as ``dlcli --help``, and likewise, ``dlcli COMMAND --help SUBCOMMAND`` will have the same output as ``dlcli COMMAND --help``.


The top-level help output looks like this:

.. code-block:: none
    $ dlcli --help
    Usage: dlcli [OPTIONS] COMMAND [ARGS]...

    Dataloop Command Line Tool

    See https://www.dataloop.io


    Options:
    --debug            Debug mode
    --loglevel TEXT    Log level
    --logfile TEXT     log file
    --version          Show the version and exit.
    --help             Show this message and exit.

    Commands:
    agents      Dataloop Agents



Note that all available flags and commands for this level are shown. This pattern is repeated at each successive level of ``--help``

`Using the API outside of dlcli`_
----------------------------

You can use the API code outside of the command line utility.

.. code-block:: python

    from dlcli import api
    
    settings = {
        'url': 'https://app.dataloop.io/api/v1',
        'org': 'org_name',
        'account': 'account_name',
        'key': 'api_key',
    }
    
    print api.agents.get_agents(**settings)
    
Where org_name, account_name and api_key need to be updated with your personal settings.
