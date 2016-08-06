<img src="https://media.giphy.com/media/l3fQe8ahU9XcWpHnG/giphy.gif">

Just eating some data.

# What

This is a python script that will automate an entire development environment for the airbnb project "Caravel". It automates the installation of several important things in a deployment:

  1. Vagrant VM Provisioning of an Ubuntu 14.04 box
  2. VirtualBox 
  3. Ansible Tower - in the box
  4. nginx - in the box
  5. PHP & database config - in the box
  6. Caravel - in the box
  7. Import the complex dataset - in the box

# How

  `cd UnicornBreakfast-master`

  `python main.py`

It will likely prompt for your password (sudo) if you have not entered it recently.

# Requirements

  This was tested on Ubuntu 14.04 after manually:
  
  `sudo apt-get update && sudo apt-get install upgrade`
  
  `sudo apt-get install linux-headers-$(uname -r)`
  
  `sudo apt-get install build-essential`
