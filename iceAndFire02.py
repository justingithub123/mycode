#!/usr/bin/python3
"""Exploring OpenAPIs with requests with Fire and Ice"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import pprint
import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    ## Send HTTPS GET to the API of ICE and Fire books resource
    gotresp = requests.get(AOIF_BOOKS).json()


    ## print the response
    ## using pretty print so we can read it
    pprint.pprint(gotresp)

if __name__ == "__main__":
    main()

