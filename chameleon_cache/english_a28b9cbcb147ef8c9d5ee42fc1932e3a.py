# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/SHARK/src/lang_templates/english.pylng'

__tokens = {0: ('STR_GRF_NAME                                                    :${repo_vars.repo_title}', 1, 0), 67: ('repo_vars.repo_title', 1, 67), 149: ('ships', 4, 38), 157: ('STR_NAME_${ship.id}                                          :${ship.get_name_substr()}{STRING}', 5, 0), 168: ('ship.id', 5, 11), 221: ('ship.get_name_substr()', 5, 64)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_140188664645808 = {}

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

            # <Interpolation value=<Substitution 'STR_GRF_NAME                                                    :${repo_vars.repo_title}\n\n' (1:0)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f803779fa30> -> __content_140188669528304
            __token = 0
            __token = 67
            __content_140188669528304 = _lookup_attr(getitem('repo_vars'), 'repo_title')
            __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
            __content_140188669528304 = ('%s%s%s' % ('STR_GRF_NAME                                                    :', (__content_140188669528304 if (__content_140188669528304 is not None) else ''), '\n\n', ))
            if (__content_140188669528304 is None):
                pass
            else:
                if (__content_140188669528304 is None):
                    __content_140188669528304 = None
                else:
                    __tt = type(__content_140188669528304)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140188669528304 = str(__content_140188669528304)
                    else:
                        if (__tt is bytes):
                            __content_140188669528304 = decode(__content_140188669528304)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140188669528304 = __content_140188669528304.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140188669528304)
                                    __content_140188669528304 = (str(__content_140188669528304) if (__content_140188669528304 is __converted) else __converted)
                                else:
                                    __content_140188669528304 = __content_140188669528304()
            if (__content_140188669528304 is not None):
                __append(__content_140188669528304)
            __append('\n')

            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663282704
            __attrs_140188663282704 = _static_140188664645808
            __backup_ship_140188663215968 = get('ship', __marker)

            # <Value 'ships' (4:38)> -> __iterator
            __token = 149
            __iterator = getitem('ships')
            (__iterator, ____index_140188663280400, ) = getitem('repeat')('ship', __iterator)
            econtext['ship'] = None
            for __item in __iterator:
                econtext['ship'] = __item

                # <Interpolation value=<Substitution '\nSTR_NAME_${ship.id}                                          :${ship.get_name_substr()}{STRING} ' (4:45)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f803779f640> -> __content_140188669528304
                __token = 157
                __token = 168
                __content_140188669528304 = _lookup_attr(getitem('ship'), 'id')
                __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
                __token = 221
                __content_140188669528304_219 = _lookup_attr(getitem('ship'), 'get_name_substr')()
                __content_140188669528304_219 = __quote(__content_140188669528304_219, '\x00', '&#0;', None, None)
                __content_140188669528304 = ('%s%s%s%s%s' % ('\nSTR_NAME_', (__content_140188669528304 if (__content_140188669528304 is not None) else ''), '                                          :', (__content_140188669528304_219 if (__content_140188669528304_219 is not None) else ''), '{STRING} ', ))
                if (__content_140188669528304 is None):
                    pass
                else:
                    if (__content_140188669528304 is None):
                        __content_140188669528304 = None
                    else:
                        __tt = type(__content_140188669528304)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140188669528304 = str(__content_140188669528304)
                        else:
                            if (__tt is bytes):
                                __content_140188669528304 = decode(__content_140188669528304)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140188669528304 = __content_140188669528304.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140188669528304)
                                        __content_140188669528304 = (str(__content_140188669528304) if (__content_140188669528304 is __converted) else __converted)
                                    else:
                                        __content_140188669528304 = __content_140188669528304()
                if (__content_140188669528304 is not None):
                    __append(__content_140188669528304)
                __append('\n')
                ____index_140188663280400 -= 1
                if (____index_140188663280400 > 0):
                    __append('')
            if (__backup_ship_140188663215968 is __marker):
                del econtext['ship']
            else:
                econtext['ship'] = __backup_ship_140188663215968
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }