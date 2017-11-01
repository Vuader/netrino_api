.. _services:

Services
========

The Services section provides the device configuration templates that define services.
Each service has to be associated to an :ref:`Interface Group<igs>`, as well as a
`User Role <http://tachyonic-ui.readthedocs.io/>`_.

This way one can ensure that services are only applied to interfaces for which they are allowed, and only by users
that are allowed to provision them.

Templating Engine
-----------------
The `Jinja2 <http://jinja.pocoo.org/docs/dev/templates/>`_ templating engine is used to expand the text entered in
the configuration sections. Any variable referenced with ``{{ .. }}``, will result in an additional text field in the
:ref:`Create Service Request <srs>` form.

For example, this template:

.. code:: jinja

    interface FastEthernet0/0
      description "{{ description }}"
      ip address {{ ipv4 }} {{ mask }}

Will result in three additional required fields to be completed when creating a service request with this Service:
``description``,
``ipv4`` and ``mask``

Load merge technique will be used to deploy the configuration.

Special Variables
-----------------

**Ports/Interfaces**:

The ``{{ interface }}`` variable will not result in a text field, but a drop-down list instead. This list will be
populated with the most recent ports discovered on the selected device.

Creating a Service
------------------
After at least one :ref:`Interface Group<create_ig>` has been created,
navigate to ``Infrastructure -> Network -> Services``, and hit the ``Create`` button.

Complete the fields for the ``Service Name``, ``Interface Group`` and ``User Role``.

Next, there are three paragraph fields. Only the first one, ``Config``, is compulsary.

**1. Config**

This is the configuration that will be deployed when the Service Request is :ref:`created <createsr>`.

**2. Activation config**

This is the configuration that will be deployed when the Service Request is :ref:`activated <activatesr>`. This may be
used for example to enable a port once it has been confirmed that payment for the service was received.

If left blank, Service Requests can be activated without touching the device.

**3. Deactivation config**

Use this part of the Service template to provide the decomissioning configuration. It will be deployed when the Service
Request is :ref:`deactivated <deactivatesr>`.

If left blank, Service Requests can be deactivated without touching the device.
