import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'island_trader',
            numeric_id = 1031,
            title = 'Island Trader [Blank]',
            capacity_pax = 360,
            capacity_cargo_holds = 240,
            capacity_mail = 720,
            replacement_id = '-none',
            buy_cost = 39,
            fixed_run_cost_factor = 12.0,
            fuel_run_cost_factor = 1.0,
            speed = 30.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -40], [-84, -22], [-69, -29], [-31, -20], [-14, -40], [-75, -23], [-70, -29], [-10, -18]],
            buy_menu_width = 104,
            loading_speed = 20,
            intro_date = 1930,
            buy_menu_bb_xy = [630, 28],
            str_type_info = 'FAST_PACKET_STEAMER',
            effects = ['EFFECT_SPRITE_DIESEL, 5, 0, 27'],
            vehicle_life = 25,
            gross_tonnage = 460)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
