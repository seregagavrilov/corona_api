import os

from .settings_common import *


if os.environ.get('DYNO_RAM'):
    from .settings_prod_heroku import *
else:
    from .settings_local import *
