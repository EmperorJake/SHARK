# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/SHARK/src/docs_templates/markdown_wrapper.pt'

__tokens = {153: ('${structure: content}', 7, 4), 155: ('structure: content', 7, 6), 166: ('content', 7, 17), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from chameleon.utils import Markup as _Markup
from collections import deque as _deque

_static_140188663377296 = {'class': 'span12', }
_static_140188663375664 = 'load:main_template.pt'
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

            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663377584
            __attrs_140188663377584 = _static_140188664645808
            __backup_macroname_140188664078144 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f80377b6730> name=None at 7f80377b66a0> -> __value
            __value = _static_140188663375664
            econtext['macroname'] = __value

            def __fill_sidebar_nav(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663377488
                __attrs_140188663377488 = _static_140188664645808

                # <div ... (3:0)
                # --------------------------------------------------------
                __append('<div>\n</div>')
            _slots = econtext['__slot_sidebar_nav'] = _deque((__fill_sidebar_nav, ))

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f80377b6d90> name=None at 7f80377b6d00> -> __attrs_140188663602144
                __attrs_140188663602144 = _static_140188663377296

                # <div ... (6:0)
                # --------------------------------------------------------
                __append('<div class="span12">')

                # <Interpolation value=<Substitution '\n    ${structure: content}\n' (6:43)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f80377ed0a0> -> __content_140188669528304
                __token = 153
                __token = 155
                __token = 166
                __content_140188669528304 = getitem('content')
                __content_140188669528304 = _Markup(__content_140188669528304)
                __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
                __content_140188669528304 = ('%s%s%s' % ('\n    ', (__content_140188669528304 if (__content_140188669528304 is not None) else ''), '\n', ))
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
                __append('</div>')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'load:main_template.pt' (1:36)> -> __macro
            __token = 36
            __macro = 'main_template.pt'
            __macro = __loader(__macro)
            __token = 36
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140188664078144 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140188664078144
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }