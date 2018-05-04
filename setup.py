#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Installation script.
""" 
import re
import setuptools


# Extract any `__builtin__` names with string values that are single quoted.
attr_pattern = r"^__(.+)__ ?= ?'([^\'])'$"


with open('leftpad.py') as fp:
    attr = {k: v for k, v in re.findall(attr_pattern, fp.read())}


setuptools.setup(
    name='leftpad.py',
    packages=('leftpad',),
    description='Pads strings with leading whitespace. For people who '
                'want 1,000,001 pointless dependencies in their project '
                'rather than writing a function with a single line of code '
                'themselves.',
    **attr
)
