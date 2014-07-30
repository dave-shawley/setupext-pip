from setuptools.command.test import test as TestCommand
import codecs
import setuptools
import sys

from setupext import pip


def _read_file(filename):
    with codecs.open(filename, 'rb', encoding='utf-8') as file_obj:
        return '\n' + file_obj.read()


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', 'Arguments to pass to tox')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import shlex
        import tox
        sys.exit(tox.cmdline(args=shlex.split(self.tox_args or '')))


setuptools.setup(
    name='setupext-pip',
    version=pip.__version__,
    author='Dave Shawley',
    author_email='daveshawley@gmail.com',
    url='http://github.com/dave-shawley/setupext-pip',
    description='Setuptools extension for installing requirements',
    long_description=_read_file('README.rst'),
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    namespace_packages=['setupext'],
    zip_safe=False,
    platforms='any',
    install_requires=['pip>=1.5'],
    tests_require=['tox'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Setuptools Plugin',
        'Development Status :: 4 - Beta',
    ],
    cmdclass={'test': Tox},
    entry_points={
        'distutils.commands': [
            'requirements = setupext.pip:PipInstall',
        ],
    },
)
