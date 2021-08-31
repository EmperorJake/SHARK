import global_constants
from ship import Tanker

ship = Tanker(id = 'eddystone_tanker',
            numeric_id = 1245,
            title = 'Eddystone [Tanker]',
            capacity_cargo_holds = 0,
            capacity_tanks = 110,
            replacement_id = '-none',
            buy_cost = 12,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 2.0,
            speed = 26.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 51,
            loading_speed = 20,
            intro_date = 1940,
            buy_menu_bb_xy = [663, 21],
            str_type_info = 'SMALL_TANKER_COASTAL_INLAND',
            effects = ['EFFECT_SPRITE_DIESEL, 4, 0, 18'],
            vehicle_life = 35,
            gross_tonnage = 120)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
