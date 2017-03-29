from tachyonic.neutrino.config import Config
from tachyonic.neutrino.exceptions import Error
from tachyonic.neutrino.mysql import Mysql
import os
from celery import Celery


# if 'NEUTRINO_CONFIG' in os.environ:
#    if os.path.isfile(os.environ['NEUTRINO_CONFIG']):
# 	nfw.config.nfw_config = os.environ['NEUTRINO_CONFIG']
#    else:
# 	raise nfw.Error("Configuration file not found: %s"
# 				% (os.environ['NEUTRINO_CONFIG'],))
# else:
#    raise nfw.Error("Configuration file not found in os.environment")

celeryConfPath = '/etc/netrino-celery.cfg'

config = Config(celeryConfPath)

try:
    celery = config.get('celery')
    app = Celery(celery.get('app'),
                     broker=celery.get('broker'),
                     backend=celery.get('backend'),
                     include=celery.get('include').split(','))

    app.conf.update(
        result_expires=celery.get('result_expires')
    )
except:
    raise Error("No Celery settings found in %s" % celeryConfPath)

try:
    mysql = config.get('mysql')
    db = Mysql(host=mysql.get('host'),
                   database=mysql.get('database'),
                   username=mysql.get('username'),
                   password=mysql.get('password'))
except:
    raise Error("No Celery settings found in %s" % celeryConfPath)
