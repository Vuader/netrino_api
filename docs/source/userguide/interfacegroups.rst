.. _igs:
Interface Groups
================

`Interface Groups` is a mechanism to prevent certain users from configuring certain device ports.

It thus allow users to attach a :ref:`Service Request <srs>` only to a device port for which he or she is authorized to do
so.

For example, one can have a ``backbone`` interface group, which only users with the ``Core Engineer``
`role <http://tachyonic-ui.readthedocs.io/>`_ is allowed to provision on.

When a device is newly discovered, the device ports belong to no interface group. This means by default no port is
configurable. This is done intentionally to safeguard against unauthorized network configuration.

.. _create_ig:
Creating Interface Groups
-------------------------
Navigate to ``Infrastructure -> Network -> Interface Groups`` and hit the ``Create`` button.

Simply enter the name of the Interface Group, and hit the ``Save`` button.

Viewing Interface Groups
------------------------
Navigate to ``Infrastructure -> Network -> Interface Groups``. Here a list of all configured Interface Groups are displayed.

Edit Interface Group Names
--------------------------
Navigate to ``Infrastructure -> Network -> Interface Groups`` and click on the view icon next to the Interface Group to
be renamed. Hit the ``Edit`` button, provide the new name, and hit ``Save``.

Deleting Interface Groups
-------------------------
Navigate to ``Infrastructure -> Network -> Interface Groups`` and click on the view icon next to the Interface Group to
be deleted. Hit the ``Edit`` button, and then the ``Delete`` button.

Assign Device ports to an Interface Group
-----------------------------------------
After a device has been :ref:`discovered <add_device>`, and at least one Interface group has been :ref:`created <create_ig>`
, navigate to ``Infrastructure -> Network -> Devices``
and click on the view icon next to the Device. Hit the ``Add Interface Groups`` button below the list of ports.

Now a checkbox appears to the right of each port, and a drop-down list below the table. Select one or more ports by
checking the checkboxes, as well as the Interface Group from the drop-down list, and hit the ``Save`` button.
