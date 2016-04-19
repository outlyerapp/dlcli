import os

global settings
settings = {
    'settingsfile': str(os.path.join(os.path.expanduser("~"), "dlcli.yaml")),
    'url': 'https://app.dataloop.io/api/v1',
    'org': None,
    'account': None,
    'key': None,
    'backupdir': 'dlbackups',
}