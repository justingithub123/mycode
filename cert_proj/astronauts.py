#!/usr/bin/python3
""" application to track who is in space"""

import requests
import pprint
from crayons import blue, red

def main():
    astro = requests.get("http://api.open-notify.org/astros.json").json()
    astronauts = astro["people"]
    
    pprint.pprint(astronauts)

    print(f'There are {astro["number"]} people in space')

    craft_choice = input("Which craft would you like to see? Enter 1 for ISS, or 2 for Tiangong: ")

    # create for loop for astronauts
    for a in astronauts:
        craft_color = blue if a["craft"] == "ISS" else red
        print(f'{a["name"]} is on the {craft_color(a["craft"])}')

if __name__ == "__main__":
    main()

