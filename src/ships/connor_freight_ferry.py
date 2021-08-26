import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'connor_freight_ferry',
            numeric_id = 1032,
            title = 'Connor Freight [Ferry]',
            capacity_pax = 320,
            capacity_cargo_holds = 640,
            capacity_mail = 1280,
            replacement_id = '-none',
            buy_cost = 65,
            fixed_run_cost_factor = 16.0,
            fuel_run_cost_factor = 1.0,
            speed = 30.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -50], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 20,
            intro_date = 1960,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'FAST_PACKET_STEAMER',
            effects = ['EFFECT_SPRITE_DIESEL, 16, 2, 23', 'EFFECT_SPRITE_DIESEL, 16, -2, 23'],
            vehicle_life = 40,
            gross_tonnage = 1100)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
