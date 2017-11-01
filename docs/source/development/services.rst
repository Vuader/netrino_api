Services
========

The ``/infrastructure/network/services`` route takes an optional ``X-Format`` HTTP Header:

* fields: returns only the variables mentioned in the Service templates, as a JSON array
* fields+igroup: returns a JSON object with two keys: the interface group text name, and the fields array.
