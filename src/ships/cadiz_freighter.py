import global_constants
from ship import GeneralCargoVessel

ship = GeneralCargoVessel(id = 'cadiz_freighter',
            numeric_id = 1130,
            title = 'Cadiz [Freighter]',
            capacity_cargo_holds = 450,
            replacement_id = '-none',
            buy_cost = 40,
            fixed_run_cost_factor = 5.0,
            fuel_run_cost_factor = 2.0,
            speed = 26.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -46], [-61, -30], [-50, -29], [-10, -29], [-14, -58], [-60, -30], [-50, -29], [-6, -23]],
            buy_menu_width = 100,
            loading_speed = 20,
            intro_date = 1970,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'COASTER',
            effects = ['EFFECT_SPRITE_DIESEL, 10, 0, 21'],
            vehicle_life = 40,
            gross_tonnage = 360)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
