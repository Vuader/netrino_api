from __future__ import absolute_import
from __future__ import unicode_literals

import logging

import json
import sys

from tachyonic import app
from tachyonic import router
from tachyonic.api.api import orm as api
from tachyonic.neutrino import constants as const
from tachyonic.netrino_common import model as modelapi
from ..functions import viewSR, createSR, activateSR, deactivateSR, getServices

log = logging.getLogger(__name__)


@app.resources()
class NetworkService(object):

    def __init__(self):
        router.add(const.HTTP_GET, '/infrastructure/network/services', self.get,
                       'network:admin')
        router.add(const.HTTP_GET, '/infrastructure/network/services/{id}', self.get,
                       'network:admin')
        router.add(const.HTTP_POST, '/infrastructure/network/services', self.post,
                       'network:admin')
        router.add(const.HTTP_PUT, '/infrastructure/network/services/{id}', self.put,
                       'network:admin')
        router.add(const.HTTP_DELETE, '/infrastructure/network/services/{id}', self.delete,
                       'network:admin')

    def get(self, req, resp, id=None):
        view = req.post.get('view', None)
        if view == "datatable":
            result = getServices(req,resp,sid=id)
            return json.dumps(result, indent=4)
        else:
            return api.get(modelapi.NetworkServices, req, resp, id)

    def post(self, req, resp):
        return api.post(modelapi.NetworkService, req)

    def put(self, req, resp, id):
        return api.put(modelapi.NetworkService, req, id)

    def delete(self, req, resp, id):
        return api.delete(modelapi.NetworkService, req, id)
