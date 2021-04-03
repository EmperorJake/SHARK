import global_constants
from ship import ContainerCarrier

ship = ContainerCarrier(id = 'dieze_container_barge',
            numeric_id = 2280,
            title = 'Dieze [Container Barge]',
            capacity_cargo_holds = 350,
            replacement_id = '-none',
            buy_cost = 58,
            fixed_run_cost_factor = 10.0,
            fuel_run_cost_factor = 1.0,
            speed = 25.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = False,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -25], [-14, -45], [-75, -25], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = 35,
            intro_date = 1990,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'CONTAINER_FEEDER',
            vehicle_life = 30,
            gross_tonnage = 800)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
