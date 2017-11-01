Devices
=======

.. _add_device:
Adding Devices
--------------
In order to add a new device to the system, navigate to

``Infrastructure -> Network -> Devices``

and click on Create.

Complete the two fields: device IP address and SNMP community string.

Once you hit the ``Create`` button, the system will generate a new :ref:`service request <srs>` for this discovery.

SNMP v2 is used, and only to detect the device hostname and operating system.

Thereafter the system will log into the device to obtain interface and IP address information. In order to do that
be sure to have the :ref:`user SSH keys <users>` configured.

For this action, a :ref:`Service Request <srs>` is created. It will have no customer or service attached, but you may observe
the status and result at the :ref:`Service Requests <viewsrs>` page.

.. note::

    One may supply a subnet in order to provide a device range. In that case, each and every IP address in the
    subnet will be queried, and a service request will be created for each IP address.

Devices currently supported:

* Cisco IOS
* Junos

Need more? Let us know by loggin an issue on `github <https://github.com/TachyonProject/netrino_api/issues>`_.

Viewing Devices
---------------
Simply Navigate to ``Infrastructure -> Network -> Devices``. Here you can see a list of all devices. The table is searchable
(all fields) and sortable.
To view the specific port, service and customer information for a specific device, click on the magnify glass to the
right of the device. This takes you to the view device page, which will also show you when last the device port and
ip address information was updated. Because Netrino knows about the customers and services (that it provisioned)
attached to an interface, this information will be up to date automatically. Once again, this table is searchable and
sortable.

.. _update_device:

Updating Devices
----------------
From time to time it might be required to update the port information of a device. To do this, navigate to
``Infrastructure -> Network -> Devices``, click on the ``view device`` icon, and hit the ``edit`` button. Here you are
presented with the same form as when the device was discovered initially. Simply hit the ``save`` button to initiate
a new device discovery service request.

Deleting Devices
----------------
In order to delete a device, navigate to ``Infrastructure -> Network -> Devices``, click on the ``view device`` icon,
and hit the ``edit`` button. Then click on the ``delete`` button, you will be prompted with a confirmation dialog.
If there are any service requests ACTIVE on the device, it will list the number of active services. To view them,
navigate to the :ref:`srs` page, and enter the IP address for the device (in decimal form, the dialog will provide it).
