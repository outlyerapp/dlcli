import os

# Check for settings in order:
settings_path = [os.path.expanduser("~") + '/.dlcli.yaml',
                 os.path.expanduser("~") + '/dlcli.yaml',
                 os.getcwd() + '/dlcli.yaml']

# Determine which one is valid
for path in settings_path:
    if os.path.exists(path):
        settingsfile = path
        break
    else:
        settingsfile = os.getcwd() + '/dlcli.yaml'

global settings
settings = {
    'settingsfile': settingsfile,
    'url': 'https://app.dataloop.io/api/v1',
    'org': None,
    'account': None,
    'key': None,
    'backupdir': 'dlbackups',
    'timeout': 60
}
