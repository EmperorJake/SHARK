import global_constants
from ship import GeneralCargoVessel

ship = GeneralCargoVessel(id = 'whitgift_freight_barge',
            numeric_id = 1160,
            title = 'Whitgift [Freight Barge]',
            capacity_cargo_holds = 65,
            replacement_id = '-none',
            buy_cost = 4,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 2.0,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = False,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 44,
            loading_speed = 20,
            intro_date = 1860,
            buy_menu_bb_xy = [667, 21],
            str_type_info = 'SMALL_CARGO_VESSEL_INLAND',
            effect_spawn_model = 'EFFECT_SPAWN_MODEL_DIESEL',
            effects = ['EFFECT_SPRITE_DIESEL, 6, 0, 8'],
            vehicle_life = 60,
            gross_tonnage = 60)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
