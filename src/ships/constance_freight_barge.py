import global_constants
from ship import GeneralCargoVessel

ship = GeneralCargoVessel(id = 'constance_freight_barge',
            numeric_id = 2120,
            title = 'Constance [Freight Barge]',
            capacity_cargo_holds = 240,
            replacement_id = '-none',
            buy_cost = 4,
            fixed_run_cost_factor = 1.0,
            fuel_run_cost_factor = 1.0,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = False,
            offsets = [[-14, -40], [-84, -25], [-68, -21], [-33, -25], [-14, -40], [-83, -24], [-66, -21], [-32, -23]],
            buy_menu_width = 78,
            loading_speed = 20,
            intro_date = 1860,
            buy_menu_bb_xy = [649, 21],
            str_type_info = 'CARGO_VESSEL_INLAND',
            effects = ['EFFECT_SPRITE_STEAM, 6, 0, 13'],
            vehicle_life = 60,
            gross_tonnage = 580)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
