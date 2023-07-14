#!/usr/bin/python3
""" Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF = "https://www.anapioficeandfire.com/api"

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    gotresp = requests.get(AOIF).json()

    
          
    ## display only the keys within
    ## the dictionary by using dict.keys()
    ## great for seeing what keys are available for lookup
    print(gotresp)
    print(gotresp.keys())

if __name__ == "__main__":
    main()

