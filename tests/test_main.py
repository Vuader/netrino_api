# -*- coding: utf-8 -*-
import pytest
parametrize = pytest.mark.parametrize

#import tachyonic.neutrino
#import tachyonic.netrino_api

from tachyonic.client import Client
from tachyonic.common.exceptions import ClientError

def test_api_avail():
    global api
    api = Client('http://localhost/api')
    assert 'api' in globals()

def test_login_pass():
    auth = api.authenticate('root', 'password', 'default')
    assert len(auth) > 0

class Netrino():
    def __init__(self):
        self.response = None

    def execute(self, req, url, obj):
        headers, self.response = api.execute(req,
                                        '/infrastructure/network/' + url,
                                        obj=obj,
                                        endpoint='netrino_api')

@pytest.fixture
def netrino():
    '''Returns a Netrino test object'''
    return Netrino()
    # req, url, obj = request.param
    # headers, response = api.execute(req,
    #                                 '/infrastructure/network/' + url,
    #                                 obj=obj,
    #                                 endpoint='netrino_api')
    # return response

igroup_params = [
    ('POST', 'igroups', {'name': 'unittest'}, 'create'),
    ('GET', 'igroups', {}, 'viewall'),
    ('GET', 'igroup/', {}, 'view'),
    ('PUT', 'igroup/', {'name': 'updatedunittest'}, 'update'),
    ('DELETE', 'igroup/', {}, 'delete')
]

@pytest.mark.parametrize('req, url, obj, test', igroup_params)
def test_crud_igroup(netrino, req, url, obj, test):
    if test == 'create':
        netrino.execute(req, url, obj)
        assert 'id' in netrino.response
        global igroup_id
        igroup_id = netrino.response['id']
        assert 'name' in netrino.response
        assert netrino.response['name'] == 'unittest'
    elif test == 'viewall':
        netrino.execute(req, url, obj)
        assert igroup_id in netrino.response
        assert netrino.response[igroup_id] == 'unittest'
    elif test == 'view':
        netrino.execute(req, url + igroup_id, obj)
        assert 'id' in netrino.response
        assert 'name' in netrino.response
        assert netrino.response['id'] == igroup_id
        assert netrino.response['name'] == 'unittest'
    elif test == 'update':
        netrino.execute(req, url + igroup_id, obj)
        assert 'id' in netrino.response
        assert 'name' in netrino.response
        assert netrino.response['id'] == igroup_id
        assert netrino.response['name'] == 'updatedunittest'
    elif test == 'delete':
        netrino.execute(req, url + igroup_id, obj)
        assert 'action' in netrino.response
        assert netrino.response['action'] == 'success'
        netrino.execute('GET', 'igroups', obj)
        with pytest.raises(AssertionError):
            assert igroup_id in netrino.response


#def test_login_fail():
#    with pytest.raises(ClientError):
#        auth = api.authenticate('fake_user', 'fake_pass', 'default')

# def test_create_igroup():
#     headers, response = api.execute('POST',
#                                     '/infrastructure/network/igroups',
#                                     obj={'name': 'unittest'},
#                                     endpoint='netrino_api')
#     assert 'id' in response
#     global igroup_id
#     igroup_id = response['id']
#     assert 'name' in response
#     assert response['name'] == 'unittest'
#
# def test_view_igroups():
#     headers, response = api.execute('GET',
#                                     '/infrastructure/network/igroups',
#                                     endpoint='netrino_api')
#     assert igroup_id in response
#     assert response[igroup_id] == 'unittest'
#     return response
#
# def test_view_igroup():
#     headers, response = api.execute('GET',
#                                     '/infrastructure/network/igroup/%s'
#                                     % (igroup_id,),
#                                     endpoint='netrino_api')
#     assert 'id' in response
#     assert 'name' in response
#     assert response['id'] == igroup_id
#     assert response['name'] == 'unittest'
#
# def test_update_igroup():
#     headers, response = api.execute('PUT',
#                                     '/infrastructure/network/igroup/%s'
#                                     % (igroup_id,),
#                                     obj={'name': 'updatedunittest'},
#                                     endpoint='netrino_api')
#     assert 'id' in response
#     assert 'name' in response
#     assert response['id'] == igroup_id
#     assert response['name'] == 'updatedunittest'
#
# def test_delete_igroup():
#     headers, response = api.execute('DELETE',
#                                     '/infrastructure/network/igroup/%s'
#                                     % (igroup_id,),
#                                     endpoint='netrino_api')
#     assert 'action' in response
#     assert response['action'] == 'success'
#     with pytest.raises(AssertionError):
#         test_view_igroups()
