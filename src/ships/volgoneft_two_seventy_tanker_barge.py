import global_constants
from ship import Tanker

# http://en.wikipedia.org/wiki/Vandal_(tanker)

ship = Tanker(id = 'volgoneft_two_seventy_tanker_barge',
            numeric_id = 2250,
            title = 'Volgoneft 270 [Tanker Barge]',
            capacity_cargo_holds = 0,
            capacity_tanks = 270,
            replacement_id = '-none',
            buy_cost = 64,
            fixed_run_cost_factor = 12.0,
            fuel_run_cost_factor = 1.1,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = False,
            offsets = [[-14, -40], [-84, -25], [-68, -21], [-33, -25], [-14, -40], [-83, -24], [-66, -21], [-32, -23]],
            buy_menu_width = 78,
            loading_speed = 40,
            intro_date = 1900,
            buy_menu_bb_xy = [649, 21],
            str_type_info = 'SMALL_TANKER_INLAND',
            effects = ['EFFECT_SPRITE_STEAM, 6, 0, 13'],
            vehicle_life = 45,
            gross_tonnage = 270)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
