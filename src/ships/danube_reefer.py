import global_constants
from ship import Reefer

ship = Reefer(id = 'danube_reefer',
            numeric_id = 2210,
            title = 'DANUBE [Reefer]',
            capacity_cargo_holds = 360,
            replacement_id = '-none',
            buy_cost = 85,
            fixed_run_cost_factor = 7.0,
            fuel_run_cost_factor = 1.0,
            speed = 26.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -45], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 20,
            intro_date = 1936,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'REEFER',
            vehicle_life = 35,
            gross_tonnage = 700)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
