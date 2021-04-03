print("[RENDER NML] render_nml.py")

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join('src')) # add to the module search path

import codecs # used for writing files - more unicode friendly than standard open() module

import fish
import utils
import global_constants

from rosters import registered_rosters

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))


def main():
    ships = fish.get_ships_in_buy_menu_order()

    grf_nml = codecs.open(os.path.join('fish.nml'),'w','utf8')
    header_items = ['header', 'cargo_table', 'disable_default_ships']
    for header_item in header_items:
        template = templates[header_item + '.pynml']
        grf_nml.write(utils.unescape_chameleon_output(template(ships=ships, global_constants=global_constants,
                                                        registered_rosters=registered_rosters, utils=utils,
                                                        sys=sys, repo_vars=repo_vars)))

    for ship in set(ships):
        grf_nml.write(utils.unescape_chameleon_output(ship.render()))

    grf_nml.close()

if __name__ == '__main__':
    main()
