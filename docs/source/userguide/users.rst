.. _users:
Users
=====

Creating users follows the same procedure as with `Tachyon UI <http://tachyonic-ui.readthedocs.io/>`_.

With Netrino, the username has to match the login that the user makes use of to log into the network device.
For example, if the network devices makes use of TACACS+, and a user uses TACACS+ username ``bob``, then the
Netrino username must also be ``bob``.

At this time only SSH is supported, and only key authentication. All the user private SSH keys need to exist on the server.
The location of this directory must be listed in the `netrino-celery.cfg <http://neutrino-api.readthedocs.io/>`_ file
under the section ``[locations]``:

.. code::

    [locations]
    ssh_keys = /some/secure/location


Each key has to be in the format:

    `username`.key

where `username` is the user's login name.

Note that this directory and these key files have to be readable by the user that runs the neutrino WSGI process.
Be sure to have strict file permissions.

This means that whatever user creates the Netrino service request(s), will also be the user that logs into the network device.
This way you do not require any additional RBAC methods in order to use Netrino - existing RBAC will be used.
