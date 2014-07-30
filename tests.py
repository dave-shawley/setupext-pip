"""

Test that ``PipInstall`` is a ``Command``.

The ``distutils`` package defines what is required by a ``Command``
inside of the source code (see *distutils/cmd.py:_Command*).  The
tests in this module verify that ``setupext.pip.PipInstall`` meets
the requirements described below.

``command_name``

    string returned from the ``get_command_name()`` method

``initialize_options()``

    provide default values for all options; may be customized by
    setup script, by options from config file(s), or by command-line
    options

``finalize_options()``

    decide on the final values for all options; this is called
    after all possible intervention from the outside world
    (command-line, option file, etc.) has been processed

``run()``

    run the command: do whatever it is we're here to do,
    controlled by the command's various option values

"""
from distutils import dist
import atexit
import os
import tempfile
try:
    from unittest import mock
except ImportError:
    import mock

from pip.commands import install
import setuptools

from setupext import pip


########################################################################
# setupext.pip.PipInstall
########################################################################

def should_define_command_name():
    assert pip.PipInstall.command_name is not None


def should_define_description():
    assert pip.PipInstall.description is not None


def should_define_default_for_each_option():
    distribution = mock.Mock(spec=dist.Distribution)
    distribution.verbose = mock.sentinel.verbose

    command = pip.PipInstall(distribution)
    for long_opt, short_opt, desc in pip.PipInstall.user_options:
        attr_name = long_opt.replace('-', '_').rstrip('=')
        attr_value = getattr(command, attr_name, mock.sentinel.unspecified)
        assert attr_value is not mock.sentinel.unspecified, (
            'attribute for option {0} was not found'.format(long_opt))


@mock.patch('setupext.pip.install')
def should_implement_setuptools_command_protocol(install_module=None):
    pip_command = install.InstallCommand()
    pip_command.run = mock.Mock()
    pip_command.cmd_opts = mock.MagicMock()
    install_module.InstallCommand.return_value = pip_command

    setuptools.setup(
        name='testing-setup',
        cmdclass={'requirements': pip.PipInstall},
        script_name='setup.py',
        script_args=[
            'requirements',
            '--requirement-file', 'requirements.txt',
            '--find-links', 'http://cheese-shop.local/links',
            '--index-url', 'http://cheese-shop.local/simple',
            '--pre',
            '--no-use-wheel',
        ],
    )

    pip_command.cmd_opts.parser.parse_args.assert_called_with([
        '-f', 'http://cheese-shop.local/links',
        '-i', 'http://cheese-shop.local/simple',
        '-r', 'requirements.txt',
        '--no-use-wheel',
        '--pre',
    ])


@mock.patch('setupext.pip.install')
def should_default_to_installing_package_requirements(install_module=None):
    pip_command = install.InstallCommand()
    pip_command.run = mock.Mock()
    pip_command.cmd_opts = mock.MagicMock()
    install_module.InstallCommand.return_value = pip_command

    setuptools.setup(
        name='testing-setup',
        cmdclass={'requirements': pip.PipInstall},
        script_name='setup.py',
        script_args=['requirements'],
        install_requires=[
            'docopt==0.6.1',
            'requests==2.3.0',
        ],
    )

    pip_command.cmd_opts.parser.parse_args.assert_called_with(
        ['docopt==0.6.1', 'requests==2.3.0'])


########################################################################
# setupext.pip.read_requirements_from_file
########################################################################

def should_read_complex_requirements_file():
    fd, name = tempfile.mkstemp()
    atexit.register(os.unlink, name)
    os.write(fd, '\n'.join([
        '# this comment is ignored',
        '  --always-unzip  # ignored',
        '-Z',
        'Unsafe_Name>1',
        '-i ignored/index/url',
        '--index-url=ignored/url',
        '-f ignored-links-path',
        '--find-links=ignored',
        'requests==1.2.3',
        'illegal name ignored',
    ]).encode('utf-8'))

    requirements = pip.read_requirements_from_file(name)

    assert requirements[0] == 'Unsafe-Name>1', 'Unsafe name not adjusted'
    assert requirements[1] == 'requests==1.2.3', 'Simple dependency broken'
    assert len(requirements) == 2
