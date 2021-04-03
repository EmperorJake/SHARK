# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/templates/container_carrier.pynml'
__tokens = {0: ('${ship.render_debug_info()}\n\n// graphics\ntemplate spriteset_template_${ship.id}(y) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y,                       flags]\n    [20,        y,          28,         89,          ${ship.offsets[0][0]}, ${ship.offsets[0][1]}, ANIM]\n    [60,        y,          113,        71,          ${ship.offsets[1][0]}, ${ship.offsets[1][1]}, ANIM]\n    [186,       y,          138,        48,          ${ship.offsets[2][0]}, ${ship.offsets[2][1]}, ANIM]\n    [328,       y,          113,        71,          ${ship.offsets[3][0]}, ${ship.offsets[3][1]}, ANIM]\n    [454,       y,          28,         89,          ${ship.offsets[4][0]}, ${ship.offsets[4][1]}, ANIM]\n    [494,       y,          113,        71,          ${ship.offsets[5][0]}, ${ship.offsets[5][1]}, ANIM]\n    [620,       y,          138,        48,          ${ship.offsets[6][0]}, ${ship.offsets[6][1]}, ANIM]\n    [762,       y,          113,        71,          ${ship.offsets[7][0]}, ${ship.offsets[7][1]}, ANIM]\n}\n\nspriteset(${ship.id}_ss_empty_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(10)\n}\nspriteset(${ship.id}_ss_empty_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(110)\n}\nspriteset(${ship.id}_ss_loading_0_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(210)\n}\nspriteset(${ship.id}_ss_loaded_1_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(310)\n}\nspriteset(${ship.id}_ss_loaded_1_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(410)\n}\nspriteset(${ship.id}_ss_loaded_2_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(510)\n}\nspriteset(${ship.id}_ss_loaded_2_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(610)\n}\nspriteset(${ship.id}_ss_loaded_3_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(710)\n}\nspriteset(${ship.id}_ss_loaded_3_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(810)\n}\nspriteset(${ship.id}_ss_loaded_4_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(910)\n}\nspriteset(${ship.id}_ss_loaded_4_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(1010)\n}\n\nspritegroup ${ship.id}_sg_moving {\n    loaded:  [\n        ${ship.id}_ss_empty_moving,\n        ${ship.id}_ss_loaded_1_moving,\n        ${ship.id}_ss_loaded_2_moving,\n        ${ship.id}_ss_loaded_3_moving,\n        ${ship.id}_ss_loaded_4_moving,\n    ];\n    loading: [ // can\'t be loading when moving, but we\'ll overlook that, it\'s required by nml ;)\n        ${ship.id}_ss_empty_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_not_moving {\n    loaded:  [\n        ${ship.id}_ss_empty_not_moving,\n        ${ship.id}_ss_loaded_1_not_moving,\n        ${ship.id}_ss_loaded_2_not_moving,\n        ${ship.id}_ss_loaded_3_not_moving,\n        ${ship.id}_ss_loaded_4_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_loading_0_not_moving,\n        ${ship.id}_ss_loaded_1_not_moving,\n        ${ship.id}_ss_loaded_2_not_moving,\n        ${ship.id}_ss_loaded_3_not_moving,\n        ${ship.id}_ss_loaded_4_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, current_speed) {\n    0: return ${ship.id}_sg_not_moving;\n    return ${ship.id}_sg_moving;\n}\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_${ship.id}() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [${ship.buy_menu_bb_xy[0]}, ${ship.buy_menu_bb_xy[1]}, ${ship.buy_menu_width}, 22, -${int(ship.buy_menu_width / 2)}, -10]\n}\n\nspriteset(${ship.id}_ss_purchase, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_purchase_${ship.id}()\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_purchase,\n    ];\n    loading: [\n        ${ship.id}_ss_purchase,\n    ];\n}\n\n${ship.render_speed_switches()}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}', 1, 0), 2: ('ship.render_debug_info()', 1, 2), 71: ('ship.id', 4, 30), 246: ('ship.offsets[0][0]', 6, 55), 269: ('ship.offsets[0][1]', 6, 78), 351: ('ship.offsets[1][0]', 7, 55), 374: ('ship.offsets[1][1]', 7, 78), 456: ('ship.offsets[2][0]', 8, 55), 479: ('ship.offsets[2][1]', 8, 78), 561: ('ship.offsets[3][0]', 9, 55), 584: ('ship.offsets[3][1]', 9, 78), 666: ('ship.offsets[4][0]', 10, 55), 689: ('ship.offsets[4][1]', 10, 78), 771: ('ship.offsets[5][0]', 11, 55), 794: ('ship.offsets[5][1]', 11, 78), 876: ('ship.offsets[6][0]', 12, 55), 899: ('ship.offsets[6][1]', 12, 78), 981: ('ship.offsets[7][0]', 13, 55), 1004: ('ship.offsets[7][1]', 13, 78), 1046: ('ship.id', 16, 12), 1092: ('ship.id', 16, 58), 1134: ('ship.id', 17, 23), 1161: ('ship.id', 19, 12), 1203: ('ship.id', 19, 54), 1245: ('ship.id', 20, 23), 1273: ('ship.id', 22, 12), 1323: ('ship.id', 22, 62), 1365: ('ship.id', 23, 23), 1393: ('ship.id', 25, 12), 1442: ('ship.id', 25, 61), 1484: ('ship.id', 26, 23), 1512: ('ship.id', 28, 12), 1557: ('ship.id', 28, 57), 1599: ('ship.id', 29, 23), 1627: ('ship.id', 31, 12), 1676: ('ship.id', 31, 61), 1718: ('ship.id', 32, 23), 1746: ('ship.id', 34, 12), 1791: ('ship.id', 34, 57), 1833: ('ship.id', 35, 23), 1861: ('ship.id', 37, 12), 1910: ('ship.id', 37, 61), 1952: ('ship.id', 38, 23), 1980: ('ship.id', 40, 12), 2025: ('ship.id', 40, 57), 2067: ('ship.id', 41, 23), 2095: ('ship.id', 43, 12), 2144: ('ship.id', 43, 61), 2186: ('ship.id', 44, 23), 2214: ('ship.id', 46, 12), 2259: ('ship.id', 46, 57), 2301: ('ship.id', 47, 23), 2333: ('ship.id', 50, 14), 2379: ('ship.id', 52, 10), 2415: ('ship.id', 53, 10), 2454: ('ship.id', 54, 10), 2493: ('ship.id', 55, 10), 2532: ('ship.id', 56, 10), 2675: ('ship.id', 59, 10), 2725: ('ship.id', 63, 14), 2775: ('ship.id', 65, 10), 2815: ('ship.id', 66, 10), 2858: ('ship.id', 67, 10), 2901: ('ship.id', 68, 10), 2944: ('ship.id', 69, 10), 3009: ('ship.id', 72, 10), 3053: ('ship.id', 73, 10), 3096: ('ship.id', 74, 10), 3139: ('ship.id', 75, 10), 3182: ('ship.id', 76, 10), 3253: ('ship.id', 80, 28), 3312: ('ship.id', 81, 16), 3349: ('ship.id', 82, 13), 3433: ('ship.id', 87, 39), 3530: ('ship.buy_menu_bb_xy[0]', 89, 7), 3557: ('ship.buy_menu_bb_xy[1]', 89, 34), 3584: ('ship.buy_menu_width', 89, 61), 3613: ('int(ship.buy_menu_width / 2)', 89, 90), 3664: ('ship.id', 92, 12), 3702: ('ship.id', 92, 50), 3753: ('ship.id', 93, 32), 3781: ('ship.id', 96, 14), 3829: ('ship.id', 98, 10), 3883: ('ship.id', 101, 10), 3917: ('ship.render_speed_switches()', 105, 2), 3950: ('ship.render_cargo_capacity()', 107, 2), 3983: ('ship.render_properties()', 109, 2)}

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

            # <Interpolation value=<Substitution '${ship.render_debug_info()}\n\n// graphics\ntemplate spriteset_template_${ship.id}(y) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y,                       flags]\n    [20,        y,          28,         89,          ${ship.offsets[0][0]}, ${ship.offsets[0][1]}, ANIM]\n    [60,        y,          113,        71,          ${ship.offsets[1][0]}, ${ship.offsets[1][1]}, ANIM]\n    [186,       y,          138,        48,          ${ship.offsets[2][0]}, ${ship.offsets[2][1]}, ANIM]\n    [328,       y,          113,        71,          ${ship.offsets[3][0]}, ${ship.offsets[3][1]}, ANIM]\n    [454,       y,          28,         89,          ${ship.offsets[4][0]}, ${ship.offsets[4][1]}, ANIM]\n    [494,       y,          113,        71,          ${ship.offsets[5][0]}, ${ship.offsets[5][1]}, ANIM]\n    [620,       y,          138,        48,          ${ship.offsets[6][0]}, ${ship.offsets[6][1]}, ANIM]\n    [762,       y,          113,        71,          ${ship.offsets[7][0]}, ${ship.offsets[7][1]}, ANIM]\n}\n\nspriteset(${ship.id}_ss_empty_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(10)\n}\nspriteset(${ship.id}_ss_empty_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(110)\n}\nspriteset(${ship.id}_ss_loading_0_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(210)\n}\nspriteset(${ship.id}_ss_loaded_1_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(310)\n}\nspriteset(${ship.id}_ss_loaded_1_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(410)\n}\nspriteset(${ship.id}_ss_loaded_2_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(510)\n}\nspriteset(${ship.id}_ss_loaded_2_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(610)\n}\nspriteset(${ship.id}_ss_loaded_3_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(710)\n}\nspriteset(${ship.id}_ss_loaded_3_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(810)\n}\nspriteset(${ship.id}_ss_loaded_4_not_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(910)\n}\nspriteset(${ship.id}_ss_loaded_4_moving, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(1010)\n}\n\nspritegroup ${ship.id}_sg_moving {\n    loaded:  [\n        ${ship.id}_ss_empty_moving,\n        ${ship.id}_ss_loaded_1_moving,\n        ${ship.id}_ss_loaded_2_moving,\n        ${ship.id}_ss_loaded_3_moving,\n        ${ship.id}_ss_loaded_4_moving,\n    ];\n    loading: [ // can\'t be loading when moving, but we\'ll overlook that, it\'s required by nml ;)\n        ${ship.id}_ss_empty_moving,\n    ];\n}\n\nspritegroup ${ship.id}_sg_not_moving {\n    loaded:  [\n        ${ship.id}_ss_empty_not_moving,\n        ${ship.id}_ss_loaded_1_not_moving,\n        ${ship.id}_ss_loaded_2_not_moving,\n        ${ship.id}_ss_loaded_3_not_moving,\n        ${ship.id}_ss_loaded_4_not_moving,\n    ];\n    loading: [\n        ${ship.id}_ss_loading_0_not_moving,\n        ${ship.id}_ss_loaded_1_not_moving,\n        ${ship.id}_ss_loaded_2_not_moving,\n        ${ship.id}_ss_loaded_3_not_moving,\n        ${ship.id}_ss_loaded_4_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, current_speed) {\n    0: return ${ship.id}_sg_not_moving;\n    return ${ship.id}_sg_moving;\n}\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_${ship.id}() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [${ship.buy_menu_bb_xy[0]}, ${ship.buy_menu_bb_xy[1]}, ${ship.buy_menu_width}, 22, -${int(ship.buy_menu_width / 2)}, -10]\n}\n\nspriteset(${ship.id}_ss_purchase, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_purchase_${ship.id}()\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_purchase,\n    ];\n    loading: [\n        ${ship.id}_ss_purchase,\n    ];\n}\n\n${ship.render_speed_switches()}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}\n' (1:0)> braces_required=True translation=False at 7f29f4098780> -> __content_139818181960344
            __token = 0
            __token = 2
            __content_139818181960344 = _lookup_attr(getitem('ship'), 'render_debug_info')()
            __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
            __token = 71
            __content_139818181960344_69 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_69 = __quote(__content_139818181960344_69, '\x00', '&#0;', None, False)
            __token = 246
            __content_139818181960344_244 = _lookup_attr(getitem('ship'), 'offsets')[0][0]
            __content_139818181960344_244 = __quote(__content_139818181960344_244, '\x00', '&#0;', None, False)
            __token = 269
            __content_139818181960344_267 = _lookup_attr(getitem('ship'), 'offsets')[0][1]
            __content_139818181960344_267 = __quote(__content_139818181960344_267, '\x00', '&#0;', None, False)
            __token = 351
            __content_139818181960344_349 = _lookup_attr(getitem('ship'), 'offsets')[1][0]
            __content_139818181960344_349 = __quote(__content_139818181960344_349, '\x00', '&#0;', None, False)
            __token = 374
            __content_139818181960344_372 = _lookup_attr(getitem('ship'), 'offsets')[1][1]
            __content_139818181960344_372 = __quote(__content_139818181960344_372, '\x00', '&#0;', None, False)
            __token = 456
            __content_139818181960344_454 = _lookup_attr(getitem('ship'), 'offsets')[2][0]
            __content_139818181960344_454 = __quote(__content_139818181960344_454, '\x00', '&#0;', None, False)
            __token = 479
            __content_139818181960344_477 = _lookup_attr(getitem('ship'), 'offsets')[2][1]
            __content_139818181960344_477 = __quote(__content_139818181960344_477, '\x00', '&#0;', None, False)
            __token = 561
            __content_139818181960344_559 = _lookup_attr(getitem('ship'), 'offsets')[3][0]
            __content_139818181960344_559 = __quote(__content_139818181960344_559, '\x00', '&#0;', None, False)
            __token = 584
            __content_139818181960344_582 = _lookup_attr(getitem('ship'), 'offsets')[3][1]
            __content_139818181960344_582 = __quote(__content_139818181960344_582, '\x00', '&#0;', None, False)
            __token = 666
            __content_139818181960344_664 = _lookup_attr(getitem('ship'), 'offsets')[4][0]
            __content_139818181960344_664 = __quote(__content_139818181960344_664, '\x00', '&#0;', None, False)
            __token = 689
            __content_139818181960344_687 = _lookup_attr(getitem('ship'), 'offsets')[4][1]
            __content_139818181960344_687 = __quote(__content_139818181960344_687, '\x00', '&#0;', None, False)
            __token = 771
            __content_139818181960344_769 = _lookup_attr(getitem('ship'), 'offsets')[5][0]
            __content_139818181960344_769 = __quote(__content_139818181960344_769, '\x00', '&#0;', None, False)
            __token = 794
            __content_139818181960344_792 = _lookup_attr(getitem('ship'), 'offsets')[5][1]
            __content_139818181960344_792 = __quote(__content_139818181960344_792, '\x00', '&#0;', None, False)
            __token = 876
            __content_139818181960344_874 = _lookup_attr(getitem('ship'), 'offsets')[6][0]
            __content_139818181960344_874 = __quote(__content_139818181960344_874, '\x00', '&#0;', None, False)
            __token = 899
            __content_139818181960344_897 = _lookup_attr(getitem('ship'), 'offsets')[6][1]
            __content_139818181960344_897 = __quote(__content_139818181960344_897, '\x00', '&#0;', None, False)
            __token = 981
            __content_139818181960344_979 = _lookup_attr(getitem('ship'), 'offsets')[7][0]
            __content_139818181960344_979 = __quote(__content_139818181960344_979, '\x00', '&#0;', None, False)
            __token = 1004
            __content_139818181960344_1002 = _lookup_attr(getitem('ship'), 'offsets')[7][1]
            __content_139818181960344_1002 = __quote(__content_139818181960344_1002, '\x00', '&#0;', None, False)
            __token = 1046
            __content_139818181960344_1044 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1044 = __quote(__content_139818181960344_1044, '\x00', '&#0;', None, False)
            __token = 1092
            __content_139818181960344_1090 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1090 = __quote(__content_139818181960344_1090, '\x00', '&#0;', None, False)
            __token = 1134
            __content_139818181960344_1132 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1132 = __quote(__content_139818181960344_1132, '\x00', '&#0;', None, False)
            __token = 1161
            __content_139818181960344_1159 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1159 = __quote(__content_139818181960344_1159, '\x00', '&#0;', None, False)
            __token = 1203
            __content_139818181960344_1201 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1201 = __quote(__content_139818181960344_1201, '\x00', '&#0;', None, False)
            __token = 1245
            __content_139818181960344_1243 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1243 = __quote(__content_139818181960344_1243, '\x00', '&#0;', None, False)
            __token = 1273
            __content_139818181960344_1271 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1271 = __quote(__content_139818181960344_1271, '\x00', '&#0;', None, False)
            __token = 1323
            __content_139818181960344_1321 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1321 = __quote(__content_139818181960344_1321, '\x00', '&#0;', None, False)
            __token = 1365
            __content_139818181960344_1363 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1363 = __quote(__content_139818181960344_1363, '\x00', '&#0;', None, False)
            __token = 1393
            __content_139818181960344_1391 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1391 = __quote(__content_139818181960344_1391, '\x00', '&#0;', None, False)
            __token = 1442
            __content_139818181960344_1440 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1440 = __quote(__content_139818181960344_1440, '\x00', '&#0;', None, False)
            __token = 1484
            __content_139818181960344_1482 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1482 = __quote(__content_139818181960344_1482, '\x00', '&#0;', None, False)
            __token = 1512
            __content_139818181960344_1510 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1510 = __quote(__content_139818181960344_1510, '\x00', '&#0;', None, False)
            __token = 1557
            __content_139818181960344_1555 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1555 = __quote(__content_139818181960344_1555, '\x00', '&#0;', None, False)
            __token = 1599
            __content_139818181960344_1597 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1597 = __quote(__content_139818181960344_1597, '\x00', '&#0;', None, False)
            __token = 1627
            __content_139818181960344_1625 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1625 = __quote(__content_139818181960344_1625, '\x00', '&#0;', None, False)
            __token = 1676
            __content_139818181960344_1674 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1674 = __quote(__content_139818181960344_1674, '\x00', '&#0;', None, False)
            __token = 1718
            __content_139818181960344_1716 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1716 = __quote(__content_139818181960344_1716, '\x00', '&#0;', None, False)
            __token = 1746
            __content_139818181960344_1744 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1744 = __quote(__content_139818181960344_1744, '\x00', '&#0;', None, False)
            __token = 1791
            __content_139818181960344_1789 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1789 = __quote(__content_139818181960344_1789, '\x00', '&#0;', None, False)
            __token = 1833
            __content_139818181960344_1831 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1831 = __quote(__content_139818181960344_1831, '\x00', '&#0;', None, False)
            __token = 1861
            __content_139818181960344_1859 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1859 = __quote(__content_139818181960344_1859, '\x00', '&#0;', None, False)
            __token = 1910
            __content_139818181960344_1908 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1908 = __quote(__content_139818181960344_1908, '\x00', '&#0;', None, False)
            __token = 1952
            __content_139818181960344_1950 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1950 = __quote(__content_139818181960344_1950, '\x00', '&#0;', None, False)
            __token = 1980
            __content_139818181960344_1978 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_1978 = __quote(__content_139818181960344_1978, '\x00', '&#0;', None, False)
            __token = 2025
            __content_139818181960344_2023 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2023 = __quote(__content_139818181960344_2023, '\x00', '&#0;', None, False)
            __token = 2067
            __content_139818181960344_2065 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2065 = __quote(__content_139818181960344_2065, '\x00', '&#0;', None, False)
            __token = 2095
            __content_139818181960344_2093 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2093 = __quote(__content_139818181960344_2093, '\x00', '&#0;', None, False)
            __token = 2144
            __content_139818181960344_2142 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2142 = __quote(__content_139818181960344_2142, '\x00', '&#0;', None, False)
            __token = 2186
            __content_139818181960344_2184 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2184 = __quote(__content_139818181960344_2184, '\x00', '&#0;', None, False)
            __token = 2214
            __content_139818181960344_2212 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2212 = __quote(__content_139818181960344_2212, '\x00', '&#0;', None, False)
            __token = 2259
            __content_139818181960344_2257 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2257 = __quote(__content_139818181960344_2257, '\x00', '&#0;', None, False)
            __token = 2301
            __content_139818181960344_2299 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2299 = __quote(__content_139818181960344_2299, '\x00', '&#0;', None, False)
            __token = 2333
            __content_139818181960344_2331 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2331 = __quote(__content_139818181960344_2331, '\x00', '&#0;', None, False)
            __token = 2379
            __content_139818181960344_2377 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2377 = __quote(__content_139818181960344_2377, '\x00', '&#0;', None, False)
            __token = 2415
            __content_139818181960344_2413 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2413 = __quote(__content_139818181960344_2413, '\x00', '&#0;', None, False)
            __token = 2454
            __content_139818181960344_2452 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2452 = __quote(__content_139818181960344_2452, '\x00', '&#0;', None, False)
            __token = 2493
            __content_139818181960344_2491 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2491 = __quote(__content_139818181960344_2491, '\x00', '&#0;', None, False)
            __token = 2532
            __content_139818181960344_2530 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2530 = __quote(__content_139818181960344_2530, '\x00', '&#0;', None, False)
            __token = 2675
            __content_139818181960344_2673 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2673 = __quote(__content_139818181960344_2673, '\x00', '&#0;', None, False)
            __token = 2725
            __content_139818181960344_2723 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2723 = __quote(__content_139818181960344_2723, '\x00', '&#0;', None, False)
            __token = 2775
            __content_139818181960344_2773 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2773 = __quote(__content_139818181960344_2773, '\x00', '&#0;', None, False)
            __token = 2815
            __content_139818181960344_2813 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2813 = __quote(__content_139818181960344_2813, '\x00', '&#0;', None, False)
            __token = 2858
            __content_139818181960344_2856 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2856 = __quote(__content_139818181960344_2856, '\x00', '&#0;', None, False)
            __token = 2901
            __content_139818181960344_2899 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2899 = __quote(__content_139818181960344_2899, '\x00', '&#0;', None, False)
            __token = 2944
            __content_139818181960344_2942 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2942 = __quote(__content_139818181960344_2942, '\x00', '&#0;', None, False)
            __token = 3009
            __content_139818181960344_3007 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3007 = __quote(__content_139818181960344_3007, '\x00', '&#0;', None, False)
            __token = 3053
            __content_139818181960344_3051 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3051 = __quote(__content_139818181960344_3051, '\x00', '&#0;', None, False)
            __token = 3096
            __content_139818181960344_3094 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3094 = __quote(__content_139818181960344_3094, '\x00', '&#0;', None, False)
            __token = 3139
            __content_139818181960344_3137 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3137 = __quote(__content_139818181960344_3137, '\x00', '&#0;', None, False)
            __token = 3182
            __content_139818181960344_3180 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3180 = __quote(__content_139818181960344_3180, '\x00', '&#0;', None, False)
            __token = 3253
            __content_139818181960344_3251 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3251 = __quote(__content_139818181960344_3251, '\x00', '&#0;', None, False)
            __token = 3312
            __content_139818181960344_3310 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3310 = __quote(__content_139818181960344_3310, '\x00', '&#0;', None, False)
            __token = 3349
            __content_139818181960344_3347 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3347 = __quote(__content_139818181960344_3347, '\x00', '&#0;', None, False)
            __token = 3433
            __content_139818181960344_3431 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3431 = __quote(__content_139818181960344_3431, '\x00', '&#0;', None, False)
            __token = 3530
            __content_139818181960344_3528 = _lookup_attr(getitem('ship'), 'buy_menu_bb_xy')[0]
            __content_139818181960344_3528 = __quote(__content_139818181960344_3528, '\x00', '&#0;', None, False)
            __token = 3557
            __content_139818181960344_3555 = _lookup_attr(getitem('ship'), 'buy_menu_bb_xy')[1]
            __content_139818181960344_3555 = __quote(__content_139818181960344_3555, '\x00', '&#0;', None, False)
            __token = 3584
            __content_139818181960344_3582 = _lookup_attr(getitem('ship'), 'buy_menu_width')
            __content_139818181960344_3582 = __quote(__content_139818181960344_3582, '\x00', '&#0;', None, False)
            __token = 3613
            __content_139818181960344_3611 = int((_lookup_attr(getitem('ship'), 'buy_menu_width') / 2))
            __content_139818181960344_3611 = __quote(__content_139818181960344_3611, '\x00', '&#0;', None, False)
            __token = 3664
            __content_139818181960344_3662 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3662 = __quote(__content_139818181960344_3662, '\x00', '&#0;', None, False)
            __token = 3702
            __content_139818181960344_3700 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3700 = __quote(__content_139818181960344_3700, '\x00', '&#0;', None, False)
            __token = 3753
            __content_139818181960344_3751 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3751 = __quote(__content_139818181960344_3751, '\x00', '&#0;', None, False)
            __token = 3781
            __content_139818181960344_3779 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3779 = __quote(__content_139818181960344_3779, '\x00', '&#0;', None, False)
            __token = 3829
            __content_139818181960344_3827 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3827 = __quote(__content_139818181960344_3827, '\x00', '&#0;', None, False)
            __token = 3883
            __content_139818181960344_3881 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3881 = __quote(__content_139818181960344_3881, '\x00', '&#0;', None, False)
            __token = 3917
            __content_139818181960344_3915 = _lookup_attr(getitem('ship'), 'render_speed_switches')()
            __content_139818181960344_3915 = __quote(__content_139818181960344_3915, '\x00', '&#0;', None, False)
            __token = 3950
            __content_139818181960344_3948 = _lookup_attr(getitem('ship'), 'render_cargo_capacity')()
            __content_139818181960344_3948 = __quote(__content_139818181960344_3948, '\x00', '&#0;', None, False)
            __token = 3983
            __content_139818181960344_3981 = _lookup_attr(getitem('ship'), 'render_properties')()
            __content_139818181960344_3981 = __quote(__content_139818181960344_3981, '\x00', '&#0;', None, False)
            __content_139818181960344 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ((__content_139818181960344 if (__content_139818181960344 is not None) else ''), '\n\n// graphics\ntemplate spriteset_template_', (__content_139818181960344_69 if (__content_139818181960344_69 is not None) else ''), '(y) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y,                       flags]\n    [20,        y,          28,         89,          ', (__content_139818181960344_244 if (__content_139818181960344_244 is not None) else ''), ', ', (__content_139818181960344_267 if (__content_139818181960344_267 is not None) else ''), ', ANIM]\n    [60,        y,          113,        71,          ', (__content_139818181960344_349 if (__content_139818181960344_349 is not None) else ''), ', ', (__content_139818181960344_372 if (__content_139818181960344_372 is not None) else ''), ', ANIM]\n    [186,       y,          138,        48,          ', (__content_139818181960344_454 if (__content_139818181960344_454 is not None) else ''), ', ', (__content_139818181960344_477 if (__content_139818181960344_477 is not None) else ''), ', ANIM]\n    [328,       y,          113,        71,          ', (__content_139818181960344_559 if (__content_139818181960344_559 is not None) else ''), ', ', (__content_139818181960344_582 if (__content_139818181960344_582 is not None) else ''), ', ANIM]\n    [454,       y,          28,         89,          ', (__content_139818181960344_664 if (__content_139818181960344_664 is not None) else ''), ', ', (__content_139818181960344_687 if (__content_139818181960344_687 is not None) else ''), ', ANIM]\n    [494,       y,          113,        71,          ', (__content_139818181960344_769 if (__content_139818181960344_769 is not None) else ''), ', ', (__content_139818181960344_792 if (__content_139818181960344_792 is not None) else ''), ', ANIM]\n    [620,       y,          138,        48,          ', (__content_139818181960344_874 if (__content_139818181960344_874 is not None) else ''), ', ', (__content_139818181960344_897 if (__content_139818181960344_897 is not None) else ''), ', ANIM]\n    [762,       y,          113,        71,          ', (__content_139818181960344_979 if (__content_139818181960344_979 is not None) else ''), ', ', (__content_139818181960344_1002 if (__content_139818181960344_1002 is not None) else ''), ', ANIM]\n}\n\nspriteset(', (__content_139818181960344_1044 if (__content_139818181960344_1044 is not None) else ''), '_ss_empty_not_moving, "src/graphics/', (__content_139818181960344_1090 if (__content_139818181960344_1090 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139818181960344_1132 if (__content_139818181960344_1132 is not None) else ''), '(10)\n}\nspriteset(', (__content_139818181960344_1159 if (__content_139818181960344_1159 is not None) else ''), '_ss_empty_moving, "src/graphics/', (__content_139818181960344_1201 if (__content_139818181960344_1201 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139818181960344_1243 if (__content_139818181960344_1243 is not None) else ''), '(110)\n}\nspriteset(', (__content_139818181960344_1271 if (__content_139818181960344_1271 is not None) else ''), '_ss_loading_0_not_moving, "src/graphics/', (__content_139818181960344_1321 if (__content_139818181960344_1321 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139818181960344_1363 if (__content_139818181960344_1363 is not None) else ''), '(210)\n}\nspriteset(', (__content_139818181960344_1391 if (__content_139818181960344_1391 is not None) else ''), '_ss_loaded_1_not_moving, "src/graphics/', (__content_139818181960344_1440 if (__content_139818181960344_1440 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139818181960344_1482 if (__content_139818181960344_1482 is not None) else ''), '(310)\n}\nspriteset(', (__content_139818181960344_1510 if (__content_139818181960344_1510 is not None) else ''), '_ss_loaded_1_moving, "src/graphics/', (__content_139818181960344_1555 if (__content_139818181960344_1555 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139818181960344_1597 if (__content_139818181960344_1597 is not None) else ''), '(410)\n}\nspriteset(', (__content_139818181960344_1625 if (__content_139818181960344_1625 is not None) else ''), '_ss_loaded_2_not_moving, "src/graphics/', (__content_139818181960344_1674 if (__content_139818181960344_1674 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139818181960344_1716 if (__content_139818181960344_1716 is not None) else ''), '(510)\n}\nspriteset(', (__content_139818181960344_1744 if (__content_139818181960344_1744 is not None) else ''), '_ss_loaded_2_moving, "src/graphics/', (__content_139818181960344_1789 if (__content_139818181960344_1789 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139818181960344_1831 if (__content_139818181960344_1831 is not None) else ''), '(610)\n}\nspriteset(', (__content_139818181960344_1859 if (__content_139818181960344_1859 is not None) else ''), '_ss_loaded_3_not_moving, "src/graphics/', (__content_139818181960344_1908 if (__content_139818181960344_1908 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139818181960344_1950 if (__content_139818181960344_1950 is not None) else ''), '(710)\n}\nspriteset(', (__content_139818181960344_1978 if (__content_139818181960344_1978 is not None) else ''), '_ss_loaded_3_moving, "src/graphics/', (__content_139818181960344_2023 if (__content_139818181960344_2023 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139818181960344_2065 if (__content_139818181960344_2065 is not None) else ''), '(810)\n}\nspriteset(', (__content_139818181960344_2093 if (__content_139818181960344_2093 is not None) else ''), '_ss_loaded_4_not_moving, "src/graphics/', (__content_139818181960344_2142 if (__content_139818181960344_2142 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139818181960344_2184 if (__content_139818181960344_2184 is not None) else ''), '(910)\n}\nspriteset(', (__content_139818181960344_2212 if (__content_139818181960344_2212 is not None) else ''), '_ss_loaded_4_moving, "src/graphics/', (__content_139818181960344_2257 if (__content_139818181960344_2257 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_139818181960344_2299 if (__content_139818181960344_2299 is not None) else ''), '(1010)\n}\n\nspritegroup ', (__content_139818181960344_2331 if (__content_139818181960344_2331 is not None) else ''), '_sg_moving {\n    loaded:  [\n        ', (__content_139818181960344_2377 if (__content_139818181960344_2377 is not None) else ''), '_ss_empty_moving,\n        ', (__content_139818181960344_2413 if (__content_139818181960344_2413 is not None) else ''), '_ss_loaded_1_moving,\n        ', (__content_139818181960344_2452 if (__content_139818181960344_2452 is not None) else ''), '_ss_loaded_2_moving,\n        ', (__content_139818181960344_2491 if (__content_139818181960344_2491 is not None) else ''), '_ss_loaded_3_moving,\n        ', (__content_139818181960344_2530 if (__content_139818181960344_2530 is not None) else ''), "_ss_loaded_4_moving,\n    ];\n    loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n        ", (__content_139818181960344_2673 if (__content_139818181960344_2673 is not None) else ''), '_ss_empty_moving,\n    ];\n}\n\nspritegroup ', (__content_139818181960344_2723 if (__content_139818181960344_2723 is not None) else ''), '_sg_not_moving {\n    loaded:  [\n        ', (__content_139818181960344_2773 if (__content_139818181960344_2773 is not None) else ''), '_ss_empty_not_moving,\n        ', (__content_139818181960344_2813 if (__content_139818181960344_2813 is not None) else ''), '_ss_loaded_1_not_moving,\n        ', (__content_139818181960344_2856 if (__content_139818181960344_2856 is not None) else ''), '_ss_loaded_2_not_moving,\n        ', (__content_139818181960344_2899 if (__content_139818181960344_2899 is not None) else ''), '_ss_loaded_3_not_moving,\n        ', (__content_139818181960344_2942 if (__content_139818181960344_2942 is not None) else ''), '_ss_loaded_4_not_moving,\n    ];\n    loading: [\n        ', (__content_139818181960344_3007 if (__content_139818181960344_3007 is not None) else ''), '_ss_loading_0_not_moving,\n        ', (__content_139818181960344_3051 if (__content_139818181960344_3051 is not None) else ''), '_ss_loaded_1_not_moving,\n        ', (__content_139818181960344_3094 if (__content_139818181960344_3094 is not None) else ''), '_ss_loaded_2_not_moving,\n        ', (__content_139818181960344_3137 if (__content_139818181960344_3137 is not None) else ''), '_ss_loaded_3_not_moving,\n        ', (__content_139818181960344_3180 if (__content_139818181960344_3180 is not None) else ''), '_ss_loaded_4_not_moving,\n    ];\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_139818181960344_3251 if (__content_139818181960344_3251 is not None) else ''), '_switch_graphics, current_speed) {\n    0: return ', (__content_139818181960344_3310 if (__content_139818181960344_3310 is not None) else ''), '_sg_not_moving;\n    return ', (__content_139818181960344_3347 if (__content_139818181960344_3347 is not None) else ''), '_sg_moving;\n}\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_', (__content_139818181960344_3431 if (__content_139818181960344_3431 is not None) else ''), '() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [', (__content_139818181960344_3528 if (__content_139818181960344_3528 is not None) else ''), ', ', (__content_139818181960344_3555 if (__content_139818181960344_3555 is not None) else ''), ', ', (__content_139818181960344_3582 if (__content_139818181960344_3582 is not None) else ''), ', 22, -', (__content_139818181960344_3611 if (__content_139818181960344_3611 is not None) else ''), ', -10]\n}\n\nspriteset(', (__content_139818181960344_3662 if (__content_139818181960344_3662 is not None) else ''), '_ss_purchase, "src/graphics/', (__content_139818181960344_3700 if (__content_139818181960344_3700 is not None) else ''), '_0.png") {\n  spriteset_template_purchase_', (__content_139818181960344_3751 if (__content_139818181960344_3751 is not None) else ''), '()\n}\n\nspritegroup ', (__content_139818181960344_3779 if (__content_139818181960344_3779 is not None) else ''), '_sg_purchase {\n    loaded:  [\n        ', (__content_139818181960344_3827 if (__content_139818181960344_3827 is not None) else ''), '_ss_purchase,\n    ];\n    loading: [\n        ', (__content_139818181960344_3881 if (__content_139818181960344_3881 is not None) else ''), '_ss_purchase,\n    ];\n}\n\n', (__content_139818181960344_3915 if (__content_139818181960344_3915 is not None) else ''), '\n\n', (__content_139818181960344_3948 if (__content_139818181960344_3948 is not None) else ''), '\n\n', (__content_139818181960344_3981 if (__content_139818181960344_3981 is not None) else ''), '\n', ))
            if (__content_139818181960344 is None):
                pass
            else:
                if (__content_139818181960344 is False):
                    __content_139818181960344 = None
                else:
                    __tt = type(__content_139818181960344)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139818181960344 = str(__content_139818181960344)
                    else:
                        if (__tt is bytes):
                            __content_139818181960344 = decode(__content_139818181960344)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139818181960344 = __content_139818181960344.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139818181960344)
                                    __content_139818181960344 = (str(__content_139818181960344) if (__content_139818181960344 is __converted) else __converted)
                                else:
                                    __content_139818181960344 = __content_139818181960344()
            if (__content_139818181960344 is not None):
                __append(__content_139818181960344)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }