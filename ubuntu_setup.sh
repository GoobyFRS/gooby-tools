#!/bin/bash

# Update package libraries and upgrade packages
echo "Step 1 of 6 started."
echo "Fetching updates and applying upgrades. This may take a moment."
sudo apt update && sudo apt upgrade -y || { echo "Failed to update and upgrade packages."; exit 1; }
echo "Step 1 of 6 completed successfully."

# Install favorite packages
echo "Step 2 of 6 started."
echo "Installing packages: pydf, git, curl, wget, whois, fail2ban."
sudo apt install -y pydf git curl wget whois fail2ban || { echo "Failed to install packages."; exit 1; }
echo "Step 2 of 6 completed successfully."

# Set Timezone
echo "Step 3 of 6 started."
echo "Checking default Timezone."
date
echo "Setting Timezone to CST."
sudo timedatectl set-timezone America/Chicago || { echo "Failed to set timezone."; exit 1; }
echo "Updated Timezone:"
date
echo "Step 3 of 6 completed successfully."

# Create user account
echo "Step 4 of 6 started."
USERNAME="matt"
echo "Creating user account: $USERNAME"
sudo useradd -m -G sudo -s /bin/bash "$USERNAME" || { echo "Failed to create user $USERNAME."; exit 1; }
echo "Account for $USERNAME created successfully."
echo "Step 4 of 6 completed successfully."

# Install and configure CrowdSec
echo "Step 5 of 6 started."
echo "Installing CrowdSec. This may take a moment."
curl -s https://install.crowdsec.net | sudo sh || { echo "Failed to install CrowdSec."; exit 1; }
sudo apt install -y crowdsec || { echo "Failed to install CrowdSec."; exit 1; }
echo "Step 5 of 6 completed successfully."

# Configure Fail2Ban
echo "Step 6 of 6 started."
echo "Configuring Fail2Ban."
sudo cp /etc/fail2ban/fail2ban.conf /etc/fail2ban/fail2ban.local || { echo "Failed to copy Fail2Ban configuration."; exit 1; }
sudo systemctl enable fail2ban.service
sudo systemctl start fail2ban.service
sudo systemctl status fail2ban.service --no-pager || { echo "Fail2Ban service failed to start."; exit 1; }
echo "Fail2Ban enabled and running."
echo "Step 6 of 6 completed successfully."

# Final message
echo "System setup complete. CrowdSec and Fail2Ban are operational."
