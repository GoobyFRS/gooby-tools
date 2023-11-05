#!/usr/bin/env python3
"""
Run this script to add Matt's personal selection of domains to your blacklist. This is catered to my personal preferences. This may not be the list for you!
"""
import os
print("*** Adding Matts Curated Domains to the PiHole Blacklist Now ***")

domains = ["twiter.com", "facebok.com", "youtuube.com", "yutube.com", "olayfans.com", "pronhub.com", "comparecards.com", "fury.ca"]

for domain in domains:
	os.system("pihole -b " + domain)
	#
print("*** Blacklisting Completed - Updating Gravity Now ***")
os.system("pihole -g")
print("*** Gravity Updated - Matt's Blacklisting has been applied ***")