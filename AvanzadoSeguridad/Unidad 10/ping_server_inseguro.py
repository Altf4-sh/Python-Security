import subprocess

def ping_inseguro(server):
    return subprocess.Popen('ping -c 1 %s' % server, shell=True)

print(ping_inseguro('8.8.8.8 & touch file'))
