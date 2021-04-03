# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/fish1672/src/templates/general_cargo_vessel.pynml'
__tokens = {0: ('${ship.render_debug_info()}\n\n// graphics\ntemplate spriteset_template_${ship.id}(y) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [20,        y,          28,         89,          ${ship.offsets[0][0]}, ${ship.offsets[0][1]}, ANIM]\n    [60,        y,          113,        71,          ${ship.offsets[1][0]}, ${ship.offsets[1][1]}, ANIM]\n    [186,       y,          138,        48,          ${ship.offsets[2][0]}, ${ship.offsets[2][1]}, ANIM]\n    [328,       y,          113,        71,          ${ship.offsets[3][0]}, ${ship.offsets[3][1]}, ANIM]\n    [454,       y,          28,         89,          ${ship.offsets[4][0]}, ${ship.offsets[4][1]}, ANIM]\n    [494,       y,          113,        71,          ${ship.offsets[5][0]}, ${ship.offsets[5][1]}, ANIM]\n    [620,       y,          138,        48,          ${ship.offsets[6][0]}, ${ship.offsets[6][1]}, ANIM]\n    [762,       y,          113,        71,          ${ship.offsets[7][0]}, ${ship.offsets[7][1]}, ANIM]\n}', 1, 0), 2: ('ship.render_debug_info()', 1, 2), 71: ('ship.id', 4, 30), 217: ('ship.offsets[0][0]', 6, 55), 240: ('ship.offsets[0][1]', 6, 78), 322: ('ship.offsets[1][0]', 7, 55), 345: ('ship.offsets[1][1]', 7, 78), 427: ('ship.offsets[2][0]', 8, 55), 450: ('ship.offsets[2][1]', 8, 78), 532: ('ship.offsets[3][0]', 9, 55), 555: ('ship.offsets[3][1]', 9, 78), 637: ('ship.offsets[4][0]', 10, 55), 660: ('ship.offsets[4][1]', 10, 78), 742: ('ship.offsets[5][0]', 11, 55), 765: ('ship.offsets[5][1]', 11, 78), 847: ('ship.offsets[6][0]', 12, 55), 870: ('ship.offsets[6][1]', 12, 78), 952: ('ship.offsets[7][0]', 13, 55), 975: ('ship.offsets[7][1]', 13, 78), 1058: ('python:range(ship.get_num_spritesets())', 16, 53), 1104: ('spriteset(${ship.id}_ss_not_loaded_not_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(10)\n    }\n    spriteset(${ship.id}_ss_not_loaded_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(110)\n    }\n    spriteset(${ship.id}_ss_loading_0_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(210)\n    }\n    spriteset(${ship.id}_ss_loading_1_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(310)\n    }\n    spriteset(${ship.id}_ss_loading_2_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(410)\n    }\n    spriteset(${ship.id}_ss_loading_3_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(510)\n    }\n    spriteset(${ship.id}_ss_loaded_not_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(610)\n    }\n    spriteset(${ship.id}_ss_loaded_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(710)\n    }\n\n    spritegroup ${ship.id}_sg_moving_${variation_num} {\n        loaded:  [\n            ${ship.id}_ss_not_loaded_moving_${variation_num},\n            ${ship.id}_ss_loaded_moving_${variation_num},\n        ];\n        loading: [ // can\'t be loading when moving, but we\'ll overlook that, it\'s required by nml ;)\n            ${ship.id}_ss_loaded_moving_${variation_num},\n        ];\n    }\n\n    spritegroup ${ship.id}_sg_not_moving_${variation_num} {\n        loaded:  [\n            ${ship.id}_ss_not_loaded_not_moving_${variation_num},\n            ${ship.id}_ss_loaded_not_moving_${variation_num},\n        ];\n        loading: [\n            ${ship.id}_ss_loading_0_${variation_num},\n            ${ship.id}_ss_loading_1_${variation_num},\n            ${ship.id}_ss_loading_2_${variation_num},\n            ${ship.id}_ss_loading_3_${variation_num},\n        ];\n    }\n\n    switch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_${variation_num}, current_speed) {\n        0: return ${ship.id}_sg_not_moving_${variation_num};\n        return ${ship.id}_sg_moving_${variation_num};\n    }', 17, 4), 1116: ('ship.id', 17, 16), 1152: ('variation_num', 17, 52), 1184: ('ship.id', 17, 84), 1195: ('variation_num', 17, 95), 1245: ('ship.id', 18, 27), 1280: ('ship.id', 20, 16), 1312: ('variation_num', 20, 48), 1344: ('ship.id', 20, 80), 1355: ('variation_num', 20, 91), 1405: ('ship.id', 21, 27), 1441: ('ship.id', 23, 16), 1465: ('variation_num', 23, 40), 1497: ('ship.id', 23, 72), 1508: ('variation_num', 23, 83), 1558: ('ship.id', 24, 27), 1594: ('ship.id', 26, 16), 1618: ('variation_num', 26, 40), 1650: ('ship.id', 26, 72), 1661: ('variation_num', 26, 83), 1711: ('ship.id', 27, 27), 1747: ('ship.id', 29, 16), 1771: ('variation_num', 29, 40), 1803: ('ship.id', 29, 72), 1814: ('variation_num', 29, 83), 1864: ('ship.id', 30, 27), 1900: ('ship.id', 32, 16), 1924: ('variation_num', 32, 40), 1956: ('ship.id', 32, 72), 1967: ('variation_num', 32, 83), 2017: ('ship.id', 33, 27), 2053: ('ship.id', 35, 16), 2085: ('variation_num', 35, 48), 2117: ('ship.id', 35, 80), 2128: ('variation_num', 35, 91), 2178: ('ship.id', 36, 27), 2214: ('ship.id', 38, 16), 2242: ('variation_num', 38, 44), 2274: ('ship.id', 38, 76), 2285: ('variation_num', 38, 87), 2335: ('ship.id', 39, 27), 2374: ('ship.id', 42, 18), 2395: ('variation_num', 42, 39), 2445: ('ship.id', 44, 14), 2477: ('variation_num', 44, 46), 2507: ('ship.id', 45, 14), 2535: ('variation_num', 45, 42), 2677: ('ship.id', 48, 14), 2705: ('variation_num', 48, 42), 2757: ('ship.id', 52, 18), 2782: ('variation_num', 52, 43), 2832: ('ship.id', 54, 14), 2868: ('variation_num', 54, 50), 2898: ('ship.id', 55, 14), 2930: ('variation_num', 55, 46), 2990: ('ship.id', 58, 14), 3014: ('variation_num', 58, 38), 3044: ('ship.id', 59, 14), 3068: ('variation_num', 59, 38), 3098: ('ship.id', 60, 14), 3122: ('variation_num', 60, 38), 3152: ('ship.id', 61, 14), 3176: ('variation_num', 61, 38), 3242: ('ship.id', 65, 32), 3269: ('variation_num', 65, 59), 3322: ('ship.id', 66, 20), 3347: ('variation_num', 66, 45), 3380: ('ship.id', 67, 17), 3401: ('variation_num', 67, 38), 3503: ('load: graphics_random_switches.pynml', 71, 46), 3558: ('graphics_random_switches', 71, 101), 3558: ('graphics_random_switches', 71, 101), 3588: ('// buy menu graphics\n\ntemplate spriteset_template_purchase_${ship.id}() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [${ship.buy_menu_bb_xy[0]}, ${ship.buy_menu_bb_xy[1]}, ${ship.buy_menu_width}, 22, -${int(ship.buy_menu_width / 2)}, -10, ANIM]\n}\n\nspriteset(${ship.id}_ss_purchase, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_purchase_${ship.id}()\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_purchase,\n    ];\n    loading: [\n        ${ship.id}_ss_purchase,\n    ];\n}\n\n\n${ship.render_speed_switches()}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}', 73, 0), 3649: ('ship.id', 75, 39), 3746: ('ship.buy_menu_bb_xy[0]', 77, 7), 3773: ('ship.buy_menu_bb_xy[1]', 77, 34), 3800: ('ship.buy_menu_width', 77, 61), 3829: ('int(ship.buy_menu_width / 2)', 77, 90), 3886: ('ship.id', 80, 12), 3924: ('ship.id', 80, 50), 3975: ('ship.id', 81, 32), 4003: ('ship.id', 84, 14), 4051: ('ship.id', 86, 10), 4105: ('ship.id', 89, 10), 4140: ('ship.render_speed_switches()', 94, 2), 4173: ('ship.render_cargo_capacity()', 96, 2), 4206: ('ship.render_properties()', 98, 2)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_139865822277360 = 'graphics_random_switches'

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

            # <Interpolation value=<Substitution '${ship.render_debug_info()}\n\n// graphics\ntemplate spriteset_template_${ship.id}(y) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [20,        y,          28,         89,          ${ship.offsets[0][0]}, ${ship.offsets[0][1]}, ANIM]\n    [60,        y,          113,        71,          ${ship.offsets[1][0]}, ${ship.offsets[1][1]}, ANIM]\n    [186,       y,          138,        48,          ${ship.offsets[2][0]}, ${ship.offsets[2][1]}, ANIM]\n    [328,       y,          113,        71,          ${ship.offsets[3][0]}, ${ship.offsets[3][1]}, ANIM]\n    [454,       y,          28,         89,          ${ship.offsets[4][0]}, ${ship.offsets[4][1]}, ANIM]\n    [494,       y,          113,        71,          ${ship.offsets[5][0]}, ${ship.offsets[5][1]}, ANIM]\n    [620,       y,          138,        48,          ${ship.offsets[6][0]}, ${ship.offsets[6][1]}, ANIM]\n    [762,       y,          113,        71,          ${ship.offsets[7][0]}, ${ship.offsets[7][1]}, ANIM]\n}\n\n' (1:0)> braces_required=True translation=False at 7f350ca72940> -> __content_139865838111856
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
            __content_139865838111856 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ((__content_139865838111856 if (__content_139865838111856 is not None) else ''), '\n\n// graphics\ntemplate spriteset_template_', (__content_139865838111856_69 if (__content_139865838111856_69 is not None) else ''), '(y) {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [20,        y,          28,         89,          ', (__content_139865838111856_215 if (__content_139865838111856_215 is not None) else ''), ', ', (__content_139865838111856_238 if (__content_139865838111856_238 is not None) else ''), ', ANIM]\n    [60,        y,          113,        71,          ', (__content_139865838111856_320 if (__content_139865838111856_320 is not None) else ''), ', ', (__content_139865838111856_343 if (__content_139865838111856_343 is not None) else ''), ', ANIM]\n    [186,       y,          138,        48,          ', (__content_139865838111856_425 if (__content_139865838111856_425 is not None) else ''), ', ', (__content_139865838111856_448 if (__content_139865838111856_448 is not None) else ''), ', ANIM]\n    [328,       y,          113,        71,          ', (__content_139865838111856_530 if (__content_139865838111856_530 is not None) else ''), ', ', (__content_139865838111856_553 if (__content_139865838111856_553 is not None) else ''), ', ANIM]\n    [454,       y,          28,         89,          ', (__content_139865838111856_635 if (__content_139865838111856_635 is not None) else ''), ', ', (__content_139865838111856_658 if (__content_139865838111856_658 is not None) else ''), ', ANIM]\n    [494,       y,          113,        71,          ', (__content_139865838111856_740 if (__content_139865838111856_740 is not None) else ''), ', ', (__content_139865838111856_763 if (__content_139865838111856_763 is not None) else ''), ', ANIM]\n    [620,       y,          138,        48,          ', (__content_139865838111856_845 if (__content_139865838111856_845 is not None) else ''), ', ', (__content_139865838111856_868 if (__content_139865838111856_868 is not None) else ''), ', ANIM]\n    [762,       y,          113,        71,          ', (__content_139865838111856_950 if (__content_139865838111856_950 is not None) else ''), ', ', (__content_139865838111856_973 if (__content_139865838111856_973 is not None) else ''), ', ANIM]\n}\n\n', ))
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
            __backup_variation_num_139865822273776 = get('variation_num', __marker)

            # <Value 'python:range(ship.get_num_spritesets())' (16:53)> -> __iterator
            __token = 1058
            __iterator = get('range', range)(_lookup_attr(getitem('ship'), 'get_num_spritesets')())
            (__iterator, ____index_139865822275960, ) = getitem('repeat')('variation_num', __iterator)
            econtext['variation_num'] = None
            for __item in __iterator:
                econtext['variation_num'] = __item

                # <Interpolation value=<Substitution '\n    spriteset(${ship.id}_ss_not_loaded_not_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(10)\n    }\n    spriteset(${ship.id}_ss_not_loaded_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(110)\n    }\n    spriteset(${ship.id}_ss_loading_0_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(210)\n    }\n    spriteset(${ship.id}_ss_loading_1_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(310)\n    }\n    spriteset(${ship.id}_ss_loading_2_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(410)\n    }\n    spriteset(${ship.id}_ss_loading_3_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(510)\n    }\n    spriteset(${ship.id}_ss_loaded_not_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(610)\n    }\n    spriteset(${ship.id}_ss_loaded_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(710)\n    }\n\n    spritegroup ${ship.id}_sg_moving_${variation_num} {\n        loaded:  [\n            ${ship.id}_ss_not_loaded_moving_${variation_num},\n            ${ship.id}_ss_loaded_moving_${variation_num},\n        ];\n        loading: [ // can\'t be loading when moving, but we\'ll overlook that, it\'s required by nml ;)\n            ${ship.id}_ss_loaded_moving_${variation_num},\n        ];\n    }\n\n    spritegroup ${ship.id}_sg_not_moving_${variation_num} {\n        loaded:  [\n            ${ship.id}_ss_not_loaded_not_moving_${variation_num},\n            ${ship.id}_ss_loaded_not_moving_${variation_num},\n        ];\n        loading: [\n            ${ship.id}_ss_loading_0_${variation_num},\n            ${ship.id}_ss_loading_1_${variation_num},\n            ${ship.id}_ss_loading_2_${variation_num},\n            ${ship.id}_ss_loading_3_${variation_num},\n        ];\n    }\n\n    switch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_${variation_num}, current_speed) {\n        0: return ${ship.id}_sg_not_moving_${variation_num};\n        return ${ship.id}_sg_moving_${variation_num};\n    }\n' (16:94)> braces_required=True translation=False at 7f350ca72ba8> -> __content_139865838111856
                __token = 1104
                __token = 1116
                __content_139865838111856 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
                __token = 1152
                __content_139865838111856_1150 = getitem('variation_num')
                __content_139865838111856_1150 = __quote(__content_139865838111856_1150, '\x00', '&#0;', None, False)
                __token = 1184
                __content_139865838111856_1182 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1182 = __quote(__content_139865838111856_1182, '\x00', '&#0;', None, False)
                __token = 1195
                __content_139865838111856_1193 = getitem('variation_num')
                __content_139865838111856_1193 = __quote(__content_139865838111856_1193, '\x00', '&#0;', None, False)
                __token = 1245
                __content_139865838111856_1243 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1243 = __quote(__content_139865838111856_1243, '\x00', '&#0;', None, False)
                __token = 1280
                __content_139865838111856_1278 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1278 = __quote(__content_139865838111856_1278, '\x00', '&#0;', None, False)
                __token = 1312
                __content_139865838111856_1310 = getitem('variation_num')
                __content_139865838111856_1310 = __quote(__content_139865838111856_1310, '\x00', '&#0;', None, False)
                __token = 1344
                __content_139865838111856_1342 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1342 = __quote(__content_139865838111856_1342, '\x00', '&#0;', None, False)
                __token = 1355
                __content_139865838111856_1353 = getitem('variation_num')
                __content_139865838111856_1353 = __quote(__content_139865838111856_1353, '\x00', '&#0;', None, False)
                __token = 1405
                __content_139865838111856_1403 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1403 = __quote(__content_139865838111856_1403, '\x00', '&#0;', None, False)
                __token = 1441
                __content_139865838111856_1439 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1439 = __quote(__content_139865838111856_1439, '\x00', '&#0;', None, False)
                __token = 1465
                __content_139865838111856_1463 = getitem('variation_num')
                __content_139865838111856_1463 = __quote(__content_139865838111856_1463, '\x00', '&#0;', None, False)
                __token = 1497
                __content_139865838111856_1495 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1495 = __quote(__content_139865838111856_1495, '\x00', '&#0;', None, False)
                __token = 1508
                __content_139865838111856_1506 = getitem('variation_num')
                __content_139865838111856_1506 = __quote(__content_139865838111856_1506, '\x00', '&#0;', None, False)
                __token = 1558
                __content_139865838111856_1556 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1556 = __quote(__content_139865838111856_1556, '\x00', '&#0;', None, False)
                __token = 1594
                __content_139865838111856_1592 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1592 = __quote(__content_139865838111856_1592, '\x00', '&#0;', None, False)
                __token = 1618
                __content_139865838111856_1616 = getitem('variation_num')
                __content_139865838111856_1616 = __quote(__content_139865838111856_1616, '\x00', '&#0;', None, False)
                __token = 1650
                __content_139865838111856_1648 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1648 = __quote(__content_139865838111856_1648, '\x00', '&#0;', None, False)
                __token = 1661
                __content_139865838111856_1659 = getitem('variation_num')
                __content_139865838111856_1659 = __quote(__content_139865838111856_1659, '\x00', '&#0;', None, False)
                __token = 1711
                __content_139865838111856_1709 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1709 = __quote(__content_139865838111856_1709, '\x00', '&#0;', None, False)
                __token = 1747
                __content_139865838111856_1745 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1745 = __quote(__content_139865838111856_1745, '\x00', '&#0;', None, False)
                __token = 1771
                __content_139865838111856_1769 = getitem('variation_num')
                __content_139865838111856_1769 = __quote(__content_139865838111856_1769, '\x00', '&#0;', None, False)
                __token = 1803
                __content_139865838111856_1801 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1801 = __quote(__content_139865838111856_1801, '\x00', '&#0;', None, False)
                __token = 1814
                __content_139865838111856_1812 = getitem('variation_num')
                __content_139865838111856_1812 = __quote(__content_139865838111856_1812, '\x00', '&#0;', None, False)
                __token = 1864
                __content_139865838111856_1862 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1862 = __quote(__content_139865838111856_1862, '\x00', '&#0;', None, False)
                __token = 1900
                __content_139865838111856_1898 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1898 = __quote(__content_139865838111856_1898, '\x00', '&#0;', None, False)
                __token = 1924
                __content_139865838111856_1922 = getitem('variation_num')
                __content_139865838111856_1922 = __quote(__content_139865838111856_1922, '\x00', '&#0;', None, False)
                __token = 1956
                __content_139865838111856_1954 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1954 = __quote(__content_139865838111856_1954, '\x00', '&#0;', None, False)
                __token = 1967
                __content_139865838111856_1965 = getitem('variation_num')
                __content_139865838111856_1965 = __quote(__content_139865838111856_1965, '\x00', '&#0;', None, False)
                __token = 2017
                __content_139865838111856_2015 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2015 = __quote(__content_139865838111856_2015, '\x00', '&#0;', None, False)
                __token = 2053
                __content_139865838111856_2051 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2051 = __quote(__content_139865838111856_2051, '\x00', '&#0;', None, False)
                __token = 2085
                __content_139865838111856_2083 = getitem('variation_num')
                __content_139865838111856_2083 = __quote(__content_139865838111856_2083, '\x00', '&#0;', None, False)
                __token = 2117
                __content_139865838111856_2115 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2115 = __quote(__content_139865838111856_2115, '\x00', '&#0;', None, False)
                __token = 2128
                __content_139865838111856_2126 = getitem('variation_num')
                __content_139865838111856_2126 = __quote(__content_139865838111856_2126, '\x00', '&#0;', None, False)
                __token = 2178
                __content_139865838111856_2176 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2176 = __quote(__content_139865838111856_2176, '\x00', '&#0;', None, False)
                __token = 2214
                __content_139865838111856_2212 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2212 = __quote(__content_139865838111856_2212, '\x00', '&#0;', None, False)
                __token = 2242
                __content_139865838111856_2240 = getitem('variation_num')
                __content_139865838111856_2240 = __quote(__content_139865838111856_2240, '\x00', '&#0;', None, False)
                __token = 2274
                __content_139865838111856_2272 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2272 = __quote(__content_139865838111856_2272, '\x00', '&#0;', None, False)
                __token = 2285
                __content_139865838111856_2283 = getitem('variation_num')
                __content_139865838111856_2283 = __quote(__content_139865838111856_2283, '\x00', '&#0;', None, False)
                __token = 2335
                __content_139865838111856_2333 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2333 = __quote(__content_139865838111856_2333, '\x00', '&#0;', None, False)
                __token = 2374
                __content_139865838111856_2372 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2372 = __quote(__content_139865838111856_2372, '\x00', '&#0;', None, False)
                __token = 2395
                __content_139865838111856_2393 = getitem('variation_num')
                __content_139865838111856_2393 = __quote(__content_139865838111856_2393, '\x00', '&#0;', None, False)
                __token = 2445
                __content_139865838111856_2443 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2443 = __quote(__content_139865838111856_2443, '\x00', '&#0;', None, False)
                __token = 2477
                __content_139865838111856_2475 = getitem('variation_num')
                __content_139865838111856_2475 = __quote(__content_139865838111856_2475, '\x00', '&#0;', None, False)
                __token = 2507
                __content_139865838111856_2505 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2505 = __quote(__content_139865838111856_2505, '\x00', '&#0;', None, False)
                __token = 2535
                __content_139865838111856_2533 = getitem('variation_num')
                __content_139865838111856_2533 = __quote(__content_139865838111856_2533, '\x00', '&#0;', None, False)
                __token = 2677
                __content_139865838111856_2675 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2675 = __quote(__content_139865838111856_2675, '\x00', '&#0;', None, False)
                __token = 2705
                __content_139865838111856_2703 = getitem('variation_num')
                __content_139865838111856_2703 = __quote(__content_139865838111856_2703, '\x00', '&#0;', None, False)
                __token = 2757
                __content_139865838111856_2755 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2755 = __quote(__content_139865838111856_2755, '\x00', '&#0;', None, False)
                __token = 2782
                __content_139865838111856_2780 = getitem('variation_num')
                __content_139865838111856_2780 = __quote(__content_139865838111856_2780, '\x00', '&#0;', None, False)
                __token = 2832
                __content_139865838111856_2830 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2830 = __quote(__content_139865838111856_2830, '\x00', '&#0;', None, False)
                __token = 2868
                __content_139865838111856_2866 = getitem('variation_num')
                __content_139865838111856_2866 = __quote(__content_139865838111856_2866, '\x00', '&#0;', None, False)
                __token = 2898
                __content_139865838111856_2896 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2896 = __quote(__content_139865838111856_2896, '\x00', '&#0;', None, False)
                __token = 2930
                __content_139865838111856_2928 = getitem('variation_num')
                __content_139865838111856_2928 = __quote(__content_139865838111856_2928, '\x00', '&#0;', None, False)
                __token = 2990
                __content_139865838111856_2988 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2988 = __quote(__content_139865838111856_2988, '\x00', '&#0;', None, False)
                __token = 3014
                __content_139865838111856_3012 = getitem('variation_num')
                __content_139865838111856_3012 = __quote(__content_139865838111856_3012, '\x00', '&#0;', None, False)
                __token = 3044
                __content_139865838111856_3042 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_3042 = __quote(__content_139865838111856_3042, '\x00', '&#0;', None, False)
                __token = 3068
                __content_139865838111856_3066 = getitem('variation_num')
                __content_139865838111856_3066 = __quote(__content_139865838111856_3066, '\x00', '&#0;', None, False)
                __token = 3098
                __content_139865838111856_3096 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_3096 = __quote(__content_139865838111856_3096, '\x00', '&#0;', None, False)
                __token = 3122
                __content_139865838111856_3120 = getitem('variation_num')
                __content_139865838111856_3120 = __quote(__content_139865838111856_3120, '\x00', '&#0;', None, False)
                __token = 3152
                __content_139865838111856_3150 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_3150 = __quote(__content_139865838111856_3150, '\x00', '&#0;', None, False)
                __token = 3176
                __content_139865838111856_3174 = getitem('variation_num')
                __content_139865838111856_3174 = __quote(__content_139865838111856_3174, '\x00', '&#0;', None, False)
                __token = 3242
                __content_139865838111856_3240 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_3240 = __quote(__content_139865838111856_3240, '\x00', '&#0;', None, False)
                __token = 3269
                __content_139865838111856_3267 = getitem('variation_num')
                __content_139865838111856_3267 = __quote(__content_139865838111856_3267, '\x00', '&#0;', None, False)
                __token = 3322
                __content_139865838111856_3320 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_3320 = __quote(__content_139865838111856_3320, '\x00', '&#0;', None, False)
                __token = 3347
                __content_139865838111856_3345 = getitem('variation_num')
                __content_139865838111856_3345 = __quote(__content_139865838111856_3345, '\x00', '&#0;', None, False)
                __token = 3380
                __content_139865838111856_3378 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_3378 = __quote(__content_139865838111856_3378, '\x00', '&#0;', None, False)
                __token = 3401
                __content_139865838111856_3399 = getitem('variation_num')
                __content_139865838111856_3399 = __quote(__content_139865838111856_3399, '\x00', '&#0;', None, False)
                __content_139865838111856 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    spriteset(', (__content_139865838111856 if (__content_139865838111856 is not None) else ''), '_ss_not_loaded_not_moving_', (__content_139865838111856_1150 if (__content_139865838111856_1150 is not None) else ''), ', "src/graphics/', (__content_139865838111856_1182 if (__content_139865838111856_1182 is not None) else ''), '_', (__content_139865838111856_1193 if (__content_139865838111856_1193 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139865838111856_1243 if (__content_139865838111856_1243 is not None) else ''), '(10)\n    }\n    spriteset(', (__content_139865838111856_1278 if (__content_139865838111856_1278 is not None) else ''), '_ss_not_loaded_moving_', (__content_139865838111856_1310 if (__content_139865838111856_1310 is not None) else ''), ', "src/graphics/', (__content_139865838111856_1342 if (__content_139865838111856_1342 is not None) else ''), '_', (__content_139865838111856_1353 if (__content_139865838111856_1353 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139865838111856_1403 if (__content_139865838111856_1403 is not None) else ''), '(110)\n    }\n    spriteset(', (__content_139865838111856_1439 if (__content_139865838111856_1439 is not None) else ''), '_ss_loading_0_', (__content_139865838111856_1463 if (__content_139865838111856_1463 is not None) else ''), ', "src/graphics/', (__content_139865838111856_1495 if (__content_139865838111856_1495 is not None) else ''), '_', (__content_139865838111856_1506 if (__content_139865838111856_1506 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139865838111856_1556 if (__content_139865838111856_1556 is not None) else ''), '(210)\n    }\n    spriteset(', (__content_139865838111856_1592 if (__content_139865838111856_1592 is not None) else ''), '_ss_loading_1_', (__content_139865838111856_1616 if (__content_139865838111856_1616 is not None) else ''), ', "src/graphics/', (__content_139865838111856_1648 if (__content_139865838111856_1648 is not None) else ''), '_', (__content_139865838111856_1659 if (__content_139865838111856_1659 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139865838111856_1709 if (__content_139865838111856_1709 is not None) else ''), '(310)\n    }\n    spriteset(', (__content_139865838111856_1745 if (__content_139865838111856_1745 is not None) else ''), '_ss_loading_2_', (__content_139865838111856_1769 if (__content_139865838111856_1769 is not None) else ''), ', "src/graphics/', (__content_139865838111856_1801 if (__content_139865838111856_1801 is not None) else ''), '_', (__content_139865838111856_1812 if (__content_139865838111856_1812 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139865838111856_1862 if (__content_139865838111856_1862 is not None) else ''), '(410)\n    }\n    spriteset(', (__content_139865838111856_1898 if (__content_139865838111856_1898 is not None) else ''), '_ss_loading_3_', (__content_139865838111856_1922 if (__content_139865838111856_1922 is not None) else ''), ', "src/graphics/', (__content_139865838111856_1954 if (__content_139865838111856_1954 is not None) else ''), '_', (__content_139865838111856_1965 if (__content_139865838111856_1965 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139865838111856_2015 if (__content_139865838111856_2015 is not None) else ''), '(510)\n    }\n    spriteset(', (__content_139865838111856_2051 if (__content_139865838111856_2051 is not None) else ''), '_ss_loaded_not_moving_', (__content_139865838111856_2083 if (__content_139865838111856_2083 is not None) else ''), ', "src/graphics/', (__content_139865838111856_2115 if (__content_139865838111856_2115 is not None) else ''), '_', (__content_139865838111856_2126 if (__content_139865838111856_2126 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139865838111856_2176 if (__content_139865838111856_2176 is not None) else ''), '(610)\n    }\n    spriteset(', (__content_139865838111856_2212 if (__content_139865838111856_2212 is not None) else ''), '_ss_loaded_moving_', (__content_139865838111856_2240 if (__content_139865838111856_2240 is not None) else ''), ', "src/graphics/', (__content_139865838111856_2272 if (__content_139865838111856_2272 is not None) else ''), '_', (__content_139865838111856_2283 if (__content_139865838111856_2283 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139865838111856_2333 if (__content_139865838111856_2333 is not None) else ''), '(710)\n    }\n\n    spritegroup ', (__content_139865838111856_2372 if (__content_139865838111856_2372 is not None) else ''), '_sg_moving_', (__content_139865838111856_2393 if (__content_139865838111856_2393 is not None) else ''), ' {\n        loaded:  [\n            ', (__content_139865838111856_2443 if (__content_139865838111856_2443 is not None) else ''), '_ss_not_loaded_moving_', (__content_139865838111856_2475 if (__content_139865838111856_2475 is not None) else ''), ',\n            ', (__content_139865838111856_2505 if (__content_139865838111856_2505 is not None) else ''), '_ss_loaded_moving_', (__content_139865838111856_2533 if (__content_139865838111856_2533 is not None) else ''), ",\n        ];\n        loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n            ", (__content_139865838111856_2675 if (__content_139865838111856_2675 is not None) else ''), '_ss_loaded_moving_', (__content_139865838111856_2703 if (__content_139865838111856_2703 is not None) else ''), ',\n        ];\n    }\n\n    spritegroup ', (__content_139865838111856_2755 if (__content_139865838111856_2755 is not None) else ''), '_sg_not_moving_', (__content_139865838111856_2780 if (__content_139865838111856_2780 is not None) else ''), ' {\n        loaded:  [\n            ', (__content_139865838111856_2830 if (__content_139865838111856_2830 is not None) else ''), '_ss_not_loaded_not_moving_', (__content_139865838111856_2866 if (__content_139865838111856_2866 is not None) else ''), ',\n            ', (__content_139865838111856_2896 if (__content_139865838111856_2896 is not None) else ''), '_ss_loaded_not_moving_', (__content_139865838111856_2928 if (__content_139865838111856_2928 is not None) else ''), ',\n        ];\n        loading: [\n            ', (__content_139865838111856_2988 if (__content_139865838111856_2988 is not None) else ''), '_ss_loading_0_', (__content_139865838111856_3012 if (__content_139865838111856_3012 is not None) else ''), ',\n            ', (__content_139865838111856_3042 if (__content_139865838111856_3042 is not None) else ''), '_ss_loading_1_', (__content_139865838111856_3066 if (__content_139865838111856_3066 is not None) else ''), ',\n            ', (__content_139865838111856_3096 if (__content_139865838111856_3096 is not None) else ''), '_ss_loading_2_', (__content_139865838111856_3120 if (__content_139865838111856_3120 is not None) else ''), ',\n            ', (__content_139865838111856_3150 if (__content_139865838111856_3150 is not None) else ''), '_ss_loading_3_', (__content_139865838111856_3174 if (__content_139865838111856_3174 is not None) else ''), ',\n        ];\n    }\n\n    switch (FEAT_SHIPS, SELF, ', (__content_139865838111856_3240 if (__content_139865838111856_3240 is not None) else ''), '_switch_graphics_', (__content_139865838111856_3267 if (__content_139865838111856_3267 is not None) else ''), ', current_speed) {\n        0: return ', (__content_139865838111856_3320 if (__content_139865838111856_3320 is not None) else ''), '_sg_not_moving_', (__content_139865838111856_3345 if (__content_139865838111856_3345 is not None) else ''), ';\n        return ', (__content_139865838111856_3378 if (__content_139865838111856_3378 is not None) else ''), '_sg_moving_', (__content_139865838111856_3399 if (__content_139865838111856_3399 is not None) else ''), ';\n    }\n', ))
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
                ____index_139865822275960 -= 1
                if (____index_139865822275960 > 0):
                    __append('')
            if (__backup_variation_num_139865822273776 is __marker):
                del econtext['variation_num']
            else:
                econtext['variation_num'] = __backup_variation_num_139865822273776
            __append('\n\n')
            __backup_graphics_random_switches_139865847201184 = get('graphics_random_switches', __marker)

            # <Value 'load: graphics_random_switches.pynml' (71:46)> -> __value
            __token = 3503
            __value = ' graphics_random_switches.pynml'
            __value = __loader(__value)
            econtext['graphics_random_switches'] = __value
            __backup_macroname_139865821531592 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f350ca72ef0> name=None at 7f350ca72b00> -> __value
            __value = _static_139865822277360
            econtext['macroname'] = __value

            # <Value 'graphics_random_switches' (71:101)> -> __macro
            __token = 3558
            __macro = getitem('graphics_random_switches')
            __token = 3558
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139865821531592 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139865821531592
            if (__backup_graphics_random_switches_139865847201184 is __marker):
                del econtext['graphics_random_switches']
            else:
                econtext['graphics_random_switches'] = __backup_graphics_random_switches_139865847201184

            # <Interpolation value=<Substitution '\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_${ship.id}() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [${ship.buy_menu_bb_xy[0]}, ${ship.buy_menu_bb_xy[1]}, ${ship.buy_menu_width}, 22, -${int(ship.buy_menu_width / 2)}, -10, ANIM]\n}\n\nspriteset(${ship.id}_ss_purchase, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_purchase_${ship.id}()\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_purchase,\n    ];\n    loading: [\n        ${ship.id}_ss_purchase,\n    ];\n}\n\n\n${ship.render_speed_switches()}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}\n' (71:129)> braces_required=True translation=False at 7f350ca72c50> -> __content_139865838111856
            __token = 3588
            __token = 3649
            __content_139865838111856 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
            __token = 3746
            __content_139865838111856_3744 = _lookup_attr(getitem('ship'), 'buy_menu_bb_xy')[0]
            __content_139865838111856_3744 = __quote(__content_139865838111856_3744, '\x00', '&#0;', None, False)
            __token = 3773
            __content_139865838111856_3771 = _lookup_attr(getitem('ship'), 'buy_menu_bb_xy')[1]
            __content_139865838111856_3771 = __quote(__content_139865838111856_3771, '\x00', '&#0;', None, False)
            __token = 3800
            __content_139865838111856_3798 = _lookup_attr(getitem('ship'), 'buy_menu_width')
            __content_139865838111856_3798 = __quote(__content_139865838111856_3798, '\x00', '&#0;', None, False)
            __token = 3829
            __content_139865838111856_3827 = int((_lookup_attr(getitem('ship'), 'buy_menu_width') / 2))
            __content_139865838111856_3827 = __quote(__content_139865838111856_3827, '\x00', '&#0;', None, False)
            __token = 3886
            __content_139865838111856_3884 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_3884 = __quote(__content_139865838111856_3884, '\x00', '&#0;', None, False)
            __token = 3924
            __content_139865838111856_3922 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_3922 = __quote(__content_139865838111856_3922, '\x00', '&#0;', None, False)
            __token = 3975
            __content_139865838111856_3973 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_3973 = __quote(__content_139865838111856_3973, '\x00', '&#0;', None, False)
            __token = 4003
            __content_139865838111856_4001 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_4001 = __quote(__content_139865838111856_4001, '\x00', '&#0;', None, False)
            __token = 4051
            __content_139865838111856_4049 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_4049 = __quote(__content_139865838111856_4049, '\x00', '&#0;', None, False)
            __token = 4105
            __content_139865838111856_4103 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_4103 = __quote(__content_139865838111856_4103, '\x00', '&#0;', None, False)
            __token = 4140
            __content_139865838111856_4138 = _lookup_attr(getitem('ship'), 'render_speed_switches')()
            __content_139865838111856_4138 = __quote(__content_139865838111856_4138, '\x00', '&#0;', None, False)
            __token = 4173
            __content_139865838111856_4171 = _lookup_attr(getitem('ship'), 'render_cargo_capacity')()
            __content_139865838111856_4171 = __quote(__content_139865838111856_4171, '\x00', '&#0;', None, False)
            __token = 4206
            __content_139865838111856_4204 = _lookup_attr(getitem('ship'), 'render_properties')()
            __content_139865838111856_4204 = __quote(__content_139865838111856_4204, '\x00', '&#0;', None, False)
            __content_139865838111856 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_', (__content_139865838111856 if (__content_139865838111856 is not None) else ''), '() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [', (__content_139865838111856_3744 if (__content_139865838111856_3744 is not None) else ''), ', ', (__content_139865838111856_3771 if (__content_139865838111856_3771 is not None) else ''), ', ', (__content_139865838111856_3798 if (__content_139865838111856_3798 is not None) else ''), ', 22, -', (__content_139865838111856_3827 if (__content_139865838111856_3827 is not None) else ''), ', -10, ANIM]\n}\n\nspriteset(', (__content_139865838111856_3884 if (__content_139865838111856_3884 is not None) else ''), '_ss_purchase, "src/graphics/', (__content_139865838111856_3922 if (__content_139865838111856_3922 is not None) else ''), '_0.png") {\n  spriteset_template_purchase_', (__content_139865838111856_3973 if (__content_139865838111856_3973 is not None) else ''), '()\n}\n\nspritegroup ', (__content_139865838111856_4001 if (__content_139865838111856_4001 is not None) else ''), '_sg_purchase {\n    loaded:  [\n        ', (__content_139865838111856_4049 if (__content_139865838111856_4049 is not None) else ''), '_ss_purchase,\n    ];\n    loading: [\n        ', (__content_139865838111856_4103 if (__content_139865838111856_4103 is not None) else ''), '_ss_purchase,\n    ];\n}\n\n\n', (__content_139865838111856_4138 if (__content_139865838111856_4138 is not None) else ''), '\n\n', (__content_139865838111856_4171 if (__content_139865838111856_4171 is not None) else ''), '\n\n', (__content_139865838111856_4204 if (__content_139865838111856_4204 is not None) else ''), '\n', ))
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