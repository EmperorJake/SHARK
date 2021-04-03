import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'tiree_vehicle_ferry',
            numeric_id = 49,
            title = 'Tiree [Ferry]',
            capacity_pax = 220,
            capacity_cargo_holds = 110,
            capacity_mail = 220,
            replacement_id = '-none',
            buy_cost = 19,
            fixed_run_cost_factor = 5.0,
            fuel_run_cost_factor = 1.0,
            speed = 21.0,
            speed_factor_unladen = 1.0,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -54], [-61, -28], [-36, -29], [-10, -28], [-14, -54], [-55, -26], [-36, -29], [0, -24]],
            buy_menu_width = 89,
            loading_speed = 35,
            intro_date = 1917,
            buy_menu_bb_xy = [622, 28],
            str_type_info = 'VEHICLE_FERRY',
            vehicle_life = 60,
            gross_tonnage = 500)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
