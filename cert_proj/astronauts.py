#!/usr/bin/python3
""" application to track who is in space"""

import requests
import pprint

def main():

    astro = requests.get("http://api.open-notify.org/astros.json").json()
    astronauts = astro["people"]
    
    pprint.pprint(astronauts)

    print(f'There are {astro["number"]} people in space')
    
    # create for loop for astronauts
    for a in astronauts:
        print(f'{a["name"]} is on the {a["craft"]}')

if __name__ == "__main__":
    main()

# which craft would you like to see, enter 1 for this enter 2 for this
# for errors could do while loop or program ends
# loop through astronauts, could loop through and sort in a list. For each dict append a name to a list that was created. Would need to initialize lists.# sum number of people on a craft
# crayons for name vs craft
# if {a["craft"}] equals this append to a list then print out list
