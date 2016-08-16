from subprocess import call

call("sudo apt-get install -y python-pip --force-yes", shell=True)
call("sudo pip install caravel", shell=True
