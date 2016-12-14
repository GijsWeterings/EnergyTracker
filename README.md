# EnergyTracker

Tracks power usage in house, using packets coming from a smart power meter's p1 port. It logs data in a FireBase realtime db.

## Installation
This project was built to work on an always connected raspberry pi (I'm using a model 2 in my case, but any device with an internet connection and a usb port should work)

### Hardware setup
* Connect Pi to the p1 port (I'm using https://www.sossolutions.nl/slimme-meter-kabel), but you can also craft your own cable (domotix has a pinout at http://domoticx.com/wp-content/uploads/p1-uitlezen-arduino-BC170-transistor-768x545.png)
* Connect Pi to ethernet cable
* Power up pi and ssh into it (default user is `pi` with password `raspberry`, but you should change this, as your router likely allows external ssh sessions.)

### Software setup
I am basing these commands on Raspbian Jessie, but they shouldn't differ much if you're running another distro, beyond possibly using a different package manager

Install dependencies:
```
sudo apt-get install python python-pip
sudo pip install pyrebase pyserial
```

## Configuration
```
// TODO
```

## Running
running this as root user:
```
python reader.py
```