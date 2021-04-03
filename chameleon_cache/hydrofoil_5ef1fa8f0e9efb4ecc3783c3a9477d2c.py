# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/fish1672/src/templates/hydrofoil.pynml'
__tokens = {0: ('${ship.render_debug_info()}\n\n// graphics\n\ntemplate spriteset_template_${ship.id}(y, y_offs_adjust) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [20,        y,          28,         89,          ${ship.offsets[0][0]}, ${ship.offsets[0][1]} + y_offs_adjust, ANIM]\n    [60,        y,          113,        66,          ${ship.offsets[1][0]}, ${ship.offsets[1][1]} + y_offs_adjust, ANIM]\n    [186,       y,          138,        48,          ${ship.offsets[2][0]}, ${ship.offsets[2][1]} + y_offs_adjust, ANIM]\n    [328,       y,          113,        66,          ${ship.offsets[3][0]}, ${ship.offsets[3][1]} + y_offs_adjust, ANIM]\n    [454,       y,          28,         89,          ${ship.offsets[4][0]}, ${ship.offsets[4][1]} + y_offs_adjust, ANIM]\n    [494,       y,          113,        66,          ${ship.offsets[5][0]}, ${ship.offsets[5][1]} + y_offs_adjust, ANIM]\n    [620,       y,          138,        48,          ${ship.offsets[6][0]}, ${ship.offsets[6][1]} + y_offs_adjust, ANIM]\n    [762,       y,          113,        66,          ${ship.offsets[7][0]}, ${ship.offsets[7][1]} + y_offs_adjust, ANIM]\n}\n\nspriteset(${ship.id}_ss_speed_1, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(10, 0)\n}\nspriteset(${ship.id}_ss_speed_2, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(110, -1)\n}\nspriteset(${ship.id}_ss_speed_3, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(210, -2)\n}\nspriteset(${ship.id}_ss_speed_4, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(310, -3)\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, current_speed) {\n    0: return ${ship.id}_ss_speed_1;\n    1..${int((0.45*ship.speed) / 3) - 1}: ${ship.id}_ss_speed_2;\n    ${int((0.45*ship.speed) / 3)}..${2 * int((0.45*ship.speed) / 3) - 1}: ${ship.id}_ss_speed_3;\n    return ${ship.id}_ss_speed_4;\n}\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_${ship.id}() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [${ship.buy_menu_bb_xy[0]}, ${ship.buy_menu_bb_xy[1]}, ${ship.buy_menu_width}, 22, -${int(ship.buy_menu_width / 2)}, -10]\n}\n\nspriteset(${ship.id}_ss_purchase, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_purchase_${ship.id}()\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_purchase,\n    ];\n    loading: [\n        ${ship.id}_ss_purchase,\n    ];\n}\n\n${ship.render_speed_switches()}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}', 1, 0), 2: ('ship.render_debug_info()', 1, 2), 72: ('ship.id', 5, 30), 233: ('ship.offsets[0][0]', 7, 55), 256: ('ship.offsets[0][1]', 7, 78), 354: ('ship.offsets[1][0]', 8, 55), 377: ('ship.offsets[1][1]', 8, 78), 475: ('ship.offsets[2][0]', 9, 55), 498: ('ship.offsets[2][1]', 9, 78), 596: ('ship.offsets[3][0]', 10, 55), 619: ('ship.offsets[3][1]', 10, 78), 717: ('ship.offsets[4][0]', 11, 55), 740: ('ship.offsets[4][1]', 11, 78), 838: ('ship.offsets[5][0]', 12, 55), 861: ('ship.offsets[5][1]', 12, 78), 959: ('ship.offsets[6][0]', 13, 55), 982: ('ship.offsets[6][1]', 13, 78), 1080: ('ship.offsets[7][0]', 14, 55), 1103: ('ship.offsets[7][1]', 14, 78), 1161: ('ship.id', 17, 12), 1198: ('ship.id', 17, 49), 1240: ('ship.id', 18, 23), 1270: ('ship.id', 20, 12), 1307: ('ship.id', 20, 49), 1349: ('ship.id', 21, 23), 1381: ('ship.id', 23, 12), 1418: ('ship.id', 23, 49), 1460: ('ship.id', 24, 23), 1492: ('ship.id', 26, 12), 1529: ('ship.id', 26, 49), 1571: ('ship.id', 27, 23), 1620: ('ship.id', 30, 28), 1679: ('ship.id', 31, 16), 1709: ('int((0.45*ship.speed) / 3) - 1', 32, 9), 1744: ('ship.id', 32, 44), 1771: ('int((0.45*ship.speed) / 3)', 33, 6), 1802: ('2 * int((0.45*ship.speed) / 3) - 1', 33, 37), 1841: ('ship.id', 33, 76), 1875: ('ship.id', 34, 13), 1960: ('ship.id', 39, 39), 2057: ('ship.buy_menu_bb_xy[0]', 41, 7), 2084: ('ship.buy_menu_bb_xy[1]', 41, 34), 2111: ('ship.buy_menu_width', 41, 61), 2140: ('int(ship.buy_menu_width / 2)', 41, 90), 2191: ('ship.id', 44, 12), 2229: ('ship.id', 44, 50), 2280: ('ship.id', 45, 32), 2308: ('ship.id', 48, 14), 2356: ('ship.id', 50, 10), 2410: ('ship.id', 53, 10), 2444: ('ship.render_speed_switches()', 57, 2), 2477: ('ship.render_cargo_capacity()', 59, 2), 2510: ('ship.render_properties()', 61, 2)}

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

            # <Interpolation value=<Substitution '${ship.render_debug_info()}\n\n// graphics\n\ntemplate spriteset_template_${ship.id}(y, y_offs_adjust) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [20,        y,          28,         89,          ${ship.offsets[0][0]}, ${ship.offsets[0][1]} + y_offs_adjust, ANIM]\n    [60,        y,          113,        66,          ${ship.offsets[1][0]}, ${ship.offsets[1][1]} + y_offs_adjust, ANIM]\n    [186,       y,          138,        48,          ${ship.offsets[2][0]}, ${ship.offsets[2][1]} + y_offs_adjust, ANIM]\n    [328,       y,          113,        66,          ${ship.offsets[3][0]}, ${ship.offsets[3][1]} + y_offs_adjust, ANIM]\n    [454,       y,          28,         89,          ${ship.offsets[4][0]}, ${ship.offsets[4][1]} + y_offs_adjust, ANIM]\n    [494,       y,          113,        66,          ${ship.offsets[5][0]}, ${ship.offsets[5][1]} + y_offs_adjust, ANIM]\n    [620,       y,          138,        48,          ${ship.offsets[6][0]}, ${ship.offsets[6][1]} + y_offs_adjust, ANIM]\n    [762,       y,          113,        66,          ${ship.offsets[7][0]}, ${ship.offsets[7][1]} + y_offs_adjust, ANIM]\n}\n\nspriteset(${ship.id}_ss_speed_1, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(10, 0)\n}\nspriteset(${ship.id}_ss_speed_2, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(110, -1)\n}\nspriteset(${ship.id}_ss_speed_3, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(210, -2)\n}\nspriteset(${ship.id}_ss_speed_4, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_${ship.id}(310, -3)\n}\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, current_speed) {\n    0: return ${ship.id}_ss_speed_1;\n    1..${int((0.45*ship.speed) / 3) - 1}: ${ship.id}_ss_speed_2;\n    ${int((0.45*ship.speed) / 3)}..${2 * int((0.45*ship.speed) / 3) - 1}: ${ship.id}_ss_speed_3;\n    return ${ship.id}_ss_speed_4;\n}\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_${ship.id}() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [${ship.buy_menu_bb_xy[0]}, ${ship.buy_menu_bb_xy[1]}, ${ship.buy_menu_width}, 22, -${int(ship.buy_menu_width / 2)}, -10]\n}\n\nspriteset(${ship.id}_ss_purchase, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_purchase_${ship.id}()\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_purchase,\n    ];\n    loading: [\n        ${ship.id}_ss_purchase,\n    ];\n}\n\n${ship.render_speed_switches()}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}\n' (1:0)> braces_required=True translation=False at 7ff884e98da0> -> __content_140705374776208
            __token = 0
            __token = 2
            __content_140705374776208 = _lookup_attr(getitem('ship'), 'render_debug_info')()
            __content_140705374776208 = __quote(__content_140705374776208, '\x00', '&#0;', None, False)
            __token = 72
            __content_140705374776208_70 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_70 = __quote(__content_140705374776208_70, '\x00', '&#0;', None, False)
            __token = 233
            __content_140705374776208_231 = _lookup_attr(getitem('ship'), 'offsets')[0][0]
            __content_140705374776208_231 = __quote(__content_140705374776208_231, '\x00', '&#0;', None, False)
            __token = 256
            __content_140705374776208_254 = _lookup_attr(getitem('ship'), 'offsets')[0][1]
            __content_140705374776208_254 = __quote(__content_140705374776208_254, '\x00', '&#0;', None, False)
            __token = 354
            __content_140705374776208_352 = _lookup_attr(getitem('ship'), 'offsets')[1][0]
            __content_140705374776208_352 = __quote(__content_140705374776208_352, '\x00', '&#0;', None, False)
            __token = 377
            __content_140705374776208_375 = _lookup_attr(getitem('ship'), 'offsets')[1][1]
            __content_140705374776208_375 = __quote(__content_140705374776208_375, '\x00', '&#0;', None, False)
            __token = 475
            __content_140705374776208_473 = _lookup_attr(getitem('ship'), 'offsets')[2][0]
            __content_140705374776208_473 = __quote(__content_140705374776208_473, '\x00', '&#0;', None, False)
            __token = 498
            __content_140705374776208_496 = _lookup_attr(getitem('ship'), 'offsets')[2][1]
            __content_140705374776208_496 = __quote(__content_140705374776208_496, '\x00', '&#0;', None, False)
            __token = 596
            __content_140705374776208_594 = _lookup_attr(getitem('ship'), 'offsets')[3][0]
            __content_140705374776208_594 = __quote(__content_140705374776208_594, '\x00', '&#0;', None, False)
            __token = 619
            __content_140705374776208_617 = _lookup_attr(getitem('ship'), 'offsets')[3][1]
            __content_140705374776208_617 = __quote(__content_140705374776208_617, '\x00', '&#0;', None, False)
            __token = 717
            __content_140705374776208_715 = _lookup_attr(getitem('ship'), 'offsets')[4][0]
            __content_140705374776208_715 = __quote(__content_140705374776208_715, '\x00', '&#0;', None, False)
            __token = 740
            __content_140705374776208_738 = _lookup_attr(getitem('ship'), 'offsets')[4][1]
            __content_140705374776208_738 = __quote(__content_140705374776208_738, '\x00', '&#0;', None, False)
            __token = 838
            __content_140705374776208_836 = _lookup_attr(getitem('ship'), 'offsets')[5][0]
            __content_140705374776208_836 = __quote(__content_140705374776208_836, '\x00', '&#0;', None, False)
            __token = 861
            __content_140705374776208_859 = _lookup_attr(getitem('ship'), 'offsets')[5][1]
            __content_140705374776208_859 = __quote(__content_140705374776208_859, '\x00', '&#0;', None, False)
            __token = 959
            __content_140705374776208_957 = _lookup_attr(getitem('ship'), 'offsets')[6][0]
            __content_140705374776208_957 = __quote(__content_140705374776208_957, '\x00', '&#0;', None, False)
            __token = 982
            __content_140705374776208_980 = _lookup_attr(getitem('ship'), 'offsets')[6][1]
            __content_140705374776208_980 = __quote(__content_140705374776208_980, '\x00', '&#0;', None, False)
            __token = 1080
            __content_140705374776208_1078 = _lookup_attr(getitem('ship'), 'offsets')[7][0]
            __content_140705374776208_1078 = __quote(__content_140705374776208_1078, '\x00', '&#0;', None, False)
            __token = 1103
            __content_140705374776208_1101 = _lookup_attr(getitem('ship'), 'offsets')[7][1]
            __content_140705374776208_1101 = __quote(__content_140705374776208_1101, '\x00', '&#0;', None, False)
            __token = 1161
            __content_140705374776208_1159 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1159 = __quote(__content_140705374776208_1159, '\x00', '&#0;', None, False)
            __token = 1198
            __content_140705374776208_1196 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1196 = __quote(__content_140705374776208_1196, '\x00', '&#0;', None, False)
            __token = 1240
            __content_140705374776208_1238 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1238 = __quote(__content_140705374776208_1238, '\x00', '&#0;', None, False)
            __token = 1270
            __content_140705374776208_1268 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1268 = __quote(__content_140705374776208_1268, '\x00', '&#0;', None, False)
            __token = 1307
            __content_140705374776208_1305 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1305 = __quote(__content_140705374776208_1305, '\x00', '&#0;', None, False)
            __token = 1349
            __content_140705374776208_1347 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1347 = __quote(__content_140705374776208_1347, '\x00', '&#0;', None, False)
            __token = 1381
            __content_140705374776208_1379 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1379 = __quote(__content_140705374776208_1379, '\x00', '&#0;', None, False)
            __token = 1418
            __content_140705374776208_1416 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1416 = __quote(__content_140705374776208_1416, '\x00', '&#0;', None, False)
            __token = 1460
            __content_140705374776208_1458 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1458 = __quote(__content_140705374776208_1458, '\x00', '&#0;', None, False)
            __token = 1492
            __content_140705374776208_1490 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1490 = __quote(__content_140705374776208_1490, '\x00', '&#0;', None, False)
            __token = 1529
            __content_140705374776208_1527 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1527 = __quote(__content_140705374776208_1527, '\x00', '&#0;', None, False)
            __token = 1571
            __content_140705374776208_1569 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1569 = __quote(__content_140705374776208_1569, '\x00', '&#0;', None, False)
            __token = 1620
            __content_140705374776208_1618 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1618 = __quote(__content_140705374776208_1618, '\x00', '&#0;', None, False)
            __token = 1679
            __content_140705374776208_1677 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1677 = __quote(__content_140705374776208_1677, '\x00', '&#0;', None, False)
            __token = 1709
            __content_140705374776208_1707 = (int(((0.45 * _lookup_attr(getitem('ship'), 'speed')) / 3)) - 1)
            __content_140705374776208_1707 = __quote(__content_140705374776208_1707, '\x00', '&#0;', None, False)
            __token = 1744
            __content_140705374776208_1742 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1742 = __quote(__content_140705374776208_1742, '\x00', '&#0;', None, False)
            __token = 1771
            __content_140705374776208_1769 = int(((0.45 * _lookup_attr(getitem('ship'), 'speed')) / 3))
            __content_140705374776208_1769 = __quote(__content_140705374776208_1769, '\x00', '&#0;', None, False)
            __token = 1802
            __content_140705374776208_1800 = ((2 * int(((0.45 * _lookup_attr(getitem('ship'), 'speed')) / 3))) - 1)
            __content_140705374776208_1800 = __quote(__content_140705374776208_1800, '\x00', '&#0;', None, False)
            __token = 1841
            __content_140705374776208_1839 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1839 = __quote(__content_140705374776208_1839, '\x00', '&#0;', None, False)
            __token = 1875
            __content_140705374776208_1873 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1873 = __quote(__content_140705374776208_1873, '\x00', '&#0;', None, False)
            __token = 1960
            __content_140705374776208_1958 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_1958 = __quote(__content_140705374776208_1958, '\x00', '&#0;', None, False)
            __token = 2057
            __content_140705374776208_2055 = _lookup_attr(getitem('ship'), 'buy_menu_bb_xy')[0]
            __content_140705374776208_2055 = __quote(__content_140705374776208_2055, '\x00', '&#0;', None, False)
            __token = 2084
            __content_140705374776208_2082 = _lookup_attr(getitem('ship'), 'buy_menu_bb_xy')[1]
            __content_140705374776208_2082 = __quote(__content_140705374776208_2082, '\x00', '&#0;', None, False)
            __token = 2111
            __content_140705374776208_2109 = _lookup_attr(getitem('ship'), 'buy_menu_width')
            __content_140705374776208_2109 = __quote(__content_140705374776208_2109, '\x00', '&#0;', None, False)
            __token = 2140
            __content_140705374776208_2138 = int((_lookup_attr(getitem('ship'), 'buy_menu_width') / 2))
            __content_140705374776208_2138 = __quote(__content_140705374776208_2138, '\x00', '&#0;', None, False)
            __token = 2191
            __content_140705374776208_2189 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_2189 = __quote(__content_140705374776208_2189, '\x00', '&#0;', None, False)
            __token = 2229
            __content_140705374776208_2227 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_2227 = __quote(__content_140705374776208_2227, '\x00', '&#0;', None, False)
            __token = 2280
            __content_140705374776208_2278 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_2278 = __quote(__content_140705374776208_2278, '\x00', '&#0;', None, False)
            __token = 2308
            __content_140705374776208_2306 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_2306 = __quote(__content_140705374776208_2306, '\x00', '&#0;', None, False)
            __token = 2356
            __content_140705374776208_2354 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_2354 = __quote(__content_140705374776208_2354, '\x00', '&#0;', None, False)
            __token = 2410
            __content_140705374776208_2408 = _lookup_attr(getitem('ship'), 'id')
            __content_140705374776208_2408 = __quote(__content_140705374776208_2408, '\x00', '&#0;', None, False)
            __token = 2444
            __content_140705374776208_2442 = _lookup_attr(getitem('ship'), 'render_speed_switches')()
            __content_140705374776208_2442 = __quote(__content_140705374776208_2442, '\x00', '&#0;', None, False)
            __token = 2477
            __content_140705374776208_2475 = _lookup_attr(getitem('ship'), 'render_cargo_capacity')()
            __content_140705374776208_2475 = __quote(__content_140705374776208_2475, '\x00', '&#0;', None, False)
            __token = 2510
            __content_140705374776208_2508 = _lookup_attr(getitem('ship'), 'render_properties')()
            __content_140705374776208_2508 = __quote(__content_140705374776208_2508, '\x00', '&#0;', None, False)
            __content_140705374776208 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ((__content_140705374776208 if (__content_140705374776208 is not None) else ''), '\n\n// graphics\n\ntemplate spriteset_template_', (__content_140705374776208_70 if (__content_140705374776208_70 is not None) else ''), '(y, y_offs_adjust) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [20,        y,          28,         89,          ', (__content_140705374776208_231 if (__content_140705374776208_231 is not None) else ''), ', ', (__content_140705374776208_254 if (__content_140705374776208_254 is not None) else ''), ' + y_offs_adjust, ANIM]\n    [60,        y,          113,        66,          ', (__content_140705374776208_352 if (__content_140705374776208_352 is not None) else ''), ', ', (__content_140705374776208_375 if (__content_140705374776208_375 is not None) else ''), ' + y_offs_adjust, ANIM]\n    [186,       y,          138,        48,          ', (__content_140705374776208_473 if (__content_140705374776208_473 is not None) else ''), ', ', (__content_140705374776208_496 if (__content_140705374776208_496 is not None) else ''), ' + y_offs_adjust, ANIM]\n    [328,       y,          113,        66,          ', (__content_140705374776208_594 if (__content_140705374776208_594 is not None) else ''), ', ', (__content_140705374776208_617 if (__content_140705374776208_617 is not None) else ''), ' + y_offs_adjust, ANIM]\n    [454,       y,          28,         89,          ', (__content_140705374776208_715 if (__content_140705374776208_715 is not None) else ''), ', ', (__content_140705374776208_738 if (__content_140705374776208_738 is not None) else ''), ' + y_offs_adjust, ANIM]\n    [494,       y,          113,        66,          ', (__content_140705374776208_836 if (__content_140705374776208_836 is not None) else ''), ', ', (__content_140705374776208_859 if (__content_140705374776208_859 is not None) else ''), ' + y_offs_adjust, ANIM]\n    [620,       y,          138,        48,          ', (__content_140705374776208_957 if (__content_140705374776208_957 is not None) else ''), ', ', (__content_140705374776208_980 if (__content_140705374776208_980 is not None) else ''), ' + y_offs_adjust, ANIM]\n    [762,       y,          113,        66,          ', (__content_140705374776208_1078 if (__content_140705374776208_1078 is not None) else ''), ', ', (__content_140705374776208_1101 if (__content_140705374776208_1101 is not None) else ''), ' + y_offs_adjust, ANIM]\n}\n\nspriteset(', (__content_140705374776208_1159 if (__content_140705374776208_1159 is not None) else ''), '_ss_speed_1, "src/graphics/', (__content_140705374776208_1196 if (__content_140705374776208_1196 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_140705374776208_1238 if (__content_140705374776208_1238 is not None) else ''), '(10, 0)\n}\nspriteset(', (__content_140705374776208_1268 if (__content_140705374776208_1268 is not None) else ''), '_ss_speed_2, "src/graphics/', (__content_140705374776208_1305 if (__content_140705374776208_1305 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_140705374776208_1347 if (__content_140705374776208_1347 is not None) else ''), '(110, -1)\n}\nspriteset(', (__content_140705374776208_1379 if (__content_140705374776208_1379 is not None) else ''), '_ss_speed_3, "src/graphics/', (__content_140705374776208_1416 if (__content_140705374776208_1416 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_140705374776208_1458 if (__content_140705374776208_1458 is not None) else ''), '(210, -2)\n}\nspriteset(', (__content_140705374776208_1490 if (__content_140705374776208_1490 is not None) else ''), '_ss_speed_4, "src/graphics/', (__content_140705374776208_1527 if (__content_140705374776208_1527 is not None) else ''), '_0.png") {\n  spriteset_template_', (__content_140705374776208_1569 if (__content_140705374776208_1569 is not None) else ''), '(310, -3)\n}\n\nswitch (FEAT_SHIPS, SELF, ', (__content_140705374776208_1618 if (__content_140705374776208_1618 is not None) else ''), '_switch_graphics, current_speed) {\n    0: return ', (__content_140705374776208_1677 if (__content_140705374776208_1677 is not None) else ''), '_ss_speed_1;\n    1..', (__content_140705374776208_1707 if (__content_140705374776208_1707 is not None) else ''), ': ', (__content_140705374776208_1742 if (__content_140705374776208_1742 is not None) else ''), '_ss_speed_2;\n    ', (__content_140705374776208_1769 if (__content_140705374776208_1769 is not None) else ''), '..', (__content_140705374776208_1800 if (__content_140705374776208_1800 is not None) else ''), ': ', (__content_140705374776208_1839 if (__content_140705374776208_1839 is not None) else ''), '_ss_speed_3;\n    return ', (__content_140705374776208_1873 if (__content_140705374776208_1873 is not None) else ''), '_ss_speed_4;\n}\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_', (__content_140705374776208_1958 if (__content_140705374776208_1958 is not None) else ''), '() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [', (__content_140705374776208_2055 if (__content_140705374776208_2055 is not None) else ''), ', ', (__content_140705374776208_2082 if (__content_140705374776208_2082 is not None) else ''), ', ', (__content_140705374776208_2109 if (__content_140705374776208_2109 is not None) else ''), ', 22, -', (__content_140705374776208_2138 if (__content_140705374776208_2138 is not None) else ''), ', -10]\n}\n\nspriteset(', (__content_140705374776208_2189 if (__content_140705374776208_2189 is not None) else ''), '_ss_purchase, "src/graphics/', (__content_140705374776208_2227 if (__content_140705374776208_2227 is not None) else ''), '_0.png") {\n  spriteset_template_purchase_', (__content_140705374776208_2278 if (__content_140705374776208_2278 is not None) else ''), '()\n}\n\nspritegroup ', (__content_140705374776208_2306 if (__content_140705374776208_2306 is not None) else ''), '_sg_purchase {\n    loaded:  [\n        ', (__content_140705374776208_2354 if (__content_140705374776208_2354 is not None) else ''), '_ss_purchase,\n    ];\n    loading: [\n        ', (__content_140705374776208_2408 if (__content_140705374776208_2408 is not None) else ''), '_ss_purchase,\n    ];\n}\n\n', (__content_140705374776208_2442 if (__content_140705374776208_2442 is not None) else ''), '\n\n', (__content_140705374776208_2475 if (__content_140705374776208_2475 is not None) else ''), '\n\n', (__content_140705374776208_2508 if (__content_140705374776208_2508 is not None) else ''), '\n', ))
            if (__content_140705374776208 is None):
                pass
            else:
                if (__content_140705374776208 is False):
                    __content_140705374776208 = None
                else:
                    __tt = type(__content_140705374776208)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140705374776208 = str(__content_140705374776208)
                    else:
                        if (__tt is bytes):
                            __content_140705374776208 = decode(__content_140705374776208)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140705374776208 = __content_140705374776208.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140705374776208)
                                    __content_140705374776208 = (str(__content_140705374776208) if (__content_140705374776208 is __converted) else __converted)
                                else:
                                    __content_140705374776208 = __content_140705374776208()
            if (__content_140705374776208 is not None):
                __append(__content_140705374776208)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }