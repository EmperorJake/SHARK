# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/templates/capacity_refittable.pynml'
__tokens = {202: ('switch (FEAT_SHIPS, SELF, ${ship.id}_switch_cargo_capacity, cargo_subtype) {\n    0: return ${ship.capacities_refittable[0]};\n    1: return ${ship.capacities_refittable[1]};\n    2: return ${ship.capacities_refittable[2]};\n    return ${ship.capacities_refittable[0]};\n}\n\n// -- handle subtype strings, used to aid players understand auto-refitting -- //\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_cargo_subtype_text, cargo_subtype) {\n    0: return string(STR_GENERIC_REFIT_SUBTYPE, ${ship.capacities_refittable[0]}, ${ship.get_cargo_suffix()});\n    1: return string(STR_GENERIC_REFIT_SUBTYPE, ${ship.capacities_refittable[1]}, ${ship.get_cargo_suffix()});\n    2: return string(STR_GENERIC_REFIT_SUBTYPE, ${ship.capacities_refittable[2]}, ${ship.get_cargo_suffix()});\n    return CB_RESULT_NO_TEXT;\n}', 3, 0), 230: ('ship.id', 3, 28), 295: ('ship.capacities_refittable[0]', 4, 16), 343: ('ship.capacities_refittable[1]', 5, 16), 391: ('ship.capacities_refittable[2]', 6, 16), 436: ('ship.capacities_refittable[0]', 7, 13), 581: ('ship.id', 11, 28), 684: ('ship.capacities_refittable[0]', 12, 50), 718: ('ship.get_cargo_suffix()', 12, 84), 795: ('ship.capacities_refittable[1]', 13, 50), 829: ('ship.get_cargo_suffix()', 13, 84), 906: ('ship.capacities_refittable[2]', 14, 50), 940: ('ship.get_cargo_suffix()', 14, 84)}

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
            __append('// -- ships that have subtype refits for capacity rely on the capacities_refittable prop //\n')

            # <Interpolation value=<Substitution '\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_cargo_capacity, cargo_subtype) {\n    0: return ${ship.capacities_refittable[0]};\n    1: return ${ship.capacities_refittable[1]};\n    2: return ${ship.capacities_refittable[2]};\n    return ${ship.capacities_refittable[0]};\n}\n\n// -- handle subtype strings, used to aid players understand auto-refitting -- //\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_cargo_subtype_text, cargo_subtype) {\n    0: return string(STR_GENERIC_REFIT_SUBTYPE, ${ship.capacities_refittable[0]}, ${ship.get_cargo_suffix()});\n    1: return string(STR_GENERIC_REFIT_SUBTYPE, ${ship.capacities_refittable[1]}, ${ship.get_cargo_suffix()});\n    2: return string(STR_GENERIC_REFIT_SUBTYPE, ${ship.capacities_refittable[2]}, ${ship.get_cargo_suffix()});\n    return CB_RESULT_NO_TEXT;\n}\n' (2:109)> braces_required=True translation=False at 7efdb052e9e8> -> __content_139628066513336
            __token = 202
            __token = 230
            __content_139628066513336 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336 = __quote(__content_139628066513336, '\x00', '&#0;', None, False)
            __token = 295
            __content_139628066513336_293 = _lookup_attr(getitem('ship'), 'capacities_refittable')[0]
            __content_139628066513336_293 = __quote(__content_139628066513336_293, '\x00', '&#0;', None, False)
            __token = 343
            __content_139628066513336_341 = _lookup_attr(getitem('ship'), 'capacities_refittable')[1]
            __content_139628066513336_341 = __quote(__content_139628066513336_341, '\x00', '&#0;', None, False)
            __token = 391
            __content_139628066513336_389 = _lookup_attr(getitem('ship'), 'capacities_refittable')[2]
            __content_139628066513336_389 = __quote(__content_139628066513336_389, '\x00', '&#0;', None, False)
            __token = 436
            __content_139628066513336_434 = _lookup_attr(getitem('ship'), 'capacities_refittable')[0]
            __content_139628066513336_434 = __quote(__content_139628066513336_434, '\x00', '&#0;', None, False)
            __token = 581
            __content_139628066513336_579 = _lookup_attr(getitem('ship'), 'id')
            __content_139628066513336_579 = __quote(__content_139628066513336_579, '\x00', '&#0;', None, False)
            __token = 684
            __content_139628066513336_682 = _lookup_attr(getitem('ship'), 'capacities_refittable')[0]
            __content_139628066513336_682 = __quote(__content_139628066513336_682, '\x00', '&#0;', None, False)
            __token = 718
            __content_139628066513336_716 = _lookup_attr(getitem('ship'), 'get_cargo_suffix')()
            __content_139628066513336_716 = __quote(__content_139628066513336_716, '\x00', '&#0;', None, False)
            __token = 795
            __content_139628066513336_793 = _lookup_attr(getitem('ship'), 'capacities_refittable')[1]
            __content_139628066513336_793 = __quote(__content_139628066513336_793, '\x00', '&#0;', None, False)
            __token = 829
            __content_139628066513336_827 = _lookup_attr(getitem('ship'), 'get_cargo_suffix')()
            __content_139628066513336_827 = __quote(__content_139628066513336_827, '\x00', '&#0;', None, False)
            __token = 906
            __content_139628066513336_904 = _lookup_attr(getitem('ship'), 'capacities_refittable')[2]
            __content_139628066513336_904 = __quote(__content_139628066513336_904, '\x00', '&#0;', None, False)
            __token = 940
            __content_139628066513336_938 = _lookup_attr(getitem('ship'), 'get_cargo_suffix')()
            __content_139628066513336_938 = __quote(__content_139628066513336_938, '\x00', '&#0;', None, False)
            __content_139628066513336 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\nswitch (FEAT_SHIPS, SELF, ', (__content_139628066513336 if (__content_139628066513336 is not None) else ''), '_switch_cargo_capacity, cargo_subtype) {\n    0: return ', (__content_139628066513336_293 if (__content_139628066513336_293 is not None) else ''), ';\n    1: return ', (__content_139628066513336_341 if (__content_139628066513336_341 is not None) else ''), ';\n    2: return ', (__content_139628066513336_389 if (__content_139628066513336_389 is not None) else ''), ';\n    return ', (__content_139628066513336_434 if (__content_139628066513336_434 is not None) else ''), ';\n}\n\n// -- handle subtype strings, used to aid players understand auto-refitting -- //\nswitch (FEAT_SHIPS, SELF, ', (__content_139628066513336_579 if (__content_139628066513336_579 is not None) else ''), '_switch_cargo_subtype_text, cargo_subtype) {\n    0: return string(STR_GENERIC_REFIT_SUBTYPE, ', (__content_139628066513336_682 if (__content_139628066513336_682 is not None) else ''), ', ', (__content_139628066513336_716 if (__content_139628066513336_716 is not None) else ''), ');\n    1: return string(STR_GENERIC_REFIT_SUBTYPE, ', (__content_139628066513336_793 if (__content_139628066513336_793 is not None) else ''), ', ', (__content_139628066513336_827 if (__content_139628066513336_827 is not None) else ''), ');\n    2: return string(STR_GENERIC_REFIT_SUBTYPE, ', (__content_139628066513336_904 if (__content_139628066513336_904 is not None) else ''), ', ', (__content_139628066513336_938 if (__content_139628066513336_938 is not None) else ''), ');\n    return CB_RESULT_NO_TEXT;\n}\n', ))
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