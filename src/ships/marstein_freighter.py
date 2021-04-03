import global_constants
from ship import GeneralCargoVessel

ship = GeneralCargoVessel(id = 'marstein_freighter',
            numeric_id = 1170,
            title = 'Marstein [Freighter]',
            capacity_cargo_holds = 270,
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 4.5,
            fuel_run_cost_factor = 1.0,
            speed = 26.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-80, -24], [-66, -21], [-33, -25], [-14, -40], [-78, -26], [-66, -21], [-32, -23]],
            buy_menu_width = 78,
            loading_speed = 20,
            intro_date = 1968,
            buy_menu_bb_xy = [649, 21],
            str_type_info = 'SMALL_FREIGHTER',
            effects = ['EFFECT_SPRITE_DIESEL, 8, 0, 18'],
            vehicle_life = 40,
            gross_tonnage = 270)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
