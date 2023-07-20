#!/usr/bin/python3
"""application to track who is in space"""

import requests
import pprint
from crayons import blue, red

def prompt_craft_choice():
    while True:
        craft_choice = input("Which craft would you like to see? Enter 1 for Craft 1 (ISS), 2 for Craft 2 (Tiangong), or 'q' to quit: ")
        if craft_choice.lower() == 'q':
            print("Goodbye")
            exit()
        elif craft_choice == "1":
            return "ISS"
        elif craft_choice == "2":
            return "Tiangong"
        else:
            print("Invalid input. Please select Craft 1 (ISS) or Craft 2 (Tiangong).")

def main():
    try:
        astro = requests.get("http://api.open-notify.org/astros.json", timeout=30).json()
    except requests.Timeout:
        print("Timeout occurred. Please try again later.")
        exit()

    astronauts = astro["people"]

    # Create a list to store astronaut information
    astronaut_info = []

    for a in astronauts:
        astronaut_info.append({"name": a["name"], "craft": a["craft"]})

    # Sort the astronaut_info list first by craft and then by alphabetical order
    astronaut_info.sort(key=lambda x: (x["craft"], x["name"]))

    pprint.pprint(astronaut_info)

    craft_choice = prompt_craft_choice()

    # create for loop for astronauts
    for a in astronaut_info:
        if a["craft"] == craft_choice:
            craft_color = blue if a["craft"] == "ISS" else red
            print(f'{a["name"]} is on the {craft_color(a["craft"])}')

    print(f'There are {astro["number"]} people in space')

if __name__ == "__main__":
    main()

