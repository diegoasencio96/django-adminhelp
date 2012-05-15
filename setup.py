# Copyright (c) 2010 Guilherme Gondim and contributors
#
# This file is part of Django Admin Help.
#
# Django Admin Help is free software under terms of the GNU Lesser
# General Public License version 3 (LGPLv3) as published by the Free
# Software Foundation. See the file README for copying conditions.

import codecs
import os
import sys

from setuptools import setup, find_packages


if 'publish' in sys.argv:
    os.system('python setup.py sdist upload')
    sys.exit()

read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()


# Dynamically calculate the version based on adminhelp.VERSION.
version = __import__('adminhelp').get_version()

setup(
    name = 'django-adminhelp',
    version = version,
    description = 'A help application for Django admin',
    long_description=read(os.path.join(os.path.dirname(__file__), 'README.rst')),
    keywords = 'django apps admin help',
    author = 'Guilherme Gondim',
    author_email = 'semente+django-adminhelp@taurinus.org',
    maintainer = 'Guilherme Gondim',
    maintainer_email = 'semente+django-adminhelp@taurinus.org',
    url = 'http://github.com/semente/django-adminhelp',
    download_url = 'http://github.com/semente/django-adminhelp/downloads',
    license = 'GNU Lesser General Public License (LGPL), Version 3',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['django-positions',],
)
