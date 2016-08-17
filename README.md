<img src="http://thisiswhereidostuff.com/unicorn.gif" width="100%">

# Why

So I wanted a way to visualize good data. Caravel is a project by Airbnb that allows for easy connections of databases to visualize data very quickly. Caravel is great but has some quirks(I'll explain more later), and it's open-source. 

I selected a significant dataset that I cleaned up a little bit to better suit the way Caravel picks up labels, etc. for easy organization. Countries, for example, had to be simplified. The bottom line is data is ambiguously labeled by parties and it remains a huge task to find common standards, and good database management. Good data is very valuable.

What I picked out was the Zika epidemic dataset from IBM's Open Zika project. The information is very fascinating, has time series information, and will be a great way to learn about the different perspectives we can look at data from. We will infer some obvious conclusions from the visualizations, and some not-so-obvious conclusions. We will also talk about how the data could have been improved, and what would be useful in Caravel's visualization engine in the future so others may benefit as well.

# What

This is a python script that will automate an entire development environment for the airbnb project "Caravel". It automates the installation of several important things in a deployment:

  1. Vagrant VM Provisioning of an Ubuntu 14.04 box using Atlas
  
    a. port forward to :1234

  2. VirtualBox 
  3. Ansible

     a. Caravel prerequisites & install
     
     b. Copy dataset

# How

  `sudo python main.py`

Once the box is up and running and you're ssh'd into it, it's time to create your Caravel user and start it up.

`sudo fabmanager create-admin --app caravel`
   - Keep these credentials in mind, you'll need them to log into Caravel.

`sudo caravel db upgrade`

`sudo caravel init`

`sudo caravel runserver`

At which point we can explore our Caravel interface at `localhost:1234` or `127.0.0.1:1234`

<center><img src="http://thisiswhereidostuff.com/caravel.gif" width="100%"></center>

You'll notice in the gif I type into the SQLAlchemyURI "sqlite:////zikanew.db" and this is because I had been trying a couple versions. You'll want to stick with "sqlite:////zika.db" because I finalized my naming conventions before finishing up. Other than that, you want to follow it precisely.

Some steps in that .gif in the event that it doesn't load for you:

  1. From Carvel start, go to "Sources -> Databases" and add the URI I talk about just above this text. Name the DB anything you want.
  2. Test it by clicking "Test Connection" on the same page. You should get conf and a small box on the bottom with the name of the table.
  3. Go from "Sources -> Databases" to "Sources -> Tables" and add a table with the name "zika" (MANDATORY and not in the Caravel docs, the table name shouldn't even be a user option!) and select our database's name from the drop down.
  4. Go to your "Tables" page again and click on the edit button in the row and select the tab up top "List Table Column", select "temporal" for the "report_date" column and select everything remaining for the columns left or if you know specifically how you're going to interpret the data beforehand, select only what you need. 
  5. Go back to "Tables", click on the name ("zika") of the table you've entitled Caravel to and begin looking at data in new ways!

# Requirements

  This was tested on Ubuntu 14.04 (due to Ansible reqs and me going the path of least resistence as I'm familiar with Ubuntu) after upgrading the system with recent packages:
  
  <b>at least 4GB of RAM total + at least a 4-core CPU or 2 w/ hyperthreading. We're working with a somewhat large db and you'll want a quick interface.</b>
  
# Details & Afterthought

  The zika data has several useful classes. I'll let you explore some but the pertinent ones I find were "data_field" which is the type of record it was (anything from "confirmed_microcephaly" to "suspected_zika_infection"), as well as "location" which speaks for itself. You won't be surprised to find out it's mostly South America. If you're able to load the gif, you can see an example of what I use and you'll want to use "sum__value" instead of "COUNT*" for the base metric because of the nature of this data and how it's organized per incident in each respective nation, not per row of data.
  
  I had originally cleaned up the "location" data axis to hold easy-to-interpret country names but frankly, Carvel's "World Visualization" is in desperate need of an overhaul. The initial loading doesn't make it easy or even possible to change the metrics and it initializes the wrong ones for location data. It should include, like a "temporal" axis of data, a "spatial" or "geographical" one that is also exclusive to avoid this problem. Additionally, the GUI is somewhat backward in that countries with summed metrics simply turn white to signify a lower end of the spectrum, whereas countries with 0 data are grey. This results in countries with little data turning invisible against the background, and countries with no data remaining visible which is a pretty useless way to visualize global data. It should have been a heatmap so I'll fork it and fix these silly issues soon; at which point it'll be included as a specific installation candidate in this repo.
  
  Caravel is powerful but you must adhere to the way it wants to read your data which makes it limited in the sense any data scientist was probably worried about when looking into this; it's stubborn like everything else (minus pandas I guess). Airbnb considers this a red-headed stepchild. They're not going to invest much time into it and it's definitely up to the community to carry out any changes they want; you see evidence of this in the "Issues" part of their repo. It doesn't always handle memory well either so keep that in mind when creating a VM. You'll notice the Vagrantfile this creates allows for 2GB of RAM standard. It's no joke reading from a huge DB.
