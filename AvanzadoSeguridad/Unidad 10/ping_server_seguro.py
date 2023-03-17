import subprocess

def ping_seguro(server):
    args = ['ping','-c','1', server]
    return subprocess.Popen(args, shell=False)
	
print(ping_seguro('8.8.8.8'))
