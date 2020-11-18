#!/usr/bin/env sh


#EC Additions vs lab
#Adjust architecture
#TODO add uname -m for architecture inline?

echo "deb [arch=x86_64] http://archives.dianomic.com/foglamp/nightly/ubuntu1804/x86_64/ ./" | sudo tee -a /etc/apt/sources.list.d/foglamp.list

wget -O - http://archives.dianomic.com/KEY.gpg | sudo apt-key add -

sudo apt-get update

sudo apt-get -y install foglamp foglamp-gui

