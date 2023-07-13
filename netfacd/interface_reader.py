#!/usr/bin/env python3
"""Exploring Network Interfaces with Netifaces"""

#standard library imports

#3rd Party Imports
import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        
        try: 
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
            print(netifaces.ifaddresses(i)[netifaces.AF_INEF:][0]['addr'])
        except: 
            print('Could not collect adapter information')
