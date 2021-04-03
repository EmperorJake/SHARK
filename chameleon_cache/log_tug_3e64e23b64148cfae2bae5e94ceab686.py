# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/templates/log_tug.pynml'
__tokens = {0: ('${ship.render_debug_info()}\n\n// graphics', 1, 0), 2: ('ship.render_debug_info()', 1, 2), 76: ("python:{'not_moving': 0 ,'moving': 600}", 4, 35), 154: (" python:('28, 89', '113, 66', '138, 48', '113, 66'", 5, 37), 241: ('states', 6, 34), 287: ('python:states[state]', 7, 37), 318: ('spriteset(${ship.id}_ss_not_loaded_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 10}, ${x_y_crops[0]},  -13,  -6]\n            [60,  ${y_start + 10}, ${x_y_crops[1]}, -124,   5]\n            [186, ${y_start + 10}, ${x_y_crops[2]}, -124, -28]\n            [328, ${y_start + 10}, ${x_y_crops[3]},  -76, -37]\n            [454, ${y_start + 10}, ${x_y_crops[0]},  -14, -76]\n            [494, ${y_start + 10}, ${x_y_crops[1]},  -34, -38]\n            [620, ${y_start + 10}, ${x_y_crops[2]},  -15, -28]\n            [762, ${y_start + 10}, ${x_y_crops[3]},   15,   6]\n        }\n        spriteset(${ship.id}_ss_load_1_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 110}, ${x_y_crops[0]},  -13, -14]\n            [60,  ${y_start + 110}, ${x_y_crops[1]}, -118,   1]\n            [186, ${y_start + 110}, ${x_y_crops[2]}, -112, -28]\n            [328, ${y_start + 110}, ${x_y_crops[3]},  -64, -32]\n            [454, ${y_start + 110}, ${x_y_crops[0]},  -14, -65]\n            [494, ${y_start + 110}, ${x_y_crops[1]},  -45, -32]\n            [620, ${y_start + 110}, ${x_y_crops[2]},  -26, -28]\n            [762, ${y_start + 110}, ${x_y_crops[3]},    2,   0]\n        }\n        spriteset(${ship.id}_ss_load_2_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 210}, ${x_y_crops[0]},  -13, -21]\n            [60,  ${y_start + 210}, ${x_y_crops[1]}, -107,  -4]\n            [186, ${y_start + 210}, ${x_y_crops[2]}, -100, -28]\n            [328, ${y_start + 210}, ${x_y_crops[3]},  -59, -30]\n            [454, ${y_start + 210}, ${x_y_crops[0]},  -14, -57]\n            [494, ${y_start + 210}, ${x_y_crops[1]},  -53, -30]\n            [620, ${y_start + 210}, ${x_y_crops[2]},  -49, -28]\n            [762, ${y_start + 210}, ${x_y_crops[3]},   -4,  -4]\n        }\n        spriteset(${ship.id}_ss_load_3_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 310}, ${x_y_crops[0]},  -13, -29]\n            [60,  ${y_start + 310}, ${x_y_crops[1]}, -102,  -8]\n            [186, ${y_start + 310}, ${x_y_crops[2]},  -84, -28]\n            [328, ${y_start + 310}, ${x_y_crops[3]},  -48, -26]\n            [454, ${y_start + 310}, ${x_y_crops[0]},  -14, -47]\n            [494, ${y_start + 310}, ${x_y_crops[1]},  -60, -25]\n            [620, ${y_start + 310}, ${x_y_crops[2]},  -50, -28]\n            [762, ${y_start + 310}, ${x_y_crops[3]},   -7,  -6]\n        }\n        spriteset(${ship.id}_ss_load_4_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 410}, ${x_y_crops[0]},  -13, -35]\n            [60,  ${y_start + 410}, ${x_y_crops[1]},  -97, -10]\n            [186, ${y_start + 410}, ${x_y_crops[2]},  -69, -28]\n            [328, ${y_start + 410}, ${x_y_crops[3]},  -45, -22]\n            [454, ${y_start + 410}, ${x_y_crops[0]},  -14, -45]\n            [494, ${y_start + 410}, ${x_y_crops[1]},  -66, -22]\n            [620, ${y_start + 410}, ${x_y_crops[2]},  -61, -28]\n            [762, ${y_start + 410}, ${x_y_crops[3]},  -15, -10]\n        }\n        spriteset(${ship.id}_ss_load_5_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 510}, ${x_y_crops[0]},  -13, -41]\n            [60,  ${y_start + 510}, ${x_y_crops[1]},  -90, -13]\n            [186, ${y_start + 510}, ${x_y_crops[2]},  -65, -28]\n            [328, ${y_start + 510}, ${x_y_crops[3]},  -40, -19]\n            [454, ${y_start + 510}, ${x_y_crops[0]},  -14, -42]\n            [494, ${y_start + 510}, ${x_y_crops[1]},  -75, -17]\n            [620, ${y_start + 510}, ${x_y_crops[2]},  -68, -28]\n            [762, ${y_start + 510}, ${x_y_crops[3]},  -22, -13]\n        }', 8, 8), 330: ('ship.id', 8, 20), 355: ('state', 8, 45), 379: ('ship.id', 8, 69), 418: ('y_start + 10', 9, 20), 435: ('x_y_crops[0]', 9, 37), 481: ('y_start + 10', 10, 20), 498: ('x_y_crops[1]', 10, 37), 544: ('y_start + 10', 11, 20), 561: ('x_y_crops[2]', 11, 37), 607: ('y_start + 10', 12, 20), 624: ('x_y_crops[3]', 12, 37), 670: ('y_start + 10', 13, 20), 687: ('x_y_crops[0]', 13, 37), 733: ('y_start + 10', 14, 20), 750: ('x_y_crops[1]', 14, 37), 796: ('y_start + 10', 15, 20), 813: ('x_y_crops[2]', 15, 37), 859: ('y_start + 10', 16, 20), 876: ('x_y_crops[3]', 16, 37), 932: ('ship.id', 18, 20), 953: ('state', 18, 41), 977: ('ship.id', 18, 65), 1016: ('y_start + 110', 19, 20), 1034: ('x_y_crops[0]', 19, 38), 1080: ('y_start + 110', 20, 20), 1098: ('x_y_crops[1]', 20, 38), 1144: ('y_start + 110', 21, 20), 1162: ('x_y_crops[2]', 21, 38), 1208: ('y_start + 110', 22, 20), 1226: ('x_y_crops[3]', 22, 38), 1272: ('y_start + 110', 23, 20), 1290: ('x_y_crops[0]', 23, 38), 1336: ('y_start + 110', 24, 20), 1354: ('x_y_crops[1]', 24, 38), 1400: ('y_start + 110', 25, 20), 1418: ('x_y_crops[2]', 25, 38), 1464: ('y_start + 110', 26, 20), 1482: ('x_y_crops[3]', 26, 38), 1538: ('ship.id', 28, 20), 1559: ('state', 28, 41), 1583: ('ship.id', 28, 65), 1622: ('y_start + 210', 29, 20), 1640: ('x_y_crops[0]', 29, 38), 1686: ('y_start + 210', 30, 20), 1704: ('x_y_crops[1]', 30, 38), 1750: ('y_start + 210', 31, 20), 1768: ('x_y_crops[2]', 31, 38), 1814: ('y_start + 210', 32, 20), 1832: ('x_y_crops[3]', 32, 38), 1878: ('y_start + 210', 33, 20), 1896: ('x_y_crops[0]', 33, 38), 1942: ('y_start + 210', 34, 20), 1960: ('x_y_crops[1]', 34, 38), 2006: ('y_start + 210', 35, 20), 2024: ('x_y_crops[2]', 35, 38), 2070: ('y_start + 210', 36, 20), 2088: ('x_y_crops[3]', 36, 38), 2144: ('ship.id', 38, 20), 2165: ('state', 38, 41), 2189: ('ship.id', 38, 65), 2228: ('y_start + 310', 39, 20), 2246: ('x_y_crops[0]', 39, 38), 2292: ('y_start + 310', 40, 20), 2310: ('x_y_crops[1]', 40, 38), 2356: ('y_start + 310', 41, 20), 2374: ('x_y_crops[2]', 41, 38), 2420: ('y_start + 310', 42, 20), 2438: ('x_y_crops[3]', 42, 38), 2484: ('y_start + 310', 43, 20), 2502: ('x_y_crops[0]', 43, 38), 2548: ('y_start + 310', 44, 20), 2566: ('x_y_crops[1]', 44, 38), 2612: ('y_start + 310', 45, 20), 2630: ('x_y_crops[2]', 45, 38), 2676: ('y_start + 310', 46, 20), 2694: ('x_y_crops[3]', 46, 38), 2750: ('ship.id', 48, 20), 2771: ('state', 48, 41), 2795: ('ship.id', 48, 65), 2834: ('y_start + 410', 49, 20), 2852: ('x_y_crops[0]', 49, 38), 2898: ('y_start + 410', 50, 20), 2916: ('x_y_crops[1]', 50, 38), 2962: ('y_start + 410', 51, 20), 2980: ('x_y_crops[2]', 51, 38), 3026: ('y_start + 410', 52, 20), 3044: ('x_y_crops[3]', 52, 38), 3090: ('y_start + 410', 53, 20), 3108: ('x_y_crops[0]', 53, 38), 3154: ('y_start + 410', 54, 20), 3172: ('x_y_crops[1]', 54, 38), 3218: ('y_start + 410', 55, 20), 3236: ('x_y_crops[2]', 55, 38), 3282: ('y_start + 410', 56, 20), 3300: ('x_y_crops[3]', 56, 38), 3356: ('ship.id', 58, 20), 3377: ('state', 58, 41), 3401: ('ship.id', 58, 65), 3440: ('y_start + 510', 59, 20), 3458: ('x_y_crops[0]', 59, 38), 3504: ('y_start + 510', 60, 20), 3522: ('x_y_crops[1]', 60, 38), 3568: ('y_start + 510', 61, 20), 3586: ('x_y_crops[2]', 61, 38), 3632: ('y_start + 510', 62, 20), 3650: ('x_y_crops[3]', 62, 38), 3696: ('y_start + 510', 63, 20), 3714: ('x_y_crops[0]', 63, 38), 3760: ('y_start + 510', 64, 20), 3778: ('x_y_crops[1]', 64, 38), 3824: ('y_start + 510', 65, 20), 3842: ('x_y_crops[2]', 65, 38), 3888: ('y_start + 510', 66, 20), 3906: ('x_y_crops[3]', 66, 38), 3988: ("spritegroup ${ship.id}_sg_refit_0_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_0_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_0, current_speed) {\n    0: return ${ship.id}_sg_refit_0_not_moving;\n    return ${ship.id}_sg_refit_0_moving;\n}\n\nspritegroup ${ship.id}_sg_refit_1_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n        ${ship.id}_ss_load_2_moving,\n        ${ship.id}_ss_load_3_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_1_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_1, current_speed) {\n    0: return ${ship.id}_sg_refit_1_not_moving;\n    return ${ship.id}_sg_refit_1_moving;\n}\n\nspritegroup ${ship.id}_sg_refit_2_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n        ${ship.id}_ss_load_2_moving,\n        ${ship.id}_ss_load_3_moving,\n        ${ship.id}_ss_load_4_moving,\n        ${ship.id}_ss_load_5_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_2_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n        ${ship.id}_ss_load_4_not_moving,\n        ${ship.id}_ss_load_5_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n        ${ship.id}_ss_load_4_not_moving,\n        ${ship.id}_ss_load_5_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_2, current_speed) {\n    0: return ${ship.id}_sg_refit_2_not_moving;\n    return ${ship.id}_sg_refit_2_moving;\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, cargo_subtype) {\n    0: return ${ship.id}_switch_graphics_refit_0;\n    1: return ${ship.id}_switch_graphics_refit_1;\n    2: return ${ship.id}_switch_graphics_refit_2;\n    return ${ship.id}_switch_graphics_refit_0;\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n    ];\n}\n\n\n// -- set speed a little higher than rated speed when unladen -- //", 71, 0), 4002: ('ship.id', 71, 14), 4056: ('ship.id', 73, 10), 4097: ('ship.id', 74, 10), 4238: ('ship.id', 77, 10), 4293: ('ship.id', 81, 14), 4351: ('ship.id', 83, 10), 4396: ('ship.id', 84, 10), 4459: ('ship.id', 87, 10), 4504: ('ship.id', 88, 10), 4573: ('ship.id', 92, 28), 4640: ('ship.id', 93, 16), 4685: ('ship.id', 94, 13), 4730: ('ship.id', 97, 14), 4784: ('ship.id', 99, 10), 4825: ('ship.id', 100, 10), 4862: ('ship.id', 101, 10), 4899: ('ship.id', 102, 10), 5040: ('ship.id', 105, 10), 5095: ('ship.id', 109, 14), 5153: ('ship.id', 111, 10), 5198: ('ship.id', 112, 10), 5239: ('ship.id', 113, 10), 5280: ('ship.id', 114, 10), 5343: ('ship.id', 117, 10), 5388: ('ship.id', 118, 10), 5429: ('ship.id', 119, 10), 5470: ('ship.id', 120, 10), 5539: ('ship.id', 124, 28), 5606: ('ship.id', 125, 16), 5651: ('ship.id', 126, 13), 5696: ('ship.id', 129, 14), 5750: ('ship.id', 131, 10), 5791: ('ship.id', 132, 10), 5828: ('ship.id', 133, 10), 5865: ('ship.id', 134, 10), 5902: ('ship.id', 135, 10), 5939: ('ship.id', 136, 10), 6080: ('ship.id', 139, 10), 6135: ('ship.id', 143, 14), 6193: ('ship.id', 145, 10), 6238: ('ship.id', 146, 10), 6279: ('ship.id', 147, 10), 6320: ('ship.id', 148, 10), 6361: ('ship.id', 149, 10), 6402: ('ship.id', 150, 10), 6465: ('ship.id', 153, 10), 6510: ('ship.id', 154, 10), 6551: ('ship.id', 155, 10), 6592: ('ship.id', 156, 10), 6633: ('ship.id', 157, 10), 6674: ('ship.id', 158, 10), 6743: ('ship.id', 162, 28), 6810: ('ship.id', 163, 16), 6855: ('ship.id', 164, 13), 6914: ('ship.id', 167, 28), 6973: ('ship.id', 168, 16), 7023: ('ship.id', 169, 16), 7073: ('ship.id', 170, 16), 7120: ('ship.id', 171, 13), 7171: ('ship.id', 174, 14), 7219: ('ship.id', 176, 10), 7286: ('ship.id', 179, 10), 7432: ('python:range(3)', 185, 32), 7454: ('switch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount_${speed_factor}, cargo_count*100/cargo_capacity) {\n        0 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[0]};\n        1..100 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[4]}; // log tug is binary: loaded or unloaded; no intermediate fractional speeds\n        return 0; // should never reach this result, make it show up as a problem\n    }', 186, 4), 7482: ('ship.id', 186, 32), 7530: ('speed_factor', 186, 80), 7593: ('ship.get_speeds_adjusted_for_load_amount(speed_factor)[0]', 187, 14), 7672: ('ship.get_speeds_adjusted_for_load_amount(speed_factor)[4]', 188, 19), 7909: ('switch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount, param_adjust_ship_speed) {\n    0: ${ship.id}_switch_speed_varies_with_load_amount_0;\n    1: ${ship.id}_switch_speed_varies_with_load_amount_1;\n    2: ${ship.id}_switch_speed_varies_with_load_amount_2;\n}\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_purchase_speed, param_adjust_ship_speed) {\n    0: ${ship.get_speeds_adjusted_for_load_amount(0)[4]};\n    1: ${ship.get_speeds_adjusted_for_load_amount(1)[4]};\n    2: ${ship.get_speeds_adjusted_for_load_amount(2)[4]};\n}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}', 192, 0), 7937: ('ship.id', 192, 28), 8020: ('ship.id', 193, 9), 8078: ('ship.id', 194, 9), 8136: ('ship.id', 195, 9), 8215: ('ship.id', 197, 28), 8283: ('ship.get_speeds_adjusted_for_load_amount(0)[4]', 198, 9), 8341: ('ship.get_speeds_adjusted_for_load_amount(1)[4]', 199, 9), 8399: ('ship.get_speeds_adjusted_for_load_amount(2)[4]', 200, 9), 8453: ('ship.render_cargo_capacity()', 203, 2), 8486: ('ship.render_properties()', 205, 2)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

import re
import functools
from itertools import chain as __chain
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

            # <Interpolation value=<Substitution '${ship.render_debug_info()}\n\n// graphics\n' (1:0)> braces_required=True translation=False at 7efdb0510a58> -> __content_139628066513336
            __token = 0
            __token = 2
            __content_139628066513336 = _lookup_attr(getitem('ship'), 'render_debug_info')()
            __content_139628066513336 = __quote(__content_139628066513336, '\x00', '&#0;', None, False)
            __content_139628066513336 = ('%s%s' % ((__content_139628066513336 if (__content_139628066513336 is not None) else ''), '\n\n// graphics\n', ))
            if (__content_139628066513336 is None):
                pass
            else:
                if (__content_139628066513336 is False):
                    __content_139628066513336 = None
                else:
                    __tt = type(__content_139628066513336)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139628066513336 = str(__content_139628066513336)
                    else:
                        if (__tt is bytes):
                            __content_139628066513336 = decode(__content_139628066513336)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139628066513336 = __content_139628066513336.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139628066513336)
                                    __content_139628066513336 = (str(__content_139628066513336) if (__content_139628066513336 is __converted) else __converted)
                                else:
                                    __content_139628066513336 = __content_139628066513336()
            if (__content_139628066513336 is not None):
                __append(__content_139628066513336)
            __backup_states_139628050308232 = get('states', __marker)

            # <Value "python:{'not_moving': 0 ,'moving': 600}" (4:35)> -> __value
            __token = 76
            __value = {'not_moving': 0, 'moving': 600, }
            econtext['states'] = __value
            __backup_x_y_crops_139628050453168 = get('x_y_crops', __marker)

            # <Value "python:('28, 89', '113, 66', '138, 48', '113, 66')" (5:37)> -> __value
            __token = 154
            __value = ('28, 89', '113, 66', '138, 48', '113, 66', )
            econtext['x_y_crops'] = __value
            __backup_state_139628049819240 = get('state', __marker)

            # <Value 'states' (6:34)> -> __iterator
            __token = 241
            __iterator = getitem('states')
            (__iterator, ____index_139628049926800, ) = getitem('repeat')('state', __iterator)
            econtext['state'] = None
            for __item in __iterator:
                econtext['state'] = __item
                __append('\n    ')
                __backup_y_start_139628049819296 = get('y_start', __marker)

                # <Value 'python:states[state]' (7:37)> -> __value
                __token = 287
                __value = getitem('states')[getitem('state')]
                econtext['y_start'] = __value

                # <Interpolation value=<Substitution '\n        spriteset(${ship.id}_ss_not_loaded_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 10}, ${x_y_crops[0]},  -13,  -6]\n            [60,  ${y_start + 10}, ${x_y_crops[1]}, -124,   5]\n            [186, ${y_start + 10}, ${x_y_crops[2]}, -124, -28]\n            [328, ${y_start + 10}, ${x_y_crops[3]},  -76, -37]\n            [454, ${y_start + 10}, ${x_y_crops[0]},  -14, -76]\n            [494, ${y_start + 10}, ${x_y_crops[1]},  -34, -38]\n            [620, ${y_start + 10}, ${x_y_crops[2]},  -15, -28]\n            [762, ${y_start + 10}, ${x_y_crops[3]},   15,   6]\n        }\n        spriteset(${ship.id}_ss_load_1_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 110}, ${x_y_crops[0]},  -13, -14]\n            [60,  ${y_start + 110}, ${x_y_crops[1]}, -118,   1]\n            [186, ${y_start + 110}, ${x_y_crops[2]}, -112, -28]\n            [328, ${y_start + 110}, ${x_y_crops[3]},  -64, -32]\n            [454, ${y_start + 110}, ${x_y_crops[0]},  -14, -65]\n            [494, ${y_start + 110}, ${x_y_crops[1]},  -45, -32]\n            [620, ${y_start + 110}, ${x_y_crops[2]},  -26, -28]\n            [762, ${y_start + 110}, ${x_y_crops[3]},    2,   0]\n        }\n        spriteset(${ship.id}_ss_load_2_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 210}, ${x_y_crops[0]},  -13, -21]\n            [60,  ${y_start + 210}, ${x_y_crops[1]}, -107,  -4]\n            [186, ${y_start + 210}, ${x_y_crops[2]}, -100, -28]\n            [328, ${y_start + 210}, ${x_y_crops[3]},  -59, -30]\n            [454, ${y_start + 210}, ${x_y_crops[0]},  -14, -57]\n            [494, ${y_start + 210}, ${x_y_crops[1]},  -53, -30]\n            [620, ${y_start + 210}, ${x_y_crops[2]},  -49, -28]\n            [762, ${y_start + 210}, ${x_y_crops[3]},   -4,  -4]\n        }\n        spriteset(${ship.id}_ss_load_3_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 310}, ${x_y_crops[0]},  -13, -29]\n            [60,  ${y_start + 310}, ${x_y_crops[1]}, -102,  -8]\n            [186, ${y_start + 310}, ${x_y_crops[2]},  -84, -28]\n            [328, ${y_start + 310}, ${x_y_crops[3]},  -48, -26]\n            [454, ${y_start + 310}, ${x_y_crops[0]},  -14, -47]\n            [494, ${y_start + 310}, ${x_y_crops[1]},  -60, -25]\n            [620, ${y_start + 310}, ${x_y_crops[2]},  -50, -28]\n            [762, ${y_start + 310}, ${x_y_crops[3]},   -7,  -6]\n        }\n        spriteset(${ship.id}_ss_load_4_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 410}, ${x_y_crops[0]},  -13, -35]\n            [60,  ${y_start + 410}, ${x_y_crops[1]},  -97, -10]\n            [186, ${y_start + 410}, ${x_y_crops[2]},  -69, -28]\n            [328, ${y_start + 410}, ${x_y_crops[3]},  -45, -22]\n            [454, ${y_start + 410}, ${x_y_crops[0]},  -14, -45]\n            [494, ${y_start + 410}, ${x_y_crops[1]},  -66, -22]\n            [620, ${y_start + 410}, ${x_y_crops[2]},  -61, -28]\n            [762, ${y_start + 410}, ${x_y_crops[3]},  -15, -10]\n        }\n        spriteset(${ship.id}_ss_load_5_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 510}, ${x_y_crops[0]},  -13, -41]\n            [60,  ${y_start + 510}, ${x_y_crops[1]},  -90, -13]\n            [186, ${y_start + 510}, ${x_y_crops[2]},  -65, -28]\n            [328, ${y_start + 510}, ${x_y_crops[3]},  -40, -19]\n            [454, ${y_start + 510}, ${x_y_crops[0]},  -14, -42]\n            [494, ${y_start + 510}, ${x_y_crops[1]},  -75, -17]\n            [620, ${y_start + 510}, ${x_y_crops[2]},  -68, -28]\n            [762, ${y_start + 510}, ${x_y_crops[3]},  -22, -13]\n        }\n    ' (7:59)> braces_required=True translation=False at 7efdb05109b0> -> __content_139628066513336
                __token = 318
                __token = 330
                __content_139628066513336 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336 = __quote(__content_139628066513336, '\x00', '&#0;', None, False)
                __token = 355
                __content_139628066513336_353 = getitem('state')
                __content_139628066513336_353 = __quote(__content_139628066513336_353, '\x00', '&#0;', None, False)
                __token = 379
                __content_139628066513336_377 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336_377 = __quote(__content_139628066513336_377, '\x00', '&#0;', None, False)
                __token = 418
                __content_139628066513336_416 = (getitem('y_start') + 10)
                __content_139628066513336_416 = __quote(__content_139628066513336_416, '\x00', '&#0;', None, False)
                __token = 435
                __content_139628066513336_433 = getitem('x_y_crops')[0]
                __content_139628066513336_433 = __quote(__content_139628066513336_433, '\x00', '&#0;', None, False)
                __token = 481
                __content_139628066513336_479 = (getitem('y_start') + 10)
                __content_139628066513336_479 = __quote(__content_139628066513336_479, '\x00', '&#0;', None, False)
                __token = 498
                __content_139628066513336_496 = getitem('x_y_crops')[1]
                __content_139628066513336_496 = __quote(__content_139628066513336_496, '\x00', '&#0;', None, False)
                __token = 544
                __content_139628066513336_542 = (getitem('y_start') + 10)
                __content_139628066513336_542 = __quote(__content_139628066513336_542, '\x00', '&#0;', None, False)
                __token = 561
                __content_139628066513336_559 = getitem('x_y_crops')[2]
                __content_139628066513336_559 = __quote(__content_139628066513336_559, '\x00', '&#0;', None, False)
                __token = 607
                __content_139628066513336_605 = (getitem('y_start') + 10)
                __content_139628066513336_605 = __quote(__content_139628066513336_605, '\x00', '&#0;', None, False)
                __token = 624
                __content_139628066513336_622 = getitem('x_y_crops')[3]
                __content_139628066513336_622 = __quote(__content_139628066513336_622, '\x00', '&#0;', None, False)
                __token = 670
                __content_139628066513336_668 = (getitem('y_start') + 10)
                __content_139628066513336_668 = __quote(__content_139628066513336_668, '\x00', '&#0;', None, False)
                __token = 687
                __content_139628066513336_685 = getitem('x_y_crops')[0]
                __content_139628066513336_685 = __quote(__content_139628066513336_685, '\x00', '&#0;', None, False)
                __token = 733
                __content_139628066513336_731 = (getitem('y_start') + 10)
                __content_139628066513336_731 = __quote(__content_139628066513336_731, '\x00', '&#0;', None, False)
                __token = 750
                __content_139628066513336_748 = getitem('x_y_crops')[1]
                __content_139628066513336_748 = __quote(__content_139628066513336_748, '\x00', '&#0;', None, False)
                __token = 796
                __content_139628066513336_794 = (getitem('y_start') + 10)
                __content_139628066513336_794 = __quote(__content_139628066513336_794, '\x00', '&#0;', None, False)
                __token = 813
                __content_139628066513336_811 = getitem('x_y_crops')[2]
                __content_139628066513336_811 = __quote(__content_139628066513336_811, '\x00', '&#0;', None, False)
                __token = 859
                __content_139628066513336_857 = (getitem('y_start') + 10)
                __content_139628066513336_857 = __quote(__content_139628066513336_857, '\x00', '&#0;', None, False)
                __token = 876
                __content_139628066513336_874 = getitem('x_y_crops')[3]
                __content_139628066513336_874 = __quote(__content_139628066513336_874, '\x00', '&#0;', None, False)
                __token = 932
                __content_139628066513336_930 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336_930 = __quote(__content_139628066513336_930, '\x00', '&#0;', None, False)
                __token = 953
                __content_139628066513336_951 = getitem('state')
                __content_139628066513336_951 = __quote(__content_139628066513336_951, '\x00', '&#0;', None, False)
                __token = 977
                __content_139628066513336_975 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336_975 = __quote(__content_139628066513336_975, '\x00', '&#0;', None, False)
                __token = 1016
                __content_139628066513336_1014 = (getitem('y_start') + 110)
                __content_139628066513336_1014 = __quote(__content_139628066513336_1014, '\x00', '&#0;', None, False)
                __token = 1034
                __content_139628066513336_1032 = getitem('x_y_crops')[0]
                __content_139628066513336_1032 = __quote(__content_139628066513336_1032, '\x00', '&#0;', None, False)
                __token = 1080
                __content_139628066513336_1078 = (getitem('y_start') + 110)
                __content_139628066513336_1078 = __quote(__content_139628066513336_1078, '\x00', '&#0;', None, False)
                __token = 1098
                __content_139628066513336_1096 = getitem('x_y_crops')[1]
                __content_139628066513336_1096 = __quote(__content_139628066513336_1096, '\x00', '&#0;', None, False)
                __token = 1144
                __content_139628066513336_1142 = (getitem('y_start') + 110)
                __content_139628066513336_1142 = __quote(__content_139628066513336_1142, '\x00', '&#0;', None, False)
                __token = 1162
                __content_139628066513336_1160 = getitem('x_y_crops')[2]
                __content_139628066513336_1160 = __quote(__content_139628066513336_1160, '\x00', '&#0;', None, False)
                __token = 1208
                __content_139628066513336_1206 = (getitem('y_start') + 110)
                __content_139628066513336_1206 = __quote(__content_139628066513336_1206, '\x00', '&#0;', None, False)
                __token = 1226
                __content_139628066513336_1224 = getitem('x_y_crops')[3]
                __content_139628066513336_1224 = __quote(__content_139628066513336_1224, '\x00', '&#0;', None, False)
                __token = 1272
                __content_139628066513336_1270 = (getitem('y_start') + 110)
                __content_139628066513336_1270 = __quote(__content_139628066513336_1270, '\x00', '&#0;', None, False)
                __token = 1290
                __content_139628066513336_1288 = getitem('x_y_crops')[0]
                __content_139628066513336_1288 = __quote(__content_139628066513336_1288, '\x00', '&#0;', None, False)
                __token = 1336
                __content_139628066513336_1334 = (getitem('y_start') + 110)
                __content_139628066513336_1334 = __quote(__content_139628066513336_1334, '\x00', '&#0;', None, False)
                __token = 1354
                __content_139628066513336_1352 = getitem('x_y_crops')[1]
                __content_139628066513336_1352 = __quote(__content_139628066513336_1352, '\x00', '&#0;', None, False)
                __token = 1400
                __content_139628066513336_1398 = (getitem('y_start') + 110)
                __content_139628066513336_1398 = __quote(__content_139628066513336_1398, '\x00', '&#0;', None, False)
                __token = 1418
                __content_139628066513336_1416 = getitem('x_y_crops')[2]
                __content_139628066513336_1416 = __quote(__content_139628066513336_1416, '\x00', '&#0;', None, False)
                __token = 1464
                __content_139628066513336_1462 = (getitem('y_start') + 110)
                __content_139628066513336_1462 = __quote(__content_139628066513336_1462, '\x00', '&#0;', None, False)
                __token = 1482
                __content_139628066513336_1480 = getitem('x_y_crops')[3]
                __content_139628066513336_1480 = __quote(__content_139628066513336_1480, '\x00', '&#0;', None, False)
                __token = 1538
                __content_139628066513336_1536 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336_1536 = __quote(__content_139628066513336_1536, '\x00', '&#0;', None, False)
                __token = 1559
                __content_139628066513336_1557 = getitem('state')
                __content_139628066513336_1557 = __quote(__content_139628066513336_1557, '\x00', '&#0;', None, False)
                __token = 1583
                __content_139628066513336_1581 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336_1581 = __quote(__content_139628066513336_1581, '\x00', '&#0;', None, False)
                __token = 1622
                __content_139628066513336_1620 = (getitem('y_start') + 210)
                __content_139628066513336_1620 = __quote(__content_139628066513336_1620, '\x00', '&#0;', None, False)
                __token = 1640
                __content_139628066513336_1638 = getitem('x_y_crops')[0]
                __content_139628066513336_1638 = __quote(__content_139628066513336_1638, '\x00', '&#0;', None, False)
                __token = 1686
                __content_139628066513336_1684 = (getitem('y_start') + 210)
                __content_139628066513336_1684 = __quote(__content_139628066513336_1684, '\x00', '&#0;', None, False)
                __token = 1704
                __content_139628066513336_1702 = getitem('x_y_crops')[1]
                __content_139628066513336_1702 = __quote(__content_139628066513336_1702, '\x00', '&#0;', None, False)
                __token = 1750
                __content_139628066513336_1748 = (getitem('y_start') + 210)
                __content_139628066513336_1748 = __quote(__content_139628066513336_1748, '\x00', '&#0;', None, False)
                __token = 1768
                __content_139628066513336_1766 = getitem('x_y_crops')[2]
                __content_139628066513336_1766 = __quote(__content_139628066513336_1766, '\x00', '&#0;', None, False)
                __token = 1814
                __content_139628066513336_1812 = (getitem('y_start') + 210)
                __content_139628066513336_1812 = __quote(__content_139628066513336_1812, '\x00', '&#0;', None, False)
                __token = 1832
                __content_139628066513336_1830 = getitem('x_y_crops')[3]
                __content_139628066513336_1830 = __quote(__content_139628066513336_1830, '\x00', '&#0;', None, False)
                __token = 1878
                __content_139628066513336_1876 = (getitem('y_start') + 210)
                __content_139628066513336_1876 = __quote(__content_139628066513336_1876, '\x00', '&#0;', None, False)
                __token = 1896
                __content_139628066513336_1894 = getitem('x_y_crops')[0]
                __content_139628066513336_1894 = __quote(__content_139628066513336_1894, '\x00', '&#0;', None, False)
                __token = 1942
                __content_139628066513336_1940 = (getitem('y_start') + 210)
                __content_139628066513336_1940 = __quote(__content_139628066513336_1940, '\x00', '&#0;', None, False)
                __token = 1960
                __content_139628066513336_1958 = getitem('x_y_crops')[1]
                __content_139628066513336_1958 = __quote(__content_139628066513336_1958, '\x00', '&#0;', None, False)
                __token = 2006
                __content_139628066513336_2004 = (getitem('y_start') + 210)
                __content_139628066513336_2004 = __quote(__content_139628066513336_2004, '\x00', '&#0;', None, False)
                __token = 2024
                __content_139628066513336_2022 = getitem('x_y_crops')[2]
                __content_139628066513336_2022 = __quote(__content_139628066513336_2022, '\x00', '&#0;', None, False)
                __token = 2070
                __content_139628066513336_2068 = (getitem('y_start') + 210)
                __content_139628066513336_2068 = __quote(__content_139628066513336_2068, '\x00', '&#0;', None, False)
                __token = 2088
                __content_139628066513336_2086 = getitem('x_y_crops')[3]
                __content_139628066513336_2086 = __quote(__content_139628066513336_2086, '\x00', '&#0;', None, False)
                __token = 2144
                __content_139628066513336_2142 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336_2142 = __quote(__content_139628066513336_2142, '\x00', '&#0;', None, False)
                __token = 2165
                __content_139628066513336_2163 = getitem('state')
                __content_139628066513336_2163 = __quote(__content_139628066513336_2163, '\x00', '&#0;', None, False)
                __token = 2189
                __content_139628066513336_2187 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336_2187 = __quote(__content_139628066513336_2187, '\x00', '&#0;', None, False)
                __token = 2228
                __content_139628066513336_2226 = (getitem('y_start') + 310)
                __content_139628066513336_2226 = __quote(__content_139628066513336_2226, '\x00', '&#0;', None, False)
                __token = 2246
                __content_139628066513336_2244 = getitem('x_y_crops')[0]
                __content_139628066513336_2244 = __quote(__content_139628066513336_2244, '\x00', '&#0;', None, False)
                __token = 2292
                __content_139628066513336_2290 = (getitem('y_start') + 310)
                __content_139628066513336_2290 = __quote(__content_139628066513336_2290, '\x00', '&#0;', None, False)
                __token = 2310
                __content_139628066513336_2308 = getitem('x_y_crops')[1]
                __content_139628066513336_2308 = __quote(__content_139628066513336_2308, '\x00', '&#0;', None, False)
                __token = 2356
                __content_139628066513336_2354 = (getitem('y_start') + 310)
                __content_139628066513336_2354 = __quote(__content_139628066513336_2354, '\x00', '&#0;', None, False)
                __token = 2374
                __content_139628066513336_2372 = getitem('x_y_crops')[2]
                __content_139628066513336_2372 = __quote(__content_139628066513336_2372, '\x00', '&#0;', None, False)
                __token = 2420
                __content_139628066513336_2418 = (getitem('y_start') + 310)
                __content_139628066513336_2418 = __quote(__content_139628066513336_2418, '\x00', '&#0;', None, False)
                __token = 2438
                __content_139628066513336_2436 = getitem('x_y_crops')[3]
                __content_139628066513336_2436 = __quote(__content_139628066513336_2436, '\x00', '&#0;', None, False)
                __token = 2484
                __content_139628066513336_2482 = (getitem('y_start') + 310)
                __content_139628066513336_2482 = __quote(__content_139628066513336_2482, '\x00', '&#0;', None, False)
                __token = 2502
                __content_139628066513336_2500 = getitem('x_y_crops')[0]
                __content_139628066513336_2500 = __quote(__content_139628066513336_2500, '\x00', '&#0;', None, False)
                __token = 2548
                __content_139628066513336_2546 = (getitem('y_start') + 310)
                __content_139628066513336_2546 = __quote(__content_139628066513336_2546, '\x00', '&#0;', None, False)
                __token = 2566
                __content_139628066513336_2564 = getitem('x_y_crops')[1]
                __content_139628066513336_2564 = __quote(__content_139628066513336_2564, '\x00', '&#0;', None, False)
                __token = 2612
                __content_139628066513336_2610 = (getitem('y_start') + 310)
                __content_139628066513336_2610 = __quote(__content_139628066513336_2610, '\x00', '&#0;', None, False)
                __token = 2630
                __content_139628066513336_2628 = getitem('x_y_crops')[2]
                __content_139628066513336_2628 = __quote(__content_139628066513336_2628, '\x00', '&#0;', None, False)
                __token = 2676
                __content_139628066513336_2674 = (getitem('y_start') + 310)
                __content_139628066513336_2674 = __quote(__content_139628066513336_2674, '\x00', '&#0;', None, False)
                __token = 2694
                __content_139628066513336_2692 = getitem('x_y_crops')[3]
                __content_139628066513336_2692 = __quote(__content_139628066513336_2692, '\x00', '&#0;', None, False)
                __token = 2750
                __content_139628066513336_2748 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336_2748 = __quote(__content_139628066513336_2748, '\x00', '&#0;', None, False)
                __token = 2771
                __content_139628066513336_2769 = getitem('state')
                __content_139628066513336_2769 = __quote(__content_139628066513336_2769, '\x00', '&#0;', None, False)
                __token = 2795
                __content_139628066513336_2793 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336_2793 = __quote(__content_139628066513336_2793, '\x00', '&#0;', None, False)
                __token = 2834
                __content_139628066513336_2832 = (getitem('y_start') + 410)
                __content_139628066513336_2832 = __quote(__content_139628066513336_2832, '\x00', '&#0;', None, False)
                __token = 2852
                __content_139628066513336_2850 = getitem('x_y_crops')[0]
                __content_139628066513336_2850 = __quote(__content_139628066513336_2850, '\x00', '&#0;', None, False)
                __token = 2898
                __content_139628066513336_2896 = (getitem('y_start') + 410)
                __content_139628066513336_2896 = __quote(__content_139628066513336_2896, '\x00', '&#0;', None, False)
                __token = 2916
                __content_139628066513336_2914 = getitem('x_y_crops')[1]
                __content_139628066513336_2914 = __quote(__content_139628066513336_2914, '\x00', '&#0;', None, False)
                __token = 2962
                __content_139628066513336_2960 = (getitem('y_start') + 410)
                __content_139628066513336_2960 = __quote(__content_139628066513336_2960, '\x00', '&#0;', None, False)
                __token = 2980
                __content_139628066513336_2978 = getitem('x_y_crops')[2]
                __content_139628066513336_2978 = __quote(__content_139628066513336_2978, '\x00', '&#0;', None, False)
                __token = 3026
                __content_139628066513336_3024 = (getitem('y_start') + 410)
                __content_139628066513336_3024 = __quote(__content_139628066513336_3024, '\x00', '&#0;', None, False)
                __token = 3044
                __content_139628066513336_3042 = getitem('x_y_crops')[3]
                __content_139628066513336_3042 = __quote(__content_139628066513336_3042, '\x00', '&#0;', None, False)
                __token = 3090
                __content_139628066513336_3088 = (getitem('y_start') + 410)
                __content_139628066513336_3088 = __quote(__content_139628066513336_3088, '\x00', '&#0;', None, False)
                __token = 3108
                __content_139628066513336_3106 = getitem('x_y_crops')[0]
                __content_139628066513336_3106 = __quote(__content_139628066513336_3106, '\x00', '&#0;', None, False)
                __token = 3154
                __content_139628066513336_3152 = (getitem('y_start') + 410)
                __content_139628066513336_3152 = __quote(__content_139628066513336_3152, '\x00', '&#0;', None, False)
                __token = 3172
                __content_139628066513336_3170 = getitem('x_y_crops')[1]
                __content_139628066513336_3170 = __quote(__content_139628066513336_3170, '\x00', '&#0;', None, False)
                __token = 3218
                __content_139628066513336_3216 = (getitem('y_start') + 410)
                __content_139628066513336_3216 = __quote(__content_139628066513336_3216, '\x00', '&#0;', None, False)
                __token = 3236
                __content_139628066513336_3234 = getitem('x_y_crops')[2]
                __content_139628066513336_3234 = __quote(__content_139628066513336_3234, '\x00', '&#0;', None, False)
                __token = 3282
                __content_139628066513336_3280 = (getitem('y_start') + 410)
                __content_139628066513336_3280 = __quote(__content_139628066513336_3280, '\x00', '&#0;', None, False)
                __token = 3300
                __content_139628066513336_3298 = getitem('x_y_crops')[3]
                __content_139628066513336_3298 = __quote(__content_139628066513336_3298, '\x00', '&#0;', None, False)
                __token = 3356
                __content_139628066513336_3354 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336_3354 = __quote(__content_139628066513336_3354, '\x00', '&#0;', None, False)
                __token = 3377
                __content_139628066513336_3375 = getitem('state')
                __content_139628066513336_3375 = __quote(__content_139628066513336_3375, '\x00', '&#0;', None, False)
                __token = 3401
                __content_139628066513336_3399 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336_3399 = __quote(__content_139628066513336_3399, '\x00', '&#0;', None, False)
                __token = 3440
                __content_139628066513336_3438 = (getitem('y_start') + 510)
                __content_139628066513336_3438 = __quote(__content_139628066513336_3438, '\x00', '&#0;', None, False)
                __token = 3458
                __content_139628066513336_3456 = getitem('x_y_crops')[0]
                __content_139628066513336_3456 = __quote(__content_139628066513336_3456, '\x00', '&#0;', None, False)
                __token = 3504
                __content_139628066513336_3502 = (getitem('y_start') + 510)
                __content_139628066513336_3502 = __quote(__content_139628066513336_3502, '\x00', '&#0;', None, False)
                __token = 3522
                __content_139628066513336_3520 = getitem('x_y_crops')[1]
                __content_139628066513336_3520 = __quote(__content_139628066513336_3520, '\x00', '&#0;', None, False)
                __token = 3568
                __content_139628066513336_3566 = (getitem('y_start') + 510)
                __content_139628066513336_3566 = __quote(__content_139628066513336_3566, '\x00', '&#0;', None, False)
                __token = 3586
                __content_139628066513336_3584 = getitem('x_y_crops')[2]
                __content_139628066513336_3584 = __quote(__content_139628066513336_3584, '\x00', '&#0;', None, False)
                __token = 3632
                __content_139628066513336_3630 = (getitem('y_start') + 510)
                __content_139628066513336_3630 = __quote(__content_139628066513336_3630, '\x00', '&#0;', None, False)
                __token = 3650
                __content_139628066513336_3648 = getitem('x_y_crops')[3]
                __content_139628066513336_3648 = __quote(__content_139628066513336_3648, '\x00', '&#0;', None, False)
                __token = 3696
                __content_139628066513336_3694 = (getitem('y_start') + 510)
                __content_139628066513336_3694 = __quote(__content_139628066513336_3694, '\x00', '&#0;', None, False)
                __token = 3714
                __content_139628066513336_3712 = getitem('x_y_crops')[0]
                __content_139628066513336_3712 = __quote(__content_139628066513336_3712, '\x00', '&#0;', None, False)
                __token = 3760
                __content_139628066513336_3758 = (getitem('y_start') + 510)
                __content_139628066513336_3758 = __quote(__content_139628066513336_3758, '\x00', '&#0;', None, False)
                __token = 3778
                __content_139628066513336_3776 = getitem('x_y_crops')[1]
                __content_139628066513336_3776 = __quote(__content_139628066513336_3776, '\x00', '&#0;', None, False)
                __token = 3824
                __content_139628066513336_3822 = (getitem('y_start') + 510)
                __content_139628066513336_3822 = __quote(__content_139628066513336_3822, '\x00', '&#0;', None, False)
                __token = 3842
                __content_139628066513336_3840 = getitem('x_y_crops')[2]
                __content_139628066513336_3840 = __quote(__content_139628066513336_3840, '\x00', '&#0;', None, False)
                __token = 3888
                __content_139628066513336_3886 = (getitem('y_start') + 510)
                __content_139628066513336_3886 = __quote(__content_139628066513336_3886, '\x00', '&#0;', None, False)
                __token = 3906
                __content_139628066513336_3904 = getitem('x_y_crops')[3]
                __content_139628066513336_3904 = __quote(__content_139628066513336_3904, '\x00', '&#0;', None, False)
                __content_139628066513336 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        spriteset(', (__content_139628066513336 if (__content_139628066513336 is not None) else ''), '_ss_not_loaded_', (__content_139628066513336_353 if (__content_139628066513336_353 is not None) else ''), ', "src/graphics/', (__content_139628066513336_377 if (__content_139628066513336_377 is not None) else ''), '_0.png") {\n            [20,  ', (__content_139628066513336_416 if (__content_139628066513336_416 is not None) else ''), ', ', (__content_139628066513336_433 if (__content_139628066513336_433 is not None) else ''), ',  -13,  -6]\n            [60,  ', (__content_139628066513336_479 if (__content_139628066513336_479 is not None) else ''), ', ', (__content_139628066513336_496 if (__content_139628066513336_496 is not None) else ''), ', -124,   5]\n            [186, ', (__content_139628066513336_542 if (__content_139628066513336_542 is not None) else ''), ', ', (__content_139628066513336_559 if (__content_139628066513336_559 is not None) else ''), ', -124, -28]\n            [328, ', (__content_139628066513336_605 if (__content_139628066513336_605 is not None) else ''), ', ', (__content_139628066513336_622 if (__content_139628066513336_622 is not None) else ''), ',  -76, -37]\n            [454, ', (__content_139628066513336_668 if (__content_139628066513336_668 is not None) else ''), ', ', (__content_139628066513336_685 if (__content_139628066513336_685 is not None) else ''), ',  -14, -76]\n            [494, ', (__content_139628066513336_731 if (__content_139628066513336_731 is not None) else ''), ', ', (__content_139628066513336_748 if (__content_139628066513336_748 is not None) else ''), ',  -34, -38]\n            [620, ', (__content_139628066513336_794 if (__content_139628066513336_794 is not None) else ''), ', ', (__content_139628066513336_811 if (__content_139628066513336_811 is not None) else ''), ',  -15, -28]\n            [762, ', (__content_139628066513336_857 if (__content_139628066513336_857 is not None) else ''), ', ', (__content_139628066513336_874 if (__content_139628066513336_874 is not None) else ''), ',   15,   6]\n        }\n        spriteset(', (__content_139628066513336_930 if (__content_139628066513336_930 is not None) else ''), '_ss_load_1_', (__content_139628066513336_951 if (__content_139628066513336_951 is not None) else ''), ', "src/graphics/', (__content_139628066513336_975 if (__content_139628066513336_975 is not None) else ''), '_0.png") {\n            [20,  ', (__content_139628066513336_1014 if (__content_139628066513336_1014 is not None) else ''), ', ', (__content_139628066513336_1032 if (__content_139628066513336_1032 is not None) else ''), ',  -13, -14]\n            [60,  ', (__content_139628066513336_1078 if (__content_139628066513336_1078 is not None) else ''), ', ', (__content_139628066513336_1096 if (__content_139628066513336_1096 is not None) else ''), ', -118,   1]\n            [186, ', (__content_139628066513336_1142 if (__content_139628066513336_1142 is not None) else ''), ', ', (__content_139628066513336_1160 if (__content_139628066513336_1160 is not None) else ''), ', -112, -28]\n            [328, ', (__content_139628066513336_1206 if (__content_139628066513336_1206 is not None) else ''), ', ', (__content_139628066513336_1224 if (__content_139628066513336_1224 is not None) else ''), ',  -64, -32]\n            [454, ', (__content_139628066513336_1270 if (__content_139628066513336_1270 is not None) else ''), ', ', (__content_139628066513336_1288 if (__content_139628066513336_1288 is not None) else ''), ',  -14, -65]\n            [494, ', (__content_139628066513336_1334 if (__content_139628066513336_1334 is not None) else ''), ', ', (__content_139628066513336_1352 if (__content_139628066513336_1352 is not None) else ''), ',  -45, -32]\n            [620, ', (__content_139628066513336_1398 if (__content_139628066513336_1398 is not None) else ''), ', ', (__content_139628066513336_1416 if (__content_139628066513336_1416 is not None) else ''), ',  -26, -28]\n            [762, ', (__content_139628066513336_1462 if (__content_139628066513336_1462 is not None) else ''), ', ', (__content_139628066513336_1480 if (__content_139628066513336_1480 is not None) else ''), ',    2,   0]\n        }\n        spriteset(', (__content_139628066513336_1536 if (__content_139628066513336_1536 is not None) else ''), '_ss_load_2_', (__content_139628066513336_1557 if (__content_139628066513336_1557 is not None) else ''), ', "src/graphics/', (__content_139628066513336_1581 if (__content_139628066513336_1581 is not None) else ''), '_0.png") {\n            [20,  ', (__content_139628066513336_1620 if (__content_139628066513336_1620 is not None) else ''), ', ', (__content_139628066513336_1638 if (__content_139628066513336_1638 is not None) else ''), ',  -13, -21]\n            [60,  ', (__content_139628066513336_1684 if (__content_139628066513336_1684 is not None) else ''), ', ', (__content_139628066513336_1702 if (__content_139628066513336_1702 is not None) else ''), ', -107,  -4]\n            [186, ', (__content_139628066513336_1748 if (__content_139628066513336_1748 is not None) else ''), ', ', (__content_139628066513336_1766 if (__content_139628066513336_1766 is not None) else ''), ', -100, -28]\n            [328, ', (__content_139628066513336_1812 if (__content_139628066513336_1812 is not None) else ''), ', ', (__content_139628066513336_1830 if (__content_139628066513336_1830 is not None) else ''), ',  -59, -30]\n            [454, ', (__content_139628066513336_1876 if (__content_139628066513336_1876 is not None) else ''), ', ', (__content_139628066513336_1894 if (__content_139628066513336_1894 is not None) else ''), ',  -14, -57]\n            [494, ', (__content_139628066513336_1940 if (__content_139628066513336_1940 is not None) else ''), ', ', (__content_139628066513336_1958 if (__content_139628066513336_1958 is not None) else ''), ',  -53, -30]\n            [620, ', (__content_139628066513336_2004 if (__content_139628066513336_2004 is not None) else ''), ', ', (__content_139628066513336_2022 if (__content_139628066513336_2022 is not None) else ''), ',  -49, -28]\n            [762, ', (__content_139628066513336_2068 if (__content_139628066513336_2068 is not None) else ''), ', ', (__content_139628066513336_2086 if (__content_139628066513336_2086 is not None) else ''), ',   -4,  -4]\n        }\n        spriteset(', (__content_139628066513336_2142 if (__content_139628066513336_2142 is not None) else ''), '_ss_load_3_', (__content_139628066513336_2163 if (__content_139628066513336_2163 is not None) else ''), ', "src/graphics/', (__content_139628066513336_2187 if (__content_139628066513336_2187 is not None) else ''), '_0.png") {\n            [20,  ', (__content_139628066513336_2226 if (__content_139628066513336_2226 is not None) else ''), ', ', (__content_139628066513336_2244 if (__content_139628066513336_2244 is not None) else ''), ',  -13, -29]\n            [60,  ', (__content_139628066513336_2290 if (__content_139628066513336_2290 is not None) else ''), ', ', (__content_139628066513336_2308 if (__content_139628066513336_2308 is not None) else ''), ', -102,  -8]\n            [186, ', (__content_139628066513336_2354 if (__content_139628066513336_2354 is not None) else ''), ', ', (__content_139628066513336_2372 if (__content_139628066513336_2372 is not None) else ''), ',  -84, -28]\n            [328, ', (__content_139628066513336_2418 if (__content_139628066513336_2418 is not None) else ''), ', ', (__content_139628066513336_2436 if (__content_139628066513336_2436 is not None) else ''), ',  -48, -26]\n            [454, ', (__content_139628066513336_2482 if (__content_139628066513336_2482 is not None) else ''), ', ', (__content_139628066513336_2500 if (__content_139628066513336_2500 is not None) else ''), ',  -14, -47]\n            [494, ', (__content_139628066513336_2546 if (__content_139628066513336_2546 is not None) else ''), ', ', (__content_139628066513336_2564 if (__content_139628066513336_2564 is not None) else ''), ',  -60, -25]\n            [620, ', (__content_139628066513336_2610 if (__content_139628066513336_2610 is not None) else ''), ', ', (__content_139628066513336_2628 if (__content_139628066513336_2628 is not None) else ''), ',  -50, -28]\n            [762, ', (__content_139628066513336_2674 if (__content_139628066513336_2674 is not None) else ''), ', ', (__content_139628066513336_2692 if (__content_139628066513336_2692 is not None) else ''), ',   -7,  -6]\n        }\n        spriteset(', (__content_139628066513336_2748 if (__content_139628066513336_2748 is not None) else ''), '_ss_load_4_', (__content_139628066513336_2769 if (__content_139628066513336_2769 is not None) else ''), ', "src/graphics/', (__content_139628066513336_2793 if (__content_139628066513336_2793 is not None) else ''), '_0.png") {\n            [20,  ', (__content_139628066513336_2832 if (__content_139628066513336_2832 is not None) else ''), ', ', (__content_139628066513336_2850 if (__content_139628066513336_2850 is not None) else ''), ',  -13, -35]\n            [60,  ', (__content_139628066513336_2896 if (__content_139628066513336_2896 is not None) else ''), ', ', (__content_139628066513336_2914 if (__content_139628066513336_2914 is not None) else ''), ',  -97, -10]\n            [186, ', (__content_139628066513336_2960 if (__content_139628066513336_2960 is not None) else ''), ', ', (__content_139628066513336_2978 if (__content_139628066513336_2978 is not None) else ''), ',  -69, -28]\n            [328, ', (__content_139628066513336_3024 if (__content_139628066513336_3024 is not None) else ''), ', ', (__content_139628066513336_3042 if (__content_139628066513336_3042 is not None) else ''), ',  -45, -22]\n            [454, ', (__content_139628066513336_3088 if (__content_139628066513336_3088 is not None) else ''), ', ', (__content_139628066513336_3106 if (__content_139628066513336_3106 is not None) else ''), ',  -14, -45]\n            [494, ', (__content_139628066513336_3152 if (__content_139628066513336_3152 is not None) else ''), ', ', (__content_139628066513336_3170 if (__content_139628066513336_3170 is not None) else ''), ',  -66, -22]\n            [620, ', (__content_139628066513336_3216 if (__content_139628066513336_3216 is not None) else ''), ', ', (__content_139628066513336_3234 if (__content_139628066513336_3234 is not None) else ''), ',  -61, -28]\n            [762, ', (__content_139628066513336_3280 if (__content_139628066513336_3280 is not None) else ''), ', ', (__content_139628066513336_3298 if (__content_139628066513336_3298 is not None) else ''), ',  -15, -10]\n        }\n        spriteset(', (__content_139628066513336_3354 if (__content_139628066513336_3354 is not None) else ''), '_ss_load_5_', (__content_139628066513336_3375 if (__content_139628066513336_3375 is not None) else ''), ', "src/graphics/', (__content_139628066513336_3399 if (__content_139628066513336_3399 is not None) else ''), '_0.png") {\n            [20,  ', (__content_139628066513336_3438 if (__content_139628066513336_3438 is not None) else ''), ', ', (__content_139628066513336_3456 if (__content_139628066513336_3456 is not None) else ''), ',  -13, -41]\n            [60,  ', (__content_139628066513336_3502 if (__content_139628066513336_3502 is not None) else ''), ', ', (__content_139628066513336_3520 if (__content_139628066513336_3520 is not None) else ''), ',  -90, -13]\n            [186, ', (__content_139628066513336_3566 if (__content_139628066513336_3566 is not None) else ''), ', ', (__content_139628066513336_3584 if (__content_139628066513336_3584 is not None) else ''), ',  -65, -28]\n            [328, ', (__content_139628066513336_3630 if (__content_139628066513336_3630 is not None) else ''), ', ', (__content_139628066513336_3648 if (__content_139628066513336_3648 is not None) else ''), ',  -40, -19]\n            [454, ', (__content_139628066513336_3694 if (__content_139628066513336_3694 is not None) else ''), ', ', (__content_139628066513336_3712 if (__content_139628066513336_3712 is not None) else ''), ',  -14, -42]\n            [494, ', (__content_139628066513336_3758 if (__content_139628066513336_3758 is not None) else ''), ', ', (__content_139628066513336_3776 if (__content_139628066513336_3776 is not None) else ''), ',  -75, -17]\n            [620, ', (__content_139628066513336_3822 if (__content_139628066513336_3822 is not None) else ''), ', ', (__content_139628066513336_3840 if (__content_139628066513336_3840 is not None) else ''), ',  -68, -28]\n            [762, ', (__content_139628066513336_3886 if (__content_139628066513336_3886 is not None) else ''), ', ', (__content_139628066513336_3904 if (__content_139628066513336_3904 is not None) else ''), ',  -22, -13]\n        }\n    ', ))
                if (__content_139628066513336 is None):
                    pass
                else:
                    if (__content_139628066513336 is False):
                        __content_139628066513336 = None
                    else:
                        __tt = type(__content_139628066513336)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139628066513336 = str(__content_139628066513336)
                        else:
                            if (__tt is bytes):
                                __content_139628066513336 = decode(__content_139628066513336)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139628066513336 = __content_139628066513336.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139628066513336)
                                        __content_139628066513336 = (str(__content_139628066513336) if (__content_139628066513336 is __converted) else __converted)
                                    else:
                                        __content_139628066513336 = __content_139628066513336()
                if (__content_139628066513336 is not None):
                    __append(__content_139628066513336)
                if (__backup_y_start_139628049819296 is __marker):
                    del econtext['y_start']
                else:
                    econtext['y_start'] = __backup_y_start_139628049819296
                __append('\n')
                ____index_139628049926800 -= 1
                if (____index_139628049926800 > 0):
                    __append('')
            if (__backup_state_139628049819240 is __marker):
                del econtext['state']
            else:
                econtext['state'] = __backup_state_139628049819240
            if (__backup_states_139628050308232 is __marker):
                del econtext['states']
            else:
                econtext['states'] = __backup_states_139628050308232
            if (__backup_x_y_crops_139628050453168 is __marker):
                del econtext['x_y_crops']
            else:
                econtext['x_y_crops'] = __backup_x_y_crops_139628050453168

            # <Interpolation value=<Substitution "\n\nspritegroup ${ship.id}_sg_refit_0_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_0_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_0, current_speed) {\n    0: return ${ship.id}_sg_refit_0_not_moving;\n    return ${ship.id}_sg_refit_0_moving;\n}\n\nspritegroup ${ship.id}_sg_refit_1_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n        ${ship.id}_ss_load_2_moving,\n        ${ship.id}_ss_load_3_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_1_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_1, current_speed) {\n    0: return ${ship.id}_sg_refit_1_not_moving;\n    return ${ship.id}_sg_refit_1_moving;\n}\n\nspritegroup ${ship.id}_sg_refit_2_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n        ${ship.id}_ss_load_2_moving,\n        ${ship.id}_ss_load_3_moving,\n        ${ship.id}_ss_load_4_moving,\n        ${ship.id}_ss_load_5_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_2_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n        ${ship.id}_ss_load_4_not_moving,\n        ${ship.id}_ss_load_5_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n        ${ship.id}_ss_load_4_not_moving,\n        ${ship.id}_ss_load_5_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_2, current_speed) {\n    0: return ${ship.id}_sg_refit_2_not_moving;\n    return ${ship.id}_sg_refit_2_moving;\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, cargo_subtype) {\n    0: return ${ship.id}_switch_graphics_refit_0;\n    1: return ${ship.id}_switch_graphics_refit_1;\n    2: return ${ship.id}_switch_graphics_refit_2;\n    return ${ship.id}_switch_graphics_refit_0;\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n    ];\n}\n\n\n// -- set speed a little higher than rated speed when unladen -- //\n" (69:21)> braces_required=True translation=False at 7efdb0510ef0> -> __content_139628066513336
            __token = 3988
            __token = 4002
            __content_139628066513336 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336 = __quote(__content_139628066513336, '\x00', '&#0;', None, False)
            __token = 4056
            __content_139628066513336_4054 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4054 = __quote(__content_139628066513336_4054, '\x00', '&#0;', None, False)
            __token = 4097
            __content_139628066513336_4095 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4095 = __quote(__content_139628066513336_4095, '\x00', '&#0;', None, False)
            __token = 4238
            __content_139628066513336_4236 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4236 = __quote(__content_139628066513336_4236, '\x00', '&#0;', None, False)
            __token = 4293
            __content_139628066513336_4291 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4291 = __quote(__content_139628066513336_4291, '\x00', '&#0;', None, False)
            __token = 4351
            __content_139628066513336_4349 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4349 = __quote(__content_139628066513336_4349, '\x00', '&#0;', None, False)
            __token = 4396
            __content_139628066513336_4394 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4394 = __quote(__content_139628066513336_4394, '\x00', '&#0;', None, False)
            __token = 4459
            __content_139628066513336_4457 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4457 = __quote(__content_139628066513336_4457, '\x00', '&#0;', None, False)
            __token = 4504
            __content_139628066513336_4502 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4502 = __quote(__content_139628066513336_4502, '\x00', '&#0;', None, False)
            __token = 4573
            __content_139628066513336_4571 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4571 = __quote(__content_139628066513336_4571, '\x00', '&#0;', None, False)
            __token = 4640
            __content_139628066513336_4638 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4638 = __quote(__content_139628066513336_4638, '\x00', '&#0;', None, False)
            __token = 4685
            __content_139628066513336_4683 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4683 = __quote(__content_139628066513336_4683, '\x00', '&#0;', None, False)
            __token = 4730
            __content_139628066513336_4728 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4728 = __quote(__content_139628066513336_4728, '\x00', '&#0;', None, False)
            __token = 4784
            __content_139628066513336_4782 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4782 = __quote(__content_139628066513336_4782, '\x00', '&#0;', None, False)
            __token = 4825
            __content_139628066513336_4823 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4823 = __quote(__content_139628066513336_4823, '\x00', '&#0;', None, False)
            __token = 4862
            __content_139628066513336_4860 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4860 = __quote(__content_139628066513336_4860, '\x00', '&#0;', None, False)
            __token = 4899
            __content_139628066513336_4897 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_4897 = __quote(__content_139628066513336_4897, '\x00', '&#0;', None, False)
            __token = 5040
            __content_139628066513336_5038 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5038 = __quote(__content_139628066513336_5038, '\x00', '&#0;', None, False)
            __token = 5095
            __content_139628066513336_5093 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5093 = __quote(__content_139628066513336_5093, '\x00', '&#0;', None, False)
            __token = 5153
            __content_139628066513336_5151 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5151 = __quote(__content_139628066513336_5151, '\x00', '&#0;', None, False)
            __token = 5198
            __content_139628066513336_5196 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5196 = __quote(__content_139628066513336_5196, '\x00', '&#0;', None, False)
            __token = 5239
            __content_139628066513336_5237 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5237 = __quote(__content_139628066513336_5237, '\x00', '&#0;', None, False)
            __token = 5280
            __content_139628066513336_5278 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5278 = __quote(__content_139628066513336_5278, '\x00', '&#0;', None, False)
            __token = 5343
            __content_139628066513336_5341 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5341 = __quote(__content_139628066513336_5341, '\x00', '&#0;', None, False)
            __token = 5388
            __content_139628066513336_5386 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5386 = __quote(__content_139628066513336_5386, '\x00', '&#0;', None, False)
            __token = 5429
            __content_139628066513336_5427 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5427 = __quote(__content_139628066513336_5427, '\x00', '&#0;', None, False)
            __token = 5470
            __content_139628066513336_5468 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5468 = __quote(__content_139628066513336_5468, '\x00', '&#0;', None, False)
            __token = 5539
            __content_139628066513336_5537 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5537 = __quote(__content_139628066513336_5537, '\x00', '&#0;', None, False)
            __token = 5606
            __content_139628066513336_5604 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5604 = __quote(__content_139628066513336_5604, '\x00', '&#0;', None, False)
            __token = 5651
            __content_139628066513336_5649 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5649 = __quote(__content_139628066513336_5649, '\x00', '&#0;', None, False)
            __token = 5696
            __content_139628066513336_5694 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5694 = __quote(__content_139628066513336_5694, '\x00', '&#0;', None, False)
            __token = 5750
            __content_139628066513336_5748 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5748 = __quote(__content_139628066513336_5748, '\x00', '&#0;', None, False)
            __token = 5791
            __content_139628066513336_5789 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5789 = __quote(__content_139628066513336_5789, '\x00', '&#0;', None, False)
            __token = 5828
            __content_139628066513336_5826 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5826 = __quote(__content_139628066513336_5826, '\x00', '&#0;', None, False)
            __token = 5865
            __content_139628066513336_5863 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5863 = __quote(__content_139628066513336_5863, '\x00', '&#0;', None, False)
            __token = 5902
            __content_139628066513336_5900 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5900 = __quote(__content_139628066513336_5900, '\x00', '&#0;', None, False)
            __token = 5939
            __content_139628066513336_5937 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_5937 = __quote(__content_139628066513336_5937, '\x00', '&#0;', None, False)
            __token = 6080
            __content_139628066513336_6078 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6078 = __quote(__content_139628066513336_6078, '\x00', '&#0;', None, False)
            __token = 6135
            __content_139628066513336_6133 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6133 = __quote(__content_139628066513336_6133, '\x00', '&#0;', None, False)
            __token = 6193
            __content_139628066513336_6191 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6191 = __quote(__content_139628066513336_6191, '\x00', '&#0;', None, False)
            __token = 6238
            __content_139628066513336_6236 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6236 = __quote(__content_139628066513336_6236, '\x00', '&#0;', None, False)
            __token = 6279
            __content_139628066513336_6277 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6277 = __quote(__content_139628066513336_6277, '\x00', '&#0;', None, False)
            __token = 6320
            __content_139628066513336_6318 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6318 = __quote(__content_139628066513336_6318, '\x00', '&#0;', None, False)
            __token = 6361
            __content_139628066513336_6359 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6359 = __quote(__content_139628066513336_6359, '\x00', '&#0;', None, False)
            __token = 6402
            __content_139628066513336_6400 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6400 = __quote(__content_139628066513336_6400, '\x00', '&#0;', None, False)
            __token = 6465
            __content_139628066513336_6463 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6463 = __quote(__content_139628066513336_6463, '\x00', '&#0;', None, False)
            __token = 6510
            __content_139628066513336_6508 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6508 = __quote(__content_139628066513336_6508, '\x00', '&#0;', None, False)
            __token = 6551
            __content_139628066513336_6549 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6549 = __quote(__content_139628066513336_6549, '\x00', '&#0;', None, False)
            __token = 6592
            __content_139628066513336_6590 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6590 = __quote(__content_139628066513336_6590, '\x00', '&#0;', None, False)
            __token = 6633
            __content_139628066513336_6631 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6631 = __quote(__content_139628066513336_6631, '\x00', '&#0;', None, False)
            __token = 6674
            __content_139628066513336_6672 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6672 = __quote(__content_139628066513336_6672, '\x00', '&#0;', None, False)
            __token = 6743
            __content_139628066513336_6741 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6741 = __quote(__content_139628066513336_6741, '\x00', '&#0;', None, False)
            __token = 6810
            __content_139628066513336_6808 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6808 = __quote(__content_139628066513336_6808, '\x00', '&#0;', None, False)
            __token = 6855
            __content_139628066513336_6853 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6853 = __quote(__content_139628066513336_6853, '\x00', '&#0;', None, False)
            __token = 6914
            __content_139628066513336_6912 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6912 = __quote(__content_139628066513336_6912, '\x00', '&#0;', None, False)
            __token = 6973
            __content_139628066513336_6971 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_6971 = __quote(__content_139628066513336_6971, '\x00', '&#0;', None, False)
            __token = 7023
            __content_139628066513336_7021 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_7021 = __quote(__content_139628066513336_7021, '\x00', '&#0;', None, False)
            __token = 7073
            __content_139628066513336_7071 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_7071 = __quote(__content_139628066513336_7071, '\x00', '&#0;', None, False)
            __token = 7120
            __content_139628066513336_7118 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_7118 = __quote(__content_139628066513336_7118, '\x00', '&#0;', None, False)
            __token = 7171
            __content_139628066513336_7169 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_7169 = __quote(__content_139628066513336_7169, '\x00', '&#0;', None, False)
            __token = 7219
            __content_139628066513336_7217 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_7217 = __quote(__content_139628066513336_7217, '\x00', '&#0;', None, False)
            __token = 7286
            __content_139628066513336_7284 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_7284 = __quote(__content_139628066513336_7284, '\x00', '&#0;', None, False)
            __content_139628066513336 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n\nspritegroup ', (__content_139628066513336 if (__content_139628066513336 is not None) else ''), '_sg_refit_0_moving {\n    loaded:  [\n        ', (__content_139628066513336_4054 if (__content_139628066513336_4054 is not None) else ''), '_ss_not_loaded_moving,\n        ', (__content_139628066513336_4095 if (__content_139628066513336_4095 is not None) else ''), "_ss_load_1_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ", (__content_139628066513336_4236 if (__content_139628066513336_4236 is not None) else ''), '_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ', (__content_139628066513336_4291 if (__content_139628066513336_4291 is not None) else ''), '_sg_refit_0_not_moving {\n    loaded:  [\n        ', (__content_139628066513336_4349 if (__content_139628066513336_4349 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_139628066513336_4394 if (__content_139628066513336_4394 is not None) else ''), '_ss_load_1_not_moving,\n    ];\n    loading: [\n        ', (__content_139628066513336_4457 if (__content_139628066513336_4457 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_139628066513336_4502 if (__content_139628066513336_4502 is not None) else ''), '_ss_load_1_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_139628066513336_4571 if (__content_139628066513336_4571 is not None) else ''), '_switch_graphics_refit_0, current_speed) {\n    0: return ', (__content_139628066513336_4638 if (__content_139628066513336_4638 is not None) else ''), '_sg_refit_0_not_moving;\n    return ', (__content_139628066513336_4683 if (__content_139628066513336_4683 is not None) else ''), '_sg_refit_0_moving;\n}\n\nspritegroup ', (__content_139628066513336_4728 if (__content_139628066513336_4728 is not None) else ''), '_sg_refit_1_moving {\n    loaded:  [\n        ', (__content_139628066513336_4782 if (__content_139628066513336_4782 is not None) else ''), '_ss_not_loaded_moving,\n        ', (__content_139628066513336_4823 if (__content_139628066513336_4823 is not None) else ''), '_ss_load_1_moving,\n        ', (__content_139628066513336_4860 if (__content_139628066513336_4860 is not None) else ''), '_ss_load_2_moving,\n        ', (__content_139628066513336_4897 if (__content_139628066513336_4897 is not None) else ''), "_ss_load_3_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ", (__content_139628066513336_5038 if (__content_139628066513336_5038 is not None) else ''), '_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ', (__content_139628066513336_5093 if (__content_139628066513336_5093 is not None) else ''), '_sg_refit_1_not_moving {\n    loaded:  [\n        ', (__content_139628066513336_5151 if (__content_139628066513336_5151 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_139628066513336_5196 if (__content_139628066513336_5196 is not None) else ''), '_ss_load_1_not_moving,\n        ', (__content_139628066513336_5237 if (__content_139628066513336_5237 is not None) else ''), '_ss_load_2_not_moving,\n        ', (__content_139628066513336_5278 if (__content_139628066513336_5278 is not None) else ''), '_ss_load_3_not_moving,\n    ];\n    loading: [\n        ', (__content_139628066513336_5341 if (__content_139628066513336_5341 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_139628066513336_5386 if (__content_139628066513336_5386 is not None) else ''), '_ss_load_1_not_moving,\n        ', (__content_139628066513336_5427 if (__content_139628066513336_5427 is not None) else ''), '_ss_load_2_not_moving,\n        ', (__content_139628066513336_5468 if (__content_139628066513336_5468 is not None) else ''), '_ss_load_3_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_139628066513336_5537 if (__content_139628066513336_5537 is not None) else ''), '_switch_graphics_refit_1, current_speed) {\n    0: return ', (__content_139628066513336_5604 if (__content_139628066513336_5604 is not None) else ''), '_sg_refit_1_not_moving;\n    return ', (__content_139628066513336_5649 if (__content_139628066513336_5649 is not None) else ''), '_sg_refit_1_moving;\n}\n\nspritegroup ', (__content_139628066513336_5694 if (__content_139628066513336_5694 is not None) else ''), '_sg_refit_2_moving {\n    loaded:  [\n        ', (__content_139628066513336_5748 if (__content_139628066513336_5748 is not None) else ''), '_ss_not_loaded_moving,\n        ', (__content_139628066513336_5789 if (__content_139628066513336_5789 is not None) else ''), '_ss_load_1_moving,\n        ', (__content_139628066513336_5826 if (__content_139628066513336_5826 is not None) else ''), '_ss_load_2_moving,\n        ', (__content_139628066513336_5863 if (__content_139628066513336_5863 is not None) else ''), '_ss_load_3_moving,\n        ', (__content_139628066513336_5900 if (__content_139628066513336_5900 is not None) else ''), '_ss_load_4_moving,\n        ', (__content_139628066513336_5937 if (__content_139628066513336_5937 is not None) else ''), "_ss_load_5_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ", (__content_139628066513336_6078 if (__content_139628066513336_6078 is not None) else ''), '_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ', (__content_139628066513336_6133 if (__content_139628066513336_6133 is not None) else ''), '_sg_refit_2_not_moving {\n    loaded:  [\n        ', (__content_139628066513336_6191 if (__content_139628066513336_6191 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_139628066513336_6236 if (__content_139628066513336_6236 is not None) else ''), '_ss_load_1_not_moving,\n        ', (__content_139628066513336_6277 if (__content_139628066513336_6277 is not None) else ''), '_ss_load_2_not_moving,\n        ', (__content_139628066513336_6318 if (__content_139628066513336_6318 is not None) else ''), '_ss_load_3_not_moving,\n        ', (__content_139628066513336_6359 if (__content_139628066513336_6359 is not None) else ''), '_ss_load_4_not_moving,\n        ', (__content_139628066513336_6400 if (__content_139628066513336_6400 is not None) else ''), '_ss_load_5_not_moving,\n    ];\n    loading: [\n        ', (__content_139628066513336_6463 if (__content_139628066513336_6463 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_139628066513336_6508 if (__content_139628066513336_6508 is not None) else ''), '_ss_load_1_not_moving,\n        ', (__content_139628066513336_6549 if (__content_139628066513336_6549 is not None) else ''), '_ss_load_2_not_moving,\n        ', (__content_139628066513336_6590 if (__content_139628066513336_6590 is not None) else ''), '_ss_load_3_not_moving,\n        ', (__content_139628066513336_6631 if (__content_139628066513336_6631 is not None) else ''), '_ss_load_4_not_moving,\n        ', (__content_139628066513336_6672 if (__content_139628066513336_6672 is not None) else ''), '_ss_load_5_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_139628066513336_6741 if (__content_139628066513336_6741 is not None) else ''), '_switch_graphics_refit_2, current_speed) {\n    0: return ', (__content_139628066513336_6808 if (__content_139628066513336_6808 is not None) else ''), '_sg_refit_2_not_moving;\n    return ', (__content_139628066513336_6853 if (__content_139628066513336_6853 is not None) else ''), '_sg_refit_2_moving;\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_139628066513336_6912 if (__content_139628066513336_6912 is not None) else ''), '_switch_graphics, cargo_subtype) {\n    0: return ', (__content_139628066513336_6971 if (__content_139628066513336_6971 is not None) else ''), '_switch_graphics_refit_0;\n    1: return ', (__content_139628066513336_7021 if (__content_139628066513336_7021 is not None) else ''), '_switch_graphics_refit_1;\n    2: return ', (__content_139628066513336_7071 if (__content_139628066513336_7071 is not None) else ''), '_switch_graphics_refit_2;\n    return ', (__content_139628066513336_7118 if (__content_139628066513336_7118 is not None) else ''), '_switch_graphics_refit_0;\n}\n\nspritegroup ', (__content_139628066513336_7169 if (__content_139628066513336_7169 is not None) else ''), '_sg_purchase {\n    loaded:  [\n        ', (__content_139628066513336_7217 if (__content_139628066513336_7217 is not None) else ''), '_ss_not_loaded_not_moving,\n    ];\n    loading: [\n        ', (__content_139628066513336_7284 if (__content_139628066513336_7284 is not None) else ''), '_ss_not_loaded_not_moving,\n    ];\n}\n\n\n// -- set speed a little higher than rated speed when unladen -- //\n', ))
            if (__content_139628066513336 is None):
                pass
            else:
                if (__content_139628066513336 is False):
                    __content_139628066513336 = None
                else:
                    __tt = type(__content_139628066513336)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139628066513336 = str(__content_139628066513336)
                    else:
                        if (__tt is bytes):
                            __content_139628066513336 = decode(__content_139628066513336)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139628066513336 = __content_139628066513336.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139628066513336)
                                    __content_139628066513336 = (str(__content_139628066513336) if (__content_139628066513336 is __converted) else __converted)
                                else:
                                    __content_139628066513336 = __content_139628066513336()
            if (__content_139628066513336 is not None):
                __append(__content_139628066513336)
            __backup_speed_factor_139628049818456 = get('speed_factor', __marker)

            # <Value 'python:range(3)' (185:32)> -> __iterator
            __token = 7432
            __iterator = get('range', range)(3)
            (__iterator, ____index_139628049928032, ) = getitem('repeat')('speed_factor', __iterator)
            econtext['speed_factor'] = None
            for __item in __iterator:
                econtext['speed_factor'] = __item

                # <Interpolation value=<Substitution '\n    switch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount_${speed_factor}, cargo_count*100/cargo_capacity) {\n        0 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[0]};\n        1..100 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[4]}; // log tug is binary: loaded or unloaded; no intermediate fractional speeds\n        return 0; // should never reach this result, make it show up as a problem\n    }\n' (185:49)> braces_required=True translation=False at 7efdb0510fd0> -> __content_139628066513336
                __token = 7454
                __token = 7482
                __content_139628066513336 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336 = __quote(__content_139628066513336, '\x00', '&#0;', None, False)
                __token = 7530
                __content_139628066513336_7528 = getitem('speed_factor')
                __content_139628066513336_7528 = __quote(__content_139628066513336_7528, '\x00', '&#0;', None, False)
                __token = 7593
                __content_139628066513336_7591 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(getitem('speed_factor'))[0]
                __content_139628066513336_7591 = __quote(__content_139628066513336_7591, '\x00', '&#0;', None, False)
                __token = 7672
                __content_139628066513336_7670 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(getitem('speed_factor'))[4]
                __content_139628066513336_7670 = __quote(__content_139628066513336_7670, '\x00', '&#0;', None, False)
                __content_139628066513336 = ('%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_SHIPS, SELF, ', (__content_139628066513336 if (__content_139628066513336 is not None) else ''), '_switch_speed_varies_with_load_amount_', (__content_139628066513336_7528 if (__content_139628066513336_7528 is not None) else ''), ', cargo_count*100/cargo_capacity) {\n        0 : ', (__content_139628066513336_7591 if (__content_139628066513336_7591 is not None) else ''), ';\n        1..100 : ', (__content_139628066513336_7670 if (__content_139628066513336_7670 is not None) else ''), '; // log tug is binary: loaded or unloaded; no intermediate fractional speeds\n        return 0; // should never reach this result, make it show up as a problem\n    }\n', ))
                if (__content_139628066513336 is None):
                    pass
                else:
                    if (__content_139628066513336 is False):
                        __content_139628066513336 = None
                    else:
                        __tt = type(__content_139628066513336)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139628066513336 = str(__content_139628066513336)
                        else:
                            if (__tt is bytes):
                                __content_139628066513336 = decode(__content_139628066513336)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139628066513336 = __content_139628066513336.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139628066513336)
                                        __content_139628066513336 = (str(__content_139628066513336) if (__content_139628066513336 is __converted) else __converted)
                                    else:
                                        __content_139628066513336 = __content_139628066513336()
                if (__content_139628066513336 is not None):
                    __append(__content_139628066513336)
                ____index_139628049928032 -= 1
                if (____index_139628049928032 > 0):
                    __append('')
            if (__backup_speed_factor_139628049818456 is __marker):
                del econtext['speed_factor']
            else:
                econtext['speed_factor'] = __backup_speed_factor_139628049818456

            # <Interpolation value=<Substitution '\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount, param_adjust_ship_speed) {\n    0: ${ship.id}_switch_speed_varies_with_load_amount_0;\n    1: ${ship.id}_switch_speed_varies_with_load_amount_1;\n    2: ${ship.id}_switch_speed_varies_with_load_amount_2;\n}\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_purchase_speed, param_adjust_ship_speed) {\n    0: ${ship.get_speeds_adjusted_for_load_amount(0)[4]};\n    1: ${ship.get_speeds_adjusted_for_load_amount(1)[4]};\n    2: ${ship.get_speeds_adjusted_for_load_amount(2)[4]};\n}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}\n' (191:12)> braces_required=True translation=False at 7efdb0510c88> -> __content_139628066513336
            __token = 7909
            __token = 7937
            __content_139628066513336 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336 = __quote(__content_139628066513336, '\x00', '&#0;', None, False)
            __token = 8020
            __content_139628066513336_8018 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_8018 = __quote(__content_139628066513336_8018, '\x00', '&#0;', None, False)
            __token = 8078
            __content_139628066513336_8076 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_8076 = __quote(__content_139628066513336_8076, '\x00', '&#0;', None, False)
            __token = 8136
            __content_139628066513336_8134 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_8134 = __quote(__content_139628066513336_8134, '\x00', '&#0;', None, False)
            __token = 8215
            __content_139628066513336_8213 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_8213 = __quote(__content_139628066513336_8213, '\x00', '&#0;', None, False)
            __token = 8283
            __content_139628066513336_8281 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(0)[4]
            __content_139628066513336_8281 = __quote(__content_139628066513336_8281, '\x00', '&#0;', None, False)
            __token = 8341
            __content_139628066513336_8339 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(1)[4]
            __content_139628066513336_8339 = __quote(__content_139628066513336_8339, '\x00', '&#0;', None, False)
            __token = 8399
            __content_139628066513336_8397 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(2)[4]
            __content_139628066513336_8397 = __quote(__content_139628066513336_8397, '\x00', '&#0;', None, False)
            __token = 8453
            __content_139628066513336_8451 = _lookup_attr(getitem('ship'), 'render_cargo_capacity')()
            __content_139628066513336_8451 = __quote(__content_139628066513336_8451, '\x00', '&#0;', None, False)
            __token = 8486
            __content_139628066513336_8484 = _lookup_attr(getitem('ship'), 'render_properties')()
            __content_139628066513336_8484 = __quote(__content_139628066513336_8484, '\x00', '&#0;', None, False)
            __content_139628066513336 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\nswitch (FEAT_SHIPS, SELF, ', (__content_139628066513336 if (__content_139628066513336 is not None) else ''), '_switch_speed_varies_with_load_amount, param_adjust_ship_speed) {\n    0: ', (__content_139628066513336_8018 if (__content_139628066513336_8018 is not None) else ''), '_switch_speed_varies_with_load_amount_0;\n    1: ', (__content_139628066513336_8076 if (__content_139628066513336_8076 is not None) else ''), '_switch_speed_varies_with_load_amount_1;\n    2: ', (__content_139628066513336_8134 if (__content_139628066513336_8134 is not None) else ''), '_switch_speed_varies_with_load_amount_2;\n}\nswitch (FEAT_SHIPS, SELF, ', (__content_139628066513336_8213 if (__content_139628066513336_8213 is not None) else ''), '_switch_purchase_speed, param_adjust_ship_speed) {\n    0: ', (__content_139628066513336_8281 if (__content_139628066513336_8281 is not None) else ''), ';\n    1: ', (__content_139628066513336_8339 if (__content_139628066513336_8339 is not None) else ''), ';\n    2: ', (__content_139628066513336_8397 if (__content_139628066513336_8397 is not None) else ''), ';\n}\n\n', (__content_139628066513336_8451 if (__content_139628066513336_8451 is not None) else ''), '\n\n', (__content_139628066513336_8484 if (__content_139628066513336_8484 is not None) else ''), '\n', ))
            if (__content_139628066513336 is None):
                pass
            else:
                if (__content_139628066513336 is False):
                    __content_139628066513336 = None
                else:
                    __tt = type(__content_139628066513336)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139628066513336 = str(__content_139628066513336)
                    else:
                        if (__tt is bytes):
                            __content_139628066513336 = decode(__content_139628066513336)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139628066513336 = __content_139628066513336.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139628066513336)
                                    __content_139628066513336 = (str(__content_139628066513336) if (__content_139628066513336 is __converted) else __converted)
                                else:
                                    __content_139628066513336 = __content_139628066513336()
            if (__content_139628066513336 is not None):
                __append(__content_139628066513336)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }