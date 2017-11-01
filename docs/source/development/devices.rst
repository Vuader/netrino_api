Devices
========

The ``/infrastructure/network/devices`` route takes an optional ``X-Format`` HTTP Header:

* select2: returns a JSON object with the devices and their id's listed in select2 format. That is, a list of dictionaries with keys ``id`` and ``text``.

The ``/infrastructure/network/device/{id}/ports`` route returns a JSON object containing all
the port data for the device.

**Options:**

* An optional POST object ``igroup``. If this value is supplied, the result will only include ports belonging to the specified igroup ID.
* an optional ``X-Format`` HTTP Header:select2: returns a JSON object with the devices and their id's listed in select2 format. That is, a list of dictionaries with keys ``id`` and ``text``.
