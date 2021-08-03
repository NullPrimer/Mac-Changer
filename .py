import subprocess

interface = "wlan0"
new_mac = "00:11:22:33:44:55"

print("[+] Changing MAC address for" + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + "down", shell=True)
subprocess.call("ifconfig " + interface +  "hw ether" + new_mac, shell=True)
subprocess.call("ifconfig " + interface +  "up", shell=True)


# Code progression
# Notes - User input is not secure as user is able to exploit the interface variables

import subprocess

interface = input("interface >")
new_mac = input ("new MAC >")

print("[+] Changing MAC address for" + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + "down", shell=True)
subprocess.call("ifconfig " + interface +  "hw ether" + new_mac, shell=True)
subprocess.call("ifconfig " + interface +  "up", shell=True)

# This is a good secure alternative to the above.

subprocess.call(["ifconfing", interface, "down"])
subprocess.call(["ifconfing", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfing", interface, "up"])


# Code Progression Use this for Tron


import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_MAC

print("[+] Changing MAC address for" + interface + " to " + new_mac)

subprocess.call(["ifconfing", interface, "down"])
subprocess.call(["ifconfing", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfing", interface, "up"])


# Code Progression

import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for" + interface + " to " + new_mac)

    subprocess.call(["ifconfing", interface, "down"])
    subprocess.call(["ifconfing", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfing", interface, "up"])

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

change_mac(options.interface, options.new_mac)

# Code progression

import subprocess
import optparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for" + interface + " to " + new_mac)
    subprocess.call(["ifconfing", interface, "down"])
    subprocess.call(["ifconfing", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfing", interface, "up"])

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)

# Code Progressions Final draft

import subprocess
import optparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for" + interface + " to " + new_mac)
    subprocess.call(["ifconfing", interface, "down"])
    subprocess.call(["ifconfing", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfing", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)
