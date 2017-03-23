
from __future__ import absolute_import
from __future__ import unicode_literals

import logging

import json
import sys

from tachyonic import app
from tachyonic import router
from netrino.api import model as modelapi
from tachyonic.api.api import sql
from tachyonic.api.api import orm as api
from tachyonic.neutrino import constants as const
from ..functions import getIGroups, assignIGPort

log = logging.getLogger(__name__)


@app.resources()
class InterfaceGroup(object):

    def __init__(self):
        router.add(const.HTTP_GET, '/infrastructure/network/igroups', self.get,
                       'network:admin')
        router.add(const.HTTP_POST, '/infrastructure/network/igroups', self.post,
                       'network:admin')
        router.add(const.HTTP_GET, '/infrastructure/network/igroups/{id}', self.get,
                       'network:admin')
        router.add(const.HTTP_PUT, '/infrastructure/network/igroups/{id}', self.put,
                       'network:admin')
        router.add(const.HTTP_PUT, '/infrastructure/network/igroups/{id}/port',
                       self.portigroup, 'network:admin')
        router.add(const.HTTP_DELETE, '/infrastructure/network/igroups/{id}', self.delete,
                       'network:admin')

    def get(self, req, resp, id=None):
        view = req.post.get('view', None)
        if id or view == "datatable":
            return sql.sql_get("interface_groups", req, resp, id)
        else:
            return json.dumps(getIGroups(id, view), indent=4)

    def post(self, req, resp):
        return api.post(modelapi.IGroup, req)

    def put(self, req, resp, id):
        return api.put(modelapi.IGroup, req, id)

    def delete(self, req, resp, id):
        return api.delete(modelapi.IGroup, req, id)

    def portigroup(self, req, resp, id):
        result = assignIGPort(req, id)
        return json.dumps(result, indent=4)
