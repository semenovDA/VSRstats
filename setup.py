from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='VSRstats',
    version='1.1.0',
    author='Dmitry',
    author_email='semenov.da17@gmail.com',
    packages=['VSRstats'],
    url='http://bsu.ru/',
    description='VSR statstics compute util',
    #long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=['pyhrv', 'numpy', 'pandas==0.25.3', 'peakutils', 'matplotlib', 'xlrd'],
)
