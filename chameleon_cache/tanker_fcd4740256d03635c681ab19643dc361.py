# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/fish1672/src/templates/tanker.pynml'
__tokens = {0: ('${ship.render_debug_info()}\n\n// graphics\ntemplate spriteset_template_${ship.id}(y) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [20,        y,          28,         89,          ${ship.offsets[0][0]}, ${ship.offsets[0][1]}, ANIM]\n    [60,        y,          113,        66,          ${ship.offsets[1][0]}, ${ship.offsets[1][1]}, ANIM]\n    [186,       y,          138,        48,          ${ship.offsets[2][0]}, ${ship.offsets[2][1]}, ANIM]\n    [328,       y,          113,        66,          ${ship.offsets[3][0]}, ${ship.offsets[3][1]}, ANIM]\n    [454,       y,          28,         89,          ${ship.offsets[4][0]}, ${ship.offsets[4][1]}, ANIM]\n    [494,       y,          113,        66,          ${ship.offsets[5][0]}, ${ship.offsets[5][1]}, ANIM]\n    [620,       y,          138,        48,          ${ship.offsets[6][0]}, ${ship.offsets[6][1]}, ANIM]\n    [762,       y,          113,        66,          ${ship.offsets[7][0]}, ${ship.offsets[7][1]}, ANIM]\n}\n\nspriteset(${ship.id}_ss_not_loaded_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(10)\n}\nspriteset(${ship.id}_ss_not_loaded_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(110)\n}\nspriteset(${ship.id}_ss_loaded_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(210)\n}\nspriteset(${ship.id}_ss_loaded_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(310)\n}\n\nspritegroup ${ship.id}_sg_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_loaded_moving,\n    ];\n    loading: [ // can\'t be loading when moving, but we\'ll overlook that, it\'s required by nml ;)\n        ${ship.id}_ss_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_loaded_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_loaded_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, current_speed) {\n    0: return ${ship.id}_sg_not_moving;\n    return ${ship.id}_sg_moving;\n}\n\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_${ship.id}() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [${ship.buy_menu_bb_xy[0]}, ${ship.buy_menu_bb_xy[1]}, ${ship.buy_menu_width}, 22, -${int(ship.buy_menu_width / 2)}, -10]\n}\n\nspriteset(${ship.id}_ss_purchase, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_purchase_${ship.id}()\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_purchase,\n    ];\n    loading: [\n        ${ship.id}_ss_purchase,\n    ];\n}\n\n${ship.render_speed_switches()}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}', 1, 0), 2: ('ship.render_debug_info()', 1, 2), 71: ('ship.id', 4, 30), 217: ('ship.offsets[0][0]', 6, 55), 240: ('ship.offsets[0][1]', 6, 78), 322: ('ship.offsets[1][0]', 7, 55), 345: ('ship.offsets[1][1]', 7, 78), 427: ('ship.offsets[2][0]', 8, 55), 450: ('ship.offsets[2][1]', 8, 78), 532: ('ship.offsets[3][0]', 9, 55), 555: ('ship.offsets[3][1]', 9, 78), 637: ('ship.offsets[4][0]', 10, 55), 660: ('ship.offsets[4][1]', 10, 78), 742: ('ship.offsets[5][0]', 11, 55), 765: ('ship.offsets[5][1]', 11, 78), 847: ('ship.offsets[6][0]', 12, 55), 870: ('ship.offsets[6][1]', 12, 78), 952: ('ship.offsets[7][0]', 13, 55), 975: ('ship.offsets[7][1]', 13, 78), 1017: ('ship.id', 16, 12), 1068: ('ship.id', 16, 63), 1110: ('ship.id', 17, 23), 1137: ('ship.id', 19, 12), 1184: ('ship.id', 19, 59), 1226: ('ship.id', 20, 23), 1254: ('ship.id', 22, 12), 1301: ('ship.id', 22, 59), 1343: ('ship.id', 23, 23), 1371: ('ship.id', 25, 12), 1414: ('ship.id', 25, 55), 1456: ('ship.id', 26, 23), 1487: ('ship.id', 29, 14), 1533: ('ship.id', 31, 10), 1574: ('ship.id', 32, 10), 1715: ('ship.id', 35, 10), 1766: ('ship.id', 39, 14), 1816: ('ship.id', 41, 10), 1861: ('ship.id', 42, 10), 1924: ('ship.id', 45, 10), 1969: ('ship.id', 46, 10), 2038: ('ship.id', 50, 28), 2097: ('ship.id', 51, 16), 2134: ('ship.id', 52, 13), 2219: ('ship.id', 58, 39), 2316: ('ship.buy_menu_bb_xy[0]', 60, 7), 2343: ('ship.buy_menu_bb_xy[1]', 60, 34), 2370: ('ship.buy_menu_width', 60, 61), 2399: ('int(ship.buy_menu_width / 2)', 60, 90), 2450: ('ship.id', 63, 12), 2488: ('ship.id', 63, 50), 2539: ('ship.id', 64, 32), 2567: ('ship.id', 67, 14), 2615: ('ship.id', 69, 10), 2669: ('ship.id', 72, 10), 2703: ('ship.render_speed_switches()', 76, 2), 2736: ('ship.render_cargo_capacity()', 78, 2), 2769: ('ship.render_properties()', 80, 2)}

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

            # <Interpolation value=<Substitution '${ship.render_debug_info()}\n\n// graphics\ntemplate spriteset_template_${ship.id}(y) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [20,        y,          28,         89,          ${ship.offsets[0][0]}, ${ship.offsets[0][1]}, ANIM]\n    [60,        y,          113,        66,          ${ship.offsets[1][0]}, ${ship.offsets[1][1]}, ANIM]\n    [186,       y,          138,        48,          ${ship.offsets[2][0]}, ${ship.offsets[2][1]}, ANIM]\n    [328,       y,          113,        66,          ${ship.offsets[3][0]}, ${ship.offsets[3][1]}, ANIM]\n    [454,       y,          28,         89,          ${ship.offsets[4][0]}, ${ship.offsets[4][1]}, ANIM]\n    [494,       y,          113,        66,          ${ship.offsets[5][0]}, ${ship.offsets[5][1]}, ANIM]\n    [620,       y,          138,        48,          ${ship.offsets[6][0]}, ${ship.offsets[6][1]}, ANIM]\n    [762,       y,          113,        66,          ${ship.offsets[7][0]}, ${ship.offsets[7][1]}, ANIM]\n}\n\nspriteset(${ship.id}_ss_not_loaded_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(10)\n}\nspriteset(${ship.id}_ss_not_loaded_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(110)\n}\nspriteset(${ship.id}_ss_loaded_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(210)\n}\nspriteset(${ship.id}_ss_loaded_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(310)\n}\n\nspritegroup ${ship.id}_sg_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_moving,\n        ${ship.id}_ss_loaded_moving,\n    ];\n    loading: [ // can\'t be loading when moving, but we\'ll overlook that, it\'s required by nml ;)\n        ${ship.id}_ss_loaded_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_not_moving {\n    loaded:  [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_loaded_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_not_loaded_not_moving,\n        ${ship.id}_ss_loaded_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, current_speed) {\n    0: return ${ship.id}_sg_not_moving;\n    return ${ship.id}_sg_moving;\n}\n\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_${ship.id}() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [${ship.buy_menu_bb_xy[0]}, ${ship.buy_menu_bb_xy[1]}, ${ship.buy_menu_width}, 22, -${int(ship.buy_menu_width / 2)}, -10]\n}\n\nspriteset(${ship.id}_ss_purchase, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_purchase_${ship.id}()\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_purchase,\n    ];\n    loading: [\n        ${ship.id}_ss_purchase,\n    ];\n}\n\n${ship.render_speed_switches()}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}\n' (1:0)> braces_required=True translation=False at 7f350c98a048> -> __content_139865838111856
            __token = 0
            __token = 2
            __content_139865838111856 = _lookup_attr(getitem('ship'), 'render_debug_info')()
            __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
            __token = 71
            __content_139865838111856_69 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_69 = __quote(__content_139865838111856_69, '\x00', '&#0;', None, False)
            __token = 217
            __content_139865838111856_215 = _lookup_attr(getitem('ship'), 'offsets')[0][0]
            __content_139865838111856_215 = __quote(__content_139865838111856_215, '\x00', '&#0;', None, False)
            __token = 240
            __content_139865838111856_238 = _lookup_attr(getitem('ship'), 'offsets')[0][1]
            __content_139865838111856_238 = __quote(__content_139865838111856_238, '\x00', '&#0;', None, False)
            __token = 322
            __content_139865838111856_320 = _lookup_attr(getitem('ship'), 'offsets')[1][0]
            __content_139865838111856_320 = __quote(__content_139865838111856_320, '\x00', '&#0;', None, False)
            __token = 345
            __content_139865838111856_343 = _lookup_attr(getitem('ship'), 'offsets')[1][1]
            __content_139865838111856_343 = __quote(__content_139865838111856_343, '\x00', '&#0;', None, False)
            __token = 427
            __content_139865838111856_425 = _lookup_attr(getitem('ship'), 'offsets')[2][0]
            __content_139865838111856_425 = __quote(__content_139865838111856_425, '\x00', '&#0;', None, False)
            __token = 450
            __content_139865838111856_448 = _lookup_attr(getitem('ship'), 'offsets')[2][1]
            __content_139865838111856_448 = __quote(__content_139865838111856_448, '\x00', '&#0;', None, False)
            __token = 532
            __content_139865838111856_530 = _lookup_attr(getitem('ship'), 'offsets')[3][0]
            __content_139865838111856_530 = __quote(__content_139865838111856_530, '\x00', '&#0;', None, False)
            __token = 555
            __content_139865838111856_553 = _lookup_attr(getitem('ship'), 'offsets')[3][1]
            __content_139865838111856_553 = __quote(__content_139865838111856_553, '\x00', '&#0;', None, False)
            __token = 637
            __content_139865838111856_635 = _lookup_attr(getitem('ship'), 'offsets')[4][0]
            __content_139865838111856_635 = __quote(__content_139865838111856_635, '\x00', '&#0;', None, False)
            __token = 660
            __content_139865838111856_658 = _lookup_attr(getitem('ship'), 'offsets')[4][1]
            __content_139865838111856_658 = __quote(__content_139865838111856_658, '\x00', '&#0;', None, False)
            __token = 742
            __content_139865838111856_740 = _lookup_attr(getitem('ship'), 'offsets')[5][0]
            __content_139865838111856_740 = __quote(__content_139865838111856_740, '\x00', '&#0;', None, False)
            __token = 765
            __content_139865838111856_763 = _lookup_attr(getitem('ship'), 'offsets')[5][1]
            __content_139865838111856_763 = __quote(__content_139865838111856_763, '\x00', '&#0;', None, False)
            __token = 847
            __content_139865838111856_845 = _lookup_attr(getitem('ship'), 'offsets')[6][0]
            __content_139865838111856_845 = __quote(__content_139865838111856_845, '\x00', '&#0;', None, False)
            __token = 870
            __content_139865838111856_868 = _lookup_attr(getitem('ship'), 'offsets')[6][1]
            __content_139865838111856_868 = __quote(__content_139865838111856_868, '\x00', '&#0;', None, False)
            __token = 952
            __content_139865838111856_950 = _lookup_attr(getitem('ship'), 'offsets')[7][0]
            __content_139865838111856_950 = __quote(__content_139865838111856_950, '\x00', '&#0;', None, False)
            __token = 975
            __content_139865838111856_973 = _lookup_attr(getitem('ship'), 'offsets')[7][1]
            __content_139865838111856_973 = __quote(__content_139865838111856_973, '\x00', '&#0;', None, False)
            __token = 1017
            __content_139865838111856_1015 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1015 = __quote(__content_139865838111856_1015, '\x00', '&#0;', None, False)
            __token = 1068
            __content_139865838111856_1066 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1066 = __quote(__content_139865838111856_1066, '\x00', '&#0;', None, False)
            __token = 1110
            __content_139865838111856_1108 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1108 = __quote(__content_139865838111856_1108, '\x00', '&#0;', None, False)
            __token = 1137
            __content_139865838111856_1135 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1135 = __quote(__content_139865838111856_1135, '\x00', '&#0;', None, False)
            __token = 1184
            __content_139865838111856_1182 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1182 = __quote(__content_139865838111856_1182, '\x00', '&#0;', None, False)
            __token = 1226
            __content_139865838111856_1224 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1224 = __quote(__content_139865838111856_1224, '\x00', '&#0;', None, False)
            __token = 1254
            __content_139865838111856_1252 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1252 = __quote(__content_139865838111856_1252, '\x00', '&#0;', None, False)
            __token = 1301
            __content_139865838111856_1299 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1299 = __quote(__content_139865838111856_1299, '\x00', '&#0;', None, False)
            __token = 1343
            __content_139865838111856_1341 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1341 = __quote(__content_139865838111856_1341, '\x00', '&#0;', None, False)
            __token = 1371
            __content_139865838111856_1369 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1369 = __quote(__content_139865838111856_1369, '\x00', '&#0;', None, False)
            __token = 1414
            __content_139865838111856_1412 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1412 = __quote(__content_139865838111856_1412, '\x00', '&#0;', None, False)
            __token = 1456
            __content_139865838111856_1454 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1454 = __quote(__content_139865838111856_1454, '\x00', '&#0;', None, False)
            __token = 1487
            __content_139865838111856_1485 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1485 = __quote(__content_139865838111856_1485, '\x00', '&#0;', None, False)
            __token = 1533
            __content_139865838111856_1531 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1531 = __quote(__content_139865838111856_1531, '\x00', '&#0;', None, False)
            __token = 1574
            __content_139865838111856_1572 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1572 = __quote(__content_139865838111856_1572, '\x00', '&#0;', None, False)
            __token = 1715
            __content_139865838111856_1713 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1713 = __quote(__content_139865838111856_1713, '\x00', '&#0;', None, False)
            __token = 1766
            __content_139865838111856_1764 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1764 = __quote(__content_139865838111856_1764, '\x00', '&#0;', None, False)
            __token = 1816
            __content_139865838111856_1814 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1814 = __quote(__content_139865838111856_1814, '\x00', '&#0;', None, False)
            __token = 1861
            __content_139865838111856_1859 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1859 = __quote(__content_139865838111856_1859, '\x00', '&#0;', None, False)
            __token = 1924
            __content_139865838111856_1922 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1922 = __quote(__content_139865838111856_1922, '\x00', '&#0;', None, False)
            __token = 1969
            __content_139865838111856_1967 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1967 = __quote(__content_139865838111856_1967, '\x00', '&#0;', None, False)
            __token = 2038
            __content_139865838111856_2036 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_2036 = __quote(__content_139865838111856_2036, '\x00', '&#0;', None, False)
            __token = 2097
            __content_139865838111856_2095 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_2095 = __quote(__content_139865838111856_2095, '\x00', '&#0;', None, False)
            __token = 2134
            __content_139865838111856_2132 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_2132 = __quote(__content_139865838111856_2132, '\x00', '&#0;', None, False)
            __token = 2219
            __content_139865838111856_2217 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_2217 = __quote(__content_139865838111856_2217, '\x00', '&#0;', None, False)
            __token = 2316
            __content_139865838111856_2314 = _lookup_attr(getitem('ship'), 'buy_menu_bb_xy')[0]
            __content_139865838111856_2314 = __quote(__content_139865838111856_2314, '\x00', '&#0;', None, False)
            __token = 2343
            __content_139865838111856_2341 = _lookup_attr(getitem('ship'), 'buy_menu_bb_xy')[1]
            __content_139865838111856_2341 = __quote(__content_139865838111856_2341, '\x00', '&#0;', None, False)
            __token = 2370
            __content_139865838111856_2368 = _lookup_attr(getitem('ship'), 'buy_menu_width')
            __content_139865838111856_2368 = __quote(__content_139865838111856_2368, '\x00', '&#0;', None, False)
            __token = 2399
            __content_139865838111856_2397 = int((_lookup_attr(getitem('ship'), 'buy_menu_width') / 2))
            __content_139865838111856_2397 = __quote(__content_139865838111856_2397, '\x00', '&#0;', None, False)
            __token = 2450
            __content_139865838111856_2448 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_2448 = __quote(__content_139865838111856_2448, '\x00', '&#0;', None, False)
            __token = 2488
            __content_139865838111856_2486 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_2486 = __quote(__content_139865838111856_2486, '\x00', '&#0;', None, False)
            __token = 2539
            __content_139865838111856_2537 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_2537 = __quote(__content_139865838111856_2537, '\x00', '&#0;', None, False)
            __token = 2567
            __content_139865838111856_2565 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_2565 = __quote(__content_139865838111856_2565, '\x00', '&#0;', None, False)
            __token = 2615
            __content_139865838111856_2613 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_2613 = __quote(__content_139865838111856_2613, '\x00', '&#0;', None, False)
            __token = 2669
            __content_139865838111856_2667 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_2667 = __quote(__content_139865838111856_2667, '\x00', '&#0;', None, False)
            __token = 2703
            __content_139865838111856_2701 = _lookup_attr(getitem('ship'), 'render_speed_switches')()
            __content_139865838111856_2701 = __quote(__content_139865838111856_2701, '\x00', '&#0;', None, False)
            __token = 2736
            __content_139865838111856_2734 = _lookup_attr(getitem('ship'), 'render_cargo_capacity')()
            __content_139865838111856_2734 = __quote(__content_139865838111856_2734, '\x00', '&#0;', None, False)
            __token = 2769
            __content_139865838111856_2767 = _lookup_attr(getitem('ship'), 'render_properties')()
            __content_139865838111856_2767 = __quote(__content_139865838111856_2767, '\x00', '&#0;', None, False)
            __content_139865838111856 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ((__content_139865838111856 if (__content_139865838111856 is not None) else ''), '\n\n// graphics\ntemplate spriteset_template_', (__content_139865838111856_69 if (__content_139865838111856_69 is not None) else ''), '(y) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [20,        y,          28,         89,          ', (__content_139865838111856_215 if (__content_139865838111856_215 is not None) else ''), ', ', (__content_139865838111856_238 if (__content_139865838111856_238 is not None) else ''), ', ANIM]\n    [60,        y,          113,        66,          ', (__content_139865838111856_320 if (__content_139865838111856_320 is not None) else ''), ', ', (__content_139865838111856_343 if (__content_139865838111856_343 is not None) else ''), ', ANIM]\n    [186,       y,          138,        48,          ', (__content_139865838111856_425 if (__content_139865838111856_425 is not None) else ''), ', ', (__content_139865838111856_448 if (__content_139865838111856_448 is not None) else ''), ', ANIM]\n    [328,       y,          113,        66,          ', (__content_139865838111856_530 if (__content_139865838111856_530 is not None) else ''), ', ', (__content_139865838111856_553 if (__content_139865838111856_553 is not None) else ''), ', ANIM]\n    [454,       y,          28,         89,          ', (__content_139865838111856_635 if (__content_139865838111856_635 is not None) else ''), ', ', (__content_139865838111856_658 if (__content_139865838111856_658 is not None) else ''), ', ANIM]\n    [494,       y,          113,        66,          ', (__content_139865838111856_740 if (__content_139865838111856_740 is not None) else ''), ', ', (__content_139865838111856_763 if (__content_139865838111856_763 is not None) else ''), ', ANIM]\n    [620,       y,          138,        48,          ', (__content_139865838111856_845 if (__content_139865838111856_845 is not None) else ''), ', ', (__content_139865838111856_868 if (__content_139865838111856_868 is not None) else ''), ', ANIM]\n    [762,       y,          113,        66,          ', (__content_139865838111856_950 if (__content_139865838111856_950 is not None) else ''), ', ', (__content_139865838111856_973 if (__content_139865838111856_973 is not None) else ''), ', ANIM]\n}\n\nspriteset(', (__content_139865838111856_1015 if (__content_139865838111856_1015 is not None) else ''), '_ss_not_loaded_not_moving, "src/graphics/', (__content_139865838111856_1066 if (__content_139865838111856_1066 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139865838111856_1108 if (__content_139865838111856_1108 is not None) else ''), '(10)\n}\nspriteset(', (__content_139865838111856_1135 if (__content_139865838111856_1135 is not None) else ''), '_ss_not_loaded_moving, "src/graphics/', (__content_139865838111856_1182 if (__content_139865838111856_1182 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139865838111856_1224 if (__content_139865838111856_1224 is not None) else ''), '(110)\n}\nspriteset(', (__content_139865838111856_1252 if (__content_139865838111856_1252 is not None) else ''), '_ss_loaded_not_moving, "src/graphics/', (__content_139865838111856_1299 if (__content_139865838111856_1299 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139865838111856_1341 if (__content_139865838111856_1341 is not None) else ''), '(210)\n}\nspriteset(', (__content_139865838111856_1369 if (__content_139865838111856_1369 is not None) else ''), '_ss_loaded_moving, "src/graphics/', (__content_139865838111856_1412 if (__content_139865838111856_1412 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139865838111856_1454 if (__content_139865838111856_1454 is not None) else ''), '(310)\n}\n\nspritegroup ', (__content_139865838111856_1485 if (__content_139865838111856_1485 is not None) else ''), '_sg_moving {\n    loaded:  [\n        ', (__content_139865838111856_1531 if (__content_139865838111856_1531 is not None) else ''), '_ss_not_loaded_moving,\n        ', (__content_139865838111856_1572 if (__content_139865838111856_1572 is not None) else ''), "_ss_loaded_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ", (__content_139865838111856_1713 if (__content_139865838111856_1713 is not None) else ''), '_ss_loaded_moving,\n    ];\n}\n\nspritegroup ', (__content_139865838111856_1764 if (__content_139865838111856_1764 is not None) else ''), '_sg_not_moving {\n    loaded:  [\n        ', (__content_139865838111856_1814 if (__content_139865838111856_1814 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_139865838111856_1859 if (__content_139865838111856_1859 is not None) else ''), '_ss_loaded_not_moving,\n    ];\n    loading: [\n        ', (__content_139865838111856_1922 if (__content_139865838111856_1922 is not None) else ''), '_ss_not_loaded_not_moving,\n        ', (__content_139865838111856_1967 if (__content_139865838111856_1967 is not None) else ''), '_ss_loaded_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_139865838111856_2036 if (__content_139865838111856_2036 is not None) else ''), '_switch_graphics, current_speed) {\n    0: return ', (__content_139865838111856_2095 if (__content_139865838111856_2095 is not None) else ''), '_sg_not_moving;\n    return ', (__content_139865838111856_2132 if (__content_139865838111856_2132 is not None) else ''), '_sg_moving;\n}\n\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_', (__content_139865838111856_2217 if (__content_139865838111856_2217 is not None) else ''), '() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [', (__content_139865838111856_2314 if (__content_139865838111856_2314 is not None) else ''), ', ', (__content_139865838111856_2341 if (__content_139865838111856_2341 is not None) else ''), ', ', (__content_139865838111856_2368 if (__content_139865838111856_2368 is not None) else ''), ', 22, -', (__content_139865838111856_2397 if (__content_139865838111856_2397 is not None) else ''), ', -10]\n}\n\nspriteset(', (__content_139865838111856_2448 if (__content_139865838111856_2448 is not None) else ''), '_ss_purchase, "src/graphics/', (__content_139865838111856_2486 if (__content_139865838111856_2486 is not None) else ''), '_0.png") {\n  spriteset_template_purchase_', (__content_139865838111856_2537 if (__content_139865838111856_2537 is not None) else ''), '()\n}\n\nspritegroup ', (__content_139865838111856_2565 if (__content_139865838111856_2565 is not None) else ''), '_sg_purchase {\n    loaded:  [\n        ', (__content_139865838111856_2613 if (__content_139865838111856_2613 is not None) else ''), '_ss_purchase,\n    ];\n    loading: [\n        ', (__content_139865838111856_2667 if (__content_139865838111856_2667 is not None) else ''), '_ss_purchase,\n    ];\n}\n\n', (__content_139865838111856_2701 if (__content_139865838111856_2701 is not None) else ''), '\n\n', (__content_139865838111856_2734 if (__content_139865838111856_2734 is not None) else ''), '\n\n', (__content_139865838111856_2767 if (__content_139865838111856_2767 is not None) else ''), '\n', ))
            if (__content_139865838111856 is None):
                pass
            else:
                if (__content_139865838111856 is False):
                    __content_139865838111856 = None
                else:
                    __tt = type(__content_139865838111856)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139865838111856 = str(__content_139865838111856)
                    else:
                        if (__tt is bytes):
                            __content_139865838111856 = decode(__content_139865838111856)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139865838111856 = __content_139865838111856.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139865838111856)
                                    __content_139865838111856 = (str(__content_139865838111856) if (__content_139865838111856 is __converted) else __converted)
                                else:
                                    __content_139865838111856 = __content_139865838111856()
            if (__content_139865838111856 is not None):
                __append(__content_139865838111856)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }