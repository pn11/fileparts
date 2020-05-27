from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

MAJOR = 0
MINOR = 1
MICRO = 0
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

setup(
    name='fileparts',
    version=VERSION,
    description="Matlab's fileparts clone",
    long_description=readme,
    author='Oka Naoya',
    author_email='pn11@users.noreply.github.com',
    url='https://github.com/pn11/fileparts',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
