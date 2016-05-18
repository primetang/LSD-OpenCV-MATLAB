#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-19 02:09:53
# @Author  : Gefu Tang (tanggefu@gmail.com)
# @Link    : https://github.com/primetang/pylsd
# @Version : 0.0.1

import ctypes
import os
import sys
import random
import numpy as np


def load_lsd_library():

    root_dir = os.path.abspath(os.path.dirname(__file__))

    libnames = ['linux/liblsd.so']
    libdir = 'lib'
    if sys.platform == 'win32':
        if sys.maxsize > 2 ** 32:
            libnames = ['win32/x64/lsd.dll', 'win32/x64/liblsd.dll']
        else:
            libnames = ['win32/x86/lsd.dll', 'win32/x86/liblsd.dll']
    elif sys.platform == 'darwin':
        libnames = ['darwin/liblsd.dylib']

    while root_dir != None:
        for libname in libnames:
            try:
                lsdlib = ctypes.cdll[os.path.join(root_dir, libdir, libname)]
                return lsdlib
            except Exception, e:
                pass
        tmp = os.path.dirname(root_dir)
        if tmp == root_dir:
            root_dir = None
        else:
            root_dir = tmp

    # if we didn't find the library so far, try loading without
    # a full path as a last resort
    for libname in libnames:
        try:
            # print "Trying",libname
            lsdlib = ctypes.cdll[libname]
            return lsdlib
        except:
            pass

    return None

lsdlib = load_lsd_library()
if lsdlib == None:
    raise ImportError('Cannot load dynamic library. Did you compile LSD?')
