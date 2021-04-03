import global_constants
from ship import EdiblesTanker

ship = EdiblesTanker(id = 'provence_edibles_tanker',
            numeric_id = 1280,
            title = 'Provence Edibles [Tanker]',
            capacity_cargo_holds = 0,
            capacity_tanks = 330,
            replacement_id = '-none',
            buy_cost = 28,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 1.8,
            speed = 26.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-80, -24], [-66, -21], [-33, -25], [-14, -40], [-78, -26], [-66, -21], [-32, -23]],
            buy_menu_width = 78,
            loading_speed = 40,
            intro_date = 1965,
            buy_menu_bb_xy = [649, 21],
            str_type_info = 'SMALL_TANKER_COASTAL_INLAND',
            effects = ['EFFECT_SPRITE_DIESEL, 8, 0, 18'],
            vehicle_life = 35,
            gross_tonnage = 350)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
