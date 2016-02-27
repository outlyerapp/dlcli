# Dataloop CLI Tool

dlcli commands can be thought of as a series of nested commands, with each stage having its own options and flags.

```
dlcli [FLAGS] COMMAND [FLAGS] SUBCOMMAND [FLAGS]
```

The square braces indicate optional elements. Some commands have flags, some do not. Some of those flags are optional, some are mandatory per the command. See the list of commands and flags for more information.

The first thing to know is that help is never far away. You can use the --help flag at any stage to discover which flags are available:

```
dlcli --help

dlcli COMMAND --help

dlcli COMMAND SUBCOMMAND --help
```

Understand that using the --help flag in between two nested commands will result in the previous level --help output being shown.

```
dlcli --help COMMAND will have the same output as dlcli --help, and likewise, dlcli COMMAND --help SUBCOMMAND will have the same output as dlcli COMMAND --help.
```

The top-level help output looks like this:

```
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
```
 

Note that all available flags and commands for this level are shown. This pattern is repeated at each successive level of --help