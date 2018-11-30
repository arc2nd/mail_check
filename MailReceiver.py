#!/usr/bin/env python

import json
import types
import datetime

#from pellets.DurableReceiver import *
from pellets import DurableMessenger
import mail_check as mc

class MailReceiver(DurableMessenger):
    def load_commands(self):
        my_mc = mc.MailCheck()
        return my_mc.modules

    def callback(self, ch, method, properties, body):
        try:
            body_dict = json.loads(body)
            print(' [x] Received a JSON at {} \n{}'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'), body_dict))
        except:
            print(' [x] Received a string at {}\n {}'.format(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'), body))

        if 'command' in body_dict and 'arguments' in body_dict:
            cmd = body_dict['command']
            args = body_dict['arguments']
            if cmd.lower() == 'msg':
                print('yeah, I\'m not doing that. Too easy to infinite loop')
            elif cmd.lower() in self.plugins:
                print('cmd {} found in plugins'.format(cmd))
                print('calling with args: {}'.format(' '.join(args)))
                self.plugins[cmd.lower()](args)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    def listen(self, chan_name):
        self.plugins = self.load_commands()
        self.conn = self.get_conn()
        chan = self.make_channel(self.conn, chan_name)
        chan.basic_qos(prefetch_count=1)
        chan.basic_consume(self.callback, queue=chan_name)
        print(' [*] Waiting for mail_check messages, CTRL+C to exit')
        chan.start_consuming()

if __name__ == '__main__':
    my_rcvr = MailReceiver()
    my_rcvr.listen('mail_check')
