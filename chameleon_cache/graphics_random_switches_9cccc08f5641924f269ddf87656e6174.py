# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/templates/graphics_random_switches.pynml'
__tokens = {53: ('ship.get_reduced_set_of_variant_dates()[:-1]', 1, 53), 104: ('random_switch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_random_${year}) {', 2, 4), 139: ('ship.id', 2, 39), 173: ('year', 2, 73), 244: ('ship.get_variants_available_for_specific_year(year)', 3, 62), 310: ('1: return ${ship.id}_switch_graphics_${variation_num};', 4, 12), 322: ('ship.id', 4, 24), 349: ('variation_num', 4, 51), 457: ('switch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, build_year) {', 10, 0), 485: ('ship.id', 10, 28), 584: ('ship.get_nml_random_switch_fragments_for_model_variants()', 11, 59), 652: ('${nml_fragment};', 12, 8), 654: ('nml_fragment', 12, 10), 713: ('return ${ship.id}_switch_graphics_random_0;\n}', 14, 4), 722: ('ship.id', 14, 13)}

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
            __backup_year_139818164956800 = get('year', __marker)

            # <Value 'ship.get_reduced_set_of_variant_dates()[:-1]' (1:53)> -> __iterator
            __token = 53
            __iterator = _lookup_attr(getitem('ship'), 'get_reduced_set_of_variant_dates')()[:- 1]
            (__iterator, ____index_139818165775832, ) = getitem('repeat')('year', __iterator)
            econtext['year'] = None
            for __item in __iterator:
                econtext['year'] = __item

                # <Interpolation value=<Substitution '\n    random_switch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics_random_${year}) {\n        ' (1:99)> braces_required=True translation=False at 7f29f59a99e8> -> __content_139818181960344
                __token = 104
                __token = 139
                __content_139818181960344 = _lookup_attr(getitem('ship'), 'id')
                __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                __token = 173
                __content_139818181960344_171 = getitem('year')
                __content_139818181960344_171 = __quote(__content_139818181960344_171, '\x00', '&#0;', None, False)
                __content_139818181960344 = ('%s%s%s%s%s' % ('\n    random_switch (FEAT_SHIPS, SELF, ', (__content_139818181960344 if (__content_139818181960344 is not None) else ''), '_switch_graphics_random_', (__content_139818181960344_171 if (__content_139818181960344_171 is not None) else ''), ') {\n        ', ))
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
                __backup_variation_num_139818165763768 = get('variation_num', __marker)

                # <Value 'ship.get_variants_available_for_specific_year(year)' (3:62)> -> __iterator
                __token = 244
                __iterator = _lookup_attr(getitem('ship'), 'get_variants_available_for_specific_year')(getitem('year'))
                (__iterator, ____index_139818165734760, ) = getitem('repeat')('variation_num', __iterator)
                econtext['variation_num'] = None
                for __item in __iterator:
                    econtext['variation_num'] = __item

                    # <Interpolation value=<Substitution '\n            1: return ${ship.id}_switch_graphics_${variation_num};\n        ' (3:115)> braces_required=True translation=False at 7f29f41a0c18> -> __content_139818181960344
                    __token = 310
                    __token = 322
                    __content_139818181960344 = _lookup_attr(getitem('ship'), 'id')
                    __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                    __token = 349
                    __content_139818181960344_347 = getitem('variation_num')
                    __content_139818181960344_347 = __quote(__content_139818181960344_347, '\x00', '&#0;', None, False)
                    __content_139818181960344 = ('%s%s%s%s%s' % ('\n            1: return ', (__content_139818181960344 if (__content_139818181960344 is not None) else ''), '_switch_graphics_', (__content_139818181960344_347 if (__content_139818181960344_347 is not None) else ''), ';\n        ', ))
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
                    ____index_139818165734760 -= 1
                    if (____index_139818165734760 > 0):
                        __append('')
                if (__backup_variation_num_139818165763768 is __marker):
                    del econtext['variation_num']
                else:
                    econtext['variation_num'] = __backup_variation_num_139818165763768
                __append('\n    }\n')
                ____index_139818165775832 -= 1
                if (____index_139818165775832 > 0):
                    __append('')
            if (__backup_year_139818164956800 is __marker):
                del econtext['year']
            else:
                econtext['year'] = __backup_year_139818164956800

            # <Interpolation value=<Substitution '\n\n\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_graphics, build_year) {\n    ' (7:41)> braces_required=True translation=False at 7f29f41aad68> -> __content_139818181960344
            __token = 457
            __token = 485
            __content_139818181960344 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
            __content_139818181960344 = ('%s%s%s' % ('\n\n\nswitch (FEAT_SHIPS, SELF, ', (__content_139818181960344 if (__content_139818181960344 is not None) else ''), '_switch_graphics, build_year) {\n    ', ))
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
            __backup_nml_fragment_139818164978632 = get('nml_fragment', __marker)

            # <Value 'ship.get_nml_random_switch_fragments_for_model_variants()' (11:59)> -> __iterator
            __token = 584
            __iterator = _lookup_attr(getitem('ship'), 'get_nml_random_switch_fragments_for_model_variants')()
            (__iterator, ____index_139818165734256, ) = getitem('repeat')('nml_fragment', __iterator)
            econtext['nml_fragment'] = None
            for __item in __iterator:
                econtext['nml_fragment'] = __item

                # <Interpolation value=<Substitution '\n        ${nml_fragment};\n    ' (11:118)> braces_required=True translation=False at 7f29f41a04e0> -> __content_139818181960344
                __token = 652
                __token = 654
                __content_139818181960344 = getitem('nml_fragment')
                __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                __content_139818181960344 = ('%s%s%s' % ('\n        ', (__content_139818181960344 if (__content_139818181960344 is not None) else ''), ';\n    ', ))
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
                ____index_139818165734256 -= 1
                if (____index_139818165734256 > 0):
                    __append('')
            if (__backup_nml_fragment_139818164978632 is __marker):
                del econtext['nml_fragment']
            else:
                econtext['nml_fragment'] = __backup_nml_fragment_139818164978632

            # <Interpolation value=<Substitution '\n    return ${ship.id}_switch_graphics_random_0;\n}\n' (13:39)> braces_required=True translation=False at 7f29f41a09b0> -> __content_139818181960344
            __token = 713
            __token = 722
            __content_139818181960344 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
            __content_139818181960344 = ('%s%s%s' % ('\n    return ', (__content_139818181960344 if (__content_139818181960344 is not None) else ''), '_switch_graphics_random_0;\n}\n', ))
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