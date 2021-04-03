import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'fastnet_paddle_steamer',
            numeric_id = 1040,
            title = 'Fastnet [Paddle Steamer]',
            capacity_pax = 720,
            capacity_cargo_holds = 250,
            capacity_mail = 320,
            replacement_id = '-none',
            buy_cost = 79,
            fixed_run_cost_factor = 19.0,
            fuel_run_cost_factor = 1.0,
            speed = 28.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -38], [-75, -20], [-67, -28], [-22, -21], [-14, -42], [-75, -21], [-67, -28], [-20, -21]],
            buy_menu_width = 138,
            loading_speed = 12,
            intro_date = 1900,
            buy_menu_bb_xy = [620, 26],
            str_type_info = 'PADDLE_STEAMER',
            effects = ['EFFECT_SPRITE_STEAM, 0, 0, 28', 'EFFECT_SPRITE_STEAM, 4, 0, 28'],
            vehicle_life = 40,
            gross_tonnage = 800)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
