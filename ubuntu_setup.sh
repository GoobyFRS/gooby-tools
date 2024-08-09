#!/bin/bash

#Update package lib. & upgrade.
echo "Fetching updates and applying upgrades..."
sudo apt update && sudo apt upgrade -y

#Install fav packages
sudo apt install neofetch pydf speedtest-cli python3-pip git curl wget whois -y

#Set my Timezone 
echo "Setting my Timezone"
sudo timedatectl set-timezone America/Chicago
echo "Updated timezone:"
date

#Setup my MOTD
sudo chmod -x /etc/update-motd.d/*
sudo touch /etc/motd

echo "Script completed."
