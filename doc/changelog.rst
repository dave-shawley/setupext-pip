Changelog
---------

* 1.0.1

  - Worked around a problem with py.test output capturing and Python 3.x.
    It looks like they are patching ``sys.stdout`` and friends with something
    that does not have a ``errors`` attribute so *distutils/log.py* is
    blowing up on line 30: ``if stream.errors == 'strict'``.

    For some reason, switching to ``--capture=sys`` seems to work correctly.
    I have a feeling that this will be fixed when py.test 2.6 shows up.

* 1.0.0 (27-Jul-2014)

  Initial revision that supported the ``requirements`` command.
