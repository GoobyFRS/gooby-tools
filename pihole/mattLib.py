#!/usr/bin/env python3
#Library of Functions created by Matt Faulkner, a python beginner.
import os
import subprocess
import timedate
import getpass
import yfinance as yf
import netmiko
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException

def main():
	#
#
def getTarget():
	hostname = input("Target Host: ")

def linuxPing():
	#This will check the up/down status of a single device if ran from a Linux based OS
	sendPing = os.system("ping -c 1 " + hostname)
	if sendPing == 0:
		print(hostname + " is up.")
	else:
		print(hostname + " is down.")
#
def getCreds():
	#This will gather basic user authentication information to be used against devices. 
	username = input("Username: ")
	password1 = getpass()
	print("Please enter your password one more time to prevent lockouts...")
	password2 = getpass()
	if password1 != password2:
		print("Passwords did not match. Exiting...")
		raise SystemExit
	else:
		print("Login Success. Continuing...")

def ciscoConnet(username, password2, hostname):
	#This will connect to a Cisco IOS device and return basic diagnostic information.
	cisco_dict = {
	'device_type': 'cisco_ios',
	'host': hostname,
	'username': username,
	'password': password2,
	'verbose': 'false',
	}
	netmiko.ConnectHandler(**ciscoConnet)
	cs_ssh_session = netmiko.ConnectHandler(**cisco_dict)
	cs_ssh_session.send_command("terminal length 0\n") #Remove cli limit for parsing
	cs_uptime = cs_ssh_session.send_command("show version | include uptime")
	cs_int_desc = cs_ssh_session.send_command("show interface descriptions")
	cs_int_stat = cs_ssh_session.send_command("show interface status")
	cs_env = cs_ssh_session.send_command("show env all")
	cs_vtp_check = cs_ssh_session.send_command("show vtp status")

	#

def juniperConnect(username, password2, hostname):
	#This will connect to a Juniper EX Switch and return basic diagnostic information.
	juniper_ex_dict = {
	'device_type': 'juniper'
	'host': hostname,
	'username': username,
	'password': password2,
	'verbose': 'false',
	}
	netmiko.ConnectHandler(**juniper_ex_dict)
	js_ssh_session = netmiko.ConnectHandler(**juniper_ex_dict)
	js_ssh_session.send_command("set cli screen_length 0") #Remove CLI limit for parsing
	js_uptime = js_ssh_session.send_command("show system uptime | match up")
	js_env = js_ssh_session.send_command("show chassis enviroment")
	js_alarms = js_ssh_session.send_command("show chassis alarms")
	js_logs = js_ssh_session.send_command("show log messages")
	#

def arubaConnect(username, password2, hostname):
	#This will connect to an Aruba Wireless Controller and return basic diagnostic information.
	aruba_dict = {
	'device_type': 'aruba_os',
	'host': hostname,
	'username': username,
	'password': password2,
	'verbose': 'false',
	}
	netmiko.ConnectHandler(**aruba_dict)
	aruba_ssh_session = netmiko.ConnectHandler(**aruba_dict)
	aruba_uptime = aruba_ssh_session.send_command("show version | include uptime")
	aruba_apdb_check  = aruba_ssh_session.send_command("show ap database long")
	aruba_ssid_check = aruba_ssh_session.send_command("show ap essid")
	aruba_logs = aruba_ssh_session.send_command("show log all 500")
	#

def calcAnualIncome():
	#

def getStockPrice():
	#