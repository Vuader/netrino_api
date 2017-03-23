
from __future__ import absolute_import
from __future__ import unicode_literals

import logging

import json
import sys

from tachyonic import app
from tachyonic import router
from netrino.api import model as modelapi
from tachyonic.api.api import orm as api
from tachyonic.neutrino import constants as const
from ..functions import viewDevicePorts, discoverDevice

log = logging.getLogger(__name__)


@app.resources()
class NetworkDevice(object):

    def __init__(self):
        router.add(const.HTTP_GET, '/infrastructure/network/devices', self.get,
                       'network:admin')
        router.add(const.HTTP_GET, '/infrastructure/network/devices/{id}', self.get,
                       'network:admin')
        router.add(const.HTTP_GET, '/infrastructure/network/devices/{id}/ports', self.ports,
                       'network:admin')
        router.add(const.HTTP_POST, '/infrastructure/network/devices', self.post,
                       'network:admin')
        router.add(
            const.HTTP_PUT, '/infrastructure/network/devices/{id}', self.put, 'network:admin')
        router.add(const.HTTP_DELETE, '/infrastructure/network/devices/{id}', self.delete,
                       'users:admin')

    def get(self, req, resp, id=None):
        return api.get(modelapi.NetworkDevices, req, resp, id)

    def ports(self, req, resp, id):
        view = req.post.get('view', None)
        return viewDevicePorts(req, resp, ip=int(id), view=view)

    def post(self, req, resp):
        result = discoverDevice(req)
        return json.dumps(result, indent=4)

    def put(self, req, resp, id=None):
        result = discoverDevice(req, id)
        return json.dumps(result, indent=4)

    def delete(self, req, resp, id=None):
        return api.delete(modelapi.NetworkDevice, req, id)