import sys
import os
from subprocess import Popen, PIPE, STDOUT, call

print("\nHey there! Sit tight, this isn't going to hurt one bit.\n")

  # Install our beloved Vagrant VM manager/provision  
call("sudo apt-get install vagrant", shell=True)

  # Create folder & cd
print("Setting up Vagrant environment...\n")
if not os.path.exists("Vagrant"):
	os.makedirs("Vagrant")
os.chdir("Vagrant")

  # Download Ubuntu box from Vagrant site
print("Downloading Ubuntu for the VM...\n")
p = Popen("vagrant box add ubuntu/trusty64", stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)
print("\nUbuntu 14.04 LTS (Trusty Tahr) downloaded...\n")

  # Select "2.) virtual box" by sending binary encoded TTY stdin
stdout = p.communicate(input=b'2')[0]
print("\nSetting up VirtualBox components...\n")
print(stdout.decode())

  # Install VirtualBox if it's not present on the system
print("\nSuccessfully selected VirtualBox for setup...\n")
print("\nInstalling VirtualBox...\n")
call("sudo apt-get install virtualbox", shell=True)

  # Initialize Vagrant & system access
call("vagrant init ubuntu/trusty64", shell=True)
call("vagrant up", shell=True)
call("vagrant ssh", shell=True)
