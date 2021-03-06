# -*- coding: utf-8 -*-
""""
Created on Saturday, January 18, 2020

@author: lieur

This test case sets silver and gold to 0, which in most cases prevent the computer from
buying provinces.  This tests to see if the game ends when one more supply car hits 0 (since
silver and gold are already at 0 and the game ends when 3 supply deck hits 0)
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


# Choose and set supply cards
supply = testUtility.set_supply(box, player_names, nV, nC)

# Initialize the trash
trash = []
# Test silver and gold = 0
supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
supply["Silver"]=[Dominion.Silver()]*0
supply["Gold"]=[Dominion.Gold()]*0

# Construct the Player objects
players = testUtility.set_players(player_names)

# Play the game
testUtility.play_game(supply, supply_order, players, trash)

# Final score
testUtility.display_game_results(players)