from rosters import registered_rosters
import pickle

class Roster(object):
    """
    Rosters compose a set of vehicles which is complete for gameplay.
    """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.numeric_id = kwargs.get('numeric_id')
        self.ships = []
        for ship in [ship.ship for ship in kwargs.get('ships')]:
            self.ships.append(ship)
            ship.roster_id = self.id

    @property
    def buy_menu_sort_order(self):
        return [ship.id for ship in self.ships]

    @property
    def ships_in_buy_menu_order(self):
        for ship in self.ships:
            # if ship won't pickle, then multiprocessing blows up, catching it here is faster and easier
            try:
                pickle.dumps(ship)
            except:
                print("Pickling failed for ship:", ship.id)
                raise
        return self.ships

    def register(roster):
        registered_rosters.append(roster)
