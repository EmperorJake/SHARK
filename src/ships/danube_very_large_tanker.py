import global_constants
from ship import Tanker

ship = Tanker(id = 'danube_very_large_tanker',
            numeric_id = 2270,
            title = 'DANUBE VERY LARGE [Tanker]',
            capacity_cargo_holds = 0,
            capacity_tanks = 1000,
            replacement_id = '-none',
            buy_cost = 64,
            fixed_run_cost_factor = 12.0,
            fuel_run_cost_factor = 1.1,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -42], [-61, -28], [-55, -29], [-10, -28], [-14, -54], [-61, -28], [-55, -29], [-9, -28]],
            buy_menu_width = 114,
            loading_speed = 40,
            intro_date = 1972,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LARGE_TANKER_COASTAL_INLAND',
            vehicle_life = 45,
            gross_tonnage = 730)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
