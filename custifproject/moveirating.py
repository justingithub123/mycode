#!/usr/bin/env python3
""" project to rate movie titles """

def main():

    rating = int(input("What rating on a scale of 1-10 would you give Happy Potter? "))

    if rating <= 3:
        message = 'Low'
    elif rating <= 6:
        message = 'Medium'
    elif rating <= 9:
        message = 'High'
    elif rating == 10:
        message = 'Greatest'
    else: 
        message = "Invalid"
    print(message)

main()

