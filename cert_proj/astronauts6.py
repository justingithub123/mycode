#!/usr/bin/python3
""" application to track who is in space"""

import requests
from crayons import blue, red

def prompt_craft_choice():
    while True:
        craft_choice = input("Which craft would you like to see? Enter 1 for Craft 1 (ISS), 2 for Craft 2 (Tiangong), or 'q' to quit: ")
        if craft_choice.lower() == 'q':
            print("Goodbye!")
            exit()
        elif craft_choice == "1":
            return "ISS"
        elif craft_choice == "2":
            return "Tiangong"
        else:
            print("Invalid input. Please select Craft 1 (ISS) or Craft 2 (Tiangong).")

def main():
    try:
        astro = requests.get("http://api.open-notify.org/astros.json", timeout=5).json()
        astronauts = astro["people"]
        num_astronauts = astro["number"]
    except requests.Timeout:
        print("Timeout occurred. Please try again later.")
        exit()

    print(f'There are {num_astronauts} people in space')

    craft_choice = prompt_craft_choice()

    # create for loop for astronauts
    for a in astronauts:
        if a["craft"] == craft_choice:
            craft_color = blue if a["craft"] == "ISS" else red
            print(f'{a["name"]} is on the {craft_color(a["craft"])}')

if __name__ == "__main__":
    main()
