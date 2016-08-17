Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty32"
   config.vm.network "forwarded_port", guest: 8088, host: 1234
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
   end
  config.vm.provider \"virtualbox\" do |vb|
    vb.memory = 2048
    vb.cpus = 2
   end
end
