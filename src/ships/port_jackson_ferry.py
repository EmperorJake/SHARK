import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'port_jackson_ferry',
            numeric_id = 89,
            title = 'Port Jackson [Catamaran]',
            capacity_pax = 120,
            capacity_cargo_holds = 60,
            capacity_mail = 120,
            replacement_id = '-none',
            buy_cost = 32,
            fixed_run_cost_factor = 9.0,
            fuel_run_cost_factor = 1.0,
            speed = 45.0,
            speed_factor_unladen = 1.0,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -54], [-57, -26], [-35, -29], [-19, -32], [-14, -54], [-58, -32], [-42, -29], [-1, -26]],
            buy_menu_width = 58,
            loading_speed = 20,
            intro_date = 1988,
            buy_menu_bb_xy = [624, 28],
            str_type_info = 'CATAMARAN_FAST_FERRY',
            vehicle_life = 25,
            gross_tonnage = 350)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

