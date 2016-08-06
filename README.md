<img src="https://media.giphy.com/media/l3fQe8ahU9XcWpHnG/giphy.gif">

Just eating some data.

# What

This is a python script that will automate an entire development environment for the airbnb project "Caravel". It automates the installation of several important things in a deployment:

1. Vagrant VM Provisioning of an Ubuntu 14.04 box
2. VirtualBox 
3. Ansible Tower
4. nginx
5. PHP & database config
6. Caravel
7. Import the complex dataset

# How

`cd UnicornBreakfast-master`
`python main.py`

It will likely prompt for your password (sudo) if you have not entered it recently.

# Requirements

  This was tested on Ubuntu 14.04 after manually:
  
  `sudo apt-get update && sudo apt-get install upgrade`
  `sudo apt-get install linux-headers-$(uname -r)`
  `sudo apt-get install build-essential`
