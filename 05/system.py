import sys
import os


cmd = 'ls -l /tmp > /dev/null'
RET = os.system(cmd)
if RET == 0:
    print('[ ok ] The command complete.')
else:
    print(' [ fail ] The command not complete')
