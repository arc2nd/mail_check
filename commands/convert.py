#!/usr/bin/python

import os
import commands

def convert(url):
    print('Convert: {}'.format(url))
    cmd = 'python {} -u {}'.format(os.path.expanduser('~/scripts/convertToAudio.py'), url)
    print('cmd: {}'.format(url))
    status, output = commands.getstatusoutput(cmd)
    print('Status: {}'.format(status))
    print('Output: {}'.format(output))

