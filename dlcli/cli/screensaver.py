from ..cli import *
from termsaverlib.screen import get_available_screens
from termsaverlib.screen.helper import ScreenHelperBase
import logging


logger = logging.getLogger(__name__)

screens = [
    'asciiartfarts',
    'clock',
    'jokes4all',
    'matrix',
    'quotes4all',
    'randtxt',
    'rfc',
    'starwars',
    ]

@cli.command('screensaver')
@click.argument('screen', type=click.Choice(screens))
def screensaver(screen):
    try:
        if [screen][0] in [s().name for s in get_available_screens()]:
            for _screen in [s for s in get_available_screens() if [screen][0] == s().name]:
                _screen().autorun([screen][1:])
    except KeyboardInterrupt:
        ScreenHelperBase.clear_screen()

