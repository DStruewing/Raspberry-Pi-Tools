import subprocess
import os
import signal
import time

# Ping the pi to get its IP address.
p = subprocess.Popen(["ping raspberrypi.local"], stdout=subprocess.PIPE, shell=True)
time.sleep(0.5)
os.kill(p.pid, signal.SIGINT)

# Get output from ping.
out, err = p.communicate()

# Extract the IP address from the output
# and create a properly formatted ssh command.
a,b = out.split("(")
a,b = b.split(")")
cmd = "ssh pi@%s" % a

os.system(cmd)
