Changelog
---------

* Next Release

  - `#8`_ Fix sdist packaging and tests -- contributed by @jayvdb
  - Add Python 3.5-3.8 as supported versions
  - Remove explicit support for Python 2.6 and 3.4

.. _#8: https://github.com/dave-shawley/setupext-pip/pull/8

* 1.0.5 (15-Aug-2014)

  - Add the *--install-test-requirements* command line option.
  - Add the *--install-extra-requirements* command line option.

* 1.0.4 (02-Aug-2014)

  - Add ``from future import absolute_import`` to make the extension
    safe on older Python versions.
  - Make it safe to use without a ``setup_requires`` keyword.

* 1.0.3 (30-Jul-2014)

  - Fix ``setup.py test``.  It was hanging forever unless you passed it
    additional parameters.

* 1.0.2 (30-Jul-2014)

  - Added ``read_requirements_from_file`` function.

* 1.0.1 (27-Jul-2014)

  - Worked around a problem with py.test output capturing and Python 3.x.
    It looks like they are patching ``sys.stdout`` and friends with something
    that does not have a ``errors`` attribute so *distutils/log.py* is
    blowing up on line 30: ``if stream.errors == 'strict'``.

    For some reason, switching to ``--capture=sys`` seems to work correctly.
    I have a feeling that this will be fixed when py.test 2.6 shows up.

* 1.0.0 (27-Jul-2014)

  - Initial revision that supported the ``requirements`` command.
