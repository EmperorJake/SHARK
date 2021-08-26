# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/SHARK/src/templates/log_tug.pynml'

__tokens = {0: ('${ship.render_debug_info()}\n\n// graphics', 1, 0), 2: ('ship.render_debug_info()', 1, 2), 76: ("python:{'not_moving': 0 ,'moving': 600}", 4, 35), 154: (" python:('28, 89', '113, 66', '138, 48', '113, 66'", 5, 37), 241: ('states', 6, 34), 287: ('python:states[state]', 7, 37), 318: ('spriteset(${ship.id}_ss_not_loaded_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 10}, ${x_y_crops[0]},  -13,  -6, ANIM]\n            [60,  ${y_start + 10}, ${x_y_crops[1]}, -124,   5, ANIM]\n            [186, ${y_start + 10}, ${x_y_crops[2]}, -124, -28, ANIM]\n            [328, ${y_start + 10}, ${x_y_crops[3]},  -76, -37, ANIM]\n            [454, ${y_start + 10}, ${x_y_crops[0]},  -14, -76, ANIM]\n            [494, ${y_start + 10}, ${x_y_crops[1]},  -34, -38, ANIM]\n            [620, ${y_start + 10}, ${x_y_crops[2]},  -15, -28, ANIM]\n            [762, ${y_start + 10}, ${x_y_crops[3]},   15,   6, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_1_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 110}, ${x_y_crops[0]},  -13, -14, ANIM]\n            [60,  ${y_start + 110}, ${x_y_crops[1]}, -118,   1, ANIM]\n            [186, ${y_start + 110}, ${x_y_crops[2]}, -112, -28, ANIM]\n            [328, ${y_start + 110}, ${x_y_crops[3]},  -64, -32, ANIM]\n            [454, ${y_start + 110}, ${x_y_crops[0]},  -14, -65, ANIM]\n            [494, ${y_start + 110}, ${x_y_crops[1]},  -45, -32, ANIM]\n            [620, ${y_start + 110}, ${x_y_crops[2]},  -26, -28, ANIM]\n            [762, ${y_start + 110}, ${x_y_crops[3]},    2,   0, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_2_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 210}, ${x_y_crops[0]},  -13, -21, ANIM]\n            [60,  ${y_start + 210}, ${x_y_crops[1]}, -107,  -4, ANIM]\n            [186, ${y_start + 210}, ${x_y_crops[2]}, -100, -28, ANIM]\n            [328, ${y_start + 210}, ${x_y_crops[3]},  -59, -30, ANIM]\n            [454, ${y_start + 210}, ${x_y_crops[0]},  -14, -57, ANIM]\n            [494, ${y_start + 210}, ${x_y_crops[1]},  -53, -30, ANIM]\n            [620, ${y_start + 210}, ${x_y_crops[2]},  -49, -28, ANIM]\n            [762, ${y_start + 210}, ${x_y_crops[3]},   -4,  -4, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_3_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 310}, ${x_y_crops[0]},  -13, -29, ANIM]\n            [60,  ${y_start + 310}, ${x_y_crops[1]}, -102,  -8, ANIM]\n            [186, ${y_start + 310}, ${x_y_crops[2]},  -84, -28, ANIM]\n            [328, ${y_start + 310}, ${x_y_crops[3]},  -48, -26, ANIM]\n            [454, ${y_start + 310}, ${x_y_crops[0]},  -14, -47, ANIM]\n            [494, ${y_start + 310}, ${x_y_crops[1]},  -60, -25, ANIM]\n            [620, ${y_start + 310}, ${x_y_crops[2]},  -50, -28, ANIM]\n            [762, ${y_start + 310}, ${x_y_crops[3]},   -7,  -6, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_4_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 410}, ${x_y_crops[0]},  -13, -35, ANIM]\n            [60,  ${y_start + 410}, ${x_y_crops[1]},  -97, -10, ANIM]\n            [186, ${y_start + 410}, ${x_y_crops[2]},  -69, -28, ANIM]\n            [328, ${y_start + 410}, ${x_y_crops[3]},  -45, -22, ANIM]\n            [454, ${y_start + 410}, ${x_y_crops[0]},  -14, -45, ANIM]\n            [494, ${y_start + 410}, ${x_y_crops[1]},  -66, -22, ANIM]\n            [620, ${y_start + 410}, ${x_y_crops[2]},  -61, -28, ANIM]\n            [762, ${y_start + 410}, ${x_y_crops[3]},  -15, -10, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_5_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 510}, ${x_y_crops[0]},  -13, -41, ANIM]\n            [60,  ${y_start + 510}, ${x_y_crops[1]},  -90, -13, ANIM]\n            [186, ${y_start + 510}, ${x_y_crops[2]},  -65, -28, ANIM]\n            [328, ${y_start + 510}, ${x_y_crops[3]},  -40, -19, ANIM]\n            [454, ${y_start + 510}, ${x_y_crops[0]},  -14, -42, ANIM]\n            [494, ${y_start + 510}, ${x_y_crops[1]},  -75, -17, ANIM]\n            [620, ${y_start + 510}, ${x_y_crops[2]},  -68, -28, ANIM]\n            [762, ${y_start + 510}, ${x_y_crops[3]},  -22, -13, ANIM]\n        }', 8, 8), 330: ('ship.id', 8, 20), 355: ('state', 8, 45), 379: ('ship.id', 8, 69), 418: ('y_start + 10', 9, 20), 435: ('x_y_crops[0]', 9, 37), 487: ('y_start + 10', 10, 20), 504: ('x_y_crops[1]', 10, 37), 556: ('y_start + 10', 11, 20), 573: ('x_y_crops[2]', 11, 37), 625: ('y_start + 10', 12, 20), 642: ('x_y_crops[3]', 12, 37), 694: ('y_start + 10', 13, 20), 711: ('x_y_crops[0]', 13, 37), 763: ('y_start + 10', 14, 20), 780: ('x_y_crops[1]', 14, 37), 832: ('y_start + 10', 15, 20), 849: ('x_y_crops[2]', 15, 37), 901: ('y_start + 10', 16, 20), 918: ('x_y_crops[3]', 16, 37), 980: ('ship.id', 18, 20), 1001: ('state', 18, 41), 1025: ('ship.id', 18, 65), 1064: ('y_start + 110', 19, 20), 1082: ('x_y_crops[0]', 19, 38), 1134: ('y_start + 110', 20, 20), 1152: ('x_y_crops[1]', 20, 38), 1204: ('y_start + 110', 21, 20), 1222: ('x_y_crops[2]', 21, 38), 1274: ('y_start + 110', 22, 20), 1292: ('x_y_crops[3]', 22, 38), 1344: ('y_start + 110', 23, 20), 1362: ('x_y_crops[0]', 23, 38), 1414: ('y_start + 110', 24, 20), 1432: ('x_y_crops[1]', 24, 38), 1484: ('y_start + 110', 25, 20), 1502: ('x_y_crops[2]', 25, 38), 1554: ('y_start + 110', 26, 20), 1572: ('x_y_crops[3]', 26, 38), 1634: ('ship.id', 28, 20), 1655: ('state', 28, 41), 1679: ('ship.id', 28, 65), 1718: ('y_start + 210', 29, 20), 1736: ('x_y_crops[0]', 29, 38), 1788: ('y_start + 210', 30, 20), 1806: ('x_y_crops[1]', 30, 38), 1858: ('y_start + 210', 31, 20), 1876: ('x_y_crops[2]', 31, 38), 1928: ('y_start + 210', 32, 20), 1946: ('x_y_crops[3]', 32, 38), 1998: ('y_start + 210', 33, 20), 2016: ('x_y_crops[0]', 33, 38), 2068: ('y_start + 210', 34, 20), 2086: ('x_y_crops[1]', 34, 38), 2138: ('y_start + 210', 35, 20), 2156: ('x_y_crops[2]', 35, 38), 2208: ('y_start + 210', 36, 20), 2226: ('x_y_crops[3]', 36, 38), 2288: ('ship.id', 38, 20), 2309: ('state', 38, 41), 2333: ('ship.id', 38, 65), 2372: ('y_start + 310', 39, 20), 2390: ('x_y_crops[0]', 39, 38), 2442: ('y_start + 310', 40, 20), 2460: ('x_y_crops[1]', 40, 38), 2512: ('y_start + 310', 41, 20), 2530: ('x_y_crops[2]', 41, 38), 2582: ('y_start + 310', 42, 20), 2600: ('x_y_crops[3]', 42, 38), 2652: ('y_start + 310', 43, 20), 2670: ('x_y_crops[0]', 43, 38), 2722: ('y_start + 310', 44, 20), 2740: ('x_y_crops[1]', 44, 38), 2792: ('y_start + 310', 45, 20), 2810: ('x_y_crops[2]', 45, 38), 2862: ('y_start + 310', 46, 20), 2880: ('x_y_crops[3]', 46, 38), 2942: ('ship.id', 48, 20), 2963: ('state', 48, 41), 2987: ('ship.id', 48, 65), 3026: ('y_start + 410', 49, 20), 3044: ('x_y_crops[0]', 49, 38), 3096: ('y_start + 410', 50, 20), 3114: ('x_y_crops[1]', 50, 38), 3166: ('y_start + 410', 51, 20), 3184: ('x_y_crops[2]', 51, 38), 3236: ('y_start + 410', 52, 20), 3254: ('x_y_crops[3]', 52, 38), 3306: ('y_start + 410', 53, 20), 3324: ('x_y_crops[0]', 53, 38), 3376: ('y_start + 410', 54, 20), 3394: ('x_y_crops[1]', 54, 38), 3446: ('y_start + 410', 55, 20), 3464: ('x_y_crops[2]', 55, 38), 3516: ('y_start + 410', 56, 20), 3534: ('x_y_crops[3]', 56, 38), 3596: ('ship.id', 58, 20), 3617: ('state', 58, 41), 3641: ('ship.id', 58, 65), 3680: ('y_start + 510', 59, 20), 3698: ('x_y_crops[0]', 59, 38), 3750: ('y_start + 510', 60, 20), 3768: ('x_y_crops[1]', 60, 38), 3820: ('y_start + 510', 61, 20), 3838: ('x_y_crops[2]', 61, 38), 3890: ('y_start + 510', 62, 20), 3908: ('x_y_crops[3]', 62, 38), 3960: ('y_start + 510', 63, 20), 3978: ('x_y_crops[0]', 63, 38), 4030: ('y_start + 510', 64, 20), 4048: ('x_y_crops[1]', 64, 38), 4100: ('y_start + 510', 65, 20), 4118: ('x_y_crops[2]', 65, 38), 4170: ('y_start + 510', 66, 20), 4188: ('x_y_crops[3]', 66, 38), 4276: ("spritegroup ${ship.id}_sg_refit_0_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_0_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_0, current_speed) {\n    0: return ${ship.id}_sg_refit_0_not_moving;\n    return ${ship.id}_sg_refit_0_moving;\n}\n\nspritegroup ${ship.id}_sg_refit_1_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n        ${ship.id}_ss_load_2_moving,\n        ${ship.id}_ss_load_3_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_1_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_1, current_speed) {\n    0: return ${ship.id}_sg_refit_1_not_moving;\n    return ${ship.id}_sg_refit_1_moving;\n}\n\nspritegroup ${ship.id}_sg_refit_2_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n        ${ship.id}_ss_load_2_moving,\n        ${ship.id}_ss_load_3_moving,\n        ${ship.id}_ss_load_4_moving,\n        ${ship.id}_ss_load_5_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_2_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n        ${ship.id}_ss_load_4_not_moving,\n        ${ship.id}_ss_load_5_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n        ${ship.id}_ss_load_4_not_moving,\n        ${ship.id}_ss_load_5_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_2, current_speed) {\n    0: return ${ship.id}_sg_refit_2_not_moving;\n    return ${ship.id}_sg_refit_2_moving;\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, cargo_subtype) {\n    0: return ${ship.id}_switch_graphics_refit_0;\n    1: return ${ship.id}_switch_graphics_refit_1;\n    2: return ${ship.id}_switch_graphics_refit_2;\n    return ${ship.id}_switch_graphics_refit_0;\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n    ];\n}\n\n\n// -- set speed a little higher than rated speed when unladen -- //", 71, 0), 4290: ('ship.id', 71, 14), 4344: ('ship.id', 73, 10), 4385: ('ship.id', 74, 10), 4526: ('ship.id', 77, 10), 4581: ('ship.id', 81, 14), 4639: ('ship.id', 83, 10), 4684: ('ship.id', 84, 10), 4747: ('ship.id', 87, 10), 4792: ('ship.id', 88, 10), 4861: ('ship.id', 92, 28), 4928: ('ship.id', 93, 16), 4973: ('ship.id', 94, 13), 5018: ('ship.id', 97, 14), 5072: ('ship.id', 99, 10), 5113: ('ship.id', 100, 10), 5150: ('ship.id', 101, 10), 5187: ('ship.id', 102, 10), 5328: ('ship.id', 105, 10), 5383: ('ship.id', 109, 14), 5441: ('ship.id', 111, 10), 5486: ('ship.id', 112, 10), 5527: ('ship.id', 113, 10), 5568: ('ship.id', 114, 10), 5631: ('ship.id', 117, 10), 5676: ('ship.id', 118, 10), 5717: ('ship.id', 119, 10), 5758: ('ship.id', 120, 10), 5827: ('ship.id', 124, 28), 5894: ('ship.id', 125, 16), 5939: ('ship.id', 126, 13), 5984: ('ship.id', 129, 14), 6038: ('ship.id', 131, 10), 6079: ('ship.id', 132, 10), 6116: ('ship.id', 133, 10), 6153: ('ship.id', 134, 10), 6190: ('ship.id', 135, 10), 6227: ('ship.id', 136, 10), 6368: ('ship.id', 139, 10), 6423: ('ship.id', 143, 14), 6481: ('ship.id', 145, 10), 6526: ('ship.id', 146, 10), 6567: ('ship.id', 147, 10), 6608: ('ship.id', 148, 10), 6649: ('ship.id', 149, 10), 6690: ('ship.id', 150, 10), 6753: ('ship.id', 153, 10), 6798: ('ship.id', 154, 10), 6839: ('ship.id', 155, 10), 6880: ('ship.id', 156, 10), 6921: ('ship.id', 157, 10), 6962: ('ship.id', 158, 10), 7031: ('ship.id', 162, 28), 7098: ('ship.id', 163, 16), 7143: ('ship.id', 164, 13), 7202: ('ship.id', 167, 28), 7261: ('ship.id', 168, 16), 7311: ('ship.id', 169, 16), 7361: ('ship.id', 170, 16), 7408: ('ship.id', 171, 13), 7459: ('ship.id', 174, 14), 7507: ('ship.id', 176, 10), 7574: ('ship.id', 179, 10), 7720: ('python:range(3)', 185, 32), 7742: ('switch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount_${speed_factor}, cargo_count*100/cargo_capacity) {\n        0 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[0]};\n        1..100 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[4]}; // log tug is binary: loaded or unloaded; no intermediate fractional speeds\n        return 0; // should never reach this result, make it show up as a problem\n    }', 186, 4), 7770: ('ship.id', 186, 32), 7818: ('speed_factor', 186, 80), 7881: ('ship.get_speeds_adjusted_for_load_amount(speed_factor)[0]', 187, 14), 7960: ('ship.get_speeds_adjusted_for_load_amount(speed_factor)[4]', 188, 19), 8197: ('switch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount, param_adjust_ship_speed) {\n    0: ${ship.id}_switch_speed_varies_with_load_amount_0;\n    1: ${ship.id}_switch_speed_varies_with_load_amount_1;\n    2: ${ship.id}_switch_speed_varies_with_load_amount_2;\n}\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_purchase_speed, param_adjust_ship_speed) {\n    0: ${ship.get_speeds_adjusted_for_load_amount(0)[4]};\n    1: ${ship.get_speeds_adjusted_for_load_amount(1)[4]};\n    2: ${ship.get_speeds_adjusted_for_load_amount(2)[4]};\n}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}', 192, 0), 8225: ('ship.id', 192, 28), 8308: ('ship.id', 193, 9), 8366: ('ship.id', 194, 9), 8424: ('ship.id', 195, 9), 8503: ('ship.id', 197, 28), 8571: ('ship.get_speeds_adjusted_for_load_amount(0)[4]', 198, 9), 8629: ('ship.get_speeds_adjusted_for_load_amount(1)[4]', 199, 9), 8687: ('ship.get_speeds_adjusted_for_load_amount(2)[4]', 200, 9), 8741: ('ship.render_cargo_capacity()', 203, 2), 8774: ('ship.render_properties()', 205, 2)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_140319257121456 = {}

import re
import functools
from itertools import chain as __chain
from sys import intern
__default = intern('__default__')
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Interpolation value=<Substitution '${ship.render_debug_info()}\n\n// graphics\n' (1:0)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9e9f72c250> -> __content_140319262073200
            __token = 0
            __token = 2
            __content_140319262073200 = _lookup_attr(getitem('ship'), 'render_debug_info')()
            __content_140319262073200 = __quote(__content_140319262073200, '\x00', '&#0;', None, None)
            __content_140319262073200 = ('%s%s' % ((__content_140319262073200 if (__content_140319262073200 is not None) else ''), '\n\n// graphics\n', ))
            if (__content_140319262073200 is None):
                pass
            else:
                if (__content_140319262073200 is None):
                    __content_140319262073200 = None
                else:
                    __tt = type(__content_140319262073200)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140319262073200 = str(__content_140319262073200)
                    else:
                        if (__tt is bytes):
                            __content_140319262073200 = decode(__content_140319262073200)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140319262073200 = __content_140319262073200.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140319262073200)
                                    __content_140319262073200 = (str(__content_140319262073200) if (__content_140319262073200 is __converted) else __converted)
                                else:
                                    __content_140319262073200 = __content_140319262073200()
            if (__content_140319262073200 is not None):
                __append(__content_140319262073200)

            # <Static value=<_ast.Dict object at 0x7f9e9f79d2b0> name=None at 7f9e9f79d160> -> __attrs_140319256659424
            __attrs_140319256659424 = _static_140319257121456
            __backup_states_140319267640656 = get('states', __marker)

            # <Value "python:{'not_moving': 0 ,'moving': 600}" (4:35)> -> __value
            __token = 76
            __value = {'not_moving': 0, 'moving': 600, }
            econtext['states'] = __value
            __backup_x_y_crops_140319267640704 = get('x_y_crops', __marker)

            # <Value "python:('28, 89', '113, 66', '138, 48', '113, 66')" (5:37)> -> __value
            __token = 154
            __value = ('28, 89', '113, 66', '138, 48', '113, 66', )
            econtext['x_y_crops'] = __value
            __backup_state_140319267640800 = get('state', __marker)

            # <Value 'states' (6:34)> -> __iterator
            __token = 241
            __iterator = getitem('states')
            (__iterator, ____index_140319256660048, ) = getitem('repeat')('state', __iterator)
            econtext['state'] = None
            for __item in __iterator:
                econtext['state'] = __item
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f9e9f79d2b0> name=None at 7f9e9f79d160> -> __attrs_140319256660912
                __attrs_140319256660912 = _static_140319257121456
                __backup_y_start_140319267640896 = get('y_start', __marker)

                # <Value 'python:states[state]' (7:37)> -> __value
                __token = 287
                __value = getitem('states')[getitem('state')]
                econtext['y_start'] = __value

                # <Interpolation value=<Substitution '\n        spriteset(${ship.id}_ss_not_loaded_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 10}, ${x_y_crops[0]},  -13,  -6, ANIM]\n            [60,  ${y_start + 10}, ${x_y_crops[1]}, -124,   5, ANIM]\n            [186, ${y_start + 10}, ${x_y_crops[2]}, -124, -28, ANIM]\n            [328, ${y_start + 10}, ${x_y_crops[3]},  -76, -37, ANIM]\n            [454, ${y_start + 10}, ${x_y_crops[0]},  -14, -76, ANIM]\n            [494, ${y_start + 10}, ${x_y_crops[1]},  -34, -38, ANIM]\n            [620, ${y_start + 10}, ${x_y_crops[2]},  -15, -28, ANIM]\n            [762, ${y_start + 10}, ${x_y_crops[3]},   15,   6, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_1_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 110}, ${x_y_crops[0]},  -13, -14, ANIM]\n            [60,  ${y_start + 110}, ${x_y_crops[1]}, -118,   1, ANIM]\n            [186, ${y_start + 110}, ${x_y_crops[2]}, -112, -28, ANIM]\n            [328, ${y_start + 110}, ${x_y_crops[3]},  -64, -32, ANIM]\n            [454, ${y_start + 110}, ${x_y_crops[0]},  -14, -65, ANIM]\n            [494, ${y_start + 110}, ${x_y_crops[1]},  -45, -32, ANIM]\n            [620, ${y_start + 110}, ${x_y_crops[2]},  -26, -28, ANIM]\n            [762, ${y_start + 110}, ${x_y_crops[3]},    2,   0, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_2_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 210}, ${x_y_crops[0]},  -13, -21, ANIM]\n            [60,  ${y_start + 210}, ${x_y_crops[1]}, -107,  -4, ANIM]\n            [186, ${y_start + 210}, ${x_y_crops[2]}, -100, -28, ANIM]\n            [328, ${y_start + 210}, ${x_y_crops[3]},  -59, -30, ANIM]\n            [454, ${y_start + 210}, ${x_y_crops[0]},  -14, -57, ANIM]\n            [494, ${y_start + 210}, ${x_y_crops[1]},  -53, -30, ANIM]\n            [620, ${y_start + 210}, ${x_y_crops[2]},  -49, -28, ANIM]\n            [762, ${y_start + 210}, ${x_y_crops[3]},   -4,  -4, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_3_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 310}, ${x_y_crops[0]},  -13, -29, ANIM]\n            [60,  ${y_start + 310}, ${x_y_crops[1]}, -102,  -8, ANIM]\n            [186, ${y_start + 310}, ${x_y_crops[2]},  -84, -28, ANIM]\n            [328, ${y_start + 310}, ${x_y_crops[3]},  -48, -26, ANIM]\n            [454, ${y_start + 310}, ${x_y_crops[0]},  -14, -47, ANIM]\n            [494, ${y_start + 310}, ${x_y_crops[1]},  -60, -25, ANIM]\n            [620, ${y_start + 310}, ${x_y_crops[2]},  -50, -28, ANIM]\n            [762, ${y_start + 310}, ${x_y_crops[3]},   -7,  -6, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_4_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 410}, ${x_y_crops[0]},  -13, -35, ANIM]\n            [60,  ${y_start + 410}, ${x_y_crops[1]},  -97, -10, ANIM]\n            [186, ${y_start + 410}, ${x_y_crops[2]},  -69, -28, ANIM]\n            [328, ${y_start + 410}, ${x_y_crops[3]},  -45, -22, ANIM]\n            [454, ${y_start + 410}, ${x_y_crops[0]},  -14, -45, ANIM]\n            [494, ${y_start + 410}, ${x_y_crops[1]},  -66, -22, ANIM]\n            [620, ${y_start + 410}, ${x_y_crops[2]},  -61, -28, ANIM]\n            [762, ${y_start + 410}, ${x_y_crops[3]},  -15, -10, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_5_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 510}, ${x_y_crops[0]},  -13, -41, ANIM]\n            [60,  ${y_start + 510}, ${x_y_crops[1]},  -90, -13, ANIM]\n            [186, ${y_start + 510}, ${x_y_crops[2]},  -65, -28, ANIM]\n            [328, ${y_start + 510}, ${x_y_crops[3]},  -40, -19, ANIM]\n            [454, ${y_start + 510}, ${x_y_crops[0]},  -14, -42, ANIM]\n            [494, ${y_start + 510}, ${x_y_crops[1]},  -75, -17, ANIM]\n            [620, ${y_start + 510}, ${x_y_crops[2]},  -68, -28, ANIM]\n            [762, ${y_start + 510}, ${x_y_crops[3]},  -22, -13, ANIM]\n        }\n    ' (7:59)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9e9f72cdc0> -> __content_140319262073200
                __token = 318
                __token = 330
                __content_140319262073200 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200 = __quote(__content_140319262073200, '\x00', '&#0;', None, None)
                __token = 355
                __content_140319262073200_353 = getitem('state')
                __content_140319262073200_353 = __quote(__content_140319262073200_353, '\x00', '&#0;', None, None)
                __token = 379
                __content_140319262073200_377 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200_377 = __quote(__content_140319262073200_377, '\x00', '&#0;', None, None)
                __token = 418
                __content_140319262073200_416 = (getitem('y_start') + 10)
                __content_140319262073200_416 = __quote(__content_140319262073200_416, '\x00', '&#0;', None, None)
                __token = 435
                __content_140319262073200_433 = getitem('x_y_crops')[0]
                __content_140319262073200_433 = __quote(__content_140319262073200_433, '\x00', '&#0;', None, None)
                __token = 487
                __content_140319262073200_485 = (getitem('y_start') + 10)
                __content_140319262073200_485 = __quote(__content_140319262073200_485, '\x00', '&#0;', None, None)
                __token = 504
                __content_140319262073200_502 = getitem('x_y_crops')[1]
                __content_140319262073200_502 = __quote(__content_140319262073200_502, '\x00', '&#0;', None, None)
                __token = 556
                __content_140319262073200_554 = (getitem('y_start') + 10)
                __content_140319262073200_554 = __quote(__content_140319262073200_554, '\x00', '&#0;', None, None)
                __token = 573
                __content_140319262073200_571 = getitem('x_y_crops')[2]
                __content_140319262073200_571 = __quote(__content_140319262073200_571, '\x00', '&#0;', None, None)
                __token = 625
                __content_140319262073200_623 = (getitem('y_start') + 10)
                __content_140319262073200_623 = __quote(__content_140319262073200_623, '\x00', '&#0;', None, None)
                __token = 642
                __content_140319262073200_640 = getitem('x_y_crops')[3]
                __content_140319262073200_640 = __quote(__content_140319262073200_640, '\x00', '&#0;', None, None)
                __token = 694
                __content_140319262073200_692 = (getitem('y_start') + 10)
                __content_140319262073200_692 = __quote(__content_140319262073200_692, '\x00', '&#0;', None, None)
                __token = 711
                __content_140319262073200_709 = getitem('x_y_crops')[0]
                __content_140319262073200_709 = __quote(__content_140319262073200_709, '\x00', '&#0;', None, None)
                __token = 763
                __content_140319262073200_761 = (getitem('y_start') + 10)
                __content_140319262073200_761 = __quote(__content_140319262073200_761, '\x00', '&#0;', None, None)
                __token = 780
                __content_140319262073200_778 = getitem('x_y_crops')[1]
                __content_140319262073200_778 = __quote(__content_140319262073200_778, '\x00', '&#0;', None, None)
                __token = 832
                __content_140319262073200_830 = (getitem('y_start') + 10)
                __content_140319262073200_830 = __quote(__content_140319262073200_830, '\x00', '&#0;', None, None)
                __token = 849
                __content_140319262073200_847 = getitem('x_y_crops')[2]
                __content_140319262073200_847 = __quote(__content_140319262073200_847, '\x00', '&#0;', None, None)
                __token = 901
                __content_140319262073200_899 = (getitem('y_start') + 10)
                __content_140319262073200_899 = __quote(__content_140319262073200_899, '\x00', '&#0;', None, None)
                __token = 918
                __content_140319262073200_916 = getitem('x_y_crops')[3]
                __content_140319262073200_916 = __quote(__content_140319262073200_916, '\x00', '&#0;', None, None)
                __token = 980
                __content_140319262073200_978 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200_978 = __quote(__content_140319262073200_978, '\x00', '&#0;', None, None)
                __token = 1001
                __content_140319262073200_999 = getitem('state')
                __content_140319262073200_999 = __quote(__content_140319262073200_999, '\x00', '&#0;', None, None)
                __token = 1025
                __content_140319262073200_1023 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200_1023 = __quote(__content_140319262073200_1023, '\x00', '&#0;', None, None)
                __token = 1064
                __content_140319262073200_1062 = (getitem('y_start') + 110)
                __content_140319262073200_1062 = __quote(__content_140319262073200_1062, '\x00', '&#0;', None, None)
                __token = 1082
                __content_140319262073200_1080 = getitem('x_y_crops')[0]
                __content_140319262073200_1080 = __quote(__content_140319262073200_1080, '\x00', '&#0;', None, None)
                __token = 1134
                __content_140319262073200_1132 = (getitem('y_start') + 110)
                __content_140319262073200_1132 = __quote(__content_140319262073200_1132, '\x00', '&#0;', None, None)
                __token = 1152
                __content_140319262073200_1150 = getitem('x_y_crops')[1]
                __content_140319262073200_1150 = __quote(__content_140319262073200_1150, '\x00', '&#0;', None, None)
                __token = 1204
                __content_140319262073200_1202 = (getitem('y_start') + 110)
                __content_140319262073200_1202 = __quote(__content_140319262073200_1202, '\x00', '&#0;', None, None)
                __token = 1222
                __content_140319262073200_1220 = getitem('x_y_crops')[2]
                __content_140319262073200_1220 = __quote(__content_140319262073200_1220, '\x00', '&#0;', None, None)
                __token = 1274
                __content_140319262073200_1272 = (getitem('y_start') + 110)
                __content_140319262073200_1272 = __quote(__content_140319262073200_1272, '\x00', '&#0;', None, None)
                __token = 1292
                __content_140319262073200_1290 = getitem('x_y_crops')[3]
                __content_140319262073200_1290 = __quote(__content_140319262073200_1290, '\x00', '&#0;', None, None)
                __token = 1344
                __content_140319262073200_1342 = (getitem('y_start') + 110)
                __content_140319262073200_1342 = __quote(__content_140319262073200_1342, '\x00', '&#0;', None, None)
                __token = 1362
                __content_140319262073200_1360 = getitem('x_y_crops')[0]
                __content_140319262073200_1360 = __quote(__content_140319262073200_1360, '\x00', '&#0;', None, None)
                __token = 1414
                __content_140319262073200_1412 = (getitem('y_start') + 110)
                __content_140319262073200_1412 = __quote(__content_140319262073200_1412, '\x00', '&#0;', None, None)
                __token = 1432
                __content_140319262073200_1430 = getitem('x_y_crops')[1]
                __content_140319262073200_1430 = __quote(__content_140319262073200_1430, '\x00', '&#0;', None, None)
                __token = 1484
                __content_140319262073200_1482 = (getitem('y_start') + 110)
                __content_140319262073200_1482 = __quote(__content_140319262073200_1482, '\x00', '&#0;', None, None)
                __token = 1502
                __content_140319262073200_1500 = getitem('x_y_crops')[2]
                __content_140319262073200_1500 = __quote(__content_140319262073200_1500, '\x00', '&#0;', None, None)
                __token = 1554
                __content_140319262073200_1552 = (getitem('y_start') + 110)
                __content_140319262073200_1552 = __quote(__content_140319262073200_1552, '\x00', '&#0;', None, None)
                __token = 1572
                __content_140319262073200_1570 = getitem('x_y_crops')[3]
                __content_140319262073200_1570 = __quote(__content_140319262073200_1570, '\x00', '&#0;', None, None)
                __token = 1634
                __content_140319262073200_1632 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200_1632 = __quote(__content_140319262073200_1632, '\x00', '&#0;', None, None)
                __token = 1655
                __content_140319262073200_1653 = getitem('state')
                __content_140319262073200_1653 = __quote(__content_140319262073200_1653, '\x00', '&#0;', None, None)
                __token = 1679
                __content_140319262073200_1677 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200_1677 = __quote(__content_140319262073200_1677, '\x00', '&#0;', None, None)
                __token = 1718
                __content_140319262073200_1716 = (getitem('y_start') + 210)
                __content_140319262073200_1716 = __quote(__content_140319262073200_1716, '\x00', '&#0;', None, None)
                __token = 1736
                __content_140319262073200_1734 = getitem('x_y_crops')[0]
                __content_140319262073200_1734 = __quote(__content_140319262073200_1734, '\x00', '&#0;', None, None)
                __token = 1788
                __content_140319262073200_1786 = (getitem('y_start') + 210)
                __content_140319262073200_1786 = __quote(__content_140319262073200_1786, '\x00', '&#0;', None, None)
                __token = 1806
                __content_140319262073200_1804 = getitem('x_y_crops')[1]
                __content_140319262073200_1804 = __quote(__content_140319262073200_1804, '\x00', '&#0;', None, None)
                __token = 1858
                __content_140319262073200_1856 = (getitem('y_start') + 210)
                __content_140319262073200_1856 = __quote(__content_140319262073200_1856, '\x00', '&#0;', None, None)
                __token = 1876
                __content_140319262073200_1874 = getitem('x_y_crops')[2]
                __content_140319262073200_1874 = __quote(__content_140319262073200_1874, '\x00', '&#0;', None, None)
                __token = 1928
                __content_140319262073200_1926 = (getitem('y_start') + 210)
                __content_140319262073200_1926 = __quote(__content_140319262073200_1926, '\x00', '&#0;', None, None)
                __token = 1946
                __content_140319262073200_1944 = getitem('x_y_crops')[3]
                __content_140319262073200_1944 = __quote(__content_140319262073200_1944, '\x00', '&#0;', None, None)
                __token = 1998
                __content_140319262073200_1996 = (getitem('y_start') + 210)
                __content_140319262073200_1996 = __quote(__content_140319262073200_1996, '\x00', '&#0;', None, None)
                __token = 2016
                __content_140319262073200_2014 = getitem('x_y_crops')[0]
                __content_140319262073200_2014 = __quote(__content_140319262073200_2014, '\x00', '&#0;', None, None)
                __token = 2068
                __content_140319262073200_2066 = (getitem('y_start') + 210)
                __content_140319262073200_2066 = __quote(__content_140319262073200_2066, '\x00', '&#0;', None, None)
                __token = 2086
                __content_140319262073200_2084 = getitem('x_y_crops')[1]
                __content_140319262073200_2084 = __quote(__content_140319262073200_2084, '\x00', '&#0;', None, None)
                __token = 2138
                __content_140319262073200_2136 = (getitem('y_start') + 210)
                __content_140319262073200_2136 = __quote(__content_140319262073200_2136, '\x00', '&#0;', None, None)
                __token = 2156
                __content_140319262073200_2154 = getitem('x_y_crops')[2]
                __content_140319262073200_2154 = __quote(__content_140319262073200_2154, '\x00', '&#0;', None, None)
                __token = 2208
                __content_140319262073200_2206 = (getitem('y_start') + 210)
                __content_140319262073200_2206 = __quote(__content_140319262073200_2206, '\x00', '&#0;', None, None)
                __token = 2226
                __content_140319262073200_2224 = getitem('x_y_crops')[3]
                __content_140319262073200_2224 = __quote(__content_140319262073200_2224, '\x00', '&#0;', None, None)
                __token = 2288
                __content_140319262073200_2286 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200_2286 = __quote(__content_140319262073200_2286, '\x00', '&#0;', None, None)
                __token = 2309
                __content_140319262073200_2307 = getitem('state')
                __content_140319262073200_2307 = __quote(__content_140319262073200_2307, '\x00', '&#0;', None, None)
                __token = 2333
                __content_140319262073200_2331 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200_2331 = __quote(__content_140319262073200_2331, '\x00', '&#0;', None, None)
                __token = 2372
                __content_140319262073200_2370 = (getitem('y_start') + 310)
                __content_140319262073200_2370 = __quote(__content_140319262073200_2370, '\x00', '&#0;', None, None)
                __token = 2390
                __content_140319262073200_2388 = getitem('x_y_crops')[0]
                __content_140319262073200_2388 = __quote(__content_140319262073200_2388, '\x00', '&#0;', None, None)
                __token = 2442
                __content_140319262073200_2440 = (getitem('y_start') + 310)
                __content_140319262073200_2440 = __quote(__content_140319262073200_2440, '\x00', '&#0;', None, None)
                __token = 2460
                __content_140319262073200_2458 = getitem('x_y_crops')[1]
                __content_140319262073200_2458 = __quote(__content_140319262073200_2458, '\x00', '&#0;', None, None)
                __token = 2512
                __content_140319262073200_2510 = (getitem('y_start') + 310)
                __content_140319262073200_2510 = __quote(__content_140319262073200_2510, '\x00', '&#0;', None, None)
                __token = 2530
                __content_140319262073200_2528 = getitem('x_y_crops')[2]
                __content_140319262073200_2528 = __quote(__content_140319262073200_2528, '\x00', '&#0;', None, None)
                __token = 2582
                __content_140319262073200_2580 = (getitem('y_start') + 310)
                __content_140319262073200_2580 = __quote(__content_140319262073200_2580, '\x00', '&#0;', None, None)
                __token = 2600
                __content_140319262073200_2598 = getitem('x_y_crops')[3]
                __content_140319262073200_2598 = __quote(__content_140319262073200_2598, '\x00', '&#0;', None, None)
                __token = 2652
                __content_140319262073200_2650 = (getitem('y_start') + 310)
                __content_140319262073200_2650 = __quote(__content_140319262073200_2650, '\x00', '&#0;', None, None)
                __token = 2670
                __content_140319262073200_2668 = getitem('x_y_crops')[0]
                __content_140319262073200_2668 = __quote(__content_140319262073200_2668, '\x00', '&#0;', None, None)
                __token = 2722
                __content_140319262073200_2720 = (getitem('y_start') + 310)
                __content_140319262073200_2720 = __quote(__content_140319262073200_2720, '\x00', '&#0;', None, None)
                __token = 2740
                __content_140319262073200_2738 = getitem('x_y_crops')[1]
                __content_140319262073200_2738 = __quote(__content_140319262073200_2738, '\x00', '&#0;', None, None)
                __token = 2792
                __content_140319262073200_2790 = (getitem('y_start') + 310)
                __content_140319262073200_2790 = __quote(__content_140319262073200_2790, '\x00', '&#0;', None, None)
                __token = 2810
                __content_140319262073200_2808 = getitem('x_y_crops')[2]
                __content_140319262073200_2808 = __quote(__content_140319262073200_2808, '\x00', '&#0;', None, None)
                __token = 2862
                __content_140319262073200_2860 = (getitem('y_start') + 310)
                __content_140319262073200_2860 = __quote(__content_140319262073200_2860, '\x00', '&#0;', None, None)
                __token = 2880
                __content_140319262073200_2878 = getitem('x_y_crops')[3]
                __content_140319262073200_2878 = __quote(__content_140319262073200_2878, '\x00', '&#0;', None, None)
                __token = 2942
                __content_140319262073200_2940 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200_2940 = __quote(__content_140319262073200_2940, '\x00', '&#0;', None, None)
                __token = 2963
                __content_140319262073200_2961 = getitem('state')
                __content_140319262073200_2961 = __quote(__content_140319262073200_2961, '\x00', '&#0;', None, None)
                __token = 2987
                __content_140319262073200_2985 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200_2985 = __quote(__content_140319262073200_2985, '\x00', '&#0;', None, None)
                __token = 3026
                __content_140319262073200_3024 = (getitem('y_start') + 410)
                __content_140319262073200_3024 = __quote(__content_140319262073200_3024, '\x00', '&#0;', None, None)
                __token = 3044
                __content_140319262073200_3042 = getitem('x_y_crops')[0]
                __content_140319262073200_3042 = __quote(__content_140319262073200_3042, '\x00', '&#0;', None, None)
                __token = 3096
                __content_140319262073200_3094 = (getitem('y_start') + 410)
                __content_140319262073200_3094 = __quote(__content_140319262073200_3094, '\x00', '&#0;', None, None)
                __token = 3114
                __content_140319262073200_3112 = getitem('x_y_crops')[1]
                __content_140319262073200_3112 = __quote(__content_140319262073200_3112, '\x00', '&#0;', None, None)
                __token = 3166
                __content_140319262073200_3164 = (getitem('y_start') + 410)
                __content_140319262073200_3164 = __quote(__content_140319262073200_3164, '\x00', '&#0;', None, None)
                __token = 3184
                __content_140319262073200_3182 = getitem('x_y_crops')[2]
                __content_140319262073200_3182 = __quote(__content_140319262073200_3182, '\x00', '&#0;', None, None)
                __token = 3236
                __content_140319262073200_3234 = (getitem('y_start') + 410)
                __content_140319262073200_3234 = __quote(__content_140319262073200_3234, '\x00', '&#0;', None, None)
                __token = 3254
                __content_140319262073200_3252 = getitem('x_y_crops')[3]
                __content_140319262073200_3252 = __quote(__content_140319262073200_3252, '\x00', '&#0;', None, None)
                __token = 3306
                __content_140319262073200_3304 = (getitem('y_start') + 410)
                __content_140319262073200_3304 = __quote(__content_140319262073200_3304, '\x00', '&#0;', None, None)
                __token = 3324
                __content_140319262073200_3322 = getitem('x_y_crops')[0]
                __content_140319262073200_3322 = __quote(__content_140319262073200_3322, '\x00', '&#0;', None, None)
                __token = 3376
                __content_140319262073200_3374 = (getitem('y_start') + 410)
                __content_140319262073200_3374 = __quote(__content_140319262073200_3374, '\x00', '&#0;', None, None)
                __token = 3394
                __content_140319262073200_3392 = getitem('x_y_crops')[1]
                __content_140319262073200_3392 = __quote(__content_140319262073200_3392, '\x00', '&#0;', None, None)
                __token = 3446
                __content_140319262073200_3444 = (getitem('y_start') + 410)
                __content_140319262073200_3444 = __quote(__content_140319262073200_3444, '\x00', '&#0;', None, None)
                __token = 3464
                __content_140319262073200_3462 = getitem('x_y_crops')[2]
                __content_140319262073200_3462 = __quote(__content_140319262073200_3462, '\x00', '&#0;', None, None)
                __token = 3516
                __content_140319262073200_3514 = (getitem('y_start') + 410)
                __content_140319262073200_3514 = __quote(__content_140319262073200_3514, '\x00', '&#0;', None, None)
                __token = 3534
                __content_140319262073200_3532 = getitem('x_y_crops')[3]
                __content_140319262073200_3532 = __quote(__content_140319262073200_3532, '\x00', '&#0;', None, None)
                __token = 3596
                __content_140319262073200_3594 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200_3594 = __quote(__content_140319262073200_3594, '\x00', '&#0;', None, None)
                __token = 3617
                __content_140319262073200_3615 = getitem('state')
                __content_140319262073200_3615 = __quote(__content_140319262073200_3615, '\x00', '&#0;', None, None)
                __token = 3641
                __content_140319262073200_3639 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200_3639 = __quote(__content_140319262073200_3639, '\x00', '&#0;', None, None)
                __token = 3680
                __content_140319262073200_3678 = (getitem('y_start') + 510)
                __content_140319262073200_3678 = __quote(__content_140319262073200_3678, '\x00', '&#0;', None, None)
                __token = 3698
                __content_140319262073200_3696 = getitem('x_y_crops')[0]
                __content_140319262073200_3696 = __quote(__content_140319262073200_3696, '\x00', '&#0;', None, None)
                __token = 3750
                __content_140319262073200_3748 = (getitem('y_start') + 510)
                __content_140319262073200_3748 = __quote(__content_140319262073200_3748, '\x00', '&#0;', None, None)
                __token = 3768
                __content_140319262073200_3766 = getitem('x_y_crops')[1]
                __content_140319262073200_3766 = __quote(__content_140319262073200_3766, '\x00', '&#0;', None, None)
                __token = 3820
                __content_140319262073200_3818 = (getitem('y_start') + 510)
                __content_140319262073200_3818 = __quote(__content_140319262073200_3818, '\x00', '&#0;', None, None)
                __token = 3838
                __content_140319262073200_3836 = getitem('x_y_crops')[2]
                __content_140319262073200_3836 = __quote(__content_140319262073200_3836, '\x00', '&#0;', None, None)
                __token = 3890
                __content_140319262073200_3888 = (getitem('y_start') + 510)
                __content_140319262073200_3888 = __quote(__content_140319262073200_3888, '\x00', '&#0;', None, None)
                __token = 3908
                __content_140319262073200_3906 = getitem('x_y_crops')[3]
                __content_140319262073200_3906 = __quote(__content_140319262073200_3906, '\x00', '&#0;', None, None)
                __token = 3960
                __content_140319262073200_3958 = (getitem('y_start') + 510)
                __content_140319262073200_3958 = __quote(__content_140319262073200_3958, '\x00', '&#0;', None, None)
                __token = 3978
                __content_140319262073200_3976 = getitem('x_y_crops')[0]
                __content_140319262073200_3976 = __quote(__content_140319262073200_3976, '\x00', '&#0;', None, None)
                __token = 4030
                __content_140319262073200_4028 = (getitem('y_start') + 510)
                __content_140319262073200_4028 = __quote(__content_140319262073200_4028, '\x00', '&#0;', None, None)
                __token = 4048
                __content_140319262073200_4046 = getitem('x_y_crops')[1]
                __content_140319262073200_4046 = __quote(__content_140319262073200_4046, '\x00', '&#0;', None, None)
                __token = 4100
                __content_140319262073200_4098 = (getitem('y_start') + 510)
                __content_140319262073200_4098 = __quote(__content_140319262073200_4098, '\x00', '&#0;', None, None)
                __token = 4118
                __content_140319262073200_4116 = getitem('x_y_crops')[2]
                __content_140319262073200_4116 = __quote(__content_140319262073200_4116, '\x00', '&#0;', None, None)
                __token = 4170
                __content_140319262073200_4168 = (getitem('y_start') + 510)
                __content_140319262073200_4168 = __quote(__content_140319262073200_4168, '\x00', '&#0;', None, None)
                __token = 4188
                __content_140319262073200_4186 = getitem('x_y_crops')[3]
                __content_140319262073200_4186 = __quote(__content_140319262073200_4186, '\x00', '&#0;', None, None)
                __content_140319262073200 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        spriteset(', (__content_140319262073200 if (__content_140319262073200 is not None) else ''), '_ss_not_loaded_', (__content_140319262073200_353 if (__content_140319262073200_353 is not None) else ''), ', "src/graphics/', (__content_140319262073200_377 if (__content_140319262073200_377 is not None) else ''), '_0.png") {\n            [20,  ', (__content_140319262073200_416 if (__content_140319262073200_416 is not None) else ''), ', ', (__content_140319262073200_433 if (__content_140319262073200_433 is not None) else ''), ',  -13,  -6, ANIM]\n            [60,  ', (__content_140319262073200_485 if (__content_140319262073200_485 is not None) else ''), ', ', (__content_140319262073200_502 if (__content_140319262073200_502 is not None) else ''), ', -124,   5, ANIM]\n            [186, ', (__content_140319262073200_554 if (__content_140319262073200_554 is not None) else ''), ', ', (__content_140319262073200_571 if (__content_140319262073200_571 is not None) else ''), ', -124, -28, ANIM]\n            [328, ', (__content_140319262073200_623 if (__content_140319262073200_623 is not None) else ''), ', ', (__content_140319262073200_640 if (__content_140319262073200_640 is not None) else ''), ',  -76, -37, ANIM]\n            [454, ', (__content_140319262073200_692 if (__content_140319262073200_692 is not None) else ''), ', ', (__content_140319262073200_709 if (__content_140319262073200_709 is not None) else ''), ',  -14, -76, ANIM]\n            [494, ', (__content_140319262073200_761 if (__content_140319262073200_761 is not None) else ''), ', ', (__content_140319262073200_778 if (__content_140319262073200_778 is not None) else ''), ',  -34, -38, ANIM]\n            [620, ', (__content_140319262073200_830 if (__content_140319262073200_830 is not None) else ''), ', ', (__content_140319262073200_847 if (__content_140319262073200_847 is not None) else ''), ',  -15, -28, ANIM]\n            [762, ', (__content_140319262073200_899 if (__content_140319262073200_899 is not None) else ''), ', ', (__content_140319262073200_916 if (__content_140319262073200_916 is not None) else ''), ',   15,   6, ANIM]\n        }\n        spriteset(', (__content_140319262073200_978 if (__content_140319262073200_978 is not None) else ''), '_ss_load_1_', (__content_140319262073200_999 if (__content_140319262073200_999 is not None) else ''), ', "src/graphics/', (__content_140319262073200_1023 if (__content_140319262073200_1023 is not None) else ''), '_0.png") {\n            [20,  ', (__content_140319262073200_1062 if (__content_140319262073200_1062 is not None) else ''), ', ', (__content_140319262073200_1080 if (__content_140319262073200_1080 is not None) else ''), ',  -13, -14, ANIM]\n            [60,  ', (__content_140319262073200_1132 if (__content_140319262073200_1132 is not None) else ''), ', ', (__content_140319262073200_1150 if (__content_140319262073200_1150 is not None) else ''), ', -118,   1, ANIM]\n            [186, ', (__content_140319262073200_1202 if (__content_140319262073200_1202 is not None) else ''), ', ', (__content_140319262073200_1220 if (__content_140319262073200_1220 is not None) else ''), ', -112, -28, ANIM]\n            [328, ', (__content_140319262073200_1272 if (__content_140319262073200_1272 is not None) else ''), ', ', (__content_140319262073200_1290 if (__content_140319262073200_1290 is not None) else ''), ',  -64, -32, ANIM]\n            [454, ', (__content_140319262073200_1342 if (__content_140319262073200_1342 is not None) else ''), ', ', (__content_140319262073200_1360 if (__content_140319262073200_1360 is not None) else ''), ',  -14, -65, ANIM]\n            [494, ', (__content_140319262073200_1412 if (__content_140319262073200_1412 is not None) else ''), ', ', (__content_140319262073200_1430 if (__content_140319262073200_1430 is not None) else ''), ',  -45, -32, ANIM]\n            [620, ', (__content_140319262073200_1482 if (__content_140319262073200_1482 is not None) else ''), ', ', (__content_140319262073200_1500 if (__content_140319262073200_1500 is not None) else ''), ',  -26, -28, ANIM]\n            [762, ', (__content_140319262073200_1552 if (__content_140319262073200_1552 is not None) else ''), ', ', (__content_140319262073200_1570 if (__content_140319262073200_1570 is not None) else ''), ',    2,   0, ANIM]\n        }\n        spriteset(', (__content_140319262073200_1632 if (__content_140319262073200_1632 is not None) else ''), '_ss_load_2_', (__content_140319262073200_1653 if (__content_140319262073200_1653 is not None) else ''), ', "src/graphics/', (__content_140319262073200_1677 if (__content_140319262073200_1677 is not None) else ''), '_0.png") {\n            [20,  ', (__content_140319262073200_1716 if (__content_140319262073200_1716 is not None) else ''), ', ', (__content_140319262073200_1734 if (__content_140319262073200_1734 is not None) else ''), ',  -13, -21, ANIM]\n            [60,  ', (__content_140319262073200_1786 if (__content_140319262073200_1786 is not None) else ''), ', ', (__content_140319262073200_1804 if (__content_140319262073200_1804 is not None) else ''), ', -107,  -4, ANIM]\n            [186, ', (__content_140319262073200_1856 if (__content_140319262073200_1856 is not None) else ''), ', ', (__content_140319262073200_1874 if (__content_140319262073200_1874 is not None) else ''), ', -100, -28, ANIM]\n            [328, ', (__content_140319262073200_1926 if (__content_140319262073200_1926 is not None) else ''), ', ', (__content_140319262073200_1944 if (__content_140319262073200_1944 is not None) else ''), ',  -59, -30, ANIM]\n            [454, ', (__content_140319262073200_1996 if (__content_140319262073200_1996 is not None) else ''), ', ', (__content_140319262073200_2014 if (__content_140319262073200_2014 is not None) else ''), ',  -14, -57, ANIM]\n            [494, ', (__content_140319262073200_2066 if (__content_140319262073200_2066 is not None) else ''), ', ', (__content_140319262073200_2084 if (__content_140319262073200_2084 is not None) else ''), ',  -53, -30, ANIM]\n            [620, ', (__content_140319262073200_2136 if (__content_140319262073200_2136 is not None) else ''), ', ', (__content_140319262073200_2154 if (__content_140319262073200_2154 is not None) else ''), ',  -49, -28, ANIM]\n            [762, ', (__content_140319262073200_2206 if (__content_140319262073200_2206 is not None) else ''), ', ', (__content_140319262073200_2224 if (__content_140319262073200_2224 is not None) else ''), ',   -4,  -4, ANIM]\n        }\n        spriteset(', (__content_140319262073200_2286 if (__content_140319262073200_2286 is not None) else ''), '_ss_load_3_', (__content_140319262073200_2307 if (__content_140319262073200_2307 is not None) else ''), ', "src/graphics/', (__content_140319262073200_2331 if (__content_140319262073200_2331 is not None) else ''), '_0.png") {\n            [20,  ', (__content_140319262073200_2370 if (__content_140319262073200_2370 is not None) else ''), ', ', (__content_140319262073200_2388 if (__content_140319262073200_2388 is not None) else ''), ',  -13, -29, ANIM]\n            [60,  ', (__content_140319262073200_2440 if (__content_140319262073200_2440 is not None) else ''), ', ', (__content_140319262073200_2458 if (__content_140319262073200_2458 is not None) else ''), ', -102,  -8, ANIM]\n            [186, ', (__content_140319262073200_2510 if (__content_140319262073200_2510 is not None) else ''), ', ', (__content_140319262073200_2528 if (__content_140319262073200_2528 is not None) else ''), ',  -84, -28, ANIM]\n            [328, ', (__content_140319262073200_2580 if (__content_140319262073200_2580 is not None) else ''), ', ', (__content_140319262073200_2598 if (__content_140319262073200_2598 is not None) else ''), ',  -48, -26, ANIM]\n            [454, ', (__content_140319262073200_2650 if (__content_140319262073200_2650 is not None) else ''), ', ', (__content_140319262073200_2668 if (__content_140319262073200_2668 is not None) else ''), ',  -14, -47, ANIM]\n            [494, ', (__content_140319262073200_2720 if (__content_140319262073200_2720 is not None) else ''), ', ', (__content_140319262073200_2738 if (__content_140319262073200_2738 is not None) else ''), ',  -60, -25, ANIM]\n            [620, ', (__content_140319262073200_2790 if (__content_140319262073200_2790 is not None) else ''), ', ', (__content_140319262073200_2808 if (__content_140319262073200_2808 is not None) else ''), ',  -50, -28, ANIM]\n            [762, ', (__content_140319262073200_2860 if (__content_140319262073200_2860 is not None) else ''), ', ', (__content_140319262073200_2878 if (__content_140319262073200_2878 is not None) else ''), ',   -7,  -6, ANIM]\n        }\n        spriteset(', (__content_140319262073200_2940 if (__content_140319262073200_2940 is not None) else ''), '_ss_load_4_', (__content_140319262073200_2961 if (__content_140319262073200_2961 is not None) else ''), ', "src/graphics/', (__content_140319262073200_2985 if (__content_140319262073200_2985 is not None) else ''), '_0.png") {\n            [20,  ', (__content_140319262073200_3024 if (__content_140319262073200_3024 is not None) else ''), ', ', (__content_140319262073200_3042 if (__content_140319262073200_3042 is not None) else ''), ',  -13, -35, ANIM]\n            [60,  ', (__content_140319262073200_3094 if (__content_140319262073200_3094 is not None) else ''), ', ', (__content_140319262073200_3112 if (__content_140319262073200_3112 is not None) else ''), ',  -97, -10, ANIM]\n            [186, ', (__content_140319262073200_3164 if (__content_140319262073200_3164 is not None) else ''), ', ', (__content_140319262073200_3182 if (__content_140319262073200_3182 is not None) else ''), ',  -69, -28, ANIM]\n            [328, ', (__content_140319262073200_3234 if (__content_140319262073200_3234 is not None) else ''), ', ', (__content_140319262073200_3252 if (__content_140319262073200_3252 is not None) else ''), ',  -45, -22, ANIM]\n            [454, ', (__content_140319262073200_3304 if (__content_140319262073200_3304 is not None) else ''), ', ', (__content_140319262073200_3322 if (__content_140319262073200_3322 is not None) else ''), ',  -14, -45, ANIM]\n            [494, ', (__content_140319262073200_3374 if (__content_140319262073200_3374 is not None) else ''), ', ', (__content_140319262073200_3392 if (__content_140319262073200_3392 is not None) else ''), ',  -66, -22, ANIM]\n            [620, ', (__content_140319262073200_3444 if (__content_140319262073200_3444 is not None) else ''), ', ', (__content_140319262073200_3462 if (__content_140319262073200_3462 is not None) else ''), ',  -61, -28, ANIM]\n            [762, ', (__content_140319262073200_3514 if (__content_140319262073200_3514 is not None) else ''), ', ', (__content_140319262073200_3532 if (__content_140319262073200_3532 is not None) else ''), ',  -15, -10, ANIM]\n        }\n        spriteset(', (__content_140319262073200_3594 if (__content_140319262073200_3594 is not None) else ''), '_ss_load_5_', (__content_140319262073200_3615 if (__content_140319262073200_3615 is not None) else ''), ', "src/graphics/', (__content_140319262073200_3639 if (__content_140319262073200_3639 is not None) else ''), '_0.png") {\n            [20,  ', (__content_140319262073200_3678 if (__content_140319262073200_3678 is not None) else ''), ', ', (__content_140319262073200_3696 if (__content_140319262073200_3696 is not None) else ''), ',  -13, -41, ANIM]\n            [60,  ', (__content_140319262073200_3748 if (__content_140319262073200_3748 is not None) else ''), ', ', (__content_140319262073200_3766 if (__content_140319262073200_3766 is not None) else ''), ',  -90, -13, ANIM]\n            [186, ', (__content_140319262073200_3818 if (__content_140319262073200_3818 is not None) else ''), ', ', (__content_140319262073200_3836 if (__content_140319262073200_3836 is not None) else ''), ',  -65, -28, ANIM]\n            [328, ', (__content_140319262073200_3888 if (__content_140319262073200_3888 is not None) else ''), ', ', (__content_140319262073200_3906 if (__content_140319262073200_3906 is not None) else ''), ',  -40, -19, ANIM]\n            [454, ', (__content_140319262073200_3958 if (__content_140319262073200_3958 is not None) else ''), ', ', (__content_140319262073200_3976 if (__content_140319262073200_3976 is not None) else ''), ',  -14, -42, ANIM]\n            [494, ', (__content_140319262073200_4028 if (__content_140319262073200_4028 is not None) else ''), ', ', (__content_140319262073200_4046 if (__content_140319262073200_4046 is not None) else ''), ',  -75, -17, ANIM]\n            [620, ', (__content_140319262073200_4098 if (__content_140319262073200_4098 is not None) else ''), ', ', (__content_140319262073200_4116 if (__content_140319262073200_4116 is not None) else ''), ',  -68, -28, ANIM]\n            [762, ', (__content_140319262073200_4168 if (__content_140319262073200_4168 is not None) else ''), ', ', (__content_140319262073200_4186 if (__content_140319262073200_4186 is not None) else ''), ',  -22, -13, ANIM]\n        }\n    ', ))
                if (__content_140319262073200 is None):
                    pass
                else:
                    if (__content_140319262073200 is None):
                        __content_140319262073200 = None
                    else:
                        __tt = type(__content_140319262073200)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140319262073200 = str(__content_140319262073200)
                        else:
                            if (__tt is bytes):
                                __content_140319262073200 = decode(__content_140319262073200)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140319262073200 = __content_140319262073200.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140319262073200)
                                        __content_140319262073200 = (str(__content_140319262073200) if (__content_140319262073200 is __converted) else __converted)
                                    else:
                                        __content_140319262073200 = __content_140319262073200()
                if (__content_140319262073200 is not None):
                    __append(__content_140319262073200)
                if (__backup_y_start_140319267640896 is __marker):
                    del econtext['y_start']
                else:
                    econtext['y_start'] = __backup_y_start_140319267640896
                __append('\n')
                ____index_140319256660048 -= 1
                if (____index_140319256660048 > 0):
                    __append('')
            if (__backup_state_140319267640800 is __marker):
                del econtext['state']
            else:
                econtext['state'] = __backup_state_140319267640800
            if (__backup_x_y_crops_140319267640704 is __marker):
                del econtext['x_y_crops']
            else:
                econtext['x_y_crops'] = __backup_x_y_crops_140319267640704
            if (__backup_states_140319267640656 is __marker):
                del econtext['states']
            else:
                econtext['states'] = __backup_states_140319267640656

            # <Interpolation value=<Substitution "\n\nspritegroup ${ship.id}_sg_refit_0_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_0_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_0, current_speed) {\n    0: return ${ship.id}_sg_refit_0_not_moving;\n    return ${ship.id}_sg_refit_0_moving;\n}\n\nspritegroup ${ship.id}_sg_refit_1_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n        ${ship.id}_ss_load_2_moving,\n        ${ship.id}_ss_load_3_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_1_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_1, current_speed) {\n    0: return ${ship.id}_sg_refit_1_not_moving;\n    return ${ship.id}_sg_refit_1_moving;\n}\n\nspritegroup ${ship.id}_sg_refit_2_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n        ${ship.id}_ss_load_2_moving,\n        ${ship.id}_ss_load_3_moving,\n        ${ship.id}_ss_load_4_moving,\n        ${ship.id}_ss_load_5_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_2_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n        ${ship.id}_ss_load_4_not_moving,\n        ${ship.id}_ss_load_5_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n        ${ship.id}_ss_load_4_not_moving,\n        ${ship.id}_ss_load_5_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_2, current_speed) {\n    0: return ${ship.id}_sg_refit_2_not_moving;\n    return ${ship.id}_sg_refit_2_moving;\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, cargo_subtype) {\n    0: return ${ship.id}_switch_graphics_refit_0;\n    1: return ${ship.id}_switch_graphics_refit_1;\n    2: return ${ship.id}_switch_graphics_refit_2;\n    return ${ship.id}_switch_graphics_refit_0;\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n    ];\n}\n\n\n// -- set speed a little higher than rated speed when unladen -- //\n" (69:21)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9e9f72c3d0> -> __content_140319262073200
            __token = 4276
            __token = 4290
            __content_140319262073200 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200 = __quote(__content_140319262073200, '\x00', '&#0;', None, None)
            __token = 4344
            __content_140319262073200_4342 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_4342 = __quote(__content_140319262073200_4342, '\x00', '&#0;', None, None)
            __token = 4385
            __content_140319262073200_4383 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_4383 = __quote(__content_140319262073200_4383, '\x00', '&#0;', None, None)
            __token = 4526
            __content_140319262073200_4524 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_4524 = __quote(__content_140319262073200_4524, '\x00', '&#0;', None, None)
            __token = 4581
            __content_140319262073200_4579 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_4579 = __quote(__content_140319262073200_4579, '\x00', '&#0;', None, None)
            __token = 4639
            __content_140319262073200_4637 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_4637 = __quote(__content_140319262073200_4637, '\x00', '&#0;', None, None)
            __token = 4684
            __content_140319262073200_4682 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_4682 = __quote(__content_140319262073200_4682, '\x00', '&#0;', None, None)
            __token = 4747
            __content_140319262073200_4745 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_4745 = __quote(__content_140319262073200_4745, '\x00', '&#0;', None, None)
            __token = 4792
            __content_140319262073200_4790 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_4790 = __quote(__content_140319262073200_4790, '\x00', '&#0;', None, None)
            __token = 4861
            __content_140319262073200_4859 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_4859 = __quote(__content_140319262073200_4859, '\x00', '&#0;', None, None)
            __token = 4928
            __content_140319262073200_4926 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_4926 = __quote(__content_140319262073200_4926, '\x00', '&#0;', None, None)
            __token = 4973
            __content_140319262073200_4971 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_4971 = __quote(__content_140319262073200_4971, '\x00', '&#0;', None, None)
            __token = 5018
            __content_140319262073200_5016 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5016 = __quote(__content_140319262073200_5016, '\x00', '&#0;', None, None)
            __token = 5072
            __content_140319262073200_5070 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5070 = __quote(__content_140319262073200_5070, '\x00', '&#0;', None, None)
            __token = 5113
            __content_140319262073200_5111 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5111 = __quote(__content_140319262073200_5111, '\x00', '&#0;', None, None)
            __token = 5150
            __content_140319262073200_5148 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5148 = __quote(__content_140319262073200_5148, '\x00', '&#0;', None, None)
            __token = 5187
            __content_140319262073200_5185 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5185 = __quote(__content_140319262073200_5185, '\x00', '&#0;', None, None)
            __token = 5328
            __content_140319262073200_5326 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5326 = __quote(__content_140319262073200_5326, '\x00', '&#0;', None, None)
            __token = 5383
            __content_140319262073200_5381 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5381 = __quote(__content_140319262073200_5381, '\x00', '&#0;', None, None)
            __token = 5441
            __content_140319262073200_5439 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5439 = __quote(__content_140319262073200_5439, '\x00', '&#0;', None, None)
            __token = 5486
            __content_140319262073200_5484 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5484 = __quote(__content_140319262073200_5484, '\x00', '&#0;', None, None)
            __token = 5527
            __content_140319262073200_5525 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5525 = __quote(__content_140319262073200_5525, '\x00', '&#0;', None, None)
            __token = 5568
            __content_140319262073200_5566 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5566 = __quote(__content_140319262073200_5566, '\x00', '&#0;', None, None)
            __token = 5631
            __content_140319262073200_5629 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5629 = __quote(__content_140319262073200_5629, '\x00', '&#0;', None, None)
            __token = 5676
            __content_140319262073200_5674 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5674 = __quote(__content_140319262073200_5674, '\x00', '&#0;', None, None)
            __token = 5717
            __content_140319262073200_5715 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5715 = __quote(__content_140319262073200_5715, '\x00', '&#0;', None, None)
            __token = 5758
            __content_140319262073200_5756 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5756 = __quote(__content_140319262073200_5756, '\x00', '&#0;', None, None)
            __token = 5827
            __content_140319262073200_5825 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5825 = __quote(__content_140319262073200_5825, '\x00', '&#0;', None, None)
            __token = 5894
            __content_140319262073200_5892 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5892 = __quote(__content_140319262073200_5892, '\x00', '&#0;', None, None)
            __token = 5939
            __content_140319262073200_5937 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5937 = __quote(__content_140319262073200_5937, '\x00', '&#0;', None, None)
            __token = 5984
            __content_140319262073200_5982 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_5982 = __quote(__content_140319262073200_5982, '\x00', '&#0;', None, None)
            __token = 6038
            __content_140319262073200_6036 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6036 = __quote(__content_140319262073200_6036, '\x00', '&#0;', None, None)
            __token = 6079
            __content_140319262073200_6077 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6077 = __quote(__content_140319262073200_6077, '\x00', '&#0;', None, None)
            __token = 6116
            __content_140319262073200_6114 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6114 = __quote(__content_140319262073200_6114, '\x00', '&#0;', None, None)
            __token = 6153
            __content_140319262073200_6151 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6151 = __quote(__content_140319262073200_6151, '\x00', '&#0;', None, None)
            __token = 6190
            __content_140319262073200_6188 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6188 = __quote(__content_140319262073200_6188, '\x00', '&#0;', None, None)
            __token = 6227
            __content_140319262073200_6225 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6225 = __quote(__content_140319262073200_6225, '\x00', '&#0;', None, None)
            __token = 6368
            __content_140319262073200_6366 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6366 = __quote(__content_140319262073200_6366, '\x00', '&#0;', None, None)
            __token = 6423
            __content_140319262073200_6421 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6421 = __quote(__content_140319262073200_6421, '\x00', '&#0;', None, None)
            __token = 6481
            __content_140319262073200_6479 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6479 = __quote(__content_140319262073200_6479, '\x00', '&#0;', None, None)
            __token = 6526
            __content_140319262073200_6524 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6524 = __quote(__content_140319262073200_6524, '\x00', '&#0;', None, None)
            __token = 6567
            __content_140319262073200_6565 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6565 = __quote(__content_140319262073200_6565, '\x00', '&#0;', None, None)
            __token = 6608
            __content_140319262073200_6606 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6606 = __quote(__content_140319262073200_6606, '\x00', '&#0;', None, None)
            __token = 6649
            __content_140319262073200_6647 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6647 = __quote(__content_140319262073200_6647, '\x00', '&#0;', None, None)
            __token = 6690
            __content_140319262073200_6688 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6688 = __quote(__content_140319262073200_6688, '\x00', '&#0;', None, None)
            __token = 6753
            __content_140319262073200_6751 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6751 = __quote(__content_140319262073200_6751, '\x00', '&#0;', None, None)
            __token = 6798
            __content_140319262073200_6796 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6796 = __quote(__content_140319262073200_6796, '\x00', '&#0;', None, None)
            __token = 6839
            __content_140319262073200_6837 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6837 = __quote(__content_140319262073200_6837, '\x00', '&#0;', None, None)
            __token = 6880
            __content_140319262073200_6878 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6878 = __quote(__content_140319262073200_6878, '\x00', '&#0;', None, None)
            __token = 6921
            __content_140319262073200_6919 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6919 = __quote(__content_140319262073200_6919, '\x00', '&#0;', None, None)
            __token = 6962
            __content_140319262073200_6960 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_6960 = __quote(__content_140319262073200_6960, '\x00', '&#0;', None, None)
            __token = 7031
            __content_140319262073200_7029 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_7029 = __quote(__content_140319262073200_7029, '\x00', '&#0;', None, None)
            __token = 7098
            __content_140319262073200_7096 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_7096 = __quote(__content_140319262073200_7096, '\x00', '&#0;', None, None)
            __token = 7143
            __content_140319262073200_7141 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_7141 = __quote(__content_140319262073200_7141, '\x00', '&#0;', None, None)
            __token = 7202
            __content_140319262073200_7200 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_7200 = __quote(__content_140319262073200_7200, '\x00', '&#0;', None, None)
            __token = 7261
            __content_140319262073200_7259 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_7259 = __quote(__content_140319262073200_7259, '\x00', '&#0;', None, None)
            __token = 7311
            __content_140319262073200_7309 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_7309 = __quote(__content_140319262073200_7309, '\x00', '&#0;', None, None)
            __token = 7361
            __content_140319262073200_7359 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_7359 = __quote(__content_140319262073200_7359, '\x00', '&#0;', None, None)
            __token = 7408
            __content_140319262073200_7406 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_7406 = __quote(__content_140319262073200_7406, '\x00', '&#0;', None, None)
            __token = 7459
            __content_140319262073200_7457 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_7457 = __quote(__content_140319262073200_7457, '\x00', '&#0;', None, None)
            __token = 7507
            __content_140319262073200_7505 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_7505 = __quote(__content_140319262073200_7505, '\x00', '&#0;', None, None)
            __token = 7574
            __content_140319262073200_7572 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_7572 = __quote(__content_140319262073200_7572, '\x00', '&#0;', None, None)
            __content_140319262073200 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n\nspritegroup ', (__content_140319262073200 if (__content_140319262073200 is not None) else ''), '_sg_refit_0_moving {\n    loaded:  [\n        ', (__content_140319262073200_4342 if (__content_140319262073200_4342 is not None) else ''), '_ss_not_loaded_moving,\n        ', (__content_140319262073200_4383 if (__content_140319262073200_4383 is not None) else ''), "_ss_load_1_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ", (__content_140319262073200_4524 if (__content_140319262073200_4524 is not None) else ''), '_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ', (__content_140319262073200_4579 if (__content_140319262073200_4579 is not None) else ''), '_sg_refit_0_not_moving {\n    loaded:  [\n        ', (__content_140319262073200_4637 if (__content_140319262073200_4637 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_140319262073200_4682 if (__content_140319262073200_4682 is not None) else ''), '_ss_load_1_not_moving,\n    ];\n    loading: [\n        ', (__content_140319262073200_4745 if (__content_140319262073200_4745 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_140319262073200_4790 if (__content_140319262073200_4790 is not None) else ''), '_ss_load_1_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_140319262073200_4859 if (__content_140319262073200_4859 is not None) else ''), '_switch_graphics_refit_0, current_speed) {\n    0: return ', (__content_140319262073200_4926 if (__content_140319262073200_4926 is not None) else ''), '_sg_refit_0_not_moving;\n    return ', (__content_140319262073200_4971 if (__content_140319262073200_4971 is not None) else ''), '_sg_refit_0_moving;\n}\n\nspritegroup ', (__content_140319262073200_5016 if (__content_140319262073200_5016 is not None) else ''), '_sg_refit_1_moving {\n    loaded:  [\n        ', (__content_140319262073200_5070 if (__content_140319262073200_5070 is not None) else ''), '_ss_not_loaded_moving,\n        ', (__content_140319262073200_5111 if (__content_140319262073200_5111 is not None) else ''), '_ss_load_1_moving,\n        ', (__content_140319262073200_5148 if (__content_140319262073200_5148 is not None) else ''), '_ss_load_2_moving,\n        ', (__content_140319262073200_5185 if (__content_140319262073200_5185 is not None) else ''), "_ss_load_3_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ", (__content_140319262073200_5326 if (__content_140319262073200_5326 is not None) else ''), '_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ', (__content_140319262073200_5381 if (__content_140319262073200_5381 is not None) else ''), '_sg_refit_1_not_moving {\n    loaded:  [\n        ', (__content_140319262073200_5439 if (__content_140319262073200_5439 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_140319262073200_5484 if (__content_140319262073200_5484 is not None) else ''), '_ss_load_1_not_moving,\n        ', (__content_140319262073200_5525 if (__content_140319262073200_5525 is not None) else ''), '_ss_load_2_not_moving,\n        ', (__content_140319262073200_5566 if (__content_140319262073200_5566 is not None) else ''), '_ss_load_3_not_moving,\n    ];\n    loading: [\n        ', (__content_140319262073200_5629 if (__content_140319262073200_5629 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_140319262073200_5674 if (__content_140319262073200_5674 is not None) else ''), '_ss_load_1_not_moving,\n        ', (__content_140319262073200_5715 if (__content_140319262073200_5715 is not None) else ''), '_ss_load_2_not_moving,\n        ', (__content_140319262073200_5756 if (__content_140319262073200_5756 is not None) else ''), '_ss_load_3_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_140319262073200_5825 if (__content_140319262073200_5825 is not None) else ''), '_switch_graphics_refit_1, current_speed) {\n    0: return ', (__content_140319262073200_5892 if (__content_140319262073200_5892 is not None) else ''), '_sg_refit_1_not_moving;\n    return ', (__content_140319262073200_5937 if (__content_140319262073200_5937 is not None) else ''), '_sg_refit_1_moving;\n}\n\nspritegroup ', (__content_140319262073200_5982 if (__content_140319262073200_5982 is not None) else ''), '_sg_refit_2_moving {\n    loaded:  [\n        ', (__content_140319262073200_6036 if (__content_140319262073200_6036 is not None) else ''), '_ss_not_loaded_moving,\n        ', (__content_140319262073200_6077 if (__content_140319262073200_6077 is not None) else ''), '_ss_load_1_moving,\n        ', (__content_140319262073200_6114 if (__content_140319262073200_6114 is not None) else ''), '_ss_load_2_moving,\n        ', (__content_140319262073200_6151 if (__content_140319262073200_6151 is not None) else ''), '_ss_load_3_moving,\n        ', (__content_140319262073200_6188 if (__content_140319262073200_6188 is not None) else ''), '_ss_load_4_moving,\n        ', (__content_140319262073200_6225 if (__content_140319262073200_6225 is not None) else ''), "_ss_load_5_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ", (__content_140319262073200_6366 if (__content_140319262073200_6366 is not None) else ''), '_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ', (__content_140319262073200_6421 if (__content_140319262073200_6421 is not None) else ''), '_sg_refit_2_not_moving {\n    loaded:  [\n        ', (__content_140319262073200_6479 if (__content_140319262073200_6479 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_140319262073200_6524 if (__content_140319262073200_6524 is not None) else ''), '_ss_load_1_not_moving,\n        ', (__content_140319262073200_6565 if (__content_140319262073200_6565 is not None) else ''), '_ss_load_2_not_moving,\n        ', (__content_140319262073200_6606 if (__content_140319262073200_6606 is not None) else ''), '_ss_load_3_not_moving,\n        ', (__content_140319262073200_6647 if (__content_140319262073200_6647 is not None) else ''), '_ss_load_4_not_moving,\n        ', (__content_140319262073200_6688 if (__content_140319262073200_6688 is not None) else ''), '_ss_load_5_not_moving,\n    ];\n    loading: [\n        ', (__content_140319262073200_6751 if (__content_140319262073200_6751 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_140319262073200_6796 if (__content_140319262073200_6796 is not None) else ''), '_ss_load_1_not_moving,\n        ', (__content_140319262073200_6837 if (__content_140319262073200_6837 is not None) else ''), '_ss_load_2_not_moving,\n        ', (__content_140319262073200_6878 if (__content_140319262073200_6878 is not None) else ''), '_ss_load_3_not_moving,\n        ', (__content_140319262073200_6919 if (__content_140319262073200_6919 is not None) else ''), '_ss_load_4_not_moving,\n        ', (__content_140319262073200_6960 if (__content_140319262073200_6960 is not None) else ''), '_ss_load_5_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_140319262073200_7029 if (__content_140319262073200_7029 is not None) else ''), '_switch_graphics_refit_2, current_speed) {\n    0: return ', (__content_140319262073200_7096 if (__content_140319262073200_7096 is not None) else ''), '_sg_refit_2_not_moving;\n    return ', (__content_140319262073200_7141 if (__content_140319262073200_7141 is not None) else ''), '_sg_refit_2_moving;\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_140319262073200_7200 if (__content_140319262073200_7200 is not None) else ''), '_switch_graphics, cargo_subtype) {\n    0: return ', (__content_140319262073200_7259 if (__content_140319262073200_7259 is not None) else ''), '_switch_graphics_refit_0;\n    1: return ', (__content_140319262073200_7309 if (__content_140319262073200_7309 is not None) else ''), '_switch_graphics_refit_1;\n    2: return ', (__content_140319262073200_7359 if (__content_140319262073200_7359 is not None) else ''), '_switch_graphics_refit_2;\n    return ', (__content_140319262073200_7406 if (__content_140319262073200_7406 is not None) else ''), '_switch_graphics_refit_0;\n}\n\nspritegroup ', (__content_140319262073200_7457 if (__content_140319262073200_7457 is not None) else ''), '_sg_purchase {\n    loaded:  [\n        ', (__content_140319262073200_7505 if (__content_140319262073200_7505 is not None) else ''), '_ss_not_loaded_not_moving,\n    ];\n    loading: [\n        ', (__content_140319262073200_7572 if (__content_140319262073200_7572 is not None) else ''), '_ss_not_loaded_not_moving,\n    ];\n}\n\n\n// -- set speed a little higher than rated speed when unladen -- //\n', ))
            if (__content_140319262073200 is None):
                pass
            else:
                if (__content_140319262073200 is None):
                    __content_140319262073200 = None
                else:
                    __tt = type(__content_140319262073200)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140319262073200 = str(__content_140319262073200)
                    else:
                        if (__tt is bytes):
                            __content_140319262073200 = decode(__content_140319262073200)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140319262073200 = __content_140319262073200.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140319262073200)
                                    __content_140319262073200 = (str(__content_140319262073200) if (__content_140319262073200 is __converted) else __converted)
                                else:
                                    __content_140319262073200 = __content_140319262073200()
            if (__content_140319262073200 is not None):
                __append(__content_140319262073200)

            # <Static value=<_ast.Dict object at 0x7f9e9f79d2b0> name=None at 7f9e9f79d160> -> __attrs_140319256660768
            __attrs_140319256660768 = _static_140319257121456
            __backup_speed_factor_140319267640752 = get('speed_factor', __marker)

            # <Value 'python:range(3)' (185:32)> -> __iterator
            __token = 7720
            __iterator = get('range', range)(3)
            (__iterator, ____index_140319256661584, ) = getitem('repeat')('speed_factor', __iterator)
            econtext['speed_factor'] = None
            for __item in __iterator:
                econtext['speed_factor'] = __item

                # <Interpolation value=<Substitution '\n    switch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount_${speed_factor}, cargo_count*100/cargo_capacity) {\n        0 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[0]};\n        1..100 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[4]}; // log tug is binary: loaded or unloaded; no intermediate fractional speeds\n        return 0; // should never reach this result, make it show up as a problem\n    }\n' (185:49)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9e9f72cf70> -> __content_140319262073200
                __token = 7742
                __token = 7770
                __content_140319262073200 = _lookup_attr(getitem('ship'), 'id')
                __content_140319262073200 = __quote(__content_140319262073200, '\x00', '&#0;', None, None)
                __token = 7818
                __content_140319262073200_7816 = getitem('speed_factor')
                __content_140319262073200_7816 = __quote(__content_140319262073200_7816, '\x00', '&#0;', None, None)
                __token = 7881
                __content_140319262073200_7879 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(getitem('speed_factor'))[0]
                __content_140319262073200_7879 = __quote(__content_140319262073200_7879, '\x00', '&#0;', None, None)
                __token = 7960
                __content_140319262073200_7958 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(getitem('speed_factor'))[4]
                __content_140319262073200_7958 = __quote(__content_140319262073200_7958, '\x00', '&#0;', None, None)
                __content_140319262073200 = ('%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_SHIPS, SELF, ', (__content_140319262073200 if (__content_140319262073200 is not None) else ''), '_switch_speed_varies_with_load_amount_', (__content_140319262073200_7816 if (__content_140319262073200_7816 is not None) else ''), ', cargo_count*100/cargo_capacity) {\n        0 : ', (__content_140319262073200_7879 if (__content_140319262073200_7879 is not None) else ''), ';\n        1..100 : ', (__content_140319262073200_7958 if (__content_140319262073200_7958 is not None) else ''), '; // log tug is binary: loaded or unloaded; no intermediate fractional speeds\n        return 0; // should never reach this result, make it show up as a problem\n    }\n', ))
                if (__content_140319262073200 is None):
                    pass
                else:
                    if (__content_140319262073200 is None):
                        __content_140319262073200 = None
                    else:
                        __tt = type(__content_140319262073200)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140319262073200 = str(__content_140319262073200)
                        else:
                            if (__tt is bytes):
                                __content_140319262073200 = decode(__content_140319262073200)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140319262073200 = __content_140319262073200.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140319262073200)
                                        __content_140319262073200 = (str(__content_140319262073200) if (__content_140319262073200 is __converted) else __converted)
                                    else:
                                        __content_140319262073200 = __content_140319262073200()
                if (__content_140319262073200 is not None):
                    __append(__content_140319262073200)
                ____index_140319256661584 -= 1
                if (____index_140319256661584 > 0):
                    __append('')
            if (__backup_speed_factor_140319267640752 is __marker):
                del econtext['speed_factor']
            else:
                econtext['speed_factor'] = __backup_speed_factor_140319267640752

            # <Interpolation value=<Substitution '\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount, param_adjust_ship_speed) {\n    0: ${ship.id}_switch_speed_varies_with_load_amount_0;\n    1: ${ship.id}_switch_speed_varies_with_load_amount_1;\n    2: ${ship.id}_switch_speed_varies_with_load_amount_2;\n}\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_purchase_speed, param_adjust_ship_speed) {\n    0: ${ship.get_speeds_adjusted_for_load_amount(0)[4]};\n    1: ${ship.get_speeds_adjusted_for_load_amount(1)[4]};\n    2: ${ship.get_speeds_adjusted_for_load_amount(2)[4]};\n}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}\n' (191:12)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f9e9f72c580> -> __content_140319262073200
            __token = 8197
            __token = 8225
            __content_140319262073200 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200 = __quote(__content_140319262073200, '\x00', '&#0;', None, None)
            __token = 8308
            __content_140319262073200_8306 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_8306 = __quote(__content_140319262073200_8306, '\x00', '&#0;', None, None)
            __token = 8366
            __content_140319262073200_8364 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_8364 = __quote(__content_140319262073200_8364, '\x00', '&#0;', None, None)
            __token = 8424
            __content_140319262073200_8422 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_8422 = __quote(__content_140319262073200_8422, '\x00', '&#0;', None, None)
            __token = 8503
            __content_140319262073200_8501 = _lookup_attr(getitem('ship'), 'id')
            __content_140319262073200_8501 = __quote(__content_140319262073200_8501, '\x00', '&#0;', None, None)
            __token = 8571
            __content_140319262073200_8569 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(0)[4]
            __content_140319262073200_8569 = __quote(__content_140319262073200_8569, '\x00', '&#0;', None, None)
            __token = 8629
            __content_140319262073200_8627 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(1)[4]
            __content_140319262073200_8627 = __quote(__content_140319262073200_8627, '\x00', '&#0;', None, None)
            __token = 8687
            __content_140319262073200_8685 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(2)[4]
            __content_140319262073200_8685 = __quote(__content_140319262073200_8685, '\x00', '&#0;', None, None)
            __token = 8741
            __content_140319262073200_8739 = _lookup_attr(getitem('ship'), 'render_cargo_capacity')()
            __content_140319262073200_8739 = __quote(__content_140319262073200_8739, '\x00', '&#0;', None, None)
            __token = 8774
            __content_140319262073200_8772 = _lookup_attr(getitem('ship'), 'render_properties')()
            __content_140319262073200_8772 = __quote(__content_140319262073200_8772, '\x00', '&#0;', None, None)
            __content_140319262073200 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\nswitch (FEAT_SHIPS, SELF, ', (__content_140319262073200 if (__content_140319262073200 is not None) else ''), '_switch_speed_varies_with_load_amount, param_adjust_ship_speed) {\n    0: ', (__content_140319262073200_8306 if (__content_140319262073200_8306 is not None) else ''), '_switch_speed_varies_with_load_amount_0;\n    1: ', (__content_140319262073200_8364 if (__content_140319262073200_8364 is not None) else ''), '_switch_speed_varies_with_load_amount_1;\n    2: ', (__content_140319262073200_8422 if (__content_140319262073200_8422 is not None) else ''), '_switch_speed_varies_with_load_amount_2;\n}\nswitch (FEAT_SHIPS, SELF, ', (__content_140319262073200_8501 if (__content_140319262073200_8501 is not None) else ''), '_switch_purchase_speed, param_adjust_ship_speed) {\n    0: ', (__content_140319262073200_8569 if (__content_140319262073200_8569 is not None) else ''), ';\n    1: ', (__content_140319262073200_8627 if (__content_140319262073200_8627 is not None) else ''), ';\n    2: ', (__content_140319262073200_8685 if (__content_140319262073200_8685 is not None) else ''), ';\n}\n\n', (__content_140319262073200_8739 if (__content_140319262073200_8739 is not None) else ''), '\n\n', (__content_140319262073200_8772 if (__content_140319262073200_8772 is not None) else ''), '\n', ))
            if (__content_140319262073200 is None):
                pass
            else:
                if (__content_140319262073200 is None):
                    __content_140319262073200 = None
                else:
                    __tt = type(__content_140319262073200)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140319262073200 = str(__content_140319262073200)
                    else:
                        if (__tt is bytes):
                            __content_140319262073200 = decode(__content_140319262073200)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140319262073200 = __content_140319262073200.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140319262073200)
                                    __content_140319262073200 = (str(__content_140319262073200) if (__content_140319262073200 is __converted) else __converted)
                                else:
                                    __content_140319262073200 = __content_140319262073200()
            if (__content_140319262073200 is not None):
                __append(__content_140319262073200)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }