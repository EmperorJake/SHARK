import global_constants
from ship import ContainerReefer

ship = ContainerReefer(id = 'winterhold_container_reefer',
            numeric_id = 1222,
            title = 'Winterhold [Container Reefer]',
            capacities_refittable = [400, 800, 1600],
            replacement_id = '-none',
            buy_cost = 99,
            fixed_run_cost_factor = 11.0,
            fuel_run_cost_factor = 1.8,
            speed = 30.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -50], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 35,
            intro_date = 1990,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'REEFER',
            effects = ['EFFECT_SPRITE_DIESEL, 16, 2, 26', 'EFFECT_SPRITE_DIESEL, 16, -2, 26'],
            vehicle_life = 35,
            gross_tonnage = 960)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
