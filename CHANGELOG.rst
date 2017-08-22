=========
CHANGELOG
=========

0.7.3 - 22 August 2017
----------------------

- Fixed a bug that caused ``dlcli get alerts`` to fail with a JSON parser error.

0.7.2 - 22 August 2017
----------------------

- Fixed a bug that caused ``dlcli set org`` to fail with an error.

0.7.1 - 17 July 2017
--------------------

- Reverted command line arguments ``--backup-dir`` and ``--settings-file`` to
  ``--backupdir`` and ``--settingsfile``.
- Fixed bug in ``wrapper.delete()`` method that was causing an error message
  "delete() takes exactly 2 arguments (5 given)".

0.7.0 - 14 July 2017
--------------------

- Changed "Dataloop" references to "Outlyer".
- Updated API endpoint to `<http://api.outlyer.com/v1>`_.
- Fixed several YAML and JSON parsing bugs in the ``backup`` command (637_, 561_).
- Updated ``requirements.txt`` to use newer versions of dependent libraries.
- Enabled HTTP connection reuse to remove "bad connection" errors.

.. _637: https://outlyer.zendesk.com/agent/tickets/637
.. _561: https://outlyer.zendesk.com/agent/tickets/561