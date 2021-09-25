import global_constants
from ship import GeneralCargoVessel

ship = GeneralCargoVessel(id = 'lutschine_freight_barge',
            numeric_id = 2135,
            title = 'Lutschine [Freight Barge]',
            capacity_cargo_holds = 295,
            replacement_id = '-none',
            buy_cost = 20,
            fixed_run_cost_factor = 6.0,
            fuel_run_cost_factor = 1.0,
            speed = 21.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = False,
            offsets = [[-14, -42], [-61, -28], [-55, -29], [-10, -28], [-14, -54], [-61, -28], [-55, -29], [-9, -28]],
            buy_menu_width = 94,
            loading_speed = 20,
            intro_date = 1910,
            buy_menu_bb_xy = [620, 21],
            str_type_info = 'CARGO_VESSEL_INLAND',
            effects = ['EFFECT_SPRITE_DIESEL, 6, 0, 13'],
            vehicle_life = 60,
            gross_tonnage = 300)

ship.add_model_variant(intro_date=0,
                       end_date=1960,
                       spritesheet_suffix=0)

ship.add_model_variant(intro_date=1950,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1)

ship.add_model_variant(intro_date=1960,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=2)
