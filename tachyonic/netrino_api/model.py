from __future__ import absolute_import
from __future__ import unicode_literals

import logging

from tachyonic.neutrino.web.bootstrap3.forms import Form as Bootstrap
from tachyonic.netrino_common import model as common

log = logging.getLogger(__name__)


class NetworkDevices(Bootstrap, common.NetworkDevices):
    pass

class NetworkDevice(Bootstrap, common.NetworkDevice):
    pass

class NetworkDevicePort(Bootstrap, common.NetworkDevicePorts):
    pass

class NetworkDevicePorts(Bootstrap, common.NetworkDevicePorts):
    pass

class NetworkService(Bootstrap, common.NetworkService):
    pass

class NetworkServices(Bootstrap, common.NetworkServices):
    pass

class IGroup(Bootstrap, common.IGroup):
    pass

class IGroups(Bootstrap, common.IGroups):
    pass
