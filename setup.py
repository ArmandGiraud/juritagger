#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/juritagger.svg
        :target: https://pypi.python.org/pypi/juritagger
.. image:: https://img.shields.io/travis/ArmandGiraud/juritagger.svg
        :target: https://travis-ci.org/ArmandGiraud/juritagger

tag a text string with droit du travail entities


Links:
---------
* `Github <https://github.com/ArmandGiraud/juritagger>`_
"""

from setuptools import setup, find_packages

requirements = ['Click>=6.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Armand Giraud",
    author_email='armand.giraud.ag@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="tag a text string with droit du travail entities",
    entry_points={
        'console_scripts': [
            'juritagger=juritagger.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='juritagger',
    name='juritagger',
    packages=find_packages(include=['juritagger']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ArmandGiraud/juritagger',
    version='0.1.0',
    zip_safe=False,
)
