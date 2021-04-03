import global_constants
from ship import GeneralCargoVessel

ship = GeneralCargoVessel(id = 'little_cumbrae_freighter',
            numeric_id = 1100,
            title = 'Little Cumbrae [Freighter]',
            capacity_cargo_holds = 140,
            replacement_id = '-none',
            buy_cost = 12,
            fixed_run_cost_factor = 3.0,
            fuel_run_cost_factor = 2.0,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-84, -25], [-68, -21], [-33, -25], [-14, -40], [-83, -24], [-66, -21], [-32, -23]],
            buy_menu_width = 78,
            loading_speed = 20,
            intro_date = 1860,
            buy_menu_bb_xy = [649, 21],
            str_type_info = 'SMALL_FREIGHTER',
            effects = ['EFFECT_SPRITE_STEAM, 6, 0, 26'],
            vehicle_life = 35,
            gross_tonnage = 100)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
