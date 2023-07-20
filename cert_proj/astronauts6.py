#!/usr/bin/python3
""" application to track who and how many in space"""

import requests
from crayons import blue, red

def prompt_craft_choice(): # prompt for which craft
    while True:
        craft_choice = input("Which craft would you like to see? Enter 1 for Craft 1 (ISS), 2 for Craft 2 (Tiangong), or 'q' to quit: ")
        if craft_choice.lower() == 'q':
            print("Goodbye")
            exit() # end program upon q in prompt
        elif craft_choice == "1":
            return "ISS"
        elif craft_choice == "2":
            return "Tiangong"
        else: # error control
            print("Invalid input. Please select Craft 1 (ISS) or Craft 2 (Tiangong).")

def main(): # api pull to json and timeout (suggestion from pylint)
    try:
        astro = requests.get("http://api.open-notify.org/astros.json", timeout=30).json()
        astronauts = astro["people"]
        num_astronauts = astro["number"]
    except requests.Timeout:
        print("Timeout occurred. Please try again later.")
        exit()
   
   # print number of astronauts in space
    print(f'There are {num_astronauts} people in space')

    craft_choice = prompt_craft_choice()

    # create for loop for astronauts
    for a in astronauts:
        if a["craft"] == craft_choice:
            craft_color = blue if a["craft"] == "ISS" else red
            print(f'{a["name"]} is on the {craft_color(a["craft"])}')

if __name__ == "__main__":
    main()
