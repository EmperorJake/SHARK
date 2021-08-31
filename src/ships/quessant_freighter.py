import global_constants
from ship import Ship, GeneralCargoVessel

ship = GeneralCargoVessel(id = 'quessant_freighter',
            numeric_id = 1125,
            title = 'Quessant [Freighter]',
            capacity_cargo_holds = 1012,
            replacement_id = '-none',
            buy_cost = 62,
            fixed_run_cost_factor = 1.0,
            fuel_run_cost_factor = 1.0,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -50], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 20,
            intro_date = 1895,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LARGE_COASTER',
            effects = ['EFFECT_SPRITE_STEAM, 16, 0, 26'],
            vehicle_life = 35,
            gross_tonnage = 1110)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
