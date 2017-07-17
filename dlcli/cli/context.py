import os

# Check for settings in order:
settings_path = [os.path.expanduser("~") + '/.dlcli.yaml',
                 os.path.expanduser("~") + '/dlcli.yaml',
                 os.getcwd() + '/dlcli.yaml']
1
# Determine which one is valid
for path in settings_path:
    if os.path.exists(path):
        settings_file = path
        break
    else:
        settings_file = os.getcwd() + '/dlcli.yaml'

global settings
settings = {
    'settingsfile': settings_file,
    'url': 'https://api.outlyer.com/v1',
    'org': None,
    'account': None,
    'key': None,
    'backupdir': 'dlbackups',
    'timeout': 60
}
