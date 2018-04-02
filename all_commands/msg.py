#!/usr/bin/python

import os
import json
import commands

from pellets.DurableMessenger import *

def msg(cmd, *args):
    print('Msg: {}'.format(cmd))
    # Compose Message
    msg_dict = {'command': cmd, 'arguments': args}
    msg_str = json.dumps(msg_dict, sort_keys=True, indent=4)


    # Create Messenger Object
    my_msgr = DurableMessenger()
    my_msgr.talk(chan_name='mail_check', msg=msg_str)


