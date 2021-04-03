import global_constants
from ship import Hydrofoil

ship = Hydrofoil(id = 'feodosiya_hydrofoil',
            numeric_id = 2040,
            title = 'Klyazma [Hydrofoil]',
            capacity_pax = 100,
            capacity_cargo_holds = 45,
            capacity_mail = 60,
            replacement_id = '-none',
            buy_cost = 28,
            fixed_run_cost_factor = 5.0,
            fuel_run_cost_factor = 3.0,
            speed = 45.0,
            speed_factor_unladen = 1.0,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -59], [-58, -32], [-36, -31], [-17, -32], [-14, -58], [-55, -26], [-39, -29], [0, -24]],
            buy_menu_width = 64,
            loading_speed = 15,
            intro_date = 1957,
            buy_menu_bb_xy = [625, 28],
            str_type_info = 'HYDROFOIL_FAST_FERRY',
            vehicle_life = 35,
            gross_tonnage = 64)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
