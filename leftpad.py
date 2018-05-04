#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Left-pads a string, obviously.
"""

__all__ = ('leftpad', '__version__', '__license__',
           '__author__')

__author__ = '404'
__license__ = 'WTFPL'
__version__ = '1.0.0a1'


def leftpad(string: str, target_length: int) -> str:
    """
    Left-pads the given string until it is the given 
    length. If you actually use this as a dependency,
    you are a meme, and should return to the cabbage
    farm.
    :param string: the string to left pad.
    :param target_length: the length of the result
    :returns: the padded string. If len(string) >=
        target_length, nothing is done.
    """
    return max(0, target_length - len(string)) * ' ' + string
