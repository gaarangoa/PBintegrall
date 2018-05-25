
import subprocess

for i in range(10, 1000000000, 10):
    proc = subprocess.Popen(["head", "/etc/services"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()




