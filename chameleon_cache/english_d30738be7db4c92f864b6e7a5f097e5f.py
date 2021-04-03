# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/lang_templates/english.pylng'
__tokens = {0: ('STR_GRF_NAME                                                    :${repo_vars.repo_title}', 1, 0), 67: ('repo_vars.repo_title', 1, 67), 149: ('ships', 4, 38), 157: ('STR_NAME_${ship.id}                                          :${ship.get_name_substr()}{STRING}', 5, 0), 168: ('ship.id', 5, 11), 221: ('ship.get_name_substr()', 5, 64)}

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

            # <Interpolation value=<Substitution 'STR_GRF_NAME                                                    :${repo_vars.repo_title}\n\n' (1:0)> braces_required=True translation=False at 7efdb03daf98> -> __content_139628066513336
            __token = 0
            __token = 67
            __content_139628066513336 = _lookup_attr(getitem('repo_vars'), 'repo_title')
            __content_139628066513336 = __quote(__content_139628066513336, '\x00', '&#0;', None, False)
            __content_139628066513336 = ('%s%s%s' % ('STR_GRF_NAME                                                    :', (__content_139628066513336 if (__content_139628066513336 is not None) else ''), '\n\n', ))
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
            __append('\n')
            __backup_ship_139628048521200 = get('ship', __marker)

            # <Value 'ships' (4:38)> -> __iterator
            __token = 149
            __iterator = getitem('ships')
            (__iterator, ____index_139628049117312, ) = getitem('repeat')('ship', __iterator)
            econtext['ship'] = None
            for __item in __iterator:
                econtext['ship'] = __item

                # <Interpolation value=<Substitution '\nSTR_NAME_${ship.id}                                          :${ship.get_name_substr()}{STRING} ' (4:45)> braces_required=True translation=False at 7efdb044bf98> -> __content_139628066513336
                __token = 157
                __token = 168
                __content_139628066513336 = _lookup_attr(getitem('ship'), 'id')
                __content_139628066513336 = __quote(__content_139628066513336, '\x00', '&#0;', None, False)
                __token = 221
                __content_139628066513336_219 = _lookup_attr(getitem('ship'), 'get_name_substr')()
                __content_139628066513336_219 = __quote(__content_139628066513336_219, '\x00', '&#0;', None, False)
                __content_139628066513336 = ('%s%s%s%s%s' % ('\nSTR_NAME_', (__content_139628066513336 if (__content_139628066513336 is not None) else ''), '                                          :', (__content_139628066513336_219 if (__content_139628066513336_219 is not None) else ''), '{STRING} ', ))
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
                __append('\n')
                ____index_139628049117312 -= 1
                if (____index_139628049117312 > 0):
                    __append('')
            if (__backup_ship_139628048521200 is __marker):
                del econtext['ship']
            else:
                econtext['ship'] = __backup_ship_139628048521200
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }