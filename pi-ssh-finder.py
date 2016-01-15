import subprocess
import os
import signal
import time

output = 0
p = subprocess.Popen(["ping raspberrypi.local"], stdout=subprocess.PIPE, shell=True)
time.sleep(0.5)
os.kill(p.pid, signal.SIGINT)

out, err = p.communicate()

a,b = out.split("(")
a,b = b.split(")")

cmd = "ssh pi@%s" % a

os.system(cmd)
