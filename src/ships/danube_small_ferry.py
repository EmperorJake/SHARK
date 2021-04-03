import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'danube_small_ferry',
            numeric_id = 2010,
            title = 'DANUBE SMALL [Ferry]',
            capacity_pax = 100,
            capacity_cargo_holds = 45,
            capacity_mail = 60,
            replacement_id = '-none',
            buy_cost = 27,
            fixed_run_cost_factor = 5.0,
            fuel_run_cost_factor = 1.0,
            speed = 20.0,
            speed_factor_unladen = 1.0,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 40,
            loading_speed = 30,
            intro_date = 1860,
            buy_menu_bb_xy = [669, 21],
            str_type_info = 'SMALL_FERRY',
            vehicle_life = 40,
            gross_tonnage = 60)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
