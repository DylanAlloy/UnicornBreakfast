import sys
import os
from subprocess import Popen, PIPE, STDOUT, call

print("\nHey there! Sit tight, this isn't going to hurt one bit.\n")
print("Setting up Vagrant environment...\n")

# Create Vagrant folder for our box & related
call("sudo apt-get install -y vagrant --force-yes", shell=True)
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
call("sudo apt-add-repository -y ppa:ansible/ansible --force-yes", shell=True)
call("sudo apt-get update -y --force-yes", shell=True)
call("sudo apt-get install -y ansible --force-yes", shell=True)

# init Vagrant with the box we selected & overwrite a minimal Vagrantfile
call("vagrant init ubuntu/trusty32", shell=True)
f = open("Vagrantfile", "w")
f.write("Vagrant.configure(\"2\") do |config|\n")
f.write("  config.vm.box = \"ubuntu/trusty32\"\n")
f.write("   config.vm.network \"forwarded_port\", guest: 8088, host: 1234\n")
f.write("  config.vm.provision \"ansible\" do |ansible|\n")
f.write("    ansible.playbook = \"playbook.yml\"\n")
f.write("   end\n")
f.write("  config.vm.provider \"virtualbox\" do |vb|\n")
f.write("    vb.memory = 2048\n")
f.write("    vb.cpus = 2\n")
f.write("   end\n")
f.write("end")
f.close()

# Copy Ansible playbook to the working directory and "vagrant up"
call("sudo cp ../playbook.yml .", shell=True)
call("vagrant up", shell=True)
call("vagrant ssh", shell=True)
