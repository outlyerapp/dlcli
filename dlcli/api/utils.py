import logging
import yaml

logger = logging.getLogger(__name__)


def save_setting(ctx, setting):
    settings_file = ctx.parent.parent.params['settingsfile']
    try:
        stream = open(settings_file, 'r')
        data = yaml.load(stream)
    except IOError:
        data = {}
    data.update({k: v for k, v in setting.iteritems() if v})
    with open(settings_file, 'w') as yaml_file:
        yaml_file.write(yaml.dump(data, default_flow_style=False))