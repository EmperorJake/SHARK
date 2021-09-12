import global_constants
from ship import Trawler

ship = Trawler(id = 'kwangtung_trawler',
            numeric_id = 2050,
            title = 'Kwangtung [Trawler]',
            capacity_pax = 65,
            capacity_deck_cargo = 52,
            capacity_mail = 80,
            capacity_fish_holds = 160,
            replacement_id = '-none',
            buy_cost = 11,
            fixed_run_cost_factor = 3.0,
            fuel_run_cost_factor = 1.0,
            speed = 30.0,
            speed_factor_unladen = 1.15,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 49,
            loading_speed = 15,
            intro_date = 1972,
            buy_menu_bb_xy = [664, 21],
            str_type_info = 'TRAWLER',
            effects = ['EFFECT_SPRITE_DIESEL, 0, 2, 16', 'EFFECT_SPRITE_DIESEL, 0, -2, 16'],
            vehicle_life = 25,
            gross_tonnage = 70)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
