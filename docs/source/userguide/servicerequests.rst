.. _srs:

Service Requests
================

The purpose of Netrino is to create Service Requests.

A Service Request is the association of these 3 items:

* A Tenant/Customer,
* to a Service,
* to a Network Device and/or port.

.. _createsr:

Creating a Service Request
--------------------------

**1. Select the Tenant/Customer.**

After at least one Tenant has been `provisioned <http://tachyonic-ui.readthedocs.io/>`_ to the system,
enter the name of the Tenant at the
``Tenant Name`` Search bar at the top right. Select the name from the auto drop-down, or hit search.
From the pane below, hit the ``Open`` button for the applicable Tenant.

**2. Select the Service**

Aftter at least one :ref:`Service <add_services>` have been created, navigate to
``Infrastructure -> Network -> Service Requests``, and hit the ``Create`` button.
From the first Drop Down list, select the applicable Service. Once selected, more fields may appear in the form
if there were additional fields associated with the Service.

**3. Select the Device**

After at least one Device has been :ref:`discovered <add_device>`, from the second drop-down list,
select the applicable Device to which th service request is to be deployed.
It is possible to select more than one device, but at this time no interface/port configuration is supported in such
a case.

**4. Select the port (optional)**

If the Service contained the special variable ``{{interface}}``, a drop-down list will appear listing all the ports
on the device that:

* belong to the same Interface Group as the Service, and
* do not have any ACTIVE service requests currently attached to them.

.. note::

    Only the ports discovered in the last device discovery attempt will be listed; it might be neccesary
    to :ref:`rediscover <update_device>` the device to show an up-to-date list

Select the applicable port, and hit the create button.

The system will initiate a deployment task in the background, and redirect to the :ref:`Service Requests <viewsrs>` Page.
The status will probably be PENDING at this stage, as it takes a short while to log in and configure the device.

.. _viewsrs:

Viewing Service Requests
------------------------
Simply navigate to ``Infrastructure -> Network -> Service Requests`` to view a list of all service requests.
Note that if a Tenant is selected, only service requests for that Tenant will be displayed. Otherwise
service requests for all Tenants are displayed, as well as device discovery service requests.

.. _viewsr:

To view a specific Service Request, hit the view icon next to it. This will display the log and status
of the service request.

.. _activatesr:

Activating Services
-------------------
If the current status of the Service Request is SUCCESS, on the :ref:`View Service Request <viewsr>` page, there
will be an ``Activate`` Button. Hit this button to activate the service.

If the Activation config of the service is empty, the Status will change to ACTIVE immediately. Otherwise, the status
will change to PENDING as a new task is loaded in the background to configure the device.

.. _deactivatesr:

Deactivating Services
---------------------
If the current status of the Service Request is ACTIVE, on the :ref:`View Service Request <viewsr>` page, there
will be a ``Deactivate`` button. Hit this button to deactivate the service.

If the Deactivation config of the service is empty, the Status will change to INACTIVE immediately. Otherwise, the status
will change to PENDING as a new task is loaded in the background to configure the device.
