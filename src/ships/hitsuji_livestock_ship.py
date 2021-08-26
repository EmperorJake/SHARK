import global_constants
from ship import LivestockCarrier

ship = LivestockCarrier(id = 'hitsuji_livestock_ship',
            numeric_id = 1231,
            title = 'Hitsuji [Livestock Ship]',
            capacities_refittable = [350, 700, 1400],
            replacement_id = '-none',
            buy_cost = 63,
            fixed_run_cost_factor = 10.0,
            fuel_run_cost_factor = 1.0,
            speed = 30.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -50], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 20,
            intro_date = 1969,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LIVESTOCK_SHIP',
            effects = ['EFFECT_SPRITE_DIESEL, 16, 2, 23', 'EFFECT_SPRITE_DIESEL, 16, -2, 23'],
            vehicle_life = 35,
            gross_tonnage = 650)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
