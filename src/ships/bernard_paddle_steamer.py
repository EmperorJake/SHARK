import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'bernard_paddle_steamer',
            numeric_id = 2020,
            title = 'Bernard [Paddle Steamer]',
            capacity_pax = 300,
            capacity_cargo_holds = 125,
            capacity_mail = 300,
            replacement_id = '-none',
            buy_cost = 32,
            fixed_run_cost_factor = 9.0,
            fuel_run_cost_factor = 1.0,
            speed = 21.0,
            speed_factor_unladen = 1.0,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -54], [-63, -24], [-50, -29], [-10, -28], [-14, -55], [-58, -27], [-50, -29], [-8, -24]],
            buy_menu_width = 89,
            loading_speed = 12,
            intro_date = 1860,
            buy_menu_bb_xy = [626, 26],
            str_type_info = 'PADDLE_STEAMER',
            effects = ['EFFECT_SPRITE_STEAM, 0, 0, 24', 'EFFECT_SPRITE_STEAM, 4, 0, 24'],
            vehicle_life = 40,
            gross_tonnage = 280)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
