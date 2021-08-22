# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/SHARK/src/docs_templates/translations.pt'

__tokens = {36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque

_static_140188663374512 = {'class': 'btn btn-primary btn-large', 'href': 'https://translator.openttdcoop.org/project/fish', }
_static_140188660930352 = {'href': 'https://translator.openttdcoop.org/project/fish', }
_static_140188663601568 = 'load:main_template.pt'
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

            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663602384
            __attrs_140188663602384 = _static_140188664645808
            __backup_macroname_140188659131904 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f80377ed9a0> name=None at 7f80377ed610> -> __value
            __value = _static_140188663601568
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663601520
                __attrs_140188663601520 = _static_140188664645808

                # <div ... (2:0)
                # --------------------------------------------------------
                __append('<div>\n    ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188660932416
                __attrs_140188660932416 = _static_140188664645808

                # <div ... (3:4)
                # --------------------------------------------------------
                __append('<div>\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188660931936
                __attrs_140188660931936 = _static_140188664645808

                # <h2 ... (4:8)
                # --------------------------------------------------------
                __append('<h2>Help Translate Squid Ate FISH</h2>\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188660928864
                __attrs_140188660928864 = _static_140188664645808

                # <p ... (5:8)
                # --------------------------------------------------------
                __append('<p>Squid Ate FISH has already been translated into multiple languages, and more translations are always welcome.</p>\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188660931456
                __attrs_140188660931456 = _static_140188664645808

                # <p ... (6:8)
                # --------------------------------------------------------
                __append('<p>Translations can be added, checked and updated using the ')

                # <Static value=<_ast.Dict object at 0x7f8037561730> name=None at 7f80375616d0> -> __attrs_140188663375616
                __attrs_140188663375616 = _static_140188660930352

                # <a ... (6:68)
                # --------------------------------------------------------
                __append('<a href="https://translator.openttdcoop.org/project/fish">web translator</a>.</p>\n        ')

                # <Static value=<_ast.Dict object at 0x7f80377b62b0> name=None at 7f80377b6640> -> __attrs_140188663377344
                __attrs_140188663377344 = _static_140188663374512

                # <a ... (7:8)
                # --------------------------------------------------------
                __append('<a class="btn btn-primary btn-large" href="https://translator.openttdcoop.org/project/fish">Web Translator</a>\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663377632
                __attrs_140188663377632 = _static_140188664645808

                # <br ... (8:8)
                # --------------------------------------------------------
                __append('<br />')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663376288
                __attrs_140188663376288 = _static_140188664645808

                # <br ... (8:14)
                # --------------------------------------------------------
                __append('<br />\n    </div>\n</div>')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'load:main_template.pt' (1:36)> -> __macro
            __token = 36
            __macro = 'main_template.pt'
            __macro = __loader(__macro)
            __token = 36
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140188659131904 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140188659131904
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }