# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/fish1672/src/docs_templates/main_template.pt'
__tokens = {1742: ("${doc_helper.get_active_nav(doc_name, 'get_started')}", 40, 27), 1744: ("doc_helper.get_active_nav(doc_name, 'get_started')", 40, 29), 1910: ("${doc_helper.get_active_nav(doc_name, 'ships')}", 43, 27), 1912: ("doc_helper.get_active_nav(doc_name, 'ships')", 43, 29), 2060: ("${doc_helper.get_active_nav(doc_name, 'code_reference')}", 46, 27), 2062: ("doc_helper.get_active_nav(doc_name, 'code_reference')", 46, 29), 2306: ("${doc_helper.get_active_nav(doc_name, 'translations')}", 51, 27), 2308: ("doc_helper.get_active_nav(doc_name, 'translations')", 51, 29), 2545: ("${metadata['dev_thread_url']}", 55, 29), 2547: ("metadata['dev_thread_url']", 55, 31)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_139865820574832 = {'version': '1.0', 'encoding': 'iso-8859-1', }
_static_139865820261288 = {'style': 'margin-top:30px; text-align:center; color:#999; padding:5px; background-color:#eee; border-top:solid 1px #ddd; box-shadow: inset 0px 1px 1px #ddd', }
_static_139865820258376 = {'class': 'container', }
_static_139865820297704 = {'class': 'lead', }
_static_139865820298208 = {'style': 'font-size:48px; padding-top:30px;', }
_static_139865820297032 = {'class': 'container', }
_static_139865820295352 = {'class': 'pull-right', 'style': 'margin-top:-30px; margin-bottom:0;', 'src': "static/img/industries/'+ random_image +'.png", }
_static_139865820467152 = {'href': "ships.html#' + random_image + '", }
_static_139865820465528 = {'language': 'JavaScript', }
_static_139865820464128 = {'class': 'hero-unit subhead', }
_static_139865820463904 = {'class': 'icon-comment icon-white', }
_static_139865820388880 = {'href': "${metadata['dev_thread_url']}", }
_static_139865820386864 = {'class': 'icon-globe icon-white', }
_static_139865820385352 = {'href': 'translations.html', }
_static_139865821334272 = {'class': "${doc_helper.get_active_nav(doc_name, 'translations')}", }
_static_139865821333264 = {'class': 'nav navbar-nav pull-right', }
_static_139865821331584 = {'href': 'code_reference.html', }
_static_139865821332200 = {'class': "${doc_helper.get_active_nav(doc_name, 'code_reference')}", }
_static_139865821428480 = {'href': 'ships.html', }
_static_139865821429656 = {'class': "${doc_helper.get_active_nav(doc_name, 'ships')}", }
_static_139865821426968 = {'href': 'get_started.html', }
_static_139865821408056 = {'class': "${doc_helper.get_active_nav(doc_name, 'get_started')}", }
_static_139865821407608 = {'class': 'nav navbar-nav pull-left', }
_static_139865821405984 = {'class': 'container', }
_static_139865821407328 = {'class': 'navbar navbar-inverse navbar-static-top', 'style': 'margin-bottom:0; border-bottom:1px solid #000;', }
_static_139865821518816 = {'type': 'text/javascript', }
_static_139865821519040 = {'type': 'text/javascript', 'src': 'static/js/jquery.tablesorter.widgets.min.js', }
_static_139865821516800 = {'type': 'text/javascript', 'src': 'static/js/jquery.tablesorter.min.js', }
_static_139865820625832 = {'type': 'text/javascript', 'src': 'static/js/jquery.metadata.js', }
_static_139865820624656 = {'type': 'text/javascript', 'src': 'static/js/jquery-1.9.1.min.js', }
_static_139865820623816 = {'rel': 'stylesheet', 'href': 'static/font-awesome/css/font-awesome.min.css', }
_static_139865820510304 = {'type': 'text/css', 'href': 'static/css/style.css', 'rel': 'stylesheet', }
_static_139865820511816 = {'type': 'text/css', 'href': 'static/css/bootstrap-responsive.min.css', 'rel': 'stylesheet', }
_static_139865820509240 = {'type': 'text/css', 'href': 'static/css/bootstrap.min.css', 'rel': 'stylesheet', }
_static_139865820704952 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0', }
_static_139865820708312 = {'http-equiv': 'Content-Type', 'content': 'text/html; charset=iso-8859-1', }
_static_139865822210704 = {}
_static_139865820705232 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'en', }

