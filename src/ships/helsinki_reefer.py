import global_constants
from ship import Reefer

ship = Reefer(id = 'helsinki_reefer',
            numeric_id = 1221,
            title = 'Helsinki [Reefer]',
            capacities_refittable = [300, 600, 1200],
            replacement_id = '-none',
            buy_cost = 90,
            fixed_run_cost_factor = 7.0,
            fuel_run_cost_factor = 1.8,
            speed = 30.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -50], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 20,
            intro_date = 1963,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'REEFER',
            effects = ['EFFECT_SPRITE_DIESEL, 16, 2, 23', 'EFFECT_SPRITE_DIESEL, 16, -2, 23'],
            vehicle_life = 35,
            gross_tonnage = 960)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
