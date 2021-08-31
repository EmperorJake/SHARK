import global_constants
from ship import Tanker

ship = Tanker(id = 'roland_tanker',
            numeric_id = 1255,
            title = 'Roland [Tanker]',
            capacity_cargo_holds = 0,
            capacity_tanks = 675,
            replacement_id = '-none',
            buy_cost = 64,
            fixed_run_cost_factor = 12.0,
            fuel_run_cost_factor = 1.1,
            speed = 20.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -42], [-68, -26], [-55, -30], [-16, -26], [-14, -54], [-66, -27], [-55, -30], [-14, -26]],
            buy_menu_width = 115,
            loading_speed = 40,
            intro_date = 1908,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'COASTAL_TANKER',
            effects = ['EFFECT_SPRITE_DIESEL, 12, 0, 18'],
            vehicle_life = 45,
            gross_tonnage = 800)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
