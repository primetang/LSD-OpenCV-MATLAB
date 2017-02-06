#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-19 02:09:53
# @Author  : Gefu Tang (tanggefu@gmail.com)
# @Link    : https://github.com/primetang/pylsd

from setuptools import setup

setup(
    name='pylsd',
    version='0.0.2',
    description='pylsd is the python bindings for LSD - Line Segment Detector',
    author='Gefu Tang',
    author_email='tanggefu@gmail.com',
    license='BSD',
    keywords="LSD",
    url='https://github.com/primetang/pylsd',
    packages=['pylsd', 'pylsd.bindings', 'pylsd.lib'],
    package_dir={'pylsd.lib': 'pylsd/lib'},
    package_data={'pylsd.lib': [
        'darwin/*.dylib', 'win32/x86/*.dll', 'win32/x64/*.dll', 'linux/*.so']},
)
