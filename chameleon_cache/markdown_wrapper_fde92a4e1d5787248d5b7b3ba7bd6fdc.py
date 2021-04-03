# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/docs_templates/markdown_wrapper.pt'
__tokens = {153: ('${structure: content}', 7, 4), 155: ('structure: content', 7, 6), 166: ('content', 7, 17), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from chameleon.utils import Markup as _Markup
from collections import deque as _deque

_static_139628049824680 = {'class': 'span12', }
_static_139628050453112 = {}
_static_139628049864688 = 'load:main_template.pt'

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
            __backup_macroname_139628047390152 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7efdb05017f0> name=None at 7efdb0501c88> -> __value
            __value = _static_139628049864688
            econtext['macroname'] = __value

            def __fill_sidebar_nav(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049825576
                __attrs_139628049825576 = _static_139628050453112

                # <div ... (3:0)
                # --------------------------------------------------------
                __append('<div')
                __append('>')
                __append('\n')
                __append('</div>')
            _slots = econtext['__slot_sidebar_nav'] = _deque((__fill_sidebar_nav, ))

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7efdb04f7ba8> name=None at 7efdb04f7208> -> __attrs_139628049822552
                __attrs_139628049822552 = _static_139628049824680

                # <div ... (6:0)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="span12"')
                __append('>')

                # <Interpolation value=<Substitution '\n    ${structure: content}\n' (6:43)> braces_required=True translation=False at 7efdb04f7f60> -> __content_139628066513336
                __token = 153
                __token = 155
                __token = 166
                __content_139628066513336 = getitem('content')
                __content_139628066513336 = _Markup(__content_139628066513336)
                __content_139628066513336 = __quote(__content_139628066513336, '\x00', '&#0;', None, False)
                __content_139628066513336 = ('%s%s%s' % ('\n    ', (__content_139628066513336 if (__content_139628066513336 is not None) else ''), '\n', ))
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
            if (__backup_macroname_139628047390152 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139628047390152
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }