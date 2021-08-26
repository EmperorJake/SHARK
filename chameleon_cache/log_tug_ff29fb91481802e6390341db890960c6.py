# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/SHARK/src/templates/log_tug.pynml'

__tokens = {0: ('${ship.render_debug_info()}\n\n// graphics', 1, 0), 2: ('ship.render_debug_info()', 1, 2), 76: ("python:{'not_moving': 0 ,'moving': 600}", 4, 35), 154: (" python:('28, 89', '113, 66', '138, 48', '113, 66'", 5, 37), 241: ('states', 6, 34), 287: ('python:states[state]', 7, 37), 318: ('spriteset(${ship.id}_ss_not_loaded_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 10}, ${x_y_crops[0]},  -13,  -6, ANIM]\n            [60,  ${y_start + 10}, ${x_y_crops[1]}, -124,   5, ANIM]\n            [186, ${y_start + 10}, ${x_y_crops[2]}, -124, -28, ANIM]\n            [328, ${y_start + 10}, ${x_y_crops[3]},  -76, -37, ANIM]\n            [454, ${y_start + 10}, ${x_y_crops[0]},  -14, -76, ANIM]\n            [494, ${y_start + 10}, ${x_y_crops[1]},  -34, -38, ANIM]\n            [620, ${y_start + 10}, ${x_y_crops[2]},  -15, -28, ANIM]\n            [762, ${y_start + 10}, ${x_y_crops[3]},   15,   6, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_1_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 110}, ${x_y_crops[0]},  -13, -14, ANIM]\n            [60,  ${y_start + 110}, ${x_y_crops[1]}, -118,   1, ANIM]\n            [186, ${y_start + 110}, ${x_y_crops[2]}, -112, -28, ANIM]\n            [328, ${y_start + 110}, ${x_y_crops[3]},  -64, -32, ANIM]\n            [454, ${y_start + 110}, ${x_y_crops[0]},  -14, -65, ANIM]\n            [494, ${y_start + 110}, ${x_y_crops[1]},  -45, -32, ANIM]\n            [620, ${y_start + 110}, ${x_y_crops[2]},  -26, -28, ANIM]\n            [762, ${y_start + 110}, ${x_y_crops[3]},    2,   0, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_2_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 210}, ${x_y_crops[0]},  -13, -21, ANIM]\n            [60,  ${y_start + 210}, ${x_y_crops[1]}, -107,  -4, ANIM]\n            [186, ${y_start + 210}, ${x_y_crops[2]}, -100, -28, ANIM]\n            [328, ${y_start + 210}, ${x_y_crops[3]},  -59, -30, ANIM]\n            [454, ${y_start + 210}, ${x_y_crops[0]},  -14, -57, ANIM]\n            [494, ${y_start + 210}, ${x_y_crops[1]},  -53, -30, ANIM]\n            [620, ${y_start + 210}, ${x_y_crops[2]},  -49, -28, ANIM]\n            [762, ${y_start + 210}, ${x_y_crops[3]},   -4,  -4, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_3_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 310}, ${x_y_crops[0]},  -13, -29, ANIM]\n            [60,  ${y_start + 310}, ${x_y_crops[1]}, -102,  -8, ANIM]\n            [186, ${y_start + 310}, ${x_y_crops[2]},  -84, -28, ANIM]\n            [328, ${y_start + 310}, ${x_y_crops[3]},  -48, -26, ANIM]\n            [454, ${y_start + 310}, ${x_y_crops[0]},  -14, -47, ANIM]\n            [494, ${y_start + 310}, ${x_y_crops[1]},  -60, -25, ANIM]\n            [620, ${y_start + 310}, ${x_y_crops[2]},  -50, -28, ANIM]\n            [762, ${y_start + 310}, ${x_y_crops[3]},   -7,  -6, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_4_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 410}, ${x_y_crops[0]},  -13, -35, ANIM]\n            [60,  ${y_start + 410}, ${x_y_crops[1]},  -97, -10, ANIM]\n            [186, ${y_start + 410}, ${x_y_crops[2]},  -69, -28, ANIM]\n            [328, ${y_start + 410}, ${x_y_crops[3]},  -45, -22, ANIM]\n            [454, ${y_start + 410}, ${x_y_crops[0]},  -14, -45, ANIM]\n            [494, ${y_start + 410}, ${x_y_crops[1]},  -66, -22, ANIM]\n            [620, ${y_start + 410}, ${x_y_crops[2]},  -61, -28, ANIM]\n            [762, ${y_start + 410}, ${x_y_crops[3]},  -15, -10, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_5_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 510}, ${x_y_crops[0]},  -13, -41]\n            [60,  ${y_start + 510}, ${x_y_crops[1]},  -90, -13]\n            [186, ${y_start + 510}, ${x_y_crops[2]},  -65, -28]\n            [328, ${y_start + 510}, ${x_y_crops[3]},  -40, -19]\n            [454, ${y_start + 510}, ${x_y_crops[0]},  -14, -42]\n            [494, ${y_start + 510}, ${x_y_crops[1]},  -75, -17]\n            [620, ${y_start + 510}, ${x_y_crops[2]},  -68, -28]\n            [762, ${y_start + 510}, ${x_y_crops[3]},  -22, -13]\n        }', 8, 8), 330: ('ship.id', 8, 20), 355: ('state', 8, 45), 379: ('ship.id', 8, 69), 418: ('y_start + 10', 9, 20), 435: ('x_y_crops[0]', 9, 37), 487: ('y_start + 10', 10, 20), 504: ('x_y_crops[1]', 10, 37), 556: ('y_start + 10', 11, 20), 573: ('x_y_crops[2]', 11, 37), 625: ('y_start + 10', 12, 20), 642: ('x_y_crops[3]', 12, 37), 694: ('y_start + 10', 13, 20), 711: ('x_y_crops[0]', 13, 37), 763: ('y_start + 10', 14, 20), 780: ('x_y_crops[1]', 14, 37), 832: ('y_start + 10', 15, 20), 849: ('x_y_crops[2]', 15, 37), 901: ('y_start + 10', 16, 20), 918: ('x_y_crops[3]', 16, 37), 980: ('ship.id', 18, 20), 1001: ('state', 18, 41), 1025: ('ship.id', 18, 65), 1064: ('y_start + 110', 19, 20), 1082: ('x_y_crops[0]', 19, 38), 1134: ('y_start + 110', 20, 20), 1152: ('x_y_crops[1]', 20, 38), 1204: ('y_start + 110', 21, 20), 1222: ('x_y_crops[2]', 21, 38), 1274: ('y_start + 110', 22, 20), 1292: ('x_y_crops[3]', 22, 38), 1344: ('y_start + 110', 23, 20), 1362: ('x_y_crops[0]', 23, 38), 1414: ('y_start + 110', 24, 20), 1432: ('x_y_crops[1]', 24, 38), 1484: ('y_start + 110', 25, 20), 1502: ('x_y_crops[2]', 25, 38), 1554: ('y_start + 110', 26, 20), 1572: ('x_y_crops[3]', 26, 38), 1634: ('ship.id', 28, 20), 1655: ('state', 28, 41), 1679: ('ship.id', 28, 65), 1718: ('y_start + 210', 29, 20), 1736: ('x_y_crops[0]', 29, 38), 1788: ('y_start + 210', 30, 20), 1806: ('x_y_crops[1]', 30, 38), 1858: ('y_start + 210', 31, 20), 1876: ('x_y_crops[2]', 31, 38), 1928: ('y_start + 210', 32, 20), 1946: ('x_y_crops[3]', 32, 38), 1998: ('y_start + 210', 33, 20), 2016: ('x_y_crops[0]', 33, 38), 2068: ('y_start + 210', 34, 20), 2086: ('x_y_crops[1]', 34, 38), 2138: ('y_start + 210', 35, 20), 2156: ('x_y_crops[2]', 35, 38), 2208: ('y_start + 210', 36, 20), 2226: ('x_y_crops[3]', 36, 38), 2288: ('ship.id', 38, 20), 2309: ('state', 38, 41), 2333: ('ship.id', 38, 65), 2372: ('y_start + 310', 39, 20), 2390: ('x_y_crops[0]', 39, 38), 2442: ('y_start + 310', 40, 20), 2460: ('x_y_crops[1]', 40, 38), 2512: ('y_start + 310', 41, 20), 2530: ('x_y_crops[2]', 41, 38), 2582: ('y_start + 310', 42, 20), 2600: ('x_y_crops[3]', 42, 38), 2652: ('y_start + 310', 43, 20), 2670: ('x_y_crops[0]', 43, 38), 2722: ('y_start + 310', 44, 20), 2740: ('x_y_crops[1]', 44, 38), 2792: ('y_start + 310', 45, 20), 2810: ('x_y_crops[2]', 45, 38), 2862: ('y_start + 310', 46, 20), 2880: ('x_y_crops[3]', 46, 38), 2942: ('ship.id', 48, 20), 2963: ('state', 48, 41), 2987: ('ship.id', 48, 65), 3026: ('y_start + 410', 49, 20), 3044: ('x_y_crops[0]', 49, 38), 3096: ('y_start + 410', 50, 20), 3114: ('x_y_crops[1]', 50, 38), 3166: ('y_start + 410', 51, 20), 3184: ('x_y_crops[2]', 51, 38), 3236: ('y_start + 410', 52, 20), 3254: ('x_y_crops[3]', 52, 38), 3306: ('y_start + 410', 53, 20), 3324: ('x_y_crops[0]', 53, 38), 3376: ('y_start + 410', 54, 20), 3394: ('x_y_crops[1]', 54, 38), 3446: ('y_start + 410', 55, 20), 3464: ('x_y_crops[2]', 55, 38), 3516: ('y_start + 410', 56, 20), 3534: ('x_y_crops[3]', 56, 38), 3596: ('ship.id', 58, 20), 3617: ('state', 58, 41), 3641: ('ship.id', 58, 65), 3680: ('y_start + 510', 59, 20), 3698: ('x_y_crops[0]', 59, 38), 3744: ('y_start + 510', 60, 20), 3762: ('x_y_crops[1]', 60, 38), 3808: ('y_start + 510', 61, 20), 3826: ('x_y_crops[2]', 61, 38), 3872: ('y_start + 510', 62, 20), 3890: ('x_y_crops[3]', 62, 38), 3936: ('y_start + 510', 63, 20), 3954: ('x_y_crops[0]', 63, 38), 4000: ('y_start + 510', 64, 20), 4018: ('x_y_crops[1]', 64, 38), 4064: ('y_start + 510', 65, 20), 4082: ('x_y_crops[2]', 65, 38), 4128: ('y_start + 510', 66, 20), 4146: ('x_y_crops[3]', 66, 38), 4228: ("spritegroup ${ship.id}_sg_refit_0_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_0_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_0, current_speed) {\n    0: return ${ship.id}_sg_refit_0_not_moving;\n    return ${ship.id}_sg_refit_0_moving;\n}\n\nspritegroup ${ship.id}_sg_refit_1_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n        ${ship.id}_ss_load_2_moving,\n        ${ship.id}_ss_load_3_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_1_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_1, current_speed) {\n    0: return ${ship.id}_sg_refit_1_not_moving;\n    return ${ship.id}_sg_refit_1_moving;\n}\n\nspritegroup ${ship.id}_sg_refit_2_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n        ${ship.id}_ss_load_2_moving,\n        ${ship.id}_ss_load_3_moving,\n        ${ship.id}_ss_load_4_moving,\n        ${ship.id}_ss_load_5_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_2_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n        ${ship.id}_ss_load_4_not_moving,\n        ${ship.id}_ss_load_5_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n        ${ship.id}_ss_load_4_not_moving,\n        ${ship.id}_ss_load_5_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_2, current_speed) {\n    0: return ${ship.id}_sg_refit_2_not_moving;\n    return ${ship.id}_sg_refit_2_moving;\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, cargo_subtype) {\n    0: return ${ship.id}_switch_graphics_refit_0;\n    1: return ${ship.id}_switch_graphics_refit_1;\n    2: return ${ship.id}_switch_graphics_refit_2;\n    return ${ship.id}_switch_graphics_refit_0;\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n    ];\n}\n\n\n// -- set speed a little higher than rated speed when unladen -- //", 71, 0), 4242: ('ship.id', 71, 14), 4296: ('ship.id', 73, 10), 4337: ('ship.id', 74, 10), 4478: ('ship.id', 77, 10), 4533: ('ship.id', 81, 14), 4591: ('ship.id', 83, 10), 4636: ('ship.id', 84, 10), 4699: ('ship.id', 87, 10), 4744: ('ship.id', 88, 10), 4813: ('ship.id', 92, 28), 4880: ('ship.id', 93, 16), 4925: ('ship.id', 94, 13), 4970: ('ship.id', 97, 14), 5024: ('ship.id', 99, 10), 5065: ('ship.id', 100, 10), 5102: ('ship.id', 101, 10), 5139: ('ship.id', 102, 10), 5280: ('ship.id', 105, 10), 5335: ('ship.id', 109, 14), 5393: ('ship.id', 111, 10), 5438: ('ship.id', 112, 10), 5479: ('ship.id', 113, 10), 5520: ('ship.id', 114, 10), 5583: ('ship.id', 117, 10), 5628: ('ship.id', 118, 10), 5669: ('ship.id', 119, 10), 5710: ('ship.id', 120, 10), 5779: ('ship.id', 124, 28), 5846: ('ship.id', 125, 16), 5891: ('ship.id', 126, 13), 5936: ('ship.id', 129, 14), 5990: ('ship.id', 131, 10), 6031: ('ship.id', 132, 10), 6068: ('ship.id', 133, 10), 6105: ('ship.id', 134, 10), 6142: ('ship.id', 135, 10), 6179: ('ship.id', 136, 10), 6320: ('ship.id', 139, 10), 6375: ('ship.id', 143, 14), 6433: ('ship.id', 145, 10), 6478: ('ship.id', 146, 10), 6519: ('ship.id', 147, 10), 6560: ('ship.id', 148, 10), 6601: ('ship.id', 149, 10), 6642: ('ship.id', 150, 10), 6705: ('ship.id', 153, 10), 6750: ('ship.id', 154, 10), 6791: ('ship.id', 155, 10), 6832: ('ship.id', 156, 10), 6873: ('ship.id', 157, 10), 6914: ('ship.id', 158, 10), 6983: ('ship.id', 162, 28), 7050: ('ship.id', 163, 16), 7095: ('ship.id', 164, 13), 7154: ('ship.id', 167, 28), 7213: ('ship.id', 168, 16), 7263: ('ship.id', 169, 16), 7313: ('ship.id', 170, 16), 7360: ('ship.id', 171, 13), 7411: ('ship.id', 174, 14), 7459: ('ship.id', 176, 10), 7526: ('ship.id', 179, 10), 7672: ('python:range(3)', 185, 32), 7694: ('switch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount_${speed_factor}, cargo_count*100/cargo_capacity) {\n        0 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[0]};\n        1..100 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[4]}; // log tug is binary: loaded or unloaded; no intermediate fractional speeds\n        return 0; // should never reach this result, make it show up as a problem\n    }', 186, 4), 7722: ('ship.id', 186, 32), 7770: ('speed_factor', 186, 80), 7833: ('ship.get_speeds_adjusted_for_load_amount(speed_factor)[0]', 187, 14), 7912: ('ship.get_speeds_adjusted_for_load_amount(speed_factor)[4]', 188, 19), 8149: ('switch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount, param_adjust_ship_speed) {\n    0: ${ship.id}_switch_speed_varies_with_load_amount_0;\n    1: ${ship.id}_switch_speed_varies_with_load_amount_1;\n    2: ${ship.id}_switch_speed_varies_with_load_amount_2;\n}\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_purchase_speed, param_adjust_ship_speed) {\n    0: ${ship.get_speeds_adjusted_for_load_amount(0)[4]};\n    1: ${ship.get_speeds_adjusted_for_load_amount(1)[4]};\n    2: ${ship.get_speeds_adjusted_for_load_amount(2)[4]};\n}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}', 192, 0), 8177: ('ship.id', 192, 28), 8260: ('ship.id', 193, 9), 8318: ('ship.id', 194, 9), 8376: ('ship.id', 195, 9), 8455: ('ship.id', 197, 28), 8523: ('ship.get_speeds_adjusted_for_load_amount(0)[4]', 198, 9), 8581: ('ship.get_speeds_adjusted_for_load_amount(1)[4]', 199, 9), 8639: ('ship.get_speeds_adjusted_for_load_amount(2)[4]', 200, 9), 8693: ('ship.render_cargo_capacity()', 203, 2), 8726: ('ship.render_properties()', 205, 2)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_140077370086064 = {}

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

            # <Interpolation value=<Substitution '${ship.render_debug_info()}\n\n// graphics\n' (1:0)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f664ddb8250> -> __content_140077375041712
            __token = 0
            __token = 2
            __content_140077375041712 = _lookup_attr(getitem('ship'), 'render_debug_info')()
            __content_140077375041712 = __quote(__content_140077375041712, '\x00', '&#0;', None, None)
            __content_140077375041712 = ('%s%s' % ((__content_140077375041712 if (__content_140077375041712 is not None) else ''), '\n\n// graphics\n', ))
            if (__content_140077375041712 is None):
                pass
            else:
                if (__content_140077375041712 is None):
                    __content_140077375041712 = None
                else:
                    __tt = type(__content_140077375041712)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140077375041712 = str(__content_140077375041712)
                    else:
                        if (__tt is bytes):
                            __content_140077375041712 = decode(__content_140077375041712)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140077375041712 = __content_140077375041712.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140077375041712)
                                    __content_140077375041712 = (str(__content_140077375041712) if (__content_140077375041712 is __converted) else __converted)
                                else:
                                    __content_140077375041712 = __content_140077375041712()
            if (__content_140077375041712 is not None):
                __append(__content_140077375041712)

            # <Static value=<_ast.Dict object at 0x7f664de292b0> name=None at 7f664de29160> -> __attrs_140077369624032
            __attrs_140077369624032 = _static_140077370086064
            __backup_states_140077380605264 = get('states', __marker)

            # <Value "python:{'not_moving': 0 ,'moving': 600}" (4:35)> -> __value
            __token = 76
            __value = {'not_moving': 0, 'moving': 600, }
            econtext['states'] = __value
            __backup_x_y_crops_140077380605312 = get('x_y_crops', __marker)

            # <Value "python:('28, 89', '113, 66', '138, 48', '113, 66')" (5:37)> -> __value
            __token = 154
            __value = ('28, 89', '113, 66', '138, 48', '113, 66', )
            econtext['x_y_crops'] = __value
            __backup_state_140077380605408 = get('state', __marker)

            # <Value 'states' (6:34)> -> __iterator
            __token = 241
            __iterator = getitem('states')
            (__iterator, ____index_140077369624656, ) = getitem('repeat')('state', __iterator)
            econtext['state'] = None
            for __item in __iterator:
                econtext['state'] = __item
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f664de292b0> name=None at 7f664de29160> -> __attrs_140077369625520
                __attrs_140077369625520 = _static_140077370086064
                __backup_y_start_140077380605504 = get('y_start', __marker)

                # <Value 'python:states[state]' (7:37)> -> __value
                __token = 287
                __value = getitem('states')[getitem('state')]
                econtext['y_start'] = __value

                # <Interpolation value=<Substitution '\n        spriteset(${ship.id}_ss_not_loaded_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 10}, ${x_y_crops[0]},  -13,  -6, ANIM]\n            [60,  ${y_start + 10}, ${x_y_crops[1]}, -124,   5, ANIM]\n            [186, ${y_start + 10}, ${x_y_crops[2]}, -124, -28, ANIM]\n            [328, ${y_start + 10}, ${x_y_crops[3]},  -76, -37, ANIM]\n            [454, ${y_start + 10}, ${x_y_crops[0]},  -14, -76, ANIM]\n            [494, ${y_start + 10}, ${x_y_crops[1]},  -34, -38, ANIM]\n            [620, ${y_start + 10}, ${x_y_crops[2]},  -15, -28, ANIM]\n            [762, ${y_start + 10}, ${x_y_crops[3]},   15,   6, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_1_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 110}, ${x_y_crops[0]},  -13, -14, ANIM]\n            [60,  ${y_start + 110}, ${x_y_crops[1]}, -118,   1, ANIM]\n            [186, ${y_start + 110}, ${x_y_crops[2]}, -112, -28, ANIM]\n            [328, ${y_start + 110}, ${x_y_crops[3]},  -64, -32, ANIM]\n            [454, ${y_start + 110}, ${x_y_crops[0]},  -14, -65, ANIM]\n            [494, ${y_start + 110}, ${x_y_crops[1]},  -45, -32, ANIM]\n            [620, ${y_start + 110}, ${x_y_crops[2]},  -26, -28, ANIM]\n            [762, ${y_start + 110}, ${x_y_crops[3]},    2,   0, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_2_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 210}, ${x_y_crops[0]},  -13, -21, ANIM]\n            [60,  ${y_start + 210}, ${x_y_crops[1]}, -107,  -4, ANIM]\n            [186, ${y_start + 210}, ${x_y_crops[2]}, -100, -28, ANIM]\n            [328, ${y_start + 210}, ${x_y_crops[3]},  -59, -30, ANIM]\n            [454, ${y_start + 210}, ${x_y_crops[0]},  -14, -57, ANIM]\n            [494, ${y_start + 210}, ${x_y_crops[1]},  -53, -30, ANIM]\n            [620, ${y_start + 210}, ${x_y_crops[2]},  -49, -28, ANIM]\n            [762, ${y_start + 210}, ${x_y_crops[3]},   -4,  -4, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_3_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 310}, ${x_y_crops[0]},  -13, -29, ANIM]\n            [60,  ${y_start + 310}, ${x_y_crops[1]}, -102,  -8, ANIM]\n            [186, ${y_start + 310}, ${x_y_crops[2]},  -84, -28, ANIM]\n            [328, ${y_start + 310}, ${x_y_crops[3]},  -48, -26, ANIM]\n            [454, ${y_start + 310}, ${x_y_crops[0]},  -14, -47, ANIM]\n            [494, ${y_start + 310}, ${x_y_crops[1]},  -60, -25, ANIM]\n            [620, ${y_start + 310}, ${x_y_crops[2]},  -50, -28, ANIM]\n            [762, ${y_start + 310}, ${x_y_crops[3]},   -7,  -6, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_4_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 410}, ${x_y_crops[0]},  -13, -35, ANIM]\n            [60,  ${y_start + 410}, ${x_y_crops[1]},  -97, -10, ANIM]\n            [186, ${y_start + 410}, ${x_y_crops[2]},  -69, -28, ANIM]\n            [328, ${y_start + 410}, ${x_y_crops[3]},  -45, -22, ANIM]\n            [454, ${y_start + 410}, ${x_y_crops[0]},  -14, -45, ANIM]\n            [494, ${y_start + 410}, ${x_y_crops[1]},  -66, -22, ANIM]\n            [620, ${y_start + 410}, ${x_y_crops[2]},  -61, -28, ANIM]\n            [762, ${y_start + 410}, ${x_y_crops[3]},  -15, -10, ANIM]\n        }\n        spriteset(${ship.id}_ss_load_5_${state}, "src/graphics/${ship.id}_0.png") {\n            [20,  ${y_start + 510}, ${x_y_crops[0]},  -13, -41]\n            [60,  ${y_start + 510}, ${x_y_crops[1]},  -90, -13]\n            [186, ${y_start + 510}, ${x_y_crops[2]},  -65, -28]\n            [328, ${y_start + 510}, ${x_y_crops[3]},  -40, -19]\n            [454, ${y_start + 510}, ${x_y_crops[0]},  -14, -42]\n            [494, ${y_start + 510}, ${x_y_crops[1]},  -75, -17]\n            [620, ${y_start + 510}, ${x_y_crops[2]},  -68, -28]\n            [762, ${y_start + 510}, ${x_y_crops[3]},  -22, -13]\n        }\n    ' (7:59)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f664ddb8dc0> -> __content_140077375041712
                __token = 318
                __token = 330
                __content_140077375041712 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712 = __quote(__content_140077375041712, '\x00', '&#0;', None, None)
                __token = 355
                __content_140077375041712_353 = getitem('state')
                __content_140077375041712_353 = __quote(__content_140077375041712_353, '\x00', '&#0;', None, None)
                __token = 379
                __content_140077375041712_377 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712_377 = __quote(__content_140077375041712_377, '\x00', '&#0;', None, None)
                __token = 418
                __content_140077375041712_416 = (getitem('y_start') + 10)
                __content_140077375041712_416 = __quote(__content_140077375041712_416, '\x00', '&#0;', None, None)
                __token = 435
                __content_140077375041712_433 = getitem('x_y_crops')[0]
                __content_140077375041712_433 = __quote(__content_140077375041712_433, '\x00', '&#0;', None, None)
                __token = 487
                __content_140077375041712_485 = (getitem('y_start') + 10)
                __content_140077375041712_485 = __quote(__content_140077375041712_485, '\x00', '&#0;', None, None)
                __token = 504
                __content_140077375041712_502 = getitem('x_y_crops')[1]
                __content_140077375041712_502 = __quote(__content_140077375041712_502, '\x00', '&#0;', None, None)
                __token = 556
                __content_140077375041712_554 = (getitem('y_start') + 10)
                __content_140077375041712_554 = __quote(__content_140077375041712_554, '\x00', '&#0;', None, None)
                __token = 573
                __content_140077375041712_571 = getitem('x_y_crops')[2]
                __content_140077375041712_571 = __quote(__content_140077375041712_571, '\x00', '&#0;', None, None)
                __token = 625
                __content_140077375041712_623 = (getitem('y_start') + 10)
                __content_140077375041712_623 = __quote(__content_140077375041712_623, '\x00', '&#0;', None, None)
                __token = 642
                __content_140077375041712_640 = getitem('x_y_crops')[3]
                __content_140077375041712_640 = __quote(__content_140077375041712_640, '\x00', '&#0;', None, None)
                __token = 694
                __content_140077375041712_692 = (getitem('y_start') + 10)
                __content_140077375041712_692 = __quote(__content_140077375041712_692, '\x00', '&#0;', None, None)
                __token = 711
                __content_140077375041712_709 = getitem('x_y_crops')[0]
                __content_140077375041712_709 = __quote(__content_140077375041712_709, '\x00', '&#0;', None, None)
                __token = 763
                __content_140077375041712_761 = (getitem('y_start') + 10)
                __content_140077375041712_761 = __quote(__content_140077375041712_761, '\x00', '&#0;', None, None)
                __token = 780
                __content_140077375041712_778 = getitem('x_y_crops')[1]
                __content_140077375041712_778 = __quote(__content_140077375041712_778, '\x00', '&#0;', None, None)
                __token = 832
                __content_140077375041712_830 = (getitem('y_start') + 10)
                __content_140077375041712_830 = __quote(__content_140077375041712_830, '\x00', '&#0;', None, None)
                __token = 849
                __content_140077375041712_847 = getitem('x_y_crops')[2]
                __content_140077375041712_847 = __quote(__content_140077375041712_847, '\x00', '&#0;', None, None)
                __token = 901
                __content_140077375041712_899 = (getitem('y_start') + 10)
                __content_140077375041712_899 = __quote(__content_140077375041712_899, '\x00', '&#0;', None, None)
                __token = 918
                __content_140077375041712_916 = getitem('x_y_crops')[3]
                __content_140077375041712_916 = __quote(__content_140077375041712_916, '\x00', '&#0;', None, None)
                __token = 980
                __content_140077375041712_978 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712_978 = __quote(__content_140077375041712_978, '\x00', '&#0;', None, None)
                __token = 1001
                __content_140077375041712_999 = getitem('state')
                __content_140077375041712_999 = __quote(__content_140077375041712_999, '\x00', '&#0;', None, None)
                __token = 1025
                __content_140077375041712_1023 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712_1023 = __quote(__content_140077375041712_1023, '\x00', '&#0;', None, None)
                __token = 1064
                __content_140077375041712_1062 = (getitem('y_start') + 110)
                __content_140077375041712_1062 = __quote(__content_140077375041712_1062, '\x00', '&#0;', None, None)
                __token = 1082
                __content_140077375041712_1080 = getitem('x_y_crops')[0]
                __content_140077375041712_1080 = __quote(__content_140077375041712_1080, '\x00', '&#0;', None, None)
                __token = 1134
                __content_140077375041712_1132 = (getitem('y_start') + 110)
                __content_140077375041712_1132 = __quote(__content_140077375041712_1132, '\x00', '&#0;', None, None)
                __token = 1152
                __content_140077375041712_1150 = getitem('x_y_crops')[1]
                __content_140077375041712_1150 = __quote(__content_140077375041712_1150, '\x00', '&#0;', None, None)
                __token = 1204
                __content_140077375041712_1202 = (getitem('y_start') + 110)
                __content_140077375041712_1202 = __quote(__content_140077375041712_1202, '\x00', '&#0;', None, None)
                __token = 1222
                __content_140077375041712_1220 = getitem('x_y_crops')[2]
                __content_140077375041712_1220 = __quote(__content_140077375041712_1220, '\x00', '&#0;', None, None)
                __token = 1274
                __content_140077375041712_1272 = (getitem('y_start') + 110)
                __content_140077375041712_1272 = __quote(__content_140077375041712_1272, '\x00', '&#0;', None, None)
                __token = 1292
                __content_140077375041712_1290 = getitem('x_y_crops')[3]
                __content_140077375041712_1290 = __quote(__content_140077375041712_1290, '\x00', '&#0;', None, None)
                __token = 1344
                __content_140077375041712_1342 = (getitem('y_start') + 110)
                __content_140077375041712_1342 = __quote(__content_140077375041712_1342, '\x00', '&#0;', None, None)
                __token = 1362
                __content_140077375041712_1360 = getitem('x_y_crops')[0]
                __content_140077375041712_1360 = __quote(__content_140077375041712_1360, '\x00', '&#0;', None, None)
                __token = 1414
                __content_140077375041712_1412 = (getitem('y_start') + 110)
                __content_140077375041712_1412 = __quote(__content_140077375041712_1412, '\x00', '&#0;', None, None)
                __token = 1432
                __content_140077375041712_1430 = getitem('x_y_crops')[1]
                __content_140077375041712_1430 = __quote(__content_140077375041712_1430, '\x00', '&#0;', None, None)
                __token = 1484
                __content_140077375041712_1482 = (getitem('y_start') + 110)
                __content_140077375041712_1482 = __quote(__content_140077375041712_1482, '\x00', '&#0;', None, None)
                __token = 1502
                __content_140077375041712_1500 = getitem('x_y_crops')[2]
                __content_140077375041712_1500 = __quote(__content_140077375041712_1500, '\x00', '&#0;', None, None)
                __token = 1554
                __content_140077375041712_1552 = (getitem('y_start') + 110)
                __content_140077375041712_1552 = __quote(__content_140077375041712_1552, '\x00', '&#0;', None, None)
                __token = 1572
                __content_140077375041712_1570 = getitem('x_y_crops')[3]
                __content_140077375041712_1570 = __quote(__content_140077375041712_1570, '\x00', '&#0;', None, None)
                __token = 1634
                __content_140077375041712_1632 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712_1632 = __quote(__content_140077375041712_1632, '\x00', '&#0;', None, None)
                __token = 1655
                __content_140077375041712_1653 = getitem('state')
                __content_140077375041712_1653 = __quote(__content_140077375041712_1653, '\x00', '&#0;', None, None)
                __token = 1679
                __content_140077375041712_1677 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712_1677 = __quote(__content_140077375041712_1677, '\x00', '&#0;', None, None)
                __token = 1718
                __content_140077375041712_1716 = (getitem('y_start') + 210)
                __content_140077375041712_1716 = __quote(__content_140077375041712_1716, '\x00', '&#0;', None, None)
                __token = 1736
                __content_140077375041712_1734 = getitem('x_y_crops')[0]
                __content_140077375041712_1734 = __quote(__content_140077375041712_1734, '\x00', '&#0;', None, None)
                __token = 1788
                __content_140077375041712_1786 = (getitem('y_start') + 210)
                __content_140077375041712_1786 = __quote(__content_140077375041712_1786, '\x00', '&#0;', None, None)
                __token = 1806
                __content_140077375041712_1804 = getitem('x_y_crops')[1]
                __content_140077375041712_1804 = __quote(__content_140077375041712_1804, '\x00', '&#0;', None, None)
                __token = 1858
                __content_140077375041712_1856 = (getitem('y_start') + 210)
                __content_140077375041712_1856 = __quote(__content_140077375041712_1856, '\x00', '&#0;', None, None)
                __token = 1876
                __content_140077375041712_1874 = getitem('x_y_crops')[2]
                __content_140077375041712_1874 = __quote(__content_140077375041712_1874, '\x00', '&#0;', None, None)
                __token = 1928
                __content_140077375041712_1926 = (getitem('y_start') + 210)
                __content_140077375041712_1926 = __quote(__content_140077375041712_1926, '\x00', '&#0;', None, None)
                __token = 1946
                __content_140077375041712_1944 = getitem('x_y_crops')[3]
                __content_140077375041712_1944 = __quote(__content_140077375041712_1944, '\x00', '&#0;', None, None)
                __token = 1998
                __content_140077375041712_1996 = (getitem('y_start') + 210)
                __content_140077375041712_1996 = __quote(__content_140077375041712_1996, '\x00', '&#0;', None, None)
                __token = 2016
                __content_140077375041712_2014 = getitem('x_y_crops')[0]
                __content_140077375041712_2014 = __quote(__content_140077375041712_2014, '\x00', '&#0;', None, None)
                __token = 2068
                __content_140077375041712_2066 = (getitem('y_start') + 210)
                __content_140077375041712_2066 = __quote(__content_140077375041712_2066, '\x00', '&#0;', None, None)
                __token = 2086
                __content_140077375041712_2084 = getitem('x_y_crops')[1]
                __content_140077375041712_2084 = __quote(__content_140077375041712_2084, '\x00', '&#0;', None, None)
                __token = 2138
                __content_140077375041712_2136 = (getitem('y_start') + 210)
                __content_140077375041712_2136 = __quote(__content_140077375041712_2136, '\x00', '&#0;', None, None)
                __token = 2156
                __content_140077375041712_2154 = getitem('x_y_crops')[2]
                __content_140077375041712_2154 = __quote(__content_140077375041712_2154, '\x00', '&#0;', None, None)
                __token = 2208
                __content_140077375041712_2206 = (getitem('y_start') + 210)
                __content_140077375041712_2206 = __quote(__content_140077375041712_2206, '\x00', '&#0;', None, None)
                __token = 2226
                __content_140077375041712_2224 = getitem('x_y_crops')[3]
                __content_140077375041712_2224 = __quote(__content_140077375041712_2224, '\x00', '&#0;', None, None)
                __token = 2288
                __content_140077375041712_2286 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712_2286 = __quote(__content_140077375041712_2286, '\x00', '&#0;', None, None)
                __token = 2309
                __content_140077375041712_2307 = getitem('state')
                __content_140077375041712_2307 = __quote(__content_140077375041712_2307, '\x00', '&#0;', None, None)
                __token = 2333
                __content_140077375041712_2331 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712_2331 = __quote(__content_140077375041712_2331, '\x00', '&#0;', None, None)
                __token = 2372
                __content_140077375041712_2370 = (getitem('y_start') + 310)
                __content_140077375041712_2370 = __quote(__content_140077375041712_2370, '\x00', '&#0;', None, None)
                __token = 2390
                __content_140077375041712_2388 = getitem('x_y_crops')[0]
                __content_140077375041712_2388 = __quote(__content_140077375041712_2388, '\x00', '&#0;', None, None)
                __token = 2442
                __content_140077375041712_2440 = (getitem('y_start') + 310)
                __content_140077375041712_2440 = __quote(__content_140077375041712_2440, '\x00', '&#0;', None, None)
                __token = 2460
                __content_140077375041712_2458 = getitem('x_y_crops')[1]
                __content_140077375041712_2458 = __quote(__content_140077375041712_2458, '\x00', '&#0;', None, None)
                __token = 2512
                __content_140077375041712_2510 = (getitem('y_start') + 310)
                __content_140077375041712_2510 = __quote(__content_140077375041712_2510, '\x00', '&#0;', None, None)
                __token = 2530
                __content_140077375041712_2528 = getitem('x_y_crops')[2]
                __content_140077375041712_2528 = __quote(__content_140077375041712_2528, '\x00', '&#0;', None, None)
                __token = 2582
                __content_140077375041712_2580 = (getitem('y_start') + 310)
                __content_140077375041712_2580 = __quote(__content_140077375041712_2580, '\x00', '&#0;', None, None)
                __token = 2600
                __content_140077375041712_2598 = getitem('x_y_crops')[3]
                __content_140077375041712_2598 = __quote(__content_140077375041712_2598, '\x00', '&#0;', None, None)
                __token = 2652
                __content_140077375041712_2650 = (getitem('y_start') + 310)
                __content_140077375041712_2650 = __quote(__content_140077375041712_2650, '\x00', '&#0;', None, None)
                __token = 2670
                __content_140077375041712_2668 = getitem('x_y_crops')[0]
                __content_140077375041712_2668 = __quote(__content_140077375041712_2668, '\x00', '&#0;', None, None)
                __token = 2722
                __content_140077375041712_2720 = (getitem('y_start') + 310)
                __content_140077375041712_2720 = __quote(__content_140077375041712_2720, '\x00', '&#0;', None, None)
                __token = 2740
                __content_140077375041712_2738 = getitem('x_y_crops')[1]
                __content_140077375041712_2738 = __quote(__content_140077375041712_2738, '\x00', '&#0;', None, None)
                __token = 2792
                __content_140077375041712_2790 = (getitem('y_start') + 310)
                __content_140077375041712_2790 = __quote(__content_140077375041712_2790, '\x00', '&#0;', None, None)
                __token = 2810
                __content_140077375041712_2808 = getitem('x_y_crops')[2]
                __content_140077375041712_2808 = __quote(__content_140077375041712_2808, '\x00', '&#0;', None, None)
                __token = 2862
                __content_140077375041712_2860 = (getitem('y_start') + 310)
                __content_140077375041712_2860 = __quote(__content_140077375041712_2860, '\x00', '&#0;', None, None)
                __token = 2880
                __content_140077375041712_2878 = getitem('x_y_crops')[3]
                __content_140077375041712_2878 = __quote(__content_140077375041712_2878, '\x00', '&#0;', None, None)
                __token = 2942
                __content_140077375041712_2940 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712_2940 = __quote(__content_140077375041712_2940, '\x00', '&#0;', None, None)
                __token = 2963
                __content_140077375041712_2961 = getitem('state')
                __content_140077375041712_2961 = __quote(__content_140077375041712_2961, '\x00', '&#0;', None, None)
                __token = 2987
                __content_140077375041712_2985 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712_2985 = __quote(__content_140077375041712_2985, '\x00', '&#0;', None, None)
                __token = 3026
                __content_140077375041712_3024 = (getitem('y_start') + 410)
                __content_140077375041712_3024 = __quote(__content_140077375041712_3024, '\x00', '&#0;', None, None)
                __token = 3044
                __content_140077375041712_3042 = getitem('x_y_crops')[0]
                __content_140077375041712_3042 = __quote(__content_140077375041712_3042, '\x00', '&#0;', None, None)
                __token = 3096
                __content_140077375041712_3094 = (getitem('y_start') + 410)
                __content_140077375041712_3094 = __quote(__content_140077375041712_3094, '\x00', '&#0;', None, None)
                __token = 3114
                __content_140077375041712_3112 = getitem('x_y_crops')[1]
                __content_140077375041712_3112 = __quote(__content_140077375041712_3112, '\x00', '&#0;', None, None)
                __token = 3166
                __content_140077375041712_3164 = (getitem('y_start') + 410)
                __content_140077375041712_3164 = __quote(__content_140077375041712_3164, '\x00', '&#0;', None, None)
                __token = 3184
                __content_140077375041712_3182 = getitem('x_y_crops')[2]
                __content_140077375041712_3182 = __quote(__content_140077375041712_3182, '\x00', '&#0;', None, None)
                __token = 3236
                __content_140077375041712_3234 = (getitem('y_start') + 410)
                __content_140077375041712_3234 = __quote(__content_140077375041712_3234, '\x00', '&#0;', None, None)
                __token = 3254
                __content_140077375041712_3252 = getitem('x_y_crops')[3]
                __content_140077375041712_3252 = __quote(__content_140077375041712_3252, '\x00', '&#0;', None, None)
                __token = 3306
                __content_140077375041712_3304 = (getitem('y_start') + 410)
                __content_140077375041712_3304 = __quote(__content_140077375041712_3304, '\x00', '&#0;', None, None)
                __token = 3324
                __content_140077375041712_3322 = getitem('x_y_crops')[0]
                __content_140077375041712_3322 = __quote(__content_140077375041712_3322, '\x00', '&#0;', None, None)
                __token = 3376
                __content_140077375041712_3374 = (getitem('y_start') + 410)
                __content_140077375041712_3374 = __quote(__content_140077375041712_3374, '\x00', '&#0;', None, None)
                __token = 3394
                __content_140077375041712_3392 = getitem('x_y_crops')[1]
                __content_140077375041712_3392 = __quote(__content_140077375041712_3392, '\x00', '&#0;', None, None)
                __token = 3446
                __content_140077375041712_3444 = (getitem('y_start') + 410)
                __content_140077375041712_3444 = __quote(__content_140077375041712_3444, '\x00', '&#0;', None, None)
                __token = 3464
                __content_140077375041712_3462 = getitem('x_y_crops')[2]
                __content_140077375041712_3462 = __quote(__content_140077375041712_3462, '\x00', '&#0;', None, None)
                __token = 3516
                __content_140077375041712_3514 = (getitem('y_start') + 410)
                __content_140077375041712_3514 = __quote(__content_140077375041712_3514, '\x00', '&#0;', None, None)
                __token = 3534
                __content_140077375041712_3532 = getitem('x_y_crops')[3]
                __content_140077375041712_3532 = __quote(__content_140077375041712_3532, '\x00', '&#0;', None, None)
                __token = 3596
                __content_140077375041712_3594 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712_3594 = __quote(__content_140077375041712_3594, '\x00', '&#0;', None, None)
                __token = 3617
                __content_140077375041712_3615 = getitem('state')
                __content_140077375041712_3615 = __quote(__content_140077375041712_3615, '\x00', '&#0;', None, None)
                __token = 3641
                __content_140077375041712_3639 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712_3639 = __quote(__content_140077375041712_3639, '\x00', '&#0;', None, None)
                __token = 3680
                __content_140077375041712_3678 = (getitem('y_start') + 510)
                __content_140077375041712_3678 = __quote(__content_140077375041712_3678, '\x00', '&#0;', None, None)
                __token = 3698
                __content_140077375041712_3696 = getitem('x_y_crops')[0]
                __content_140077375041712_3696 = __quote(__content_140077375041712_3696, '\x00', '&#0;', None, None)
                __token = 3744
                __content_140077375041712_3742 = (getitem('y_start') + 510)
                __content_140077375041712_3742 = __quote(__content_140077375041712_3742, '\x00', '&#0;', None, None)
                __token = 3762
                __content_140077375041712_3760 = getitem('x_y_crops')[1]
                __content_140077375041712_3760 = __quote(__content_140077375041712_3760, '\x00', '&#0;', None, None)
                __token = 3808
                __content_140077375041712_3806 = (getitem('y_start') + 510)
                __content_140077375041712_3806 = __quote(__content_140077375041712_3806, '\x00', '&#0;', None, None)
                __token = 3826
                __content_140077375041712_3824 = getitem('x_y_crops')[2]
                __content_140077375041712_3824 = __quote(__content_140077375041712_3824, '\x00', '&#0;', None, None)
                __token = 3872
                __content_140077375041712_3870 = (getitem('y_start') + 510)
                __content_140077375041712_3870 = __quote(__content_140077375041712_3870, '\x00', '&#0;', None, None)
                __token = 3890
                __content_140077375041712_3888 = getitem('x_y_crops')[3]
                __content_140077375041712_3888 = __quote(__content_140077375041712_3888, '\x00', '&#0;', None, None)
                __token = 3936
                __content_140077375041712_3934 = (getitem('y_start') + 510)
                __content_140077375041712_3934 = __quote(__content_140077375041712_3934, '\x00', '&#0;', None, None)
                __token = 3954
                __content_140077375041712_3952 = getitem('x_y_crops')[0]
                __content_140077375041712_3952 = __quote(__content_140077375041712_3952, '\x00', '&#0;', None, None)
                __token = 4000
                __content_140077375041712_3998 = (getitem('y_start') + 510)
                __content_140077375041712_3998 = __quote(__content_140077375041712_3998, '\x00', '&#0;', None, None)
                __token = 4018
                __content_140077375041712_4016 = getitem('x_y_crops')[1]
                __content_140077375041712_4016 = __quote(__content_140077375041712_4016, '\x00', '&#0;', None, None)
                __token = 4064
                __content_140077375041712_4062 = (getitem('y_start') + 510)
                __content_140077375041712_4062 = __quote(__content_140077375041712_4062, '\x00', '&#0;', None, None)
                __token = 4082
                __content_140077375041712_4080 = getitem('x_y_crops')[2]
                __content_140077375041712_4080 = __quote(__content_140077375041712_4080, '\x00', '&#0;', None, None)
                __token = 4128
                __content_140077375041712_4126 = (getitem('y_start') + 510)
                __content_140077375041712_4126 = __quote(__content_140077375041712_4126, '\x00', '&#0;', None, None)
                __token = 4146
                __content_140077375041712_4144 = getitem('x_y_crops')[3]
                __content_140077375041712_4144 = __quote(__content_140077375041712_4144, '\x00', '&#0;', None, None)
                __content_140077375041712 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        spriteset(', (__content_140077375041712 if (__content_140077375041712 is not None) else ''), '_ss_not_loaded_', (__content_140077375041712_353 if (__content_140077375041712_353 is not None) else ''), ', "src/graphics/', (__content_140077375041712_377 if (__content_140077375041712_377 is not None) else ''), '_0.png") {\n            [20,  ', (__content_140077375041712_416 if (__content_140077375041712_416 is not None) else ''), ', ', (__content_140077375041712_433 if (__content_140077375041712_433 is not None) else ''), ',  -13,  -6, ANIM]\n            [60,  ', (__content_140077375041712_485 if (__content_140077375041712_485 is not None) else ''), ', ', (__content_140077375041712_502 if (__content_140077375041712_502 is not None) else ''), ', -124,   5, ANIM]\n            [186, ', (__content_140077375041712_554 if (__content_140077375041712_554 is not None) else ''), ', ', (__content_140077375041712_571 if (__content_140077375041712_571 is not None) else ''), ', -124, -28, ANIM]\n            [328, ', (__content_140077375041712_623 if (__content_140077375041712_623 is not None) else ''), ', ', (__content_140077375041712_640 if (__content_140077375041712_640 is not None) else ''), ',  -76, -37, ANIM]\n            [454, ', (__content_140077375041712_692 if (__content_140077375041712_692 is not None) else ''), ', ', (__content_140077375041712_709 if (__content_140077375041712_709 is not None) else ''), ',  -14, -76, ANIM]\n            [494, ', (__content_140077375041712_761 if (__content_140077375041712_761 is not None) else ''), ', ', (__content_140077375041712_778 if (__content_140077375041712_778 is not None) else ''), ',  -34, -38, ANIM]\n            [620, ', (__content_140077375041712_830 if (__content_140077375041712_830 is not None) else ''), ', ', (__content_140077375041712_847 if (__content_140077375041712_847 is not None) else ''), ',  -15, -28, ANIM]\n            [762, ', (__content_140077375041712_899 if (__content_140077375041712_899 is not None) else ''), ', ', (__content_140077375041712_916 if (__content_140077375041712_916 is not None) else ''), ',   15,   6, ANIM]\n        }\n        spriteset(', (__content_140077375041712_978 if (__content_140077375041712_978 is not None) else ''), '_ss_load_1_', (__content_140077375041712_999 if (__content_140077375041712_999 is not None) else ''), ', "src/graphics/', (__content_140077375041712_1023 if (__content_140077375041712_1023 is not None) else ''), '_0.png") {\n            [20,  ', (__content_140077375041712_1062 if (__content_140077375041712_1062 is not None) else ''), ', ', (__content_140077375041712_1080 if (__content_140077375041712_1080 is not None) else ''), ',  -13, -14, ANIM]\n            [60,  ', (__content_140077375041712_1132 if (__content_140077375041712_1132 is not None) else ''), ', ', (__content_140077375041712_1150 if (__content_140077375041712_1150 is not None) else ''), ', -118,   1, ANIM]\n            [186, ', (__content_140077375041712_1202 if (__content_140077375041712_1202 is not None) else ''), ', ', (__content_140077375041712_1220 if (__content_140077375041712_1220 is not None) else ''), ', -112, -28, ANIM]\n            [328, ', (__content_140077375041712_1272 if (__content_140077375041712_1272 is not None) else ''), ', ', (__content_140077375041712_1290 if (__content_140077375041712_1290 is not None) else ''), ',  -64, -32, ANIM]\n            [454, ', (__content_140077375041712_1342 if (__content_140077375041712_1342 is not None) else ''), ', ', (__content_140077375041712_1360 if (__content_140077375041712_1360 is not None) else ''), ',  -14, -65, ANIM]\n            [494, ', (__content_140077375041712_1412 if (__content_140077375041712_1412 is not None) else ''), ', ', (__content_140077375041712_1430 if (__content_140077375041712_1430 is not None) else ''), ',  -45, -32, ANIM]\n            [620, ', (__content_140077375041712_1482 if (__content_140077375041712_1482 is not None) else ''), ', ', (__content_140077375041712_1500 if (__content_140077375041712_1500 is not None) else ''), ',  -26, -28, ANIM]\n            [762, ', (__content_140077375041712_1552 if (__content_140077375041712_1552 is not None) else ''), ', ', (__content_140077375041712_1570 if (__content_140077375041712_1570 is not None) else ''), ',    2,   0, ANIM]\n        }\n        spriteset(', (__content_140077375041712_1632 if (__content_140077375041712_1632 is not None) else ''), '_ss_load_2_', (__content_140077375041712_1653 if (__content_140077375041712_1653 is not None) else ''), ', "src/graphics/', (__content_140077375041712_1677 if (__content_140077375041712_1677 is not None) else ''), '_0.png") {\n            [20,  ', (__content_140077375041712_1716 if (__content_140077375041712_1716 is not None) else ''), ', ', (__content_140077375041712_1734 if (__content_140077375041712_1734 is not None) else ''), ',  -13, -21, ANIM]\n            [60,  ', (__content_140077375041712_1786 if (__content_140077375041712_1786 is not None) else ''), ', ', (__content_140077375041712_1804 if (__content_140077375041712_1804 is not None) else ''), ', -107,  -4, ANIM]\n            [186, ', (__content_140077375041712_1856 if (__content_140077375041712_1856 is not None) else ''), ', ', (__content_140077375041712_1874 if (__content_140077375041712_1874 is not None) else ''), ', -100, -28, ANIM]\n            [328, ', (__content_140077375041712_1926 if (__content_140077375041712_1926 is not None) else ''), ', ', (__content_140077375041712_1944 if (__content_140077375041712_1944 is not None) else ''), ',  -59, -30, ANIM]\n            [454, ', (__content_140077375041712_1996 if (__content_140077375041712_1996 is not None) else ''), ', ', (__content_140077375041712_2014 if (__content_140077375041712_2014 is not None) else ''), ',  -14, -57, ANIM]\n            [494, ', (__content_140077375041712_2066 if (__content_140077375041712_2066 is not None) else ''), ', ', (__content_140077375041712_2084 if (__content_140077375041712_2084 is not None) else ''), ',  -53, -30, ANIM]\n            [620, ', (__content_140077375041712_2136 if (__content_140077375041712_2136 is not None) else ''), ', ', (__content_140077375041712_2154 if (__content_140077375041712_2154 is not None) else ''), ',  -49, -28, ANIM]\n            [762, ', (__content_140077375041712_2206 if (__content_140077375041712_2206 is not None) else ''), ', ', (__content_140077375041712_2224 if (__content_140077375041712_2224 is not None) else ''), ',   -4,  -4, ANIM]\n        }\n        spriteset(', (__content_140077375041712_2286 if (__content_140077375041712_2286 is not None) else ''), '_ss_load_3_', (__content_140077375041712_2307 if (__content_140077375041712_2307 is not None) else ''), ', "src/graphics/', (__content_140077375041712_2331 if (__content_140077375041712_2331 is not None) else ''), '_0.png") {\n            [20,  ', (__content_140077375041712_2370 if (__content_140077375041712_2370 is not None) else ''), ', ', (__content_140077375041712_2388 if (__content_140077375041712_2388 is not None) else ''), ',  -13, -29, ANIM]\n            [60,  ', (__content_140077375041712_2440 if (__content_140077375041712_2440 is not None) else ''), ', ', (__content_140077375041712_2458 if (__content_140077375041712_2458 is not None) else ''), ', -102,  -8, ANIM]\n            [186, ', (__content_140077375041712_2510 if (__content_140077375041712_2510 is not None) else ''), ', ', (__content_140077375041712_2528 if (__content_140077375041712_2528 is not None) else ''), ',  -84, -28, ANIM]\n            [328, ', (__content_140077375041712_2580 if (__content_140077375041712_2580 is not None) else ''), ', ', (__content_140077375041712_2598 if (__content_140077375041712_2598 is not None) else ''), ',  -48, -26, ANIM]\n            [454, ', (__content_140077375041712_2650 if (__content_140077375041712_2650 is not None) else ''), ', ', (__content_140077375041712_2668 if (__content_140077375041712_2668 is not None) else ''), ',  -14, -47, ANIM]\n            [494, ', (__content_140077375041712_2720 if (__content_140077375041712_2720 is not None) else ''), ', ', (__content_140077375041712_2738 if (__content_140077375041712_2738 is not None) else ''), ',  -60, -25, ANIM]\n            [620, ', (__content_140077375041712_2790 if (__content_140077375041712_2790 is not None) else ''), ', ', (__content_140077375041712_2808 if (__content_140077375041712_2808 is not None) else ''), ',  -50, -28, ANIM]\n            [762, ', (__content_140077375041712_2860 if (__content_140077375041712_2860 is not None) else ''), ', ', (__content_140077375041712_2878 if (__content_140077375041712_2878 is not None) else ''), ',   -7,  -6, ANIM]\n        }\n        spriteset(', (__content_140077375041712_2940 if (__content_140077375041712_2940 is not None) else ''), '_ss_load_4_', (__content_140077375041712_2961 if (__content_140077375041712_2961 is not None) else ''), ', "src/graphics/', (__content_140077375041712_2985 if (__content_140077375041712_2985 is not None) else ''), '_0.png") {\n            [20,  ', (__content_140077375041712_3024 if (__content_140077375041712_3024 is not None) else ''), ', ', (__content_140077375041712_3042 if (__content_140077375041712_3042 is not None) else ''), ',  -13, -35, ANIM]\n            [60,  ', (__content_140077375041712_3094 if (__content_140077375041712_3094 is not None) else ''), ', ', (__content_140077375041712_3112 if (__content_140077375041712_3112 is not None) else ''), ',  -97, -10, ANIM]\n            [186, ', (__content_140077375041712_3164 if (__content_140077375041712_3164 is not None) else ''), ', ', (__content_140077375041712_3182 if (__content_140077375041712_3182 is not None) else ''), ',  -69, -28, ANIM]\n            [328, ', (__content_140077375041712_3234 if (__content_140077375041712_3234 is not None) else ''), ', ', (__content_140077375041712_3252 if (__content_140077375041712_3252 is not None) else ''), ',  -45, -22, ANIM]\n            [454, ', (__content_140077375041712_3304 if (__content_140077375041712_3304 is not None) else ''), ', ', (__content_140077375041712_3322 if (__content_140077375041712_3322 is not None) else ''), ',  -14, -45, ANIM]\n            [494, ', (__content_140077375041712_3374 if (__content_140077375041712_3374 is not None) else ''), ', ', (__content_140077375041712_3392 if (__content_140077375041712_3392 is not None) else ''), ',  -66, -22, ANIM]\n            [620, ', (__content_140077375041712_3444 if (__content_140077375041712_3444 is not None) else ''), ', ', (__content_140077375041712_3462 if (__content_140077375041712_3462 is not None) else ''), ',  -61, -28, ANIM]\n            [762, ', (__content_140077375041712_3514 if (__content_140077375041712_3514 is not None) else ''), ', ', (__content_140077375041712_3532 if (__content_140077375041712_3532 is not None) else ''), ',  -15, -10, ANIM]\n        }\n        spriteset(', (__content_140077375041712_3594 if (__content_140077375041712_3594 is not None) else ''), '_ss_load_5_', (__content_140077375041712_3615 if (__content_140077375041712_3615 is not None) else ''), ', "src/graphics/', (__content_140077375041712_3639 if (__content_140077375041712_3639 is not None) else ''), '_0.png") {\n            [20,  ', (__content_140077375041712_3678 if (__content_140077375041712_3678 is not None) else ''), ', ', (__content_140077375041712_3696 if (__content_140077375041712_3696 is not None) else ''), ',  -13, -41]\n            [60,  ', (__content_140077375041712_3742 if (__content_140077375041712_3742 is not None) else ''), ', ', (__content_140077375041712_3760 if (__content_140077375041712_3760 is not None) else ''), ',  -90, -13]\n            [186, ', (__content_140077375041712_3806 if (__content_140077375041712_3806 is not None) else ''), ', ', (__content_140077375041712_3824 if (__content_140077375041712_3824 is not None) else ''), ',  -65, -28]\n            [328, ', (__content_140077375041712_3870 if (__content_140077375041712_3870 is not None) else ''), ', ', (__content_140077375041712_3888 if (__content_140077375041712_3888 is not None) else ''), ',  -40, -19]\n            [454, ', (__content_140077375041712_3934 if (__content_140077375041712_3934 is not None) else ''), ', ', (__content_140077375041712_3952 if (__content_140077375041712_3952 is not None) else ''), ',  -14, -42]\n            [494, ', (__content_140077375041712_3998 if (__content_140077375041712_3998 is not None) else ''), ', ', (__content_140077375041712_4016 if (__content_140077375041712_4016 is not None) else ''), ',  -75, -17]\n            [620, ', (__content_140077375041712_4062 if (__content_140077375041712_4062 is not None) else ''), ', ', (__content_140077375041712_4080 if (__content_140077375041712_4080 is not None) else ''), ',  -68, -28]\n            [762, ', (__content_140077375041712_4126 if (__content_140077375041712_4126 is not None) else ''), ', ', (__content_140077375041712_4144 if (__content_140077375041712_4144 is not None) else ''), ',  -22, -13]\n        }\n    ', ))
                if (__content_140077375041712 is None):
                    pass
                else:
                    if (__content_140077375041712 is None):
                        __content_140077375041712 = None
                    else:
                        __tt = type(__content_140077375041712)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140077375041712 = str(__content_140077375041712)
                        else:
                            if (__tt is bytes):
                                __content_140077375041712 = decode(__content_140077375041712)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140077375041712 = __content_140077375041712.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140077375041712)
                                        __content_140077375041712 = (str(__content_140077375041712) if (__content_140077375041712 is __converted) else __converted)
                                    else:
                                        __content_140077375041712 = __content_140077375041712()
                if (__content_140077375041712 is not None):
                    __append(__content_140077375041712)
                if (__backup_y_start_140077380605504 is __marker):
                    del econtext['y_start']
                else:
                    econtext['y_start'] = __backup_y_start_140077380605504
                __append('\n')
                ____index_140077369624656 -= 1
                if (____index_140077369624656 > 0):
                    __append('')
            if (__backup_state_140077380605408 is __marker):
                del econtext['state']
            else:
                econtext['state'] = __backup_state_140077380605408
            if (__backup_x_y_crops_140077380605312 is __marker):
                del econtext['x_y_crops']
            else:
                econtext['x_y_crops'] = __backup_x_y_crops_140077380605312
            if (__backup_states_140077380605264 is __marker):
                del econtext['states']
            else:
                econtext['states'] = __backup_states_140077380605264

            # <Interpolation value=<Substitution "\n\nspritegroup ${ship.id}_sg_refit_0_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_0_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_0, current_speed) {\n    0: return ${ship.id}_sg_refit_0_not_moving;\n    return ${ship.id}_sg_refit_0_moving;\n}\n\nspritegroup ${ship.id}_sg_refit_1_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n        ${ship.id}_ss_load_2_moving,\n        ${ship.id}_ss_load_3_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_1_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_1, current_speed) {\n    0: return ${ship.id}_sg_refit_1_not_moving;\n    return ${ship.id}_sg_refit_1_moving;\n}\n\nspritegroup ${ship.id}_sg_refit_2_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_load_1_moving,\n        ${ship.id}_ss_load_2_moving,\n        ${ship.id}_ss_load_3_moving,\n        ${ship.id}_ss_load_4_moving,\n        ${ship.id}_ss_load_5_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ${ship.id}_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_refit_2_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n        ${ship.id}_ss_load_4_not_moving,\n        ${ship.id}_ss_load_5_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_load_1_not_moving,\n        ${ship.id}_ss_load_2_not_moving,\n        ${ship.id}_ss_load_3_not_moving,\n        ${ship.id}_ss_load_4_not_moving,\n        ${ship.id}_ss_load_5_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_refit_2, current_speed) {\n    0: return ${ship.id}_sg_refit_2_not_moving;\n    return ${ship.id}_sg_refit_2_moving;\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, cargo_subtype) {\n    0: return ${ship.id}_switch_graphics_refit_0;\n    1: return ${ship.id}_switch_graphics_refit_1;\n    2: return ${ship.id}_switch_graphics_refit_2;\n    return ${ship.id}_switch_graphics_refit_0;\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n    ];\n}\n\n\n// -- set speed a little higher than rated speed when unladen -- //\n" (69:21)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f664ddb83d0> -> __content_140077375041712
            __token = 4228
            __token = 4242
            __content_140077375041712 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712 = __quote(__content_140077375041712, '\x00', '&#0;', None, None)
            __token = 4296
            __content_140077375041712_4294 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_4294 = __quote(__content_140077375041712_4294, '\x00', '&#0;', None, None)
            __token = 4337
            __content_140077375041712_4335 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_4335 = __quote(__content_140077375041712_4335, '\x00', '&#0;', None, None)
            __token = 4478
            __content_140077375041712_4476 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_4476 = __quote(__content_140077375041712_4476, '\x00', '&#0;', None, None)
            __token = 4533
            __content_140077375041712_4531 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_4531 = __quote(__content_140077375041712_4531, '\x00', '&#0;', None, None)
            __token = 4591
            __content_140077375041712_4589 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_4589 = __quote(__content_140077375041712_4589, '\x00', '&#0;', None, None)
            __token = 4636
            __content_140077375041712_4634 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_4634 = __quote(__content_140077375041712_4634, '\x00', '&#0;', None, None)
            __token = 4699
            __content_140077375041712_4697 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_4697 = __quote(__content_140077375041712_4697, '\x00', '&#0;', None, None)
            __token = 4744
            __content_140077375041712_4742 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_4742 = __quote(__content_140077375041712_4742, '\x00', '&#0;', None, None)
            __token = 4813
            __content_140077375041712_4811 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_4811 = __quote(__content_140077375041712_4811, '\x00', '&#0;', None, None)
            __token = 4880
            __content_140077375041712_4878 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_4878 = __quote(__content_140077375041712_4878, '\x00', '&#0;', None, None)
            __token = 4925
            __content_140077375041712_4923 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_4923 = __quote(__content_140077375041712_4923, '\x00', '&#0;', None, None)
            __token = 4970
            __content_140077375041712_4968 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_4968 = __quote(__content_140077375041712_4968, '\x00', '&#0;', None, None)
            __token = 5024
            __content_140077375041712_5022 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5022 = __quote(__content_140077375041712_5022, '\x00', '&#0;', None, None)
            __token = 5065
            __content_140077375041712_5063 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5063 = __quote(__content_140077375041712_5063, '\x00', '&#0;', None, None)
            __token = 5102
            __content_140077375041712_5100 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5100 = __quote(__content_140077375041712_5100, '\x00', '&#0;', None, None)
            __token = 5139
            __content_140077375041712_5137 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5137 = __quote(__content_140077375041712_5137, '\x00', '&#0;', None, None)
            __token = 5280
            __content_140077375041712_5278 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5278 = __quote(__content_140077375041712_5278, '\x00', '&#0;', None, None)
            __token = 5335
            __content_140077375041712_5333 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5333 = __quote(__content_140077375041712_5333, '\x00', '&#0;', None, None)
            __token = 5393
            __content_140077375041712_5391 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5391 = __quote(__content_140077375041712_5391, '\x00', '&#0;', None, None)
            __token = 5438
            __content_140077375041712_5436 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5436 = __quote(__content_140077375041712_5436, '\x00', '&#0;', None, None)
            __token = 5479
            __content_140077375041712_5477 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5477 = __quote(__content_140077375041712_5477, '\x00', '&#0;', None, None)
            __token = 5520
            __content_140077375041712_5518 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5518 = __quote(__content_140077375041712_5518, '\x00', '&#0;', None, None)
            __token = 5583
            __content_140077375041712_5581 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5581 = __quote(__content_140077375041712_5581, '\x00', '&#0;', None, None)
            __token = 5628
            __content_140077375041712_5626 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5626 = __quote(__content_140077375041712_5626, '\x00', '&#0;', None, None)
            __token = 5669
            __content_140077375041712_5667 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5667 = __quote(__content_140077375041712_5667, '\x00', '&#0;', None, None)
            __token = 5710
            __content_140077375041712_5708 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5708 = __quote(__content_140077375041712_5708, '\x00', '&#0;', None, None)
            __token = 5779
            __content_140077375041712_5777 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5777 = __quote(__content_140077375041712_5777, '\x00', '&#0;', None, None)
            __token = 5846
            __content_140077375041712_5844 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5844 = __quote(__content_140077375041712_5844, '\x00', '&#0;', None, None)
            __token = 5891
            __content_140077375041712_5889 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5889 = __quote(__content_140077375041712_5889, '\x00', '&#0;', None, None)
            __token = 5936
            __content_140077375041712_5934 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5934 = __quote(__content_140077375041712_5934, '\x00', '&#0;', None, None)
            __token = 5990
            __content_140077375041712_5988 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_5988 = __quote(__content_140077375041712_5988, '\x00', '&#0;', None, None)
            __token = 6031
            __content_140077375041712_6029 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6029 = __quote(__content_140077375041712_6029, '\x00', '&#0;', None, None)
            __token = 6068
            __content_140077375041712_6066 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6066 = __quote(__content_140077375041712_6066, '\x00', '&#0;', None, None)
            __token = 6105
            __content_140077375041712_6103 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6103 = __quote(__content_140077375041712_6103, '\x00', '&#0;', None, None)
            __token = 6142
            __content_140077375041712_6140 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6140 = __quote(__content_140077375041712_6140, '\x00', '&#0;', None, None)
            __token = 6179
            __content_140077375041712_6177 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6177 = __quote(__content_140077375041712_6177, '\x00', '&#0;', None, None)
            __token = 6320
            __content_140077375041712_6318 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6318 = __quote(__content_140077375041712_6318, '\x00', '&#0;', None, None)
            __token = 6375
            __content_140077375041712_6373 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6373 = __quote(__content_140077375041712_6373, '\x00', '&#0;', None, None)
            __token = 6433
            __content_140077375041712_6431 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6431 = __quote(__content_140077375041712_6431, '\x00', '&#0;', None, None)
            __token = 6478
            __content_140077375041712_6476 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6476 = __quote(__content_140077375041712_6476, '\x00', '&#0;', None, None)
            __token = 6519
            __content_140077375041712_6517 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6517 = __quote(__content_140077375041712_6517, '\x00', '&#0;', None, None)
            __token = 6560
            __content_140077375041712_6558 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6558 = __quote(__content_140077375041712_6558, '\x00', '&#0;', None, None)
            __token = 6601
            __content_140077375041712_6599 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6599 = __quote(__content_140077375041712_6599, '\x00', '&#0;', None, None)
            __token = 6642
            __content_140077375041712_6640 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6640 = __quote(__content_140077375041712_6640, '\x00', '&#0;', None, None)
            __token = 6705
            __content_140077375041712_6703 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6703 = __quote(__content_140077375041712_6703, '\x00', '&#0;', None, None)
            __token = 6750
            __content_140077375041712_6748 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6748 = __quote(__content_140077375041712_6748, '\x00', '&#0;', None, None)
            __token = 6791
            __content_140077375041712_6789 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6789 = __quote(__content_140077375041712_6789, '\x00', '&#0;', None, None)
            __token = 6832
            __content_140077375041712_6830 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6830 = __quote(__content_140077375041712_6830, '\x00', '&#0;', None, None)
            __token = 6873
            __content_140077375041712_6871 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6871 = __quote(__content_140077375041712_6871, '\x00', '&#0;', None, None)
            __token = 6914
            __content_140077375041712_6912 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6912 = __quote(__content_140077375041712_6912, '\x00', '&#0;', None, None)
            __token = 6983
            __content_140077375041712_6981 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_6981 = __quote(__content_140077375041712_6981, '\x00', '&#0;', None, None)
            __token = 7050
            __content_140077375041712_7048 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_7048 = __quote(__content_140077375041712_7048, '\x00', '&#0;', None, None)
            __token = 7095
            __content_140077375041712_7093 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_7093 = __quote(__content_140077375041712_7093, '\x00', '&#0;', None, None)
            __token = 7154
            __content_140077375041712_7152 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_7152 = __quote(__content_140077375041712_7152, '\x00', '&#0;', None, None)
            __token = 7213
            __content_140077375041712_7211 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_7211 = __quote(__content_140077375041712_7211, '\x00', '&#0;', None, None)
            __token = 7263
            __content_140077375041712_7261 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_7261 = __quote(__content_140077375041712_7261, '\x00', '&#0;', None, None)
            __token = 7313
            __content_140077375041712_7311 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_7311 = __quote(__content_140077375041712_7311, '\x00', '&#0;', None, None)
            __token = 7360
            __content_140077375041712_7358 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_7358 = __quote(__content_140077375041712_7358, '\x00', '&#0;', None, None)
            __token = 7411
            __content_140077375041712_7409 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_7409 = __quote(__content_140077375041712_7409, '\x00', '&#0;', None, None)
            __token = 7459
            __content_140077375041712_7457 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_7457 = __quote(__content_140077375041712_7457, '\x00', '&#0;', None, None)
            __token = 7526
            __content_140077375041712_7524 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_7524 = __quote(__content_140077375041712_7524, '\x00', '&#0;', None, None)
            __content_140077375041712 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n\nspritegroup ', (__content_140077375041712 if (__content_140077375041712 is not None) else ''), '_sg_refit_0_moving {\n    loaded:  [\n        ', (__content_140077375041712_4294 if (__content_140077375041712_4294 is not None) else ''), '_ss_not_loaded_moving,\n        ', (__content_140077375041712_4335 if (__content_140077375041712_4335 is not None) else ''), "_ss_load_1_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ", (__content_140077375041712_4476 if (__content_140077375041712_4476 is not None) else ''), '_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ', (__content_140077375041712_4531 if (__content_140077375041712_4531 is not None) else ''), '_sg_refit_0_not_moving {\n    loaded:  [\n        ', (__content_140077375041712_4589 if (__content_140077375041712_4589 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_140077375041712_4634 if (__content_140077375041712_4634 is not None) else ''), '_ss_load_1_not_moving,\n    ];\n    loading: [\n        ', (__content_140077375041712_4697 if (__content_140077375041712_4697 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_140077375041712_4742 if (__content_140077375041712_4742 is not None) else ''), '_ss_load_1_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_140077375041712_4811 if (__content_140077375041712_4811 is not None) else ''), '_switch_graphics_refit_0, current_speed) {\n    0: return ', (__content_140077375041712_4878 if (__content_140077375041712_4878 is not None) else ''), '_sg_refit_0_not_moving;\n    return ', (__content_140077375041712_4923 if (__content_140077375041712_4923 is not None) else ''), '_sg_refit_0_moving;\n}\n\nspritegroup ', (__content_140077375041712_4968 if (__content_140077375041712_4968 is not None) else ''), '_sg_refit_1_moving {\n    loaded:  [\n        ', (__content_140077375041712_5022 if (__content_140077375041712_5022 is not None) else ''), '_ss_not_loaded_moving,\n        ', (__content_140077375041712_5063 if (__content_140077375041712_5063 is not None) else ''), '_ss_load_1_moving,\n        ', (__content_140077375041712_5100 if (__content_140077375041712_5100 is not None) else ''), '_ss_load_2_moving,\n        ', (__content_140077375041712_5137 if (__content_140077375041712_5137 is not None) else ''), "_ss_load_3_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ", (__content_140077375041712_5278 if (__content_140077375041712_5278 is not None) else ''), '_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ', (__content_140077375041712_5333 if (__content_140077375041712_5333 is not None) else ''), '_sg_refit_1_not_moving {\n    loaded:  [\n        ', (__content_140077375041712_5391 if (__content_140077375041712_5391 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_140077375041712_5436 if (__content_140077375041712_5436 is not None) else ''), '_ss_load_1_not_moving,\n        ', (__content_140077375041712_5477 if (__content_140077375041712_5477 is not None) else ''), '_ss_load_2_not_moving,\n        ', (__content_140077375041712_5518 if (__content_140077375041712_5518 is not None) else ''), '_ss_load_3_not_moving,\n    ];\n    loading: [\n        ', (__content_140077375041712_5581 if (__content_140077375041712_5581 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_140077375041712_5626 if (__content_140077375041712_5626 is not None) else ''), '_ss_load_1_not_moving,\n        ', (__content_140077375041712_5667 if (__content_140077375041712_5667 is not None) else ''), '_ss_load_2_not_moving,\n        ', (__content_140077375041712_5708 if (__content_140077375041712_5708 is not None) else ''), '_ss_load_3_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_140077375041712_5777 if (__content_140077375041712_5777 is not None) else ''), '_switch_graphics_refit_1, current_speed) {\n    0: return ', (__content_140077375041712_5844 if (__content_140077375041712_5844 is not None) else ''), '_sg_refit_1_not_moving;\n    return ', (__content_140077375041712_5889 if (__content_140077375041712_5889 is not None) else ''), '_sg_refit_1_moving;\n}\n\nspritegroup ', (__content_140077375041712_5934 if (__content_140077375041712_5934 is not None) else ''), '_sg_refit_2_moving {\n    loaded:  [\n        ', (__content_140077375041712_5988 if (__content_140077375041712_5988 is not None) else ''), '_ss_not_loaded_moving,\n        ', (__content_140077375041712_6029 if (__content_140077375041712_6029 is not None) else ''), '_ss_load_1_moving,\n        ', (__content_140077375041712_6066 if (__content_140077375041712_6066 is not None) else ''), '_ss_load_2_moving,\n        ', (__content_140077375041712_6103 if (__content_140077375041712_6103 is not None) else ''), '_ss_load_3_moving,\n        ', (__content_140077375041712_6140 if (__content_140077375041712_6140 is not None) else ''), '_ss_load_4_moving,\n        ', (__content_140077375041712_6177 if (__content_140077375041712_6177 is not None) else ''), "_ss_load_5_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ", (__content_140077375041712_6318 if (__content_140077375041712_6318 is not None) else ''), '_ss_not_loaded_moving,\n    ];\n}\n\nspritegroup ', (__content_140077375041712_6373 if (__content_140077375041712_6373 is not None) else ''), '_sg_refit_2_not_moving {\n    loaded:  [\n        ', (__content_140077375041712_6431 if (__content_140077375041712_6431 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_140077375041712_6476 if (__content_140077375041712_6476 is not None) else ''), '_ss_load_1_not_moving,\n        ', (__content_140077375041712_6517 if (__content_140077375041712_6517 is not None) else ''), '_ss_load_2_not_moving,\n        ', (__content_140077375041712_6558 if (__content_140077375041712_6558 is not None) else ''), '_ss_load_3_not_moving,\n        ', (__content_140077375041712_6599 if (__content_140077375041712_6599 is not None) else ''), '_ss_load_4_not_moving,\n        ', (__content_140077375041712_6640 if (__content_140077375041712_6640 is not None) else ''), '_ss_load_5_not_moving,\n    ];\n    loading: [\n        ', (__content_140077375041712_6703 if (__content_140077375041712_6703 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_140077375041712_6748 if (__content_140077375041712_6748 is not None) else ''), '_ss_load_1_not_moving,\n        ', (__content_140077375041712_6789 if (__content_140077375041712_6789 is not None) else ''), '_ss_load_2_not_moving,\n        ', (__content_140077375041712_6830 if (__content_140077375041712_6830 is not None) else ''), '_ss_load_3_not_moving,\n        ', (__content_140077375041712_6871 if (__content_140077375041712_6871 is not None) else ''), '_ss_load_4_not_moving,\n        ', (__content_140077375041712_6912 if (__content_140077375041712_6912 is not None) else ''), '_ss_load_5_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_140077375041712_6981 if (__content_140077375041712_6981 is not None) else ''), '_switch_graphics_refit_2, current_speed) {\n    0: return ', (__content_140077375041712_7048 if (__content_140077375041712_7048 is not None) else ''), '_sg_refit_2_not_moving;\n    return ', (__content_140077375041712_7093 if (__content_140077375041712_7093 is not None) else ''), '_sg_refit_2_moving;\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_140077375041712_7152 if (__content_140077375041712_7152 is not None) else ''), '_switch_graphics, cargo_subtype) {\n    0: return ', (__content_140077375041712_7211 if (__content_140077375041712_7211 is not None) else ''), '_switch_graphics_refit_0;\n    1: return ', (__content_140077375041712_7261 if (__content_140077375041712_7261 is not None) else ''), '_switch_graphics_refit_1;\n    2: return ', (__content_140077375041712_7311 if (__content_140077375041712_7311 is not None) else ''), '_switch_graphics_refit_2;\n    return ', (__content_140077375041712_7358 if (__content_140077375041712_7358 is not None) else ''), '_switch_graphics_refit_0;\n}\n\nspritegroup ', (__content_140077375041712_7409 if (__content_140077375041712_7409 is not None) else ''), '_sg_purchase {\n    loaded:  [\n        ', (__content_140077375041712_7457 if (__content_140077375041712_7457 is not None) else ''), '_ss_not_loaded_not_moving,\n    ];\n    loading: [\n        ', (__content_140077375041712_7524 if (__content_140077375041712_7524 is not None) else ''), '_ss_not_loaded_not_moving,\n    ];\n}\n\n\n// -- set speed a little higher than rated speed when unladen -- //\n', ))
            if (__content_140077375041712 is None):
                pass
            else:
                if (__content_140077375041712 is None):
                    __content_140077375041712 = None
                else:
                    __tt = type(__content_140077375041712)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140077375041712 = str(__content_140077375041712)
                    else:
                        if (__tt is bytes):
                            __content_140077375041712 = decode(__content_140077375041712)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140077375041712 = __content_140077375041712.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140077375041712)
                                    __content_140077375041712 = (str(__content_140077375041712) if (__content_140077375041712 is __converted) else __converted)
                                else:
                                    __content_140077375041712 = __content_140077375041712()
            if (__content_140077375041712 is not None):
                __append(__content_140077375041712)

            # <Static value=<_ast.Dict object at 0x7f664de292b0> name=None at 7f664de29160> -> __attrs_140077369625376
            __attrs_140077369625376 = _static_140077370086064
            __backup_speed_factor_140077380605360 = get('speed_factor', __marker)

            # <Value 'python:range(3)' (185:32)> -> __iterator
            __token = 7672
            __iterator = get('range', range)(3)
            (__iterator, ____index_140077369626192, ) = getitem('repeat')('speed_factor', __iterator)
            econtext['speed_factor'] = None
            for __item in __iterator:
                econtext['speed_factor'] = __item

                # <Interpolation value=<Substitution '\n    switch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount_${speed_factor}, cargo_count*100/cargo_capacity) {\n        0 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[0]};\n        1..100 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[4]}; // log tug is binary: loaded or unloaded; no intermediate fractional speeds\n        return 0; // should never reach this result, make it show up as a problem\n    }\n' (185:49)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f664ddb8f70> -> __content_140077375041712
                __token = 7694
                __token = 7722
                __content_140077375041712 = _lookup_attr(getitem('ship'), 'id')
                __content_140077375041712 = __quote(__content_140077375041712, '\x00', '&#0;', None, None)
                __token = 7770
                __content_140077375041712_7768 = getitem('speed_factor')
                __content_140077375041712_7768 = __quote(__content_140077375041712_7768, '\x00', '&#0;', None, None)
                __token = 7833
                __content_140077375041712_7831 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(getitem('speed_factor'))[0]
                __content_140077375041712_7831 = __quote(__content_140077375041712_7831, '\x00', '&#0;', None, None)
                __token = 7912
                __content_140077375041712_7910 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(getitem('speed_factor'))[4]
                __content_140077375041712_7910 = __quote(__content_140077375041712_7910, '\x00', '&#0;', None, None)
                __content_140077375041712 = ('%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_SHIPS, SELF, ', (__content_140077375041712 if (__content_140077375041712 is not None) else ''), '_switch_speed_varies_with_load_amount_', (__content_140077375041712_7768 if (__content_140077375041712_7768 is not None) else ''), ', cargo_count*100/cargo_capacity) {\n        0 : ', (__content_140077375041712_7831 if (__content_140077375041712_7831 is not None) else ''), ';\n        1..100 : ', (__content_140077375041712_7910 if (__content_140077375041712_7910 is not None) else ''), '; // log tug is binary: loaded or unloaded; no intermediate fractional speeds\n        return 0; // should never reach this result, make it show up as a problem\n    }\n', ))
                if (__content_140077375041712 is None):
                    pass
                else:
                    if (__content_140077375041712 is None):
                        __content_140077375041712 = None
                    else:
                        __tt = type(__content_140077375041712)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140077375041712 = str(__content_140077375041712)
                        else:
                            if (__tt is bytes):
                                __content_140077375041712 = decode(__content_140077375041712)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140077375041712 = __content_140077375041712.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140077375041712)
                                        __content_140077375041712 = (str(__content_140077375041712) if (__content_140077375041712 is __converted) else __converted)
                                    else:
                                        __content_140077375041712 = __content_140077375041712()
                if (__content_140077375041712 is not None):
                    __append(__content_140077375041712)
                ____index_140077369626192 -= 1
                if (____index_140077369626192 > 0):
                    __append('')
            if (__backup_speed_factor_140077380605360 is __marker):
                del econtext['speed_factor']
            else:
                econtext['speed_factor'] = __backup_speed_factor_140077380605360

            # <Interpolation value=<Substitution '\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount, param_adjust_ship_speed) {\n    0: ${ship.id}_switch_speed_varies_with_load_amount_0;\n    1: ${ship.id}_switch_speed_varies_with_load_amount_1;\n    2: ${ship.id}_switch_speed_varies_with_load_amount_2;\n}\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_purchase_speed, param_adjust_ship_speed) {\n    0: ${ship.get_speeds_adjusted_for_load_amount(0)[4]};\n    1: ${ship.get_speeds_adjusted_for_load_amount(1)[4]};\n    2: ${ship.get_speeds_adjusted_for_load_amount(2)[4]};\n}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}\n' (191:12)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f664ddb8580> -> __content_140077375041712
            __token = 8149
            __token = 8177
            __content_140077375041712 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712 = __quote(__content_140077375041712, '\x00', '&#0;', None, None)
            __token = 8260
            __content_140077375041712_8258 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_8258 = __quote(__content_140077375041712_8258, '\x00', '&#0;', None, None)
            __token = 8318
            __content_140077375041712_8316 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_8316 = __quote(__content_140077375041712_8316, '\x00', '&#0;', None, None)
            __token = 8376
            __content_140077375041712_8374 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_8374 = __quote(__content_140077375041712_8374, '\x00', '&#0;', None, None)
            __token = 8455
            __content_140077375041712_8453 = _lookup_attr(getitem('ship'), 'id')
            __content_140077375041712_8453 = __quote(__content_140077375041712_8453, '\x00', '&#0;', None, None)
            __token = 8523
            __content_140077375041712_8521 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(0)[4]
            __content_140077375041712_8521 = __quote(__content_140077375041712_8521, '\x00', '&#0;', None, None)
            __token = 8581
            __content_140077375041712_8579 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(1)[4]
            __content_140077375041712_8579 = __quote(__content_140077375041712_8579, '\x00', '&#0;', None, None)
            __token = 8639
            __content_140077375041712_8637 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(2)[4]
            __content_140077375041712_8637 = __quote(__content_140077375041712_8637, '\x00', '&#0;', None, None)
            __token = 8693
            __content_140077375041712_8691 = _lookup_attr(getitem('ship'), 'render_cargo_capacity')()
            __content_140077375041712_8691 = __quote(__content_140077375041712_8691, '\x00', '&#0;', None, None)
            __token = 8726
            __content_140077375041712_8724 = _lookup_attr(getitem('ship'), 'render_properties')()
            __content_140077375041712_8724 = __quote(__content_140077375041712_8724, '\x00', '&#0;', None, None)
            __content_140077375041712 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\nswitch (FEAT_SHIPS, SELF, ', (__content_140077375041712 if (__content_140077375041712 is not None) else ''), '_switch_speed_varies_with_load_amount, param_adjust_ship_speed) {\n    0: ', (__content_140077375041712_8258 if (__content_140077375041712_8258 is not None) else ''), '_switch_speed_varies_with_load_amount_0;\n    1: ', (__content_140077375041712_8316 if (__content_140077375041712_8316 is not None) else ''), '_switch_speed_varies_with_load_amount_1;\n    2: ', (__content_140077375041712_8374 if (__content_140077375041712_8374 is not None) else ''), '_switch_speed_varies_with_load_amount_2;\n}\nswitch (FEAT_SHIPS, SELF, ', (__content_140077375041712_8453 if (__content_140077375041712_8453 is not None) else ''), '_switch_purchase_speed, param_adjust_ship_speed) {\n    0: ', (__content_140077375041712_8521 if (__content_140077375041712_8521 is not None) else ''), ';\n    1: ', (__content_140077375041712_8579 if (__content_140077375041712_8579 is not None) else ''), ';\n    2: ', (__content_140077375041712_8637 if (__content_140077375041712_8637 is not None) else ''), ';\n}\n\n', (__content_140077375041712_8691 if (__content_140077375041712_8691 is not None) else ''), '\n\n', (__content_140077375041712_8724 if (__content_140077375041712_8724 is not None) else ''), '\n', ))
            if (__content_140077375041712 is None):
                pass
            else:
                if (__content_140077375041712 is None):
                    __content_140077375041712 = None
                else:
                    __tt = type(__content_140077375041712)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140077375041712 = str(__content_140077375041712)
                    else:
                        if (__tt is bytes):
                            __content_140077375041712 = decode(__content_140077375041712)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140077375041712 = __content_140077375041712.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140077375041712)
                                    __content_140077375041712 = (str(__content_140077375041712) if (__content_140077375041712 is __converted) else __converted)
                                else:
                                    __content_140077375041712 = __content_140077375041712()
            if (__content_140077375041712 is not None):
                __append(__content_140077375041712)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }