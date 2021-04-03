import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'pegwell_super_4_hovercraft',
            numeric_id = 1060,
            title = 'Pegwell Super 4 [Hovercraft]',
            capacity_pax = 400,
            capacity_cargo_holds = 100,
            capacity_mail = 400,
            replacement_id = '-none',
            buy_cost = 90,
            fixed_run_cost_factor = 14.0,
            fuel_run_cost_factor = 14.0,
            speed = 70.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -40], [-82, -24], [-69, -21], [-29, -24], [-14, -42], [-80, -26], [-68, -21], [-29, -24]],
            buy_menu_width = 54,
            use_legacy_template = False,
            loading_speed = 18,
            intro_date = 1968,
            buy_menu_bb_xy = [660, 21],
            str_type_info = 'HOVERCRAFT_FAST_FERRY',
            vehicle_life = 45,
            gross_tonnage = 120)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
