<img src="http://thisiswhereidostuff.com/unicorn.gif" width="100%">

# Why

So I wanted a way to visualize good data. Caravel is a project by Airbnb that allows for easy connections of databases to visualize data very quickly. Caravel is great but has some quirks(I'll explain more later), and it's open-source. 

What I picked out was the Zika epidemic dataset from IBM's Open Zika project. The information is very fascinating, has time series information, and will be a great way to learn about the different perspectives we can look at data from. We will infer some obvious conclusions from the visualizations, and some not-so-obvious conclusions. We will also talk about how the data could have been improved, and what would be useful in Caravel's visualization engine in the future so others may benefit as well.

# What

This is a vagrant config that automates the installation of several important things in a deployment:

  1. Vagrant VM Provisioning of an Ubuntu 14.04 box using Atlas
  
    a. port forward to :1234

  2. VirtualBox 
  3. Ansible

     a. Caravel prerequisites & install
     
     b. Copy dataset

# How

  `vagrant up --provision` inside of the directory. Use sudo if it says it "fails early on" and you're on Linux.
  
  Then tell it: `sudo bash /caravel.sh` when you're in. Info on why you have to do this is in playbook.yml but essentially there is a messy deprecation warning getting in the way of Ansible properly reading from the TTY.

It will take some time to install everything until it finishes; at which point we can explore our Caravel interface at `localhost:1234` or `127.0.0.1:1234`.

# Requirements

  This was tested on Ubuntu 14.04 (due to Ansible reqs) after upgrading the system with recent packages.
  
  You will need Vagrant 1.8.5+, Ansible 2+, and virtualbox.
  
  <b>at least 4GB of RAM total + at least a 4-core CPU or 2 w/ hyperthreading. We're working with a somewhat large db and you'll want a quick interface. Reduce resources allocated by the Vagrantfile exported by main.py at your own discretion.</b>
  
# Details & Afterthought

  The zika data has several useful classes. I'll let you explore some but the pertinent ones I find were "data_field" which is the type of record it was (anything from "confirmed_microcephaly" to "suspected_zika_infection"), as well as "location" which speaks for itself. You won't be surprised to find out it's mostly South America. If you're able to load the gif, you can see an example of what I use and you'll want to use "sum__value" instead of "COUNT*" for the base metric because of the nature of this data and how it's organized per incident in each respective nation, not per row of data.
  
  Caravel is powerful but you must adhere to the way it wants to read your data which makes it limited in the sense any data scientist was probably worried about when looking into this; it's stubborn like everything else (minus pandas I guess). Airbnb considers this a red-headed stepchild. They're not going to invest much time into it and it's definitely up to the community to carry out any changes they want; you see evidence of this in the "Issues" part of their repo. It doesn't always handle memory well either so keep that in mind when creating a VM. You'll notice the Vagrantfile this creates allows for 2GB of RAM standard. It's no joke reading from a huge DB.
