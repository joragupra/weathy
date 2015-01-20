#!/usr/bin/env python

from setuptools import setup


setup(
    name = 'weathy',
    version = '1.0.0',
    description = "Weathy is a library to get up to date weather information from your current location",
    author = "Jorge Agudo Praena",
    author_email = "joragupra@gmail.com",
    license = '',
    url = '',
    scripts = ['retrieve_weather.py'],
    packages = ['weathy'],
    py_modules = [],
    classifiers = ['Programming Language :: Python'],
    entry_points={'console_scripts':[]}
)