from roster import Roster

from ships import constance_freight_barge
from ships import danube_better_reefer
from ships import danube_large_ferry
from ships import danube_livestock_barge
from ships import johann_strauss_paddle_steamer
from ships import danube_reefer
from ships import danube_small_ferry
from ships import danube_small_freight_barge
from ships import danube_small_diesel_barge
from ships import danube_trawler
from ships import danube_utility_vessel
from ships import danube_very_large_barge
from ships import danube_very_large_tanker
from ships import dieze_container_barge
from ships import endeavour_utility_catamaran
from ships import feodosiya_hydrofoil
from ships import geneva_freight_barge
from ships import saint_marie_freight_barge
from ships import volgoneft_six_thirty_tanker_barge
from ships import volgoneft_two_seventy_tanker_barge

roster = Roster(id = 'danube',
                numeric_id = 2,
                ships = [danube_utility_vessel,
                         danube_small_ferry,
                         johann_strauss_paddle_steamer,
                         danube_large_ferry,
                         feodosiya_hydrofoil,
                         danube_trawler,
                         endeavour_utility_catamaran,
                         danube_small_freight_barge,
                         saint_marie_freight_barge,
                         danube_small_diesel_barge,
                         constance_freight_barge,
                         geneva_freight_barge,
                         danube_very_large_barge,
                         volgoneft_two_seventy_tanker_barge,
                         volgoneft_six_thirty_tanker_barge,
                         danube_very_large_tanker,
                         danube_reefer,
                         danube_better_reefer,
                         danube_livestock_barge,
                         dieze_container_barge])
