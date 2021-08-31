import global_constants
from ship import GeneralCargoVessel

ship = GeneralCargoVessel(id = 'munkegrund_freighter',
            numeric_id = 1145,
            title = 'Munkegrund [Freighter]',
            capacity_cargo_holds = 980,
            replacement_id = '-none',
            buy_cost = 86,
            fixed_run_cost_factor = 5.9,
            fuel_run_cost_factor = 1.6,
            speed = 30.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -46], [-61, -30], [-50, -29], [-10, -29], [-14, -58], [-60, -30], [-50, -29], [-6, -23]],
            buy_menu_width = 115,
            loading_speed = 20,
            intro_date = 1978,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'LARGE_COASTER',
            effects = ['EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE, 10, 0, 24'],
            vehicle_life = 40,
            gross_tonnage = 900)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
