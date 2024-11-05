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


sudo useradd -m -G sudo -s /bin/bash matt
sudo apt update
apt list --upgradable
sudo apt full-upgrade -y
sudo chmod -x /etc/update-motd.d/*
sudo touch /etc/motd
timedatectl
sudo timedatectl set-timezone America/Chicago
timedatectl
sudo ufw verbose
sudo ufw allow http
sudo ufw allow https
sudo ufw allow ssh
curl -s https://install.crowdsec.net | sudo sh
sudo apt install fail2ban crowdsec -y
sudo cp /etc/fail2ban/fail2ban.conf /etc/fail2ban/fail2ban.local
sudo systemctl status fail2ban.service
sudo systemctl start fail2ban.service

tailscale up --accept-dns --advertise-exit-node --operator=$user --ssh --qr
