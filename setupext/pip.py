import setuptools

try:
    from pip.commands import install
except ImportError:
    install = None


version_info = (1, 0, 1)
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
