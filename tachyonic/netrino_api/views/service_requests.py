
from __future__ import absolute_import
from __future__ import unicode_literals

import logging

import json
import sys

from tachyonic import app
from tachyonic import router
from tachyonic.neutrino import constants as const
from ..functions import viewSR, createSR, activateSR, deactivateSR, deleteSR

log = logging.getLogger(__name__)


@app.resources()
class ServiceRequests(object):

    def __init__(self):
        router.add(const.HTTP_GET,
                   '/infrastructure/network/service_requests',
                    self.get,
                   'network:admin')
        router.add(const.HTTP_GET,
                   '/infrastructure/network/service_requests/{id}',
                    self.get,
                   'network:admin')
        router.add(const.HTTP_POST,
                   '/infrastructure/network/service_requests',
                    self.post,
                   'network:admin')
        router.add(const.HTTP_PUT,
                   '/infrastructure/network/service_requests/{id}',
                    self.put,
                   'network:admin')
        router.add(const.HTTP_PUT,
                   '/infrastructure/network/service_requests/{id}/deactivate',
                    self.deactivate,
                   'network:admin')
        router.add(const.HTTP_DELETE,
                   '/infrastructure/network/service_requests/{id}',
                   self.delete,
                   'network:admin')

    def get(self, req, resp, id=None):
        view = req.post.get('view', None)
        onlyActive = req.post.get('onlyActive', False)
        result = viewSR(req, resp, id=id, view=view, onlyActive=onlyActive)
        return json.dumps(result, indent=4)

    def post(self, req, resp):
        result = createSR(req, resp)
        return json.dumps(result, indent=4)

    def put(self, req, resp, id):
        result = activateSR(req, srid=id)
        return json.dumps(result, indent=4)

    def deactivate(self, req, resp, id):
        result = deactivateSR(req, srid=id)
        return json.dumps(result, indent=4)

    def delete(self, req, resp, id):
        """
        Typically one does not want to delete
        Service requests, for historical purposes.
        Deletion of a Service request should
        only be nessecary to cleanup after tests like
        unit tests are run
        """
        result = deleteSR(srid=id)
        return json.dumps(result, indent=4)
