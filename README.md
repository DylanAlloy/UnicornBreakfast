<img src="https://media.giphy.com/media/l3fQe8ahU9XcWpHnG/giphy.gif" width="100%">

# Why

So I wanted a way to visualize good data. Caravel is a project by Airbnb that allows for easy connections of databases to visualize data very quickly. Caravel is far from perfect(I'll explain more later), but it's open source. 

I selected a significant dataset that I cleaned up a little bit to better suit the way Caravel picks up labels, etc. for easy organization. Countries, for example, had to be simplified. The bottom line is data is ambiguously labeled by parties and it remains a huge task to find common standards, and good database management. Good data is very valuable.

What I picked out was the Zika epidemic dataset from IBM's Open Zika project. The information is very fascinating, has time series information, and will be a great way to learn about the different perspectives we can look at data from. We will infer some obvious conclusions from the visualizations, and some not-so-obvious conclusions. We will also talk about how the data could have been improved, and what would be useful in Caravel's visualization engine in the future so others may benefit as well.

# What

This is a python script that will automate an entire development environment for the airbnb project "Caravel". It automates the installation of several important things in a deployment:

  1. Vagrant VM Provisioning of an Ubuntu 14.04 box using Atlas
  
    a. port forward to :8088

  2. VirtualBox 
  3. Ansible
  
    a. install Caravel - in the box

    b. prompt user for new admin credentials - in the box
    
    c. run Caravel server - in the box
    
  4. Requirements & database download - in the box

# How
  
  (Download+unzip) or clone this repository.

  `cd UnicornBreakfast-master`

  `python main.py`

It will likely prompt for your password (sudo) if you have not entered it recently.

# Requirements

  This was tested on Ubuntu after upgrading the system with recent packages:
  
  `sudo apt-get update && sudo apt-get install upgrade`
  
  `sudo apt-get install linux-headers-$(uname -r)`
  
  `sudo apt-get install build-essential`
