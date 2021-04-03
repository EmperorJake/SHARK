# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/fish1672/src/templates/ship.pynml'
__tokens = {87: ('${ship.render_debug_info()}\n\n// graphics', 3, 0), 89: ('ship.render_debug_info()', 3, 2), 173: ('28 if ship.use_legacy_template else 36', 6, 45), 218: ('template spriteset_template_${ship.id}(y) {\n        //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n        [20,        y,          ${width},   89,          ${ship.offsets[0][0]}, ${ship.offsets[0][1]}, ANIM]\n        [60,        y,          113,        66,          ${ship.offsets[1][0]}, ${ship.offsets[1][1]}, ANIM]\n        [186,       y,          138,        48,          ${ship.offsets[2][0]}, ${ship.offsets[2][1]}, ANIM]\n        [328,       y,          113,        66,          ${ship.offsets[3][0]}, ${ship.offsets[3][1]}, ANIM]\n        [454,       y,          ${width},   89,          ${ship.offsets[4][0]}, ${ship.offsets[4][1]}, ANIM]\n        [494,       y,          113,        66,          ${ship.offsets[5][0]}, ${ship.offsets[5][1]}, ANIM]\n        [620,       y,          138,        48,          ${ship.offsets[6][0]}, ${ship.offsets[6][1]}, ANIM]\n        [762,       y,          113,        66,          ${ship.offsets[7][0]}, ${ship.offsets[7][1]}, ANIM]\n    }', 7, 4), 248: ('ship.id', 7, 34), 377: ('width', 9, 34), 402: ('ship.offsets[0][0]', 9, 59), 425: ('ship.offsets[0][1]', 9, 82), 511: ('ship.offsets[1][0]', 10, 59), 534: ('ship.offsets[1][1]', 10, 82), 620: ('ship.offsets[2][0]', 11, 59), 643: ('ship.offsets[2][1]', 11, 82), 729: ('ship.offsets[3][0]', 12, 59), 752: ('ship.offsets[3][1]', 12, 82), 813: ('width', 13, 34), 838: ('ship.offsets[4][0]', 13, 59), 861: ('ship.offsets[4][1]', 13, 82), 947: ('ship.offsets[5][0]', 14, 59), 970: ('ship.offsets[5][1]', 14, 82), 1056: ('ship.offsets[6][0]', 15, 59), 1079: ('ship.offsets[6][1]', 15, 82), 1165: ('ship.offsets[7][0]', 16, 59), 1188: ('ship.offsets[7][1]', 16, 82), 1308: ('python:range(ship.get_num_spritesets())', 20, 53), 1354: ('spriteset(${ship.id}_ss_not_loaded_not_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(10)\n    }\n    spriteset(${ship.id}_ss_not_loaded_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(110)\n    }\n    spriteset(${ship.id}_ss_loaded_not_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(510)\n    }\n    spriteset(${ship.id}_ss_loaded_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(610)\n    }\n\n    spritegroup ${ship.id}_sg_moving_${variation_num} {\n        loaded:  [\n            ${ship.id}_ss_not_loaded_moving_${variation_num},\n            ${ship.id}_ss_loaded_moving_${variation_num},\n        ];\n        loading: [ // can\'t be loading when moving, but we\'ll overlook that, it\'s required by nml ;)\n            ${ship.id}_ss_not_loaded_moving_${variation_num},\n            ${ship.id}_ss_loaded_moving_${variation_num},\n        ];\n    }\n\n    spritegroup ${ship.id}_sg_not_moving_${variation_num} {\n        loaded:  [\n            ${ship.id}_ss_not_loaded_not_moving_${variation_num},\n            ${ship.id}_ss_loaded_not_moving_${variation_num},\n        ];\n        loading: [\n            ${ship.id}_ss_not_loaded_not_moving_${variation_num},\n            ${ship.id}_ss_loaded_not_moving_${variation_num},\n        ];\n    }\n\n    switch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_${variation_num}, current_speed) {\n        0: return ${ship.id}_sg_not_moving_${variation_num};\n        return ${ship.id}_sg_moving_${variation_num};\n    }', 21, 4), 1366: ('ship.id', 21, 16), 1402: ('variation_num', 21, 52), 1434: ('ship.id', 21, 84), 1445: ('variation_num', 21, 95), 1495: ('ship.id', 22, 27), 1530: ('ship.id', 24, 16), 1562: ('variation_num', 24, 48), 1594: ('ship.id', 24, 80), 1605: ('variation_num', 24, 91), 1655: ('ship.id', 25, 27), 1691: ('ship.id', 27, 16), 1723: ('variation_num', 27, 48), 1755: ('ship.id', 27, 80), 1766: ('variation_num', 27, 91), 1816: ('ship.id', 28, 27), 1852: ('ship.id', 30, 16), 1880: ('variation_num', 30, 44), 1912: ('ship.id', 30, 76), 1923: ('variation_num', 30, 87), 1973: ('ship.id', 31, 27), 2012: ('ship.id', 34, 18), 2033: ('variation_num', 34, 39), 2083: ('ship.id', 36, 14), 2115: ('variation_num', 36, 46), 2145: ('ship.id', 37, 14), 2173: ('variation_num', 37, 42), 2315: ('ship.id', 40, 14), 2347: ('variation_num', 40, 46), 2377: ('ship.id', 41, 14), 2405: ('variation_num', 41, 42), 2457: ('ship.id', 45, 18), 2482: ('variation_num', 45, 43), 2532: ('ship.id', 47, 14), 2568: ('variation_num', 47, 50), 2598: ('ship.id', 48, 14), 2630: ('variation_num', 48, 46), 2690: ('ship.id', 51, 14), 2726: ('variation_num', 51, 50), 2756: ('ship.id', 52, 14), 2788: ('variation_num', 52, 46), 2854: ('ship.id', 56, 32), 2881: ('variation_num', 56, 59), 2934: ('ship.id', 57, 20), 2959: ('variation_num', 57, 45), 2992: ('ship.id', 58, 17), 3013: ('variation_num', 58, 38), 3115: ('load: graphics_random_switches.pynml', 62, 46), 3170: ('graphics_random_switches', 62, 101), 3170: ('graphics_random_switches', 62, 101), 3200: ('// buy menu graphics\n\ntemplate spriteset_template_purchase_${ship.id}() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [${ship.buy_menu_bb_xy[0]}, ${ship.buy_menu_bb_xy[1]}, ${int(ship.buy_menu_width)}, 22, -${int(ship.buy_menu_width / 2)}, -10, ANIM]\n}\n\nspriteset(${ship.id}_ss_purchase, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_purchase_${ship.id}()\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_purchase,\n    ];\n    loading: [\n        ${ship.id}_ss_purchase,\n    ];\n}\n\n${ship.render_speed_switches()}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}', 64, 0), 3261: ('ship.id', 66, 39), 3358: ('ship.buy_menu_bb_xy[0]', 68, 7), 3385: ('ship.buy_menu_bb_xy[1]', 68, 34), 3412: ('int(ship.buy_menu_width)', 68, 61), 3446: ('int(ship.buy_menu_width / 2)', 68, 95), 3503: ('ship.id', 71, 12), 3541: ('ship.id', 71, 50), 3592: ('ship.id', 72, 32), 3620: ('ship.id', 75, 14), 3668: ('ship.id', 77, 10), 3722: ('ship.id', 80, 10), 3756: ('ship.render_speed_switches()', 84, 2), 3789: ('ship.render_cargo_capacity()', 86, 2), 3822: ('ship.render_properties()', 88, 2)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_139865821798240 = 'graphics_random_switches'

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

            # <Interpolation value=<Substitution '\n\n${ship.render_debug_info()}\n\n// graphics\n' (1:85)> braces_required=True translation=False at 7f350c9fd080> -> __content_139865838111856
            __token = 87
            __token = 89
            __content_139865838111856 = _lookup_attr(getitem('ship'), 'render_debug_info')()
            __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
            __content_139865838111856 = ('%s%s%s' % ('\n\n', (__content_139865838111856 if (__content_139865838111856 is not None) else ''), '\n\n// graphics\n', ))
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
            __backup_width_139865820987232 = get('width', __marker)

            # <Value '28 if ship.use_legacy_template else 36' (6:45)> -> __value
            __token = 173
            __value = (28 if _lookup_attr(getitem('ship'), 'use_legacy_template') else 36)
            econtext['width'] = __value

            # <Interpolation value=<Substitution '\n    template spriteset_template_${ship.id}(y) {\n        //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n        [20,        y,          ${width},   89,          ${ship.offsets[0][0]}, ${ship.offsets[0][1]}, ANIM]\n        [60,        y,          113,        66,          ${ship.offsets[1][0]}, ${ship.offsets[1][1]}, ANIM]\n        [186,       y,          138,        48,          ${ship.offsets[2][0]}, ${ship.offsets[2][1]}, ANIM]\n        [328,       y,          113,        66,          ${ship.offsets[3][0]}, ${ship.offsets[3][1]}, ANIM]\n        [454,       y,          ${width},   89,          ${ship.offsets[4][0]}, ${ship.offsets[4][1]}, ANIM]\n        [494,       y,          113,        66,          ${ship.offsets[5][0]}, ${ship.offsets[5][1]}, ANIM]\n        [620,       y,          138,        48,          ${ship.offsets[6][0]}, ${ship.offsets[6][1]}, ANIM]\n        [762,       y,          113,        66,          ${ship.offsets[7][0]}, ${ship.offsets[7][1]}, ANIM]\n    }\n' (6:85)> braces_required=True translation=False at 7f350c9fd400> -> __content_139865838111856
            __token = 218
            __token = 248
            __content_139865838111856 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
            __token = 377
            __content_139865838111856_375 = getitem('width')
            __content_139865838111856_375 = __quote(__content_139865838111856_375, '\x00', '&#0;', None, False)
            __token = 402
            __content_139865838111856_400 = _lookup_attr(getitem('ship'), 'offsets')[0][0]
            __content_139865838111856_400 = __quote(__content_139865838111856_400, '\x00', '&#0;', None, False)
            __token = 425
            __content_139865838111856_423 = _lookup_attr(getitem('ship'), 'offsets')[0][1]
            __content_139865838111856_423 = __quote(__content_139865838111856_423, '\x00', '&#0;', None, False)
            __token = 511
            __content_139865838111856_509 = _lookup_attr(getitem('ship'), 'offsets')[1][0]
            __content_139865838111856_509 = __quote(__content_139865838111856_509, '\x00', '&#0;', None, False)
            __token = 534
            __content_139865838111856_532 = _lookup_attr(getitem('ship'), 'offsets')[1][1]
            __content_139865838111856_532 = __quote(__content_139865838111856_532, '\x00', '&#0;', None, False)
            __token = 620
            __content_139865838111856_618 = _lookup_attr(getitem('ship'), 'offsets')[2][0]
            __content_139865838111856_618 = __quote(__content_139865838111856_618, '\x00', '&#0;', None, False)
            __token = 643
            __content_139865838111856_641 = _lookup_attr(getitem('ship'), 'offsets')[2][1]
            __content_139865838111856_641 = __quote(__content_139865838111856_641, '\x00', '&#0;', None, False)
            __token = 729
            __content_139865838111856_727 = _lookup_attr(getitem('ship'), 'offsets')[3][0]
            __content_139865838111856_727 = __quote(__content_139865838111856_727, '\x00', '&#0;', None, False)
            __token = 752
            __content_139865838111856_750 = _lookup_attr(getitem('ship'), 'offsets')[3][1]
            __content_139865838111856_750 = __quote(__content_139865838111856_750, '\x00', '&#0;', None, False)
            __token = 813
            __content_139865838111856_811 = getitem('width')
            __content_139865838111856_811 = __quote(__content_139865838111856_811, '\x00', '&#0;', None, False)
            __token = 838
            __content_139865838111856_836 = _lookup_attr(getitem('ship'), 'offsets')[4][0]
            __content_139865838111856_836 = __quote(__content_139865838111856_836, '\x00', '&#0;', None, False)
            __token = 861
            __content_139865838111856_859 = _lookup_attr(getitem('ship'), 'offsets')[4][1]
            __content_139865838111856_859 = __quote(__content_139865838111856_859, '\x00', '&#0;', None, False)
            __token = 947
            __content_139865838111856_945 = _lookup_attr(getitem('ship'), 'offsets')[5][0]
            __content_139865838111856_945 = __quote(__content_139865838111856_945, '\x00', '&#0;', None, False)
            __token = 970
            __content_139865838111856_968 = _lookup_attr(getitem('ship'), 'offsets')[5][1]
            __content_139865838111856_968 = __quote(__content_139865838111856_968, '\x00', '&#0;', None, False)
            __token = 1056
            __content_139865838111856_1054 = _lookup_attr(getitem('ship'), 'offsets')[6][0]
            __content_139865838111856_1054 = __quote(__content_139865838111856_1054, '\x00', '&#0;', None, False)
            __token = 1079
            __content_139865838111856_1077 = _lookup_attr(getitem('ship'), 'offsets')[6][1]
            __content_139865838111856_1077 = __quote(__content_139865838111856_1077, '\x00', '&#0;', None, False)
            __token = 1165
            __content_139865838111856_1163 = _lookup_attr(getitem('ship'), 'offsets')[7][0]
            __content_139865838111856_1163 = __quote(__content_139865838111856_1163, '\x00', '&#0;', None, False)
            __token = 1188
            __content_139865838111856_1186 = _lookup_attr(getitem('ship'), 'offsets')[7][1]
            __content_139865838111856_1186 = __quote(__content_139865838111856_1186, '\x00', '&#0;', None, False)
            __content_139865838111856 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    template spriteset_template_', (__content_139865838111856 if (__content_139865838111856 is not None) else ''), '(y) {\n        //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n        [20,        y,          ', (__content_139865838111856_375 if (__content_139865838111856_375 is not None) else ''), ',   89,          ', (__content_139865838111856_400 if (__content_139865838111856_400 is not None) else ''), ', ', (__content_139865838111856_423 if (__content_139865838111856_423 is not None) else ''), ', ANIM]\n        [60,        y,          113,        66,          ', (__content_139865838111856_509 if (__content_139865838111856_509 is not None) else ''), ', ', (__content_139865838111856_532 if (__content_139865838111856_532 is not None) else ''), ', ANIM]\n        [186,       y,          138,        48,          ', (__content_139865838111856_618 if (__content_139865838111856_618 is not None) else ''), ', ', (__content_139865838111856_641 if (__content_139865838111856_641 is not None) else ''), ', ANIM]\n        [328,       y,          113,        66,          ', (__content_139865838111856_727 if (__content_139865838111856_727 is not None) else ''), ', ', (__content_139865838111856_750 if (__content_139865838111856_750 is not None) else ''), ', ANIM]\n        [454,       y,          ', (__content_139865838111856_811 if (__content_139865838111856_811 is not None) else ''), ',   89,          ', (__content_139865838111856_836 if (__content_139865838111856_836 is not None) else ''), ', ', (__content_139865838111856_859 if (__content_139865838111856_859 is not None) else ''), ', ANIM]\n        [494,       y,          113,        66,          ', (__content_139865838111856_945 if (__content_139865838111856_945 is not None) else ''), ', ', (__content_139865838111856_968 if (__content_139865838111856_968 is not None) else ''), ', ANIM]\n        [620,       y,          138,        48,          ', (__content_139865838111856_1054 if (__content_139865838111856_1054 is not None) else ''), ', ', (__content_139865838111856_1077 if (__content_139865838111856_1077 is not None) else ''), ', ANIM]\n        [762,       y,          113,        66,          ', (__content_139865838111856_1163 if (__content_139865838111856_1163 is not None) else ''), ', ', (__content_139865838111856_1186 if (__content_139865838111856_1186 is not None) else ''), ', ANIM]\n    }\n', ))
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
            if (__backup_width_139865820987232 is __marker):
                del econtext['width']
            else:
                econtext['width'] = __backup_width_139865820987232
            __append('\n\n')
            __backup_variation_num_139865820804152 = get('variation_num', __marker)

            # <Value 'python:range(ship.get_num_spritesets())' (20:53)> -> __iterator
            __token = 1308
            __iterator = get('range', range)(_lookup_attr(getitem('ship'), 'get_num_spritesets')())
            (__iterator, ____index_139865821795608, ) = getitem('repeat')('variation_num', __iterator)
            econtext['variation_num'] = None
            for __item in __iterator:
                econtext['variation_num'] = __item

                # <Interpolation value=<Substitution '\n    spriteset(${ship.id}_ss_not_loaded_not_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(10)\n    }\n    spriteset(${ship.id}_ss_not_loaded_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(110)\n    }\n    spriteset(${ship.id}_ss_loaded_not_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(510)\n    }\n    spriteset(${ship.id}_ss_loaded_moving_${variation_num}, "src/graphics/${ship.id}_${variation_num}.png") {\n      spriteset_template_${ship.id}(610)\n    }\n\n    spritegroup ${ship.id}_sg_moving_${variation_num} {\n        loaded:  [\n            ${ship.id}_ss_not_loaded_moving_${variation_num},\n            ${ship.id}_ss_loaded_moving_${variation_num},\n        ];\n        loading: [ // can\'t be loading when moving, but we\'ll overlook that, it\'s required by nml ;)\n            ${ship.id}_ss_not_loaded_moving_${variation_num},\n            ${ship.id}_ss_loaded_moving_${variation_num},\n        ];\n    }\n\n    spritegroup ${ship.id}_sg_not_moving_${variation_num} {\n        loaded:  [\n            ${ship.id}_ss_not_loaded_not_moving_${variation_num},\n            ${ship.id}_ss_loaded_not_moving_${variation_num},\n        ];\n        loading: [\n            ${ship.id}_ss_not_loaded_not_moving_${variation_num},\n            ${ship.id}_ss_loaded_not_moving_${variation_num},\n        ];\n    }\n\n    switch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_${variation_num}, current_speed) {\n        0: return ${ship.id}_sg_not_moving_${variation_num};\n        return ${ship.id}_sg_moving_${variation_num};\n    }\n' (20:94)> braces_required=True translation=False at 7f350c9fdef0> -> __content_139865838111856
                __token = 1354
                __token = 1366
                __content_139865838111856 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
                __token = 1402
                __content_139865838111856_1400 = getitem('variation_num')
                __content_139865838111856_1400 = __quote(__content_139865838111856_1400, '\x00', '&#0;', None, False)
                __token = 1434
                __content_139865838111856_1432 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1432 = __quote(__content_139865838111856_1432, '\x00', '&#0;', None, False)
                __token = 1445
                __content_139865838111856_1443 = getitem('variation_num')
                __content_139865838111856_1443 = __quote(__content_139865838111856_1443, '\x00', '&#0;', None, False)
                __token = 1495
                __content_139865838111856_1493 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1493 = __quote(__content_139865838111856_1493, '\x00', '&#0;', None, False)
                __token = 1530
                __content_139865838111856_1528 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1528 = __quote(__content_139865838111856_1528, '\x00', '&#0;', None, False)
                __token = 1562
                __content_139865838111856_1560 = getitem('variation_num')
                __content_139865838111856_1560 = __quote(__content_139865838111856_1560, '\x00', '&#0;', None, False)
                __token = 1594
                __content_139865838111856_1592 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1592 = __quote(__content_139865838111856_1592, '\x00', '&#0;', None, False)
                __token = 1605
                __content_139865838111856_1603 = getitem('variation_num')
                __content_139865838111856_1603 = __quote(__content_139865838111856_1603, '\x00', '&#0;', None, False)
                __token = 1655
                __content_139865838111856_1653 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1653 = __quote(__content_139865838111856_1653, '\x00', '&#0;', None, False)
                __token = 1691
                __content_139865838111856_1689 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1689 = __quote(__content_139865838111856_1689, '\x00', '&#0;', None, False)
                __token = 1723
                __content_139865838111856_1721 = getitem('variation_num')
                __content_139865838111856_1721 = __quote(__content_139865838111856_1721, '\x00', '&#0;', None, False)
                __token = 1755
                __content_139865838111856_1753 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1753 = __quote(__content_139865838111856_1753, '\x00', '&#0;', None, False)
                __token = 1766
                __content_139865838111856_1764 = getitem('variation_num')
                __content_139865838111856_1764 = __quote(__content_139865838111856_1764, '\x00', '&#0;', None, False)
                __token = 1816
                __content_139865838111856_1814 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1814 = __quote(__content_139865838111856_1814, '\x00', '&#0;', None, False)
                __token = 1852
                __content_139865838111856_1850 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1850 = __quote(__content_139865838111856_1850, '\x00', '&#0;', None, False)
                __token = 1880
                __content_139865838111856_1878 = getitem('variation_num')
                __content_139865838111856_1878 = __quote(__content_139865838111856_1878, '\x00', '&#0;', None, False)
                __token = 1912
                __content_139865838111856_1910 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1910 = __quote(__content_139865838111856_1910, '\x00', '&#0;', None, False)
                __token = 1923
                __content_139865838111856_1921 = getitem('variation_num')
                __content_139865838111856_1921 = __quote(__content_139865838111856_1921, '\x00', '&#0;', None, False)
                __token = 1973
                __content_139865838111856_1971 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_1971 = __quote(__content_139865838111856_1971, '\x00', '&#0;', None, False)
                __token = 2012
                __content_139865838111856_2010 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2010 = __quote(__content_139865838111856_2010, '\x00', '&#0;', None, False)
                __token = 2033
                __content_139865838111856_2031 = getitem('variation_num')
                __content_139865838111856_2031 = __quote(__content_139865838111856_2031, '\x00', '&#0;', None, False)
                __token = 2083
                __content_139865838111856_2081 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2081 = __quote(__content_139865838111856_2081, '\x00', '&#0;', None, False)
                __token = 2115
                __content_139865838111856_2113 = getitem('variation_num')
                __content_139865838111856_2113 = __quote(__content_139865838111856_2113, '\x00', '&#0;', None, False)
                __token = 2145
                __content_139865838111856_2143 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2143 = __quote(__content_139865838111856_2143, '\x00', '&#0;', None, False)
                __token = 2173
                __content_139865838111856_2171 = getitem('variation_num')
                __content_139865838111856_2171 = __quote(__content_139865838111856_2171, '\x00', '&#0;', None, False)
                __token = 2315
                __content_139865838111856_2313 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2313 = __quote(__content_139865838111856_2313, '\x00', '&#0;', None, False)
                __token = 2347
                __content_139865838111856_2345 = getitem('variation_num')
                __content_139865838111856_2345 = __quote(__content_139865838111856_2345, '\x00', '&#0;', None, False)
                __token = 2377
                __content_139865838111856_2375 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2375 = __quote(__content_139865838111856_2375, '\x00', '&#0;', None, False)
                __token = 2405
                __content_139865838111856_2403 = getitem('variation_num')
                __content_139865838111856_2403 = __quote(__content_139865838111856_2403, '\x00', '&#0;', None, False)
                __token = 2457
                __content_139865838111856_2455 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2455 = __quote(__content_139865838111856_2455, '\x00', '&#0;', None, False)
                __token = 2482
                __content_139865838111856_2480 = getitem('variation_num')
                __content_139865838111856_2480 = __quote(__content_139865838111856_2480, '\x00', '&#0;', None, False)
                __token = 2532
                __content_139865838111856_2530 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2530 = __quote(__content_139865838111856_2530, '\x00', '&#0;', None, False)
                __token = 2568
                __content_139865838111856_2566 = getitem('variation_num')
                __content_139865838111856_2566 = __quote(__content_139865838111856_2566, '\x00', '&#0;', None, False)
                __token = 2598
                __content_139865838111856_2596 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2596 = __quote(__content_139865838111856_2596, '\x00', '&#0;', None, False)
                __token = 2630
                __content_139865838111856_2628 = getitem('variation_num')
                __content_139865838111856_2628 = __quote(__content_139865838111856_2628, '\x00', '&#0;', None, False)
                __token = 2690
                __content_139865838111856_2688 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2688 = __quote(__content_139865838111856_2688, '\x00', '&#0;', None, False)
                __token = 2726
                __content_139865838111856_2724 = getitem('variation_num')
                __content_139865838111856_2724 = __quote(__content_139865838111856_2724, '\x00', '&#0;', None, False)
                __token = 2756
                __content_139865838111856_2754 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2754 = __quote(__content_139865838111856_2754, '\x00', '&#0;', None, False)
                __token = 2788
                __content_139865838111856_2786 = getitem('variation_num')
                __content_139865838111856_2786 = __quote(__content_139865838111856_2786, '\x00', '&#0;', None, False)
                __token = 2854
                __content_139865838111856_2852 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2852 = __quote(__content_139865838111856_2852, '\x00', '&#0;', None, False)
                __token = 2881
                __content_139865838111856_2879 = getitem('variation_num')
                __content_139865838111856_2879 = __quote(__content_139865838111856_2879, '\x00', '&#0;', None, False)
                __token = 2934
                __content_139865838111856_2932 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2932 = __quote(__content_139865838111856_2932, '\x00', '&#0;', None, False)
                __token = 2959
                __content_139865838111856_2957 = getitem('variation_num')
                __content_139865838111856_2957 = __quote(__content_139865838111856_2957, '\x00', '&#0;', None, False)
                __token = 2992
                __content_139865838111856_2990 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856_2990 = __quote(__content_139865838111856_2990, '\x00', '&#0;', None, False)
                __token = 3013
                __content_139865838111856_3011 = getitem('variation_num')
                __content_139865838111856_3011 = __quote(__content_139865838111856_3011, '\x00', '&#0;', None, False)
                __content_139865838111856 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    spriteset(', (__content_139865838111856 if (__content_139865838111856 is not None) else ''), '_ss_not_loaded_not_moving_', (__content_139865838111856_1400 if (__content_139865838111856_1400 is not None) else ''), ', "src/graphics/', (__content_139865838111856_1432 if (__content_139865838111856_1432 is not None) else ''), '_', (__content_139865838111856_1443 if (__content_139865838111856_1443 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139865838111856_1493 if (__content_139865838111856_1493 is not None) else ''), '(10)\n    }\n    spriteset(', (__content_139865838111856_1528 if (__content_139865838111856_1528 is not None) else ''), '_ss_not_loaded_moving_', (__content_139865838111856_1560 if (__content_139865838111856_1560 is not None) else ''), ', "src/graphics/', (__content_139865838111856_1592 if (__content_139865838111856_1592 is not None) else ''), '_', (__content_139865838111856_1603 if (__content_139865838111856_1603 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139865838111856_1653 if (__content_139865838111856_1653 is not None) else ''), '(110)\n    }\n    spriteset(', (__content_139865838111856_1689 if (__content_139865838111856_1689 is not None) else ''), '_ss_loaded_not_moving_', (__content_139865838111856_1721 if (__content_139865838111856_1721 is not None) else ''), ', "src/graphics/', (__content_139865838111856_1753 if (__content_139865838111856_1753 is not None) else ''), '_', (__content_139865838111856_1764 if (__content_139865838111856_1764 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139865838111856_1814 if (__content_139865838111856_1814 is not None) else ''), '(510)\n    }\n    spriteset(', (__content_139865838111856_1850 if (__content_139865838111856_1850 is not None) else ''), '_ss_loaded_moving_', (__content_139865838111856_1878 if (__content_139865838111856_1878 is not None) else ''), ', "src/graphics/', (__content_139865838111856_1910 if (__content_139865838111856_1910 is not None) else ''), '_', (__content_139865838111856_1921 if (__content_139865838111856_1921 is not None) else ''), '.png") {\n      spriteset_template_', (__content_139865838111856_1971 if (__content_139865838111856_1971 is not None) else ''), '(610)\n    }\n\n    spritegroup ', (__content_139865838111856_2010 if (__content_139865838111856_2010 is not None) else ''), '_sg_moving_', (__content_139865838111856_2031 if (__content_139865838111856_2031 is not None) else ''), ' {\n        loaded:  [\n            ', (__content_139865838111856_2081 if (__content_139865838111856_2081 is not None) else ''), '_ss_not_loaded_moving_', (__content_139865838111856_2113 if (__content_139865838111856_2113 is not None) else ''), ',\n            ', (__content_139865838111856_2143 if (__content_139865838111856_2143 is not None) else ''), '_ss_loaded_moving_', (__content_139865838111856_2171 if (__content_139865838111856_2171 is not None) else ''), ",\n        ];\n        loading: [ // can't be loading when moving, but we'll overlook that, it's required by nml ;)\n            ", (__content_139865838111856_2313 if (__content_139865838111856_2313 is not None) else ''), '_ss_not_loaded_moving_', (__content_139865838111856_2345 if (__content_139865838111856_2345 is not None) else ''), ',\n            ', (__content_139865838111856_2375 if (__content_139865838111856_2375 is not None) else ''), '_ss_loaded_moving_', (__content_139865838111856_2403 if (__content_139865838111856_2403 is not None) else ''), ',\n        ];\n    }\n\n    spritegroup ', (__content_139865838111856_2455 if (__content_139865838111856_2455 is not None) else ''), '_sg_not_moving_', (__content_139865838111856_2480 if (__content_139865838111856_2480 is not None) else ''), ' {\n        loaded:  [\n            ', (__content_139865838111856_2530 if (__content_139865838111856_2530 is not None) else ''), '_ss_not_loaded_not_moving_', (__content_139865838111856_2566 if (__content_139865838111856_2566 is not None) else ''), ',\n            ', (__content_139865838111856_2596 if (__content_139865838111856_2596 is not None) else ''), '_ss_loaded_not_moving_', (__content_139865838111856_2628 if (__content_139865838111856_2628 is not None) else ''), ',\n        ];\n        loading: [\n            ', (__content_139865838111856_2688 if (__content_139865838111856_2688 is not None) else ''), '_ss_not_loaded_not_moving_', (__content_139865838111856_2724 if (__content_139865838111856_2724 is not None) else ''), ',\n            ', (__content_139865838111856_2754 if (__content_139865838111856_2754 is not None) else ''), '_ss_loaded_not_moving_', (__content_139865838111856_2786 if (__content_139865838111856_2786 is not None) else ''), ',\n        ];\n    }\n\n    switch (FEAT_SHIPS, SELF, ', (__content_139865838111856_2852 if (__content_139865838111856_2852 is not None) else ''), '_switch_graphics_', (__content_139865838111856_2879 if (__content_139865838111856_2879 is not None) else ''), ', current_speed) {\n        0: return ', (__content_139865838111856_2932 if (__content_139865838111856_2932 is not None) else ''), '_sg_not_moving_', (__content_139865838111856_2957 if (__content_139865838111856_2957 is not None) else ''), ';\n        return ', (__content_139865838111856_2990 if (__content_139865838111856_2990 is not None) else ''), '_sg_moving_', (__content_139865838111856_3011 if (__content_139865838111856_3011 is not None) else ''), ';\n    }\n', ))
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
                ____index_139865821795608 -= 1
                if (____index_139865821795608 > 0):
                    __append('')
            if (__backup_variation_num_139865820804152 is __marker):
                del econtext['variation_num']
            else:
                econtext['variation_num'] = __backup_variation_num_139865820804152
            __append('\n\n')
            __backup_graphics_random_switches_139865820061936 = get('graphics_random_switches', __marker)

            # <Value 'load: graphics_random_switches.pynml' (62:46)> -> __value
            __token = 3115
            __value = ' graphics_random_switches.pynml'
            __value = __loader(__value)
            econtext['graphics_random_switches'] = __value
            __backup_macroname_139865821977224 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f350c9fdf60> name=None at 7f350c9fd198> -> __value
            __value = _static_139865821798240
            econtext['macroname'] = __value

            # <Value 'graphics_random_switches' (62:101)> -> __macro
            __token = 3170
            __macro = getitem('graphics_random_switches')
            __token = 3170
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139865821977224 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139865821977224
            if (__backup_graphics_random_switches_139865820061936 is __marker):
                del econtext['graphics_random_switches']
            else:
                econtext['graphics_random_switches'] = __backup_graphics_random_switches_139865820061936

            # <Interpolation value=<Substitution '\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_${ship.id}() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [${ship.buy_menu_bb_xy[0]}, ${ship.buy_menu_bb_xy[1]}, ${int(ship.buy_menu_width)}, 22, -${int(ship.buy_menu_width / 2)}, -10, ANIM]\n}\n\nspriteset(${ship.id}_ss_purchase, "src/graphics/${ship.id}_0.png") {\n  spriteset_template_purchase_${ship.id}()\n}\n\nspritegroup ${ship.id}_sg_purchase {\n    loaded:  [\n        ${ship.id}_ss_purchase,\n    ];\n    loading: [\n        ${ship.id}_ss_purchase,\n    ];\n}\n\n${ship.render_speed_switches()}\n\n${ship.render_cargo_capacity()}\n\n${ship.render_properties()}\n' (62:129)> braces_required=True translation=False at 7f350c911ba8> -> __content_139865838111856
            __token = 3200
            __token = 3261
            __content_139865838111856 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
            __token = 3358
            __content_139865838111856_3356 = _lookup_attr(getitem('ship'), 'buy_menu_bb_xy')[0]
            __content_139865838111856_3356 = __quote(__content_139865838111856_3356, '\x00', '&#0;', None, False)
            __token = 3385
            __content_139865838111856_3383 = _lookup_attr(getitem('ship'), 'buy_menu_bb_xy')[1]
            __content_139865838111856_3383 = __quote(__content_139865838111856_3383, '\x00', '&#0;', None, False)
            __token = 3412
            __content_139865838111856_3410 = int(_lookup_attr(getitem('ship'), 'buy_menu_width'))
            __content_139865838111856_3410 = __quote(__content_139865838111856_3410, '\x00', '&#0;', None, False)
            __token = 3446
            __content_139865838111856_3444 = int((_lookup_attr(getitem('ship'), 'buy_menu_width') / 2))
            __content_139865838111856_3444 = __quote(__content_139865838111856_3444, '\x00', '&#0;', None, False)
            __token = 3503
            __content_139865838111856_3501 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_3501 = __quote(__content_139865838111856_3501, '\x00', '&#0;', None, False)
            __token = 3541
            __content_139865838111856_3539 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_3539 = __quote(__content_139865838111856_3539, '\x00', '&#0;', None, False)
            __token = 3592
            __content_139865838111856_3590 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_3590 = __quote(__content_139865838111856_3590, '\x00', '&#0;', None, False)
            __token = 3620
            __content_139865838111856_3618 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_3618 = __quote(__content_139865838111856_3618, '\x00', '&#0;', None, False)
            __token = 3668
            __content_139865838111856_3666 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_3666 = __quote(__content_139865838111856_3666, '\x00', '&#0;', None, False)
            __token = 3722
            __content_139865838111856_3720 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_3720 = __quote(__content_139865838111856_3720, '\x00', '&#0;', None, False)
            __token = 3756
            __content_139865838111856_3754 = _lookup_attr(getitem('ship'), 'render_speed_switches')()
            __content_139865838111856_3754 = __quote(__content_139865838111856_3754, '\x00', '&#0;', None, False)
            __token = 3789
            __content_139865838111856_3787 = _lookup_attr(getitem('ship'), 'render_cargo_capacity')()
            __content_139865838111856_3787 = __quote(__content_139865838111856_3787, '\x00', '&#0;', None, False)
            __token = 3822
            __content_139865838111856_3820 = _lookup_attr(getitem('ship'), 'render_properties')()
            __content_139865838111856_3820 = __quote(__content_139865838111856_3820, '\x00', '&#0;', None, False)
            __content_139865838111856 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n\n// buy menu graphics\n\ntemplate spriteset_template_purchase_', (__content_139865838111856 if (__content_139865838111856 is not None) else ''), '() {\n    //[left_x,  upper_y,    width,      height,     offset_x,      offset_y]\n    [', (__content_139865838111856_3356 if (__content_139865838111856_3356 is not None) else ''), ', ', (__content_139865838111856_3383 if (__content_139865838111856_3383 is not None) else ''), ', ', (__content_139865838111856_3410 if (__content_139865838111856_3410 is not None) else ''), ', 22, -', (__content_139865838111856_3444 if (__content_139865838111856_3444 is not None) else ''), ', -10, ANIM]\n}\n\nspriteset(', (__content_139865838111856_3501 if (__content_139865838111856_3501 is not None) else ''), '_ss_purchase, "src/graphics/', (__content_139865838111856_3539 if (__content_139865838111856_3539 is not None) else ''), '_0.png") {\n  spriteset_template_purchase_', (__content_139865838111856_3590 if (__content_139865838111856_3590 is not None) else ''), '()\n}\n\nspritegroup ', (__content_139865838111856_3618 if (__content_139865838111856_3618 is not None) else ''), '_sg_purchase {\n    loaded:  [\n        ', (__content_139865838111856_3666 if (__content_139865838111856_3666 is not None) else ''), '_ss_purchase,\n    ];\n    loading: [\n        ', (__content_139865838111856_3720 if (__content_139865838111856_3720 is not None) else ''), '_ss_purchase,\n    ];\n}\n\n', (__content_139865838111856_3754 if (__content_139865838111856_3754 is not None) else ''), '\n\n', (__content_139865838111856_3787 if (__content_139865838111856_3787 is not None) else ''), '\n\n', (__content_139865838111856_3820 if (__content_139865838111856_3820 is not None) else ''), '\n', ))
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