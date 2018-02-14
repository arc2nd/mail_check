#!/usr/bin/python

import os
import commands

def dl(url):
    print('DL: {}'.format(url))
    cmd = 'youtube-dl {}'.format(url)
    print('cmd: {}'.format(url))
    status, output = commands.getstatusoutput(cmd)
    print('Status: {}'.format(status))
    print('Output: {}'.format(output))

