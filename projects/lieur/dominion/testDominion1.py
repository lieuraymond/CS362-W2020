# -*- coding: utf-8 -*-
""""
Created on Saturday, January 18, 2020

@author: lieur

This test case sets the random supply box to null, meaning only victory cards
and money exist.  This allows us to test the coin buying and victory conditions of
when the provinces are all sold out.  
"""""

import Dominion
import testUtility
import random
from collections import defaultdict

# Get player names
player_names = ["Annie", "*Ben", "*Carla"]

# Set number of curses and victory cards
nV, nC = testUtility.set_vc_number(player_names)

# Define box and supply_order
box, supply_order = testUtility.define_box(nV)

#Test no box
box = {}

# Choose and set supply cards
supply = testUtility.set_supply(box, player_names, nV, nC)

# Initialize the trash
trash = []

# Construct the Player objects
players = testUtility.set_players(player_names)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:

                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
testUtility.display_game_results(players)