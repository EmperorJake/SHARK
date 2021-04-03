import global_constants
from ship import Trawler

ship = Trawler(id = 'cape_spear_trawler',
            numeric_id = 1210,
            title = 'Cape Spear [Trawler]',
            capacity_pax = 40,
            capacity_deck_cargo = 44,
            capacity_mail = 66,
            capacity_fish_holds = 124,
            replacement_id = '-none',
            buy_cost = 7,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 1.0,
            speed = 21.0,
            speed_factor_unladen = 1.15,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 51,
            loading_speed = 15,
            intro_date = 1948,
            buy_menu_bb_xy = [663, 21],
            str_type_info = 'TRAWLER',
            effects = ['EFFECT_SPRITE_DIESEL, 0, 0, 16'],
            vehicle_life = 40,
            gross_tonnage = 84)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
