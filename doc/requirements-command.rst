.. _requirements-command:

Using the Setuptools Command
----------------------------
This library extends the `setuptools`_ utility by defining a single
new command called **requirements**.  This command installs your
package's dependencies identified by the ``setup_requires`` keyword
passed to :func:`setuptools.setup` without installing the project in
development mode.

.. code-block:: bash

   $ virtualenv -q env
   $ env/bin/python setup.py requirements

The *requirements* command supports a number of command line options
that are passed through to the underlying ``pip install`` execution.

.. option:: --index-url URL

   Use *URL* as the Python Package Index instead of the default
   (https://pypi.python.org/simple).

.. option:: --find-links URL

   Fetch additional packages by extracting the links from *URL*.  If
   *URL* refers to a directory (via a ``file://`` URL), then the
   contents of the directory are used.

.. option:: --no-use-wheel

   Do not find or prefer wheel archives when searching indexes and
   find-links locations.

.. option:: --pre

   Include pre-release and development versions.  By default, only
   stable versions are installed.

.. option:: --install-test-requirements

   Install dependencies listed in the ``tests_require`` keyword
   passed to :func:`setuptools.setup`.

.. option:: --install-extra-requirements EXTRA

   Install the ``extras_require`` dependencies associated with *EXTRA*.

Since the *requirements* command uses :command:`pip` to perform the
installation, you can use any of the `pip configuration files`_.

.. _pip configuration files:
   https://pip.readthedocs.io/en/latest/user_guide.html#configuration
.. _setuptools: https://setuptools.readthedocs.io/
