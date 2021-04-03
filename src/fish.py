#!/usr/bin/env python

print("[PARSE CONFIG] FISH.py")

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import global_constants
import utils

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ['CHAMELEON_CACHE'] = chameleon_cache_path

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

from rosters import registered_rosters

from rosters import brit
brit.roster.register()

"""
from rosters import euro
euro.roster.register()
"""

def get_ships_in_buy_menu_order():
    ships = []
    # first compose the buy menu order list
    buy_menu_sort_order = []
    if repo_vars.get('roster', '*') == '*':
        active_rosters = [roster.id for roster in registered_rosters]
    else:
        active_rosters = [repo_vars['roster']] # make sure it's iterable
    for roster in registered_rosters:
        if roster.id in active_rosters:
            buy_menu_sort_order.extend(roster.buy_menu_sort_order)
            ships.extend(roster.ships_in_buy_menu_order)

    # now guard against any ships missing from buy menu order or vice versa, as that wastes time asking 'wtf?' when they don't appear in game
    ship_id_defender = set([ship.id for ship in ships])
    buy_menu_defender = set(buy_menu_sort_order)
    for id in buy_menu_defender.difference(ship_id_defender):
        utils.echo_message("Warning: ship " + id + " in buy_menu_sort_order, but not found in registered ships")
    for id in ship_id_defender.difference(buy_menu_defender):
        utils.echo_message("Warning: ship " + id + " in ships, but not in buy_menu_sort_order - won't show in game")
    return ships
