import global_constants
from ship import GeneralCargoVessel

ship = GeneralCargoVessel(id = 'altamira_freighter',
            numeric_id = 1110,
            title = 'Altamira [Freighter]',
            capacity_cargo_holds = 360,
            replacement_id = '-none',
            buy_cost = 28,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-15, -38], [-79, -21], [-66, -25], [-38, -22], [-14, -36], [-78, -22], [-68, -25], [-38, -20]],
            buy_menu_width = 94,
            loading_speed = 20,
            intro_date = 1890,
            buy_menu_bb_xy = [646, 25],
            str_type_info = 'COASTER',
            effects = ['EFFECT_SPRITE_STEAM, 8, 0, 24'],
            vehicle_life = 40,
            gross_tonnage = 360)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
