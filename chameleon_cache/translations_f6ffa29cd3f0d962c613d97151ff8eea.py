# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/fish1672/src/docs_templates/translations.pt'
__tokens = {36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque

_static_139865819864480 = {'class': 'btn btn-primary btn-large', 'href': 'https://translator.openttdcoop.org/project/fish', }
_static_139865819863696 = {'href': 'https://translator.openttdcoop.org/project/fish', }
_static_139865822210704 = {}
_static_139865819166424 = 'load:main_template.pt'

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
            __backup_macroname_139865822389832 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f350c77b6d8> name=None at 7f350c77b2e8> -> __value
            __value = _static_139865819166424
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819165808
                __attrs_139865819165808 = _static_139865822210704

                # <div ... (2:0)
                # --------------------------------------------------------
                __append('<div')
                __append('>')
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819166536
                __attrs_139865819166536 = _static_139865822210704

                # <div ... (3:4)
                # --------------------------------------------------------
                __append('<div')
                __append('>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819863584
                __attrs_139865819863584 = _static_139865822210704

                # <h2 ... (4:8)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('Help Translate Squid Ate FISH')
                __append('</h2>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819861232
                __attrs_139865819861232 = _static_139865822210704

                # <p ... (5:8)
                # --------------------------------------------------------
                __append('<p')
                __append('>')
                __append('Squid Ate FISH has already been translated into multiple languages, and more translations are always welcome.')
                __append('</p>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819862688
                __attrs_139865819862688 = _static_139865822210704

                # <p ... (6:8)
                # --------------------------------------------------------
                __append('<p')
                __append('>')
                __append('Translations can be added, checked and updated using the ')

                # <Static value=<_ast.Dict object at 0x7f350c825a90> name=None at 7f350c825710> -> __attrs_139865819864256
                __attrs_139865819864256 = _static_139865819863696

                # <a ... (6:68)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="https://translator.openttdcoop.org/project/fish"')
                __append('>')
                __append('web translator')
                __append('</a>')
                __append('.')
                __append('</p>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f350c825da0> name=None at 7f350c825ac8> -> __attrs_139865819862968
                __attrs_139865819862968 = _static_139865819864480

                # <a ... (7:8)
                # --------------------------------------------------------
                __append('<a')
                __append(' class="btn btn-primary btn-large"')
                __append(' href="https://translator.openttdcoop.org/project/fish"')
                __append('>')
                __append('Web Translator')
                __append('</a>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821393640
                __attrs_139865821393640 = _static_139865822210704

                # <br ... (8:8)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821393024
                __attrs_139865821393024 = _static_139865822210704

                # <br ... (8:14)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n    ')
                __append('</div>')
                __append('\n')
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
            if (__backup_macroname_139865822389832 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139865822389832
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }