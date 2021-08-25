import global_constants
from ship import GeneralCargoVessel

ship = GeneralCargoVessel(id = 'maspalomas_freighter',
            numeric_id = 1150,
            title = 'Maspalomas [Freighter]',
            capacity_cargo_holds = 2160,
            replacement_id = '-none',
            buy_cost = 100,
            fixed_run_cost_factor = 7.0,
            fuel_run_cost_factor = 1.6,
            speed = 30.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -45], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 20,
            intro_date = 1988,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LARGE_COASTER',
            effects = ['EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE, 16, 0, 29'],
            vehicle_life = 35,
            gross_tonnage = 2140)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
