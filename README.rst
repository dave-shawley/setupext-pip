Pip Setuptools Extension
========================

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
providing a new setup command named **requirements**.

Having a separate *requirements.txt* is a good pattern but it is not
without its flaws.  Having dependencies identified in two places is an
outright violation of the *Don't Repeat Yourself* principle.  That is
something else that we can solve pretty easily with a function that you
can read a pip-formatted requirements file and generate a list that is
usable as the setup ``setup_requires``, ``install_requires``, or
``tests_require`` keywords.

Ok... Where?
------------
+---------------+----------------------------------------------+
| Source        | https://github.com/dave-shawley/setupext-pip |
+---------------+----------------------------------------------+
| Download      | *eventually a link to PyPi*                  |
+---------------+----------------------------------------------+
| Documentation | *eventually on Read the Docs*                |
+---------------+----------------------------------------------+
| Issues        | https://github.com/dave-shawley/setupext-pip |
+---------------+----------------------------------------------+


.. _setuptools: https://pythonhosted.org/setuptools/
.. _pip: https://pip.pypa.io/en/latest/
.. _pip-formatted requirements file: 
   https://pip.pypa.io/en/latest/reference/pip_install.html
   #requirements-file-format
