import global_constants
from ship import Tanker

ship = Tanker(id = 'huanghai_lng_tanker',
            numeric_id = 1275,
            title = 'Huanghai LNG [Tanker]',
            capacity_cargo_holds = 0,
            capacity_tanks = 1920,
            replacement_id = '-none',
            buy_cost = 140,
            fixed_run_cost_factor = 9.2,
            fuel_run_cost_factor = 2.0,
            speed = 30.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -50], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 40,
            intro_date = 1982,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LARGE_COASTAL_TANKER',
            effects = ['EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE, 16, 0, 27'],
            vehicle_life = 45,
            gross_tonnage = 1340)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
