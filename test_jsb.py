import socket
import sys
import os
import time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), 'modules'))

import fdpexpect

jsb_out_address = ('127.0.0.1', 5124)
print("JSBSim console on %s" % str(jsb_out_address))
jsb_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
jsb_out.connect(jsb_out_address)
jsb_console = fdpexpect.fdspawn(jsb_out.fileno(), logfile=sys.stdout)
jsb_console.delaybeforesend = 0.0001
jsb_console.logfile = None
while True:
    jsb_console.send('resume\n')
    t = str(0.5)
    print('set %s %s\r\n' % ('fcs/throttle-cmd-norm[1]', t))
    #time.sleep(0.2)
    jsb_console.send('set %s %s\r\n' % ('fcs/throttle-cmd-norm[1]', t))
