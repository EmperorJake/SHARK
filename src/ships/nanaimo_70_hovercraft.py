import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'nanaimo_70_hovercraft',
            numeric_id = 1050,
            title = 'Nanaimo 70 [Hovercraft]',
            capacity_pax = 70,
            capacity_cargo_holds = 25,
            capacity_mail = 30,
            replacement_id = '-none',
            buy_cost = 28,
            fixed_run_cost_factor = 12.0,
            fuel_run_cost_factor = 12.0,
            speed = 70.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -40], [-82, -24], [-69, -21], [-29, -24], [-14, -42], [-80, -26], [-68, -21], [-29, -24]],
            buy_menu_width = 52,
            use_legacy_template = False,
            loading_speed = 30,
            intro_date = 1965,
            buy_menu_bb_xy = [668, 21],
            str_type_info = 'HOVERCRAFT_FAST_FERRY',
            vehicle_life = 45,
            gross_tonnage = 30)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
