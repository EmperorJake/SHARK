import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

property_to_move = 'graphics_status'
property_to_insert_after = 'gross_tonnage'
line_to_insert = "            vehicle_groups = ['sea'], \n"

import fish

filenames = [ship.id + '.py' for ship in fish.get_ships_in_buy_menu_order()]

def move_property(filename):
    file = open(os.path.join('src','ships',filename),'r')
    content = file.readlines()

    for line in content:
        if property_to_move in line:
            cut_line = line
    content.remove(cut_line)
    """
    for line in content:
        if property_to_insert_after in line:
            line_to_insert_after = line
    insert_position = content.index(line_to_insert_after)
    content.insert(insert_position+1, cut_line)
    """

    file = open(os.path.join('src','ships',filename),'w')
    file.write(''.join(content))
    file.close

def insert_property(filename):
    file = open(os.path.join('src','ships',filename),'r')
    content = file.readlines()

    for line in content:
        if property_to_insert_after in line:
            line_to_insert_after = line
    insert_position = content.index(line_to_insert_after)
    content.insert(insert_position+1, line_to_insert)

    file = open(os.path.join('src','ships',filename),'w')
    file.write(''.join(content))
    file.close


for filename in filenames:
    #pass
    move_property(filename)
    #insert_property(filename)
