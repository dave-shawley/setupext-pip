import logging

import pkg_resources
import setuptools

try:
    from pip.commands import install
except ImportError:
    install = None


version_info = (1, 0, 3)
__version__ = '.'.join(str(c) for c in version_info)


class PipInstall(setuptools.Command):
    """Install a requirements file using pip"""

    command_name = 'requirements'
    user_options = [
        ('find-links=', 'f', 'Find links at the given location/URL'),
        ('index-url=', 'i', 'Base URL of Python Package Index'),
        ('requirement-file=', 'r', 'Install requirements from file'),
        ('pre', None,
            'Include pre-release or development versions of dependencies'),
        ('no-use-wheel', None, 'Do not find and prefer wheel archives'),
    ]

    def initialize_options(self):
        self._pip_args = []
        self.find_links = None
        self.index_url = None
        self.no_use_wheel = False
        self.pre = False
        self.requirement_file = None

    def finalize_options(self):
        if self.find_links is not None:
            self._pip_args.extend(['-f', self.find_links])
        if self.index_url is not None:
            self._pip_args.extend(['-i', self.index_url])
        if self.requirement_file is not None:
            self._pip_args.extend(['-r', self.requirement_file])
        else:
            self._pip_args.extend(self.distribution.install_requires)
        if self.no_use_wheel:
            self._pip_args.append('--no-use-wheel')
        if self.pre:
            self._pip_args.append('--pre')

    def run(self):
        cmd = install.InstallCommand()
        args = cmd.cmd_opts.parser.parse_args(self._pip_args)
        cmd.run(*args)


PipInstall.description = PipInstall.__doc__.splitlines()[0]


def read_requirements_from_file(file_name):
    """Read requirements from a pip-formatted requirements file.

    :param str file_name: the name of the file to read from
    :return: a ``list`` of requirements as strings

    This function reads the specified file, processes it as the
    :command:`pip` utility would, and returns the list of
    dependency specifiers.  Each line of the requirements file
    is parsed using the functionality provided by `pkg_resources`_
    so even the hairiest dependency specifiers will be parsed
    correctly.  However, all command line parameter overrides (e.g.,
    ``--index-file=...``) are ignored.

    .. _pkg_resources:
       https://pythonhosted.org/setuptools/pkg_resources.html
       #requirements-parsing

    """
    logger = logging.getLogger('read_requirements_from_file')
    requirements = []
    with open(file_name, 'rb') as req_file:
        for line_number, buf in enumerate(req_file):
            line = buf.decode('utf-8').strip()
            if line.find('#') >= 0:
                line = line[0:line.find('#')].strip()
            if not line:
                continue

            if line.startswith('-'):
                continue

            try:
                req = pkg_resources.Requirement.parse(line)
                requirements.append(str(req))
            except ValueError:
                logger.warning(
                    'failed to parse line %s in %s',
                    line_number, file_name,
                    exc_info=True,
                )
    return requirements
