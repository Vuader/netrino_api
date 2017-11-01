Netrino UI Development Guide
============================

This Guide describes some of the concepts used in the development of the UI for Netrino.

Introduction
------------

The Netrino UI follows the same development concepts used for `Tachyonic UI <http://tachyonic-ui.readthedocs.io/en/development/>`_.

It obtains all the data via API calls to the `Netrino API <netrino-api.readthedocs.io>`_, and as such does not have to
reside on the same server.

Each section is referenced in its own view, which makes use of functions that reside inside the ``controllers.py`` file.

All the tables are rendered with the datatables jquery plugin. The select2 jquery plugin is used for dropdown lists.

Some of the views have special options available. These are described here.

.. toctree::
   :maxdepth: 2

   devices
   interfacegroups
   services
   servicerequests
