#!/usr/bin/env bash

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-get update
sudo apt install curl
sudo apt -y install python3-pip
#sudo apt-get install -y docker-ce
sudo apt-get install docker-compose -y
sudo usermod -aG docker "${USER}"
su - "${USER}"