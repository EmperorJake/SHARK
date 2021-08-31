import global_constants
from ship import Tanker

ship = Tanker(id = 'la_orchilla_tanker',
            numeric_id = 1270,
            title = 'La Orchilla [Tanker]',
            capacity_cargo_holds = 0,
            capacity_tanks = 920,
            replacement_id = '-none',
            buy_cost = 75,
            fixed_run_cost_factor = 5.0,
            fuel_run_cost_factor = 1.5,
            speed = 26.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -50], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 20,
            intro_date = 1968,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LARGE_COASTER',
            effects = ['EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE, 16, 0, 26'],
            vehicle_life = 35,
            gross_tonnage = 1000)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
