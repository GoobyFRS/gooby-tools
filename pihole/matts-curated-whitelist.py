#!/usr/bin/env python3
"""
Run this script to add Matt's personal selection of domains to your whitelist. This is catered to my personal preferences. This may not be the list for you!
"""
import os
print("*** Adding Matts Curated Domains to the PiHole Whitelist Now ***")

domains = ["mattfaulkner.net", "bluebotpc.net", "bluebotpc.com", "goobyfrs.net", "nordstrom.com", "nordstrom.net", "nordstrom.ca", "nordstrom.app", "longview.linode.com", "flightaware.com", "gameservices.fh5.forzamotorsport.net", "e0.flightcdn.com", "	flightxml.flightaware.com", "protonmail.ch", "api.protonmail.ch", "forum.level1techs.com", "level1techs.com", "1.debian.pool.ntp.org"]

#cmd_whitelist = os.system("pihole -w " + domain)

for domain in domains:
	os.system("pihole -w " + domain)
	#
print("*** Whitelisting Completed - Updating Gravity Now ***")
os.system("pihole -g")
print("*** Gravity Updated - Matt's Whitelist has been applied ***")