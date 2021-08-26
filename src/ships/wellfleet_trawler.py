import global_constants
from ship import Trawler

ship = Trawler(id = 'wellfleet_trawler',
            numeric_id = 1200,
            title = 'Wellfleet [Trawler]',
            capacity_pax = 18,
            capacity_deck_cargo = 24,
            capacity_mail = 32,
            capacity_fish_holds = 46,
            replacement_id = '-none',
            buy_cost = 5,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 1.0,
            speed = 18.0,
            speed_factor_unladen = 1.15,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 40,
            loading_speed = 15,
            intro_date = 1860,
            buy_menu_bb_xy = [669, 21],
            str_type_info = 'TRAWLER',
            effect_spawn_model = 'EFFECT_SPAWN_MODEL_DIESEL',
            effects = ['EFFECT_SPRITE_DIESEL, 0, 0, 14'],
            vehicle_life = 40,
            gross_tonnage = 40)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
