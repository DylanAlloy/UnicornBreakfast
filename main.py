import sys
import os
from subprocess import Popen, PIPE, STDOUT, call

print("\nHey there! Sit tight, this isn't going to hurt one bit.\n")

call("sudo apt-get update -y --force-yes", shell=True)
call("sudo apt-get upgrade -y --force-yes", shell=True)
print("Setting up Vagrant environment...\n")
	
# Install & create Vagrant folder for our box & related
call("wget https://releases.hashicorp.com/vagrant/1.8.5/vagrant_1.8.5_x86_64.deb", shell=True)
call("sudo dpkg -i vagrant_1.8.5_x86_64.deb", shell=True)
call("sudo rm vagrant_1.8.5_x86_64.deb", shell=True)

if not os.path.exists("Vagrant"):
	os.makedirs("Vagrant")
	
# cd to that folder
os.chdir("Vagrant")

# Download the box from Vagrant's "Atlas"
print("Downloading Ubuntu for the VM...\n")
p = Popen("vagrant box add ubuntu/trusty32", stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=True)
print("\nUbuntu 14.04 LTS (Trusty Tahr) downloading; please wait...\n")

# Prepare '2' input in binary & enter it to automate selection of VirtualBox modules
stdout = p.communicate(input=b'2')[0]
print("\nSetting up VirtualBox components...\n")
print(stdout.decode())
print("\nSuccessfully selected VirtualBox for setup...\n")
print("\nInstalling VirtualBox...\n")
call("sudo apt-get install -y virtualbox --force-yes", shell=True)
call("sudo apt-get install -y software-properties-common --force-yes", shell=True)

# Install Ansible after loading relevant repos
call("sudo apt-add-repository -y ppa:ansible/ansible", shell=True)
call("sudo apt-get update -y --force-yes", shell=True)
call("sudo apt-get install -y ansible --force-yes", shell=True)

# Copy Ansible playbook to the working directory and "vagrant up"
call("sudo cp ../playbook.yml .", shell=True)
call("vagrant up", shell=True)
call("vagrant ssh", shell=True)
