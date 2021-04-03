import global_constants
from ship import GeneralCargoVessel

ship = GeneralCargoVessel(id = 'frisco_bay_freighter',
            numeric_id = 1120,
            title = 'Frisco Bay [Freighter]',
            capacity_cargo_holds = 810,
            replacement_id = '-none',
            buy_cost = 72,
            fixed_run_cost_factor = 10.0,
            fuel_run_cost_factor = 1.0,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -45], [-70, -26], [-57, -28], [-17, -25], [-14, -47], [-69, -25], [-57, -28], [-12, -26]],
            buy_menu_width = 119,
            loading_speed = 20,
            intro_date = 1905,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LARGE_COASTER',
            effects = ['EFFECT_SPRITE_STEAM, 0, 0, 29'],
            vehicle_life = 35,
            gross_tonnage = 820)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
