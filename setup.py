# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

long_description = open(os.path.join(
    os.path.dirname(__file__), 'backports', 'ssl_match_hostname', 'README.txt',
    )).read()

setup(
    name='backports.ssl_match_hostname',
    version='3.4.0.2',
    description='The ssl.match_hostname() function from Python 3.4',
    long_description=long_description,
    author='Brandon Rhodes',
    author_email='brandon@rhodesmill.org',
    maintainer='Toshio Kuratomi',
    maintainer_email='toshio@fedoraproject.org',
    url='http://bitbucket.org/brandon/backports.ssl_match_hostname',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Topic :: Security :: Cryptography',
        ],
    packages=find_packages('.'),
    namespace_packages=['backports'],
    include_package_data=True,
    )
