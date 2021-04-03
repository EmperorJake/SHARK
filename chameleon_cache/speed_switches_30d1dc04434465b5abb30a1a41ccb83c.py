# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/fish1672/src/templates/speed_switches.pynml'
__tokens = {161: ('python:range(3)', 3, 32), 183: ('switch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount_${speed_factor}, cargo_count*100/cargo_capacity) {\n        0 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[0]};\n        1..25 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[1]};\n        26..50 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[2]};\n        51..75 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[3]};\n        76..100 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[4]};\n        return 0; // should never reach this result, make it show up as a problem\n    }', 4, 4), 211: ('ship.id', 4, 32), 259: ('speed_factor', 4, 80), 322: ('ship.get_speeds_adjusted_for_load_amount(speed_factor)[0]', 5, 14), 400: ('ship.get_speeds_adjusted_for_load_amount(speed_factor)[1]', 6, 18), 479: ('ship.get_speeds_adjusted_for_load_amount(speed_factor)[2]', 7, 19), 558: ('ship.get_speeds_adjusted_for_load_amount(speed_factor)[3]', 8, 19), 638: ('ship.get_speeds_adjusted_for_load_amount(speed_factor)[4]', 9, 20), 799: ('switch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount, param_adjust_ship_speed) {\n    0: ${ship.id}_switch_speed_varies_with_load_amount_0;\n    1: ${ship.id}_switch_speed_varies_with_load_amount_1;\n    2: ${ship.id}_switch_speed_varies_with_load_amount_2;\n}\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_purchase_speed, param_adjust_ship_speed) {\n    0: ${ship.get_speeds_adjusted_for_load_amount(0)[4]};\n    1: ${ship.get_speeds_adjusted_for_load_amount(1)[4]};\n    2: ${ship.get_speeds_adjusted_for_load_amount(2)[4]};\n}', 13, 0), 827: ('ship.id', 13, 28), 910: ('ship.id', 14, 9), 968: ('ship.id', 15, 9), 1026: ('ship.id', 16, 9), 1105: ('ship.id', 18, 28), 1173: ('ship.get_speeds_adjusted_for_load_amount(0)[4]', 19, 9), 1231: ('ship.get_speeds_adjusted_for_load_amount(1)[4]', 20, 9), 1289: ('ship.get_speeds_adjusted_for_load_amount(2)[4]', 21, 9)}

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
            __append('// -- set speed a little higher than rated speed when unladen -- //\n// -- also apply the param_adjust_ship_speed parameter -- //\n')
            __backup_speed_factor_139865821082960 = get('speed_factor', __marker)

            # <Value 'python:range(3)' (3:32)> -> __iterator
            __token = 161
            __iterator = get('range', range)(3)
            (__iterator, ____index_139865821942392, ) = getitem('repeat')('speed_factor', __iterator)
            econtext['speed_factor'] = None
            for __item in __iterator:
                econtext['speed_factor'] = __item

                # <Interpolation value=<Substitution '\n    switch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount_${speed_factor}, cargo_count*100/cargo_capacity) {\n        0 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[0]};\n        1..25 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[1]};\n        26..50 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[2]};\n        51..75 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[3]};\n        76..100 : ${ship.get_speeds_adjusted_for_load_amount(speed_factor)[4]};\n        return 0; // should never reach this result, make it show up as a problem\n    }\n' (3:49)> braces_required=True translation=False at 7f350ca210f0> -> __content_139865838111856
                __token = 183
                __token = 211
                __content_139865838111856 = _lookup_attr(getitem('ship'), 'id')
                __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
                __token = 259
                __content_139865838111856_257 = getitem('speed_factor')
                __content_139865838111856_257 = __quote(__content_139865838111856_257, '\x00', '&#0;', None, False)
                __token = 322
                __content_139865838111856_320 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(getitem('speed_factor'))[0]
                __content_139865838111856_320 = __quote(__content_139865838111856_320, '\x00', '&#0;', None, False)
                __token = 400
                __content_139865838111856_398 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(getitem('speed_factor'))[1]
                __content_139865838111856_398 = __quote(__content_139865838111856_398, '\x00', '&#0;', None, False)
                __token = 479
                __content_139865838111856_477 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(getitem('speed_factor'))[2]
                __content_139865838111856_477 = __quote(__content_139865838111856_477, '\x00', '&#0;', None, False)
                __token = 558
                __content_139865838111856_556 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(getitem('speed_factor'))[3]
                __content_139865838111856_556 = __quote(__content_139865838111856_556, '\x00', '&#0;', None, False)
                __token = 638
                __content_139865838111856_636 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(getitem('speed_factor'))[4]
                __content_139865838111856_636 = __quote(__content_139865838111856_636, '\x00', '&#0;', None, False)
                __content_139865838111856 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    switch (FEAT_SHIPS, SELF, ', (__content_139865838111856 if (__content_139865838111856 is not None) else ''), '_switch_speed_varies_with_load_amount_', (__content_139865838111856_257 if (__content_139865838111856_257 is not None) else ''), ', cargo_count*100/cargo_capacity) {\n        0 : ', (__content_139865838111856_320 if (__content_139865838111856_320 is not None) else ''), ';\n        1..25 : ', (__content_139865838111856_398 if (__content_139865838111856_398 is not None) else ''), ';\n        26..50 : ', (__content_139865838111856_477 if (__content_139865838111856_477 is not None) else ''), ';\n        51..75 : ', (__content_139865838111856_556 if (__content_139865838111856_556 is not None) else ''), ';\n        76..100 : ', (__content_139865838111856_636 if (__content_139865838111856_636 is not None) else ''), ';\n        return 0; // should never reach this result, make it show up as a problem\n    }\n', ))
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
                ____index_139865821942392 -= 1
                if (____index_139865821942392 > 0):
                    __append('')
            if (__backup_speed_factor_139865821082960 is __marker):
                del econtext['speed_factor']
            else:
                econtext['speed_factor'] = __backup_speed_factor_139865821082960

            # <Interpolation value=<Substitution '\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_speed_varies_with_load_amount, param_adjust_ship_speed) {\n    0: ${ship.id}_switch_speed_varies_with_load_amount_0;\n    1: ${ship.id}_switch_speed_varies_with_load_amount_1;\n    2: ${ship.id}_switch_speed_varies_with_load_amount_2;\n}\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_purchase_speed, param_adjust_ship_speed) {\n    0: ${ship.get_speeds_adjusted_for_load_amount(0)[4]};\n    1: ${ship.get_speeds_adjusted_for_load_amount(1)[4]};\n    2: ${ship.get_speeds_adjusted_for_load_amount(2)[4]};\n}\n' (12:12)> braces_required=True translation=False at 7f350ca214e0> -> __content_139865838111856
            __token = 799
            __token = 827
            __content_139865838111856 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
            __token = 910
            __content_139865838111856_908 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_908 = __quote(__content_139865838111856_908, '\x00', '&#0;', None, False)
            __token = 968
            __content_139865838111856_966 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_966 = __quote(__content_139865838111856_966, '\x00', '&#0;', None, False)
            __token = 1026
            __content_139865838111856_1024 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1024 = __quote(__content_139865838111856_1024, '\x00', '&#0;', None, False)
            __token = 1105
            __content_139865838111856_1103 = _lookup_attr(getitem('ship'), 'id')
            __content_139865838111856_1103 = __quote(__content_139865838111856_1103, '\x00', '&#0;', None, False)
            __token = 1173
            __content_139865838111856_1171 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(0)[4]
            __content_139865838111856_1171 = __quote(__content_139865838111856_1171, '\x00', '&#0;', None, False)
            __token = 1231
            __content_139865838111856_1229 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(1)[4]
            __content_139865838111856_1229 = __quote(__content_139865838111856_1229, '\x00', '&#0;', None, False)
            __token = 1289
            __content_139865838111856_1287 = _lookup_attr(getitem('ship'), 'get_speeds_adjusted_for_load_amount')(2)[4]
            __content_139865838111856_1287 = __quote(__content_139865838111856_1287, '\x00', '&#0;', None, False)
            __content_139865838111856 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\nswitch (FEAT_SHIPS, SELF, ', (__content_139865838111856 if (__content_139865838111856 is not None) else ''), '_switch_speed_varies_with_load_amount, param_adjust_ship_speed) {\n    0: ', (__content_139865838111856_908 if (__content_139865838111856_908 is not None) else ''), '_switch_speed_varies_with_load_amount_0;\n    1: ', (__content_139865838111856_966 if (__content_139865838111856_966 is not None) else ''), '_switch_speed_varies_with_load_amount_1;\n    2: ', (__content_139865838111856_1024 if (__content_139865838111856_1024 is not None) else ''), '_switch_speed_varies_with_load_amount_2;\n}\nswitch (FEAT_SHIPS, SELF, ', (__content_139865838111856_1103 if (__content_139865838111856_1103 is not None) else ''), '_switch_purchase_speed, param_adjust_ship_speed) {\n    0: ', (__content_139865838111856_1171 if (__content_139865838111856_1171 is not None) else ''), ';\n    1: ', (__content_139865838111856_1229 if (__content_139865838111856_1229 is not None) else ''), ';\n    2: ', (__content_139865838111856_1287 if (__content_139865838111856_1287 is not None) else ''), ';\n}\n', ))
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