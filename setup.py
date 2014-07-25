import codecs
import setuptools

from setupext import pip


def _read_file(filename):
    with codecs.open(filename, 'rb', encoding='utf-8') as file_obj:
        return '\n' + file_obj.read()


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
    install_requires=['pip'],
    tests_require=['pytest', 'tox'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    entry_points={
        'distutils.commands': [
            'requirements = setupext.pip:PipInstall',
        ],
    },
)
