=========
CHANGELOG
=========

0.7.1 - 14 July 2017
--------------------

- Changed "Dataloop" references to "Outlyer".
- Updated API endpoint to `<http://api.outlyer.com/v1>`_.
- Fixed several YAML and JSON parsing bugs in the ``backup`` command (637_, 561_).
- Updated ``requirements.txt`` to use newer versions of dependent libraries.
- Enabled HTTP connection reuse to remove "bad connection" errors.

.. _637: https://outlyer.zendesk.com/agent/tickets/637
.. _561: https://outlyer.zendesk.com/agent/tickets/561