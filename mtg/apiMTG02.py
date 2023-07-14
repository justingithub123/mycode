#!/usr/bin/env python3
""" API studies"""

from pprint import pprint

import requests

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():

    resp = requests.get(f"{API}sets")

    pprint(resp.json())

if __name__ == "__main__":
    main()
