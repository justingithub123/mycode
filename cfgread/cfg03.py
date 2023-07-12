#!/usr/bin/env python3
"""exploring readlines() with config file"""

#count = 0
config_file = input("What file would you like to process? ")

with open(config_file, "r") as configfile:
    configlist = configfile.readlines()

 #   for line in configlist:
  #      if "vlan" in line:
   #         count += 1
print("The number of lines is", len(configlist))
print(configlist)
