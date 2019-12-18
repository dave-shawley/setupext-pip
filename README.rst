Pip Setuptools Extension
========================

|Version| |Downloads| |Status| |License|

A `setuptools`_ extension that installs requirements based on `pip`_
requirements files.

Wait... Why? What??
-------------------

Installing runtime dependencies is already handled by setuptools right?
It's as easy as running ``python setup.py develop``?!  Not quite...

*setup.py* is a great tool and the *develop* command is useful for setting
up basic development and installing the dependencies identified by the
``setup_requires`` keyword.  What it does not do is install any tools that
are used for actually hacking on the code base.  Many projects include a
`pip-formatted requirements file`_ named *requirements.txt* for this very
purposes.  It contains the dependencies that you need to have installed to
work on the project instead of use it.  This extension aims to automate
that pattern and make it easier to set up a development environment by
providing a new setup command named *requirements*.

Having a separate *requirements.txt* is a good pattern but it is not
without its flaws.  Having dependencies identified in two places is an
outright violation of the *Don't Repeat Yourself* principle.  That is
something else that we can solve pretty easily with a function that you
can read a pip-formatted requirements file and generate a list that is
usable as the setup ``setup_requires``, ``install_requires``, or
``tests_require`` keywords.  This is where the
``setupext.pip.read_requirements_from_file`` function comes in.
You can use this function to populate the ``setup_requires``,
``tests_require``, and ``extras_require`` keywords.

Ok... Where?
------------
+---------------+-------------------------------------------------+
| Source        | https://github.com/dave-shawley/setupext-pip    |
+---------------+-------------------------------------------------+
| Status        | https://travis-ci.org/dave-shawley/setupext-pip |
+---------------+-------------------------------------------------+
| Download      | https://pypi.python.org/pypi/setupext-pip       |
+---------------+-------------------------------------------------+
| Documentation | http://setupext-pip.readthedocs.org/en/latest/  |
+---------------+-------------------------------------------------+
| Issues        | https://github.com/dave-shawley/setupext-pip    |
+---------------+-------------------------------------------------+


.. _setuptools: https://setuptools.readthedocs.io/
.. _pip: https://pip.readthedocs.io/en/latest/
.. _pip-formatted requirements file:
   https://pip.readthedocs.io/en/latest/reference/pip_install.html
   #requirements-file-format
.. |Version| image:: https://img.shields.io/pypi/v/setupext-pip
   :target: https://pypi.org/project/setupext-pip
.. |Downloads| image:: https://img.shields.io/pypi/dm/setupext-pip
   :target: https://pypi.org/project/setupext-pip
.. |Status| image:: https://img.shields.io/travis/dave-shawley/setupext-pip
   :target: https://travis-ci.org/dave-shawley/setupext-pip
.. |License| image:: https://img.shields.io/pypi/l/setupext-pip
   :target: https://setupext-pip.readthedocs.io/

