import os
import time
print("pid:")
print(os.getpid())

newpid = os.fork()
if (newpid1 == 0):
    print("System call")
    print(os.uname())
    print("Done")
print(newpid)

newpid2 = os.fork()
print("second child")
if newpid2 == 0:
    print("forking")
    print(newpid2)