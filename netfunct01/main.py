#!/usr/bin/env python3
""" we'll create a function that mimics pushing commands to a file"""

import crayons

def commandpush(devicecmd):

    for ip in devicecmd.keys():
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}')
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending commmand --> {mycmds}')
    return None

def devicereboot(ips):
    for ip in ips:
        print(f"Connecting to {ip}")
        print("REBOOTING NOW!")


def main():

    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print(f"Welcome to the {crayons.blue('Network')} device command pusher")

    print("\nData set found\n")

    commandpush(devicecmd)

    print("\nRebooting devices\n")
    devicereboot(devicecmd.keys())

main()
