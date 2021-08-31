import global_constants
from ship import EdiblesTanker

ship = EdiblesTanker(id = 'lorraine_edibles_tanker',
            numeric_id = 1282,
            title = 'Lorraine Edibles [Tanker]',
            capacity_cargo_holds = 0,
            capacity_tanks = 860,
            replacement_id = '-none',
            buy_cost = 83,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 1.8,
            speed = 30.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -50], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 130,
            loading_speed = 40,
            intro_date = 1976,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LARGE_COASTAL_TANKER',
            effects = ['EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE, 16, 0, 26'],
            vehicle_life = 35,
            gross_tonnage = 850)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
