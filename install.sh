#!/bin/bash


# Setting up Ubuntu for Django / React Project

apt -y update
apt install build-essentials libssl-dev libffi-dev python-dev

# pip3 
apt install -y python3-pip

# Nodejs & npm
curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
sudo apt install npm -y
sudo npm install -g create-react-app -y

cd /vagrant 
sudo pip3 install -r requirements.txt


echo "Finished dependancies"
