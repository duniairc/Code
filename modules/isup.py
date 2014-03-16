#!/usr/bin/env python
"""
Code Copyright (C) 2012-2014 Liam Stanley
Credits: Sean B. Palmer, Michael Yanovich, andrix: https://gist.github.com/andrix/1423960
isup.py - Code isup Module
http://code.liamstanley.io/
"""

import re
from urllib import urlopen
from tools import *

def isup(code,input):
    """isup <url> - Is it down for everyone, or just you?"""
    if empty(code, input): return
    if len(input.group(2).split()) != 1: return error(code)
    try:
        data = urlopen('http://isup.me/%s' % input.group(2)).read()
        if 'not just you' in data:
            return code.say(code.color('red', '%s is down! It\'s not just you!' % input.group(2)))
        elif 'It\'s just you.' in data:
            return code.say(code.color('green', '%s is up! Must just be you!' % input.group(2)))
        else:
            return error(code)
    except:
        return error(code)
isup.commands = ['isup', 'isdown', 'check', 'up', 'down']
isup.example = 'isup http://google.com'

if __name__ == '__main__':
    print __doc__.strip()
