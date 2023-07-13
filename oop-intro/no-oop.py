#!/usr/bin/env python3
""" creating classes example"""

# standard library
import random

def main(): 

    # create lists to store the scores, empty lists for each player
    player1_dice = []
    player2_dice = []

    # running a loop through the ranges 3 times
    for i in range(3):
        player1_dice.append(random.randint(1,6)) 
        player2_dice.append(random.randint(1,6)) 
    print("Player 1 rolled", player1_dice)
    print("Player 2 rolled", player2_dice)

# determine which player won
    if sum(player1_dice) == sum(player2_dice):
      print("Draw")
    elif sum(player1_dice) > sum(player2_dice):
      print("Player 1 wins")
    else:
      print("Player 2 wins")

if __name__ == "__main__":
    main()
