import setuptools


version_info = (0, 0, 0)
__version__ = '.'.join(str(c) for c in version_info)


class PipInstall(setuptools.Command):
    """Install a requirements file using pip"""

    user_options = [
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        pass


PipInstall.description = PipInstall.__doc__.splitlines()[0]
