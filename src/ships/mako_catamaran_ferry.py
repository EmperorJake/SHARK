import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'mako_catamaran_ferry',
            numeric_id = 100,
            title = 'Mako [Fast Ferry]',
            capacity_pax = 760,
            capacity_cargo_holds = 320,
            capacity_mail = 760,
            replacement_id = '-none',
            buy_cost = 160,
            fixed_run_cost_factor = 17.0,
            fuel_run_cost_factor = 1.0,
            speed = 60.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-67, -25], [-59, -29], [-15, -26], [-14, -45], [-67, -26], [-59, -29], [-15, -25]],
            buy_menu_width = 117,
            loading_speed = 20,
            intro_date = 2008,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'CATAMARAN_FAST_FERRY',
            vehicle_life = 30,
            gross_tonnage = 1600)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
