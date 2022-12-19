

import sys

#if not len(sys.argv[1:]):
 #   print("Usage: %s arg1 arg2" % (sys.argv[0])
  #  sys.exit(1)

if len(sys.argv[1:]) != 1:
    print('[ Fail ] Usage: %s %s ' % (sys.argv[0], sys.argv[1]))
print(sys.argv[0])
print(sys.argv[1:])