import re
import functools
from itertools import chain as __chain
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_body = econtext['__slot_body'].pop()
        except:
            __slot_body = None

        try:
            __slot_opt_page_header = econtext['__slot_opt_page_header'].pop()
        except:
            __slot_opt_page_header = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get
            __append('\n')
            __append('<!DOCTYPE html>')
            __append('\n')

            # <Static value=<_ast.Dict object at 0x7f350c8f31d0> name=None at 7f350c8f3278> -> __attrs_139865820706072
            __attrs_139865820706072 = _static_139865820705232

            # <html ... (4:0)
            # --------------------------------------------------------
            __append('<html')
            __append(' xmlns="http://www.w3.org/1999/xhtml"')
            __append(' lang="en"')
            __append('>')
            __append('\n')

            # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820707304
            __attrs_139865820707304 = _static_139865822210704

            # <head ... (5:0)
            # --------------------------------------------------------
            __append('<head')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820708088
            __attrs_139865820708088 = _static_139865822210704

            # <title ... (6:4)
            # --------------------------------------------------------
            __append('<title')
            __append(' >')
            __append('Squid Ate FISH')
            __append('</title>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c8f3dd8> name=None at 7f350c8f3f98> -> __attrs_139865820706464
            __attrs_139865820706464 = _static_139865820708312

            # <meta ... (7:4)
            # --------------------------------------------------------
            __append('<meta')
            __append(' http-equiv="Content-Type"')
            __append(' content="text/html; charset=iso-8859-1"')
            __append(' />')
            __append('\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c8f30b8> name=None at 7f350c8f3390> -> __attrs_139865820508848
            __attrs_139865820508848 = _static_139865820704952

            # <meta ... (9:4)
            # --------------------------------------------------------
            __append('<meta')
            __append(' name="viewport"')
            __append(' content="width=device-width, initial-scale=1.0"')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c8c3438> name=None at 7f350c8c3358> -> __attrs_139865820511984
            __attrs_139865820511984 = _static_139865820509240

            # <link ... (10:4)
            # --------------------------------------------------------
            __append('<link')
            __append(' type="text/css"')
            __append(' href="static/css/bootstrap.min.css"')
            __append(' rel="stylesheet"')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c8c3e48> name=None at 7f350c8c3f98> -> __attrs_139865820510752
            __attrs_139865820510752 = _static_139865820511816

            # <link ... (11:4)
            # --------------------------------------------------------
            __append('<link')
            __append(' type="text/css"')
            __append(' href="static/css/bootstrap-responsive.min.css"')
            __append(' rel="stylesheet"')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c8c3860> name=None at 7f350c8c3780> -> __attrs_139865820622976
            __attrs_139865820622976 = _static_139865820510304

            # <link ... (12:4)
            # --------------------------------------------------------
            __append('<link')
            __append(' type="text/css"')
            __append(' href="static/css/style.css"')
            __append(' rel="stylesheet"')
            __append('>')
            __append('\n\n    ')
            __append('<!--Font Awesome-->')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c8df3c8> name=None at 7f350c8df160> -> __attrs_139865820623760
            __attrs_139865820623760 = _static_139865820623816

            # <link ... (15:4)
            # --------------------------------------------------------
            __append('<link')
            __append(' rel="stylesheet"')
            __append(' href="static/font-awesome/css/font-awesome.min.css"')
            __append(' />')
            __append('\n    ')
            __append('<!--/Font Awesome-->')
            __append('\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c8df710> name=None at 7f350c8df588> -> __attrs_139865820625944
            __attrs_139865820625944 = _static_139865820624656

            # <script ... (18:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append(' src="static/js/jquery-1.9.1.min.js"')
            __append('>')
            __append('</script>')
            __append('\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c8dfba8> name=None at 7f350c8dfb70> -> __attrs_139865820626784
            __attrs_139865820626784 = _static_139865820625832

            # <script ... (20:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append(' src="static/js/jquery.metadata.js"')
            __append('>')
            __append('</script>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c9b9400> name=None at 7f350c9b9550> -> __attrs_139865821517472
            __attrs_139865821517472 = _static_139865821516800

            # <script ... (21:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append(' src="static/js/jquery.tablesorter.min.js"')
            __append('>')
            __append('</script>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c9b9cc0> name=None at 7f350c9b9908> -> __attrs_139865821519208
            __attrs_139865821519208 = _static_139865821519040

            # <script ... (22:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append(' src="static/js/jquery.tablesorter.widgets.min.js"')
            __append('>')
            __append('</script>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c9b9be0> name=None at 7f350c9b9c50> -> __attrs_139865821518704
            __attrs_139865821518704 = _static_139865821518816

            # <script ... (23:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append('>')
            __append("\n        $(document).ready(function(){\n            $('.tablesorter').tablesorter({\n                textExtraction: function(node){\n                            var cell_value = $(node).text();\n                            var sort_value = $(node).data('value');\n                    return (sort_value != undefined) ? sort_value : cell_value;\n                 },\n            })\n        })\n    ")
            __append('</script>')
            __append('\n')
            __append('</head>')
            __append('\n\n')

            # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821517416
            __attrs_139865821517416 = _static_139865822210704

            # <body ... (36:0)
            # --------------------------------------------------------
            __append('<body')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c99e860> name=None at 7f350c99ea90> -> __attrs_139865821405816
            __attrs_139865821405816 = _static_139865821407328

            # <div ... (37:4)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="navbar navbar-inverse navbar-static-top"')
            __append(' style="margin-bottom:0; border-bottom:1px solid #000;"')
            __append('>')
            __append('\n        ')

            # <Static value=<_ast.Dict object at 0x7f350c99e320> name=None at 7f350c99eba8> -> __attrs_139865821408672
            __attrs_139865821408672 = _static_139865821405984

            # <div ... (38:8)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="container"')
            __append('>')
            __append('\n            ')

            # <Static value=<_ast.Dict object at 0x7f350c99e978> name=None at 7f350c99ea20> -> __attrs_139865821406992
            __attrs_139865821406992 = _static_139865821407608

            # <ul ... (39:12)
            # --------------------------------------------------------
            __append('<ul')
            __append(' class="nav navbar-nav pull-left"')
            __append('>')
            __append('\n                ')

            # <Static value=<_ast.Dict object at 0x7f350c99eb38> name=None at 7f350c99eb00> -> __attrs_139865821426072
            __attrs_139865821426072 = _static_139865821408056

            # <li ... (40:16)
            # --------------------------------------------------------
            __append('<li')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7f350d97df98> at 7f350c90bf28> -> __default_139865821426688
            __default_139865821426688 = False

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'get_started')}" (40:27)> braces_required=True translation=False at 7f350c9a35c0> -> __attr_class
            __token = 1742
            __token = 1744
            __attr_class = _lookup_attr(getitem('doc_helper'), 'get_active_nav')(getitem('doc_name'), 'get_started')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
            __attr_class = __attr_class
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is False):
                    __attr_class = None
                else:
                    __tt = type(__attr_class)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_class = str(__attr_class)
                    else:
                        if (__tt is bytes):
                            __attr_class = decode(__attr_class)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_class = __attr_class.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_class)
                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                else:
                                    __attr_class = __attr_class()
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>')
            __append('\n                    ')

            # <Static value=<_ast.Dict object at 0x7f350c9a3518> name=None at 7f350c9a3320> -> __attrs_139865821428032
            __attrs_139865821428032 = _static_139865821426968

            # <a ... (41:20)
            # --------------------------------------------------------
            __append('<a')
            __append(' href="get_started.html"')
            __append('>')
            __append('Get Started')
            __append('</a>')
            __append('\n                ')
            __append('</li>')
            __append('\n                ')

            # <Static value=<_ast.Dict object at 0x7f350c9a3f98> name=None at 7f350c9a3d68> -> __attrs_139865821429040
            __attrs_139865821429040 = _static_139865821429656

            # <li ... (43:16)
            # --------------------------------------------------------
            __append('<li')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7f350d97df98> at 7f350c90bf28> -> __default_139865821429152
            __default_139865821429152 = False

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'ships')}" (43:27)> braces_required=True translation=False at 7f350c9a3e80> -> __attr_class
            __token = 1910
            __token = 1912
            __attr_class = _lookup_attr(getitem('doc_helper'), 'get_active_nav')(getitem('doc_name'), 'ships')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
            __attr_class = __attr_class
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is False):
                    __attr_class = None
                else:
                    __tt = type(__attr_class)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_class = str(__attr_class)
                    else:
                        if (__tt is bytes):
                            __attr_class = decode(__attr_class)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_class = __attr_class.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_class)
                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                else:
                                    __attr_class = __attr_class()
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>')
            __append('\n                    ')

            # <Static value=<_ast.Dict object at 0x7f350c9a3b00> name=None at 7f350c9a3a90> -> __attrs_139865821427584
            __attrs_139865821427584 = _static_139865821428480

            # <a ... (44:20)
            # --------------------------------------------------------
            __append('<a')
            __append(' href="ships.html"')
            __append('>')
            __append('Ships')
            __append('</a>')
            __append('\n                ')
            __append('</li>')
            __append('\n                ')

            # <Static value=<_ast.Dict object at 0x7f350c98c2e8> name=None at 7f350c9a36a0> -> __attrs_139865821331864
            __attrs_139865821331864 = _static_139865821332200

            # <li ... (46:16)
            # --------------------------------------------------------
            __append('<li')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7f350d97df98> at 7f350c90bf28> -> __default_139865821332704
            __default_139865821332704 = False

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'code_reference')}" (46:27)> braces_required=True translation=False at 7f350c98c5f8> -> __attr_class
            __token = 2060
            __token = 2062
            __attr_class = _lookup_attr(getitem('doc_helper'), 'get_active_nav')(getitem('doc_name'), 'code_reference')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
            __attr_class = __attr_class
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is False):
                    __attr_class = None
                else:
                    __tt = type(__attr_class)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_class = str(__attr_class)
                    else:
                        if (__tt is bytes):
                            __attr_class = decode(__attr_class)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_class = __attr_class.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_class)
                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                else:
                                    __attr_class = __attr_class()
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>')
            __append('\n                    ')

            # <Static value=<_ast.Dict object at 0x7f350c98c080> name=None at 7f350c98c0b8> -> __attrs_139865821333040
            __attrs_139865821333040 = _static_139865821331584

            # <a ... (47:20)
            # --------------------------------------------------------
            __append('<a')
            __append(' href="code_reference.html"')
            __append('>')
            __append('Code Reference')
            __append('</a>')
            __append('\n                ')
            __append('</li>')
            __append('\n            ')
            __append('</ul>')
            __append('\n            ')

            # <Static value=<_ast.Dict object at 0x7f350c98c710> name=None at 7f350c98c518> -> __attrs_139865821333320
            __attrs_139865821333320 = _static_139865821333264

            # <ul ... (50:12)
            # --------------------------------------------------------
            __append('<ul')
            __append(' class="nav navbar-nav pull-right"')
            __append('>')
            __append('\n                ')

            # <Static value=<_ast.Dict object at 0x7f350c98cb00> name=None at 7f350c98cba8> -> __attrs_139865821335056
            __attrs_139865821335056 = _static_139865821334272

            # <li ... (51:16)
            # --------------------------------------------------------
            __append('<li')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7f350d97df98> at 7f350c90bf28> -> __default_139865821333544
            __default_139865821333544 = False

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'translations')}" (51:27)> braces_required=True translation=False at 7f350c98cbe0> -> __attr_class
            __token = 2306
            __token = 2308
            __attr_class = _lookup_attr(getitem('doc_helper'), 'get_active_nav')(getitem('doc_name'), 'translations')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, False)
            __attr_class = __attr_class
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is False):
                    __attr_class = None
                else:
                    __tt = type(__attr_class)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_class = str(__attr_class)
                    else:
                        if (__tt is bytes):
                            __attr_class = decode(__attr_class)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_class = __attr_class.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_class)
                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                else:
                                    __attr_class = __attr_class()
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>')
            __append('\n                    ')

            # <Static value=<_ast.Dict object at 0x7f350c8a5048> name=None at 7f350c98cf28> -> __attrs_139865820385744
            __attrs_139865820385744 = _static_139865820385352

            # <a ... (52:20)
            # --------------------------------------------------------
            __append('<a')
            __append(' href="translations.html"')
            __append('>')

            # <Static value=<_ast.Dict object at 0x7f350c8a5630> name=None at 7f350c8a54a8> -> __attrs_139865820387032
            __attrs_139865820387032 = _static_139865820386864

            # <i ... (52:48)
            # --------------------------------------------------------
            __append('<i')
            __append(' class="icon-globe icon-white"')
            __append('>')
            __append('</i>')
            __append(' Help Translate FISH')
            __append('</a>')
            __append('\n                ')
            __append('</li>')
            __append('\n                ')

            # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820387368
            __attrs_139865820387368 = _static_139865822210704

            # <li ... (54:16)
            # --------------------------------------------------------
            __append('<li')
            __append('>')
            __append('\n                    ')

            # <Static value=<_ast.Dict object at 0x7f350c8a5e10> name=None at 7f350c8a5dd8> -> __attrs_139865820463456
            __attrs_139865820463456 = _static_139865820388880

            # <a ... (55:20)
            # --------------------------------------------------------
            __append('<a')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7f350d97df98> at 7f350c90bf28> -> __default_139865820463232
            __default_139865820463232 = False

            # <Interpolation value=<Substitution "${metadata['dev_thread_url']}" (55:29)> braces_required=True translation=False at 7f350c8a5f98> -> __attr_href
            __token = 2545
            __token = 2547
            __attr_href = getitem('metadata')['dev_thread_url']
            __attr_href = __quote(__attr_href, '"', '&quot;', None, False)
            __attr_href = __attr_href
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is False):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_href = str(__attr_href)
                    else:
                        if (__tt is bytes):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append('>')

            # <Static value=<_ast.Dict object at 0x7f350c8b8320> name=None at 7f350c8b82b0> -> __attrs_139865820464296
            __attrs_139865820464296 = _static_139865820463904

            # <i ... (55:60)
            # --------------------------------------------------------
            __append('<i')
            __append(' class="icon-comment icon-white"')
            __append('>')
            __append('</i>')
            __append(' Discuss at TT-Forums.net')
            __append('</a>')
            __append('\n                ')
            __append('</li>')
            __append('\n            ')
            __append('</ul>')
            __append('\n        ')
            __append('</div>')
            __append('\n    ')
            __append('</div>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c8b8400> name=None at 7f350c8b8518> -> __attrs_139865820465304
            __attrs_139865820465304 = _static_139865820464128

            # <div ... (60:4)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="hero-unit subhead"')
            __append('>')
            __append('\n        ')

            # <Static value=<_ast.Dict object at 0x7f350c8b8978> name=None at 7f350c8b8668> -> __attrs_139865820465920
            __attrs_139865820465920 = _static_139865820465528

            # <script ... (61:8)
            # --------------------------------------------------------
            __append('<script')
            __append(' language="JavaScript"')
            __append('>')
            __append('\n        function random_img(){\n            var images=new Array("",\n                                 "");\n\n            var random_image=images[Math.floor(Math.random()*images.length)];\n            document.write(\'')

            # <Static value=<_ast.Dict object at 0x7f350c8b8fd0> name=None at 7f350c8b8e48> -> __attrs_139865820465248
            __attrs_139865820465248 = _static_139865820467152

            # <a ... (67:28)
            # --------------------------------------------------------
            __append('<a')
            __append(' href="ships.html#\' + random_image + \'"')
            __append('>')

            # <Static value=<_ast.Dict object at 0x7f350c88f0b8> name=None at 7f350c88f048> -> __attrs_139865820296752
            __attrs_139865820296752 = _static_139865820295352

            # <img ... (67:70)
            # --------------------------------------------------------
            __append('<img')
            __append(' class="pull-right"')
            __append(' style="margin-top:-30px; margin-bottom:0;"')
            __append(' src="static/img/industries/\'+ random_image +\'.png"')
            __append('>')
            __append('</a>')
            __append("')\n        }\n        random_img()\n        ")
            __append('</script>')
            __append('\n        ')

            # <Static value=<_ast.Dict object at 0x7f350c88f748> name=None at 7f350c88f550> -> __attrs_139865820297984
            __attrs_139865820297984 = _static_139865820297032

            # <div ... (71:8)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="container"')
            __append('>')
            __append('\n            ')

            # <Static value=<_ast.Dict object at 0x7f350c88fbe0> name=None at 7f350c88fcc0> -> __attrs_139865820297816
            __attrs_139865820297816 = _static_139865820298208

            # <h1 ... (72:12)
            # --------------------------------------------------------
            __append('<h1')
            __append(' style="font-size:48px; padding-top:30px;"')
            __append('>')
            __append('Squid Ate FISH')
            __append('</h1>')
            __append('\n            ')

            # <Static value=<_ast.Dict object at 0x7f350c88f9e8> name=None at 7f350c88fa20> -> __attrs_139865820258544
            __attrs_139865820258544 = _static_139865820297704

            # <p ... (73:12)
            # --------------------------------------------------------
            __append('<p')
            __append(' class="lead"')
            __append('>')
            __append('New Ships for OpenTTD')
            __append('</p>')
            __append('\n        ')
            __append('</div>')
            __append('\n    ')
            __append('</div>')
            __append('\n    ')
            if (__slot_opt_page_header is None):
                __append('\n        ')
                __append('\n    ')
            else:
                __slot_opt_page_header(__stream, econtext.copy(), rcontext)
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c886048> name=None at 7f350c8864a8> -> __attrs_139865820258992
            __attrs_139865820258992 = _static_139865820258376

            # <div ... (79:4)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="container"')
            __append('>')
            __append('\n        ')
            if (__slot_body is None):
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820260336
                __attrs_139865820260336 = _static_139865822210704

                # <p ... (81:12)
                # --------------------------------------------------------
                __append('<p')
                __append('>')
                __append('Ooooops - there is no content for some reason. Something has probably gone nuts in the build. ')
                __append('</p>')
                __append('\n        ')
            else:
                __slot_body(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            __append('</div>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f350c886ba8> name=None at 7f350c886710> -> __attrs_139865820261680
            __attrs_139865820261680 = _static_139865820261288

            # <div ... (84:4)
            # --------------------------------------------------------
            __append('<div')
            __append(' style="margin-top:30px; text-align:center; color:#999; padding:5px; background-color:#eee; border-top:solid 1px #ddd; box-shadow: inset 0px 1px 1px #ddd"')
            __append('>')
            __append('\n        Squid Ate FISH, with thanks to all who helped\n    ')
            __append('</div>')
            __append('\n')
            __append('</body>')
            __append('\n')
            __append('</html>')
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<_ast.Dict object at 0x7f350c8d3470> name=None at 7f350c8d3160> -> __attrs_139865820576288
            __attrs_139865820576288 = _static_139865820574832

            # <?xml ... (1:0)
            # --------------------------------------------------------
            __append('<?xml')
            __append(' version="1.0"')
            __append(' encoding="iso-8859-1"')
            __append('?>')
            __append('\n')
            __token = None
            render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n\n\n\n\n\n\n\n\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render': render, }