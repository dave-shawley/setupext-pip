.. warning::
   **Import Usage Note**

   Now there is a very important problem with taking this approach --
   **setupext has to be installed BEFORE setup.py runs**.  This means
   that you cannot depend on ``setup_requires`` to install the extension.
   This is very unfortunate and made me consider not releasing this helper
   at all.


Using Requirement Files
-----------------------
``setuptools.setup`` takes three keyword parameters that control which
requirements are installed and when.  Here's what the `setuptools
documentation`_ has to say about these parameters.

``setup_requires``

    A string or list of strings specifying what other distributions need
    to be present in order for the setup script to run.  ``setuptools``
    will attempt to obtain these (even going so far as to download them
    using ``EasyInstall``) before processing the rest of the setup script
    or commands.  This argument is needed if you are using distutils
    extensions as part of your build process; for example, extensions that
    process ``setup()`` arguments and turn them into EGG-INFO metadata files.

    (Note: projects listed in ``setup_requires`` will NOT be automatically
    installed on the system where the setup script is being run.  They are
    simply downloaded to the setup directory if they’re not locally
    available already.  If you want them to be installed, as well as being
    available when the setup script is run, you should add them to
    ``install_requires`` and ``setup_requires``.)

``tests_require``

    If your project’s tests need one or more additional packages besides
    those needed to install it, you can use this option to specify them.
    It should be a string or list of strings specifying what other
    distributions need to be present for the package’s tests to run.  When
    you run the test command, ``setuptools`` will attempt to obtain these
    (even going so far as to download them using EasyInstall).  Note that
    these required projects will not be installed on the system where the
    tests are run, but only downloaded to the project’s setup directory if
    they’re not already installed locally.

``extras_require``

    A dictionary mapping names of “extras” (optional features of your
    project) to strings or lists of strings specifying what other
    distributions must be installed to support those features. See the
    section below on Declaring Dependencies for details and examples of
    the format of this argument.

You can use :func:`~setupext.pip.read_requirements_from_file` to read each
set of dependencies from a separate file.  This practice makes it possible
to organize simple or complex dependencies in a DRY manner.

.. code-block:: python

   import setuptools
   from setupext import pip

   setuptools.setup(
       name='my-package',
       # ...
       setup_requires=pip.read_requirements_from_file('requirements.txt'),
       tests_require=pip.read_requirements_from_file('dev-requirements.txt'),
   )

Now back to the ominous warning above.  If you can't guarantee that the
extension is installed into the environment that your package is installed
into, then you can roll your own implementation of reading the requirements
file.  I've used the following snippet to work through this problem with,
admittedly, simple requirements files.

.. code-block:: python

   try:
       from setupext.pip import read_requirements_from_file
   except ImportError:
       def read_requirements_from_file(req_name):
           with open(req_name, 'r') as req_file:
               return [
                   line[0:line.find('#')] if '#' in line else line.strip()
                   for line in req_file
               ]

It's no where near perfect, but it does work in most cases.


.. autofunction:: setupext.pip.read_requirements_from_file


.. _setuptools documentation: https://setuptools.readthedocs.io/
