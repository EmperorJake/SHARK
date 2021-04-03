# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/docs_templates/main_template.pt'
__tokens = {1742: ("${doc_helper.get_active_nav(doc_name, 'get_started')}", 40, 27), 1744: ("doc_helper.get_active_nav(doc_name, 'get_started')", 40, 29), 1910: ("${doc_helper.get_active_nav(doc_name, 'ships')}", 43, 27), 1912: ("doc_helper.get_active_nav(doc_name, 'ships')", 43, 29), 2060: ("${doc_helper.get_active_nav(doc_name, 'code_reference')}", 46, 27), 2062: ("doc_helper.get_active_nav(doc_name, 'code_reference')", 46, 29), 2306: ("${doc_helper.get_active_nav(doc_name, 'translations')}", 51, 27), 2308: ("doc_helper.get_active_nav(doc_name, 'translations')", 51, 29), 2545: ("${metadata['dev_thread_url']}", 55, 29), 2547: ("metadata['dev_thread_url']", 55, 31)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_139818164548608 = {'version': '1.0', 'encoding': 'iso-8859-1', }
_static_139818164776912 = {'style': 'margin-top:30px; text-align:center; color:#999; padding:5px; background-color:#eee; border-top:solid 1px #ddd; box-shadow: inset 0px 1px 1px #ddd', }
_static_139818164559944 = {'class': 'container', }
_static_139818164561120 = {'class': 'lead', }
_static_139818164563136 = {'style': 'font-size:48px; padding-top:30px;', }
_static_139818164761488 = {'class': 'container', }
_static_139818164762888 = {'class': 'pull-right', 'style': 'margin-top:-30px; margin-bottom:0;', 'src': "static/img/industries/'+ random_image +'.png", }
_static_139818164761264 = {'href': "ships.html#' + random_image + '", }
_static_139818164761880 = {'language': 'JavaScript', }
_static_139818164620480 = {'class': 'hero-unit subhead', }
_static_139818164619920 = {'class': 'icon-comment icon-white', }
_static_139818164620144 = {'href': "${metadata['dev_thread_url']}", }
_static_139818164335224 = {'class': 'icon-globe icon-white', }
_static_139818164338416 = {'href': 'translations.html', }
_static_139818164337464 = {'class': "${doc_helper.get_active_nav(doc_name, 'translations')}", }
_static_139818164335336 = {'class': 'nav navbar-nav pull-right', }
_static_139818164367936 = {'href': 'code_reference.html', }
_static_139818164371072 = {'class': "${doc_helper.get_active_nav(doc_name, 'code_reference')}", }
_static_139818164369392 = {'href': 'ships.html', }
_static_139818164368496 = {'class': "${doc_helper.get_active_nav(doc_name, 'ships')}", }
_static_139818164443848 = {'href': 'get_started.html', }
_static_139818164445024 = {'class': "${doc_helper.get_active_nav(doc_name, 'get_started')}", }
_static_139818164442560 = {'class': 'nav navbar-nav pull-left', }
_static_139818164441552 = {'class': 'container', }
_static_139818165257048 = {'class': 'navbar navbar-inverse navbar-static-top', 'style': 'margin-bottom:0; border-bottom:1px solid #000;', }
_static_139818165259120 = {'type': 'text/javascript', }
_static_139818165256656 = {'type': 'text/javascript', 'src': 'static/js/jquery.tablesorter.widgets.min.js', }
_static_139818164133168 = {'type': 'text/javascript', 'src': 'static/js/jquery.tablesorter.min.js', }
_static_139818164131824 = {'type': 'text/javascript', 'src': 'static/js/jquery.metadata.js', }
_static_139818164130928 = {'type': 'text/javascript', 'src': 'static/js/jquery-1.9.1.min.js', }
_static_139818164354800 = {'rel': 'stylesheet', 'href': 'static/font-awesome/css/font-awesome.min.css', }
_static_139818164353008 = {'type': 'text/css', 'href': 'static/css/style.css', 'rel': 'stylesheet', }
_static_139818164351216 = {'type': 'text/css', 'href': 'static/css/bootstrap-responsive.min.css', 'rel': 'stylesheet', }
_static_139818164077288 = {'type': 'text/css', 'href': 'static/css/bootstrap.min.css', 'rel': 'stylesheet', }
_static_139818164080032 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0', }
_static_139818164079024 = {'http-equiv': 'Content-Type', 'content': 'text/html; charset=iso-8859-1', }
_static_139818165914032 = {}
_static_139818164551464 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'en', }

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

            # <Static value=<_ast.Dict object at 0x7f29f407ff28> name=None at 7f29f407fc50> -> __attrs_139818164550904
            __attrs_139818164550904 = _static_139818164551464

            # <html ... (4:0)
            # --------------------------------------------------------
            __append('<html')
            __append(' xmlns="http://www.w3.org/1999/xhtml"')
            __append(' lang="en"')
            __append('>')
            __append('\n')

            # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818190932736
            __attrs_139818190932736 = _static_139818165914032

            # <head ... (5:0)
            # --------------------------------------------------------
            __append('<head')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164079136
            __attrs_139818164079136 = _static_139818165914032

            # <title ... (6:4)
            # --------------------------------------------------------
            __append('<title')
            __append(' >')
            __append('Squid Ate FISH')
            __append('</title>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f29f400c9b0> name=None at 7f29f400c7b8> -> __attrs_139818164080200
            __attrs_139818164080200 = _static_139818164079024

            # <meta ... (7:4)
            # --------------------------------------------------------
            __append('<meta')
            __append(' http-equiv="Content-Type"')
            __append(' content="text/html; charset=iso-8859-1"')
            __append(' />')
            __append('\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f29f400cda0> name=None at 7f29f400cef0> -> __attrs_139818164078800
            __attrs_139818164078800 = _static_139818164080032

            # <meta ... (9:4)
            # --------------------------------------------------------
            __append('<meta')
            __append(' name="viewport"')
            __append(' content="width=device-width, initial-scale=1.0"')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f29f400c2e8> name=None at 7f29f400c588> -> __attrs_139818164076672
            __attrs_139818164076672 = _static_139818164077288

            # <link ... (10:4)
            # --------------------------------------------------------
            __append('<link')
            __append(' type="text/css"')
            __append(' href="static/css/bootstrap.min.css"')
            __append(' rel="stylesheet"')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f29f404f0f0> name=None at 7f29f404fa90> -> __attrs_139818164352168
            __attrs_139818164352168 = _static_139818164351216

            # <link ... (11:4)
            # --------------------------------------------------------
            __append('<link')
            __append(' type="text/css"')
            __append(' href="static/css/bootstrap-responsive.min.css"')
            __append(' rel="stylesheet"')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f29f404f7f0> name=None at 7f29f404f470> -> __attrs_139818164353288
            __attrs_139818164353288 = _static_139818164353008

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

            # <Static value=<_ast.Dict object at 0x7f29f404fef0> name=None at 7f29f404f978> -> __attrs_139818164129864
            __attrs_139818164129864 = _static_139818164354800

            # <link ... (15:4)
            # --------------------------------------------------------
            __append('<link')
            __append(' rel="stylesheet"')
            __append(' href="static/font-awesome/css/font-awesome.min.css"')
            __append(' />')
            __append('\n    ')
            __append('<!--/Font Awesome-->')
            __append('\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f29f4019470> name=None at 7f29f4019400> -> __attrs_139818164131096
            __attrs_139818164131096 = _static_139818164130928

            # <script ... (18:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append(' src="static/js/jquery-1.9.1.min.js"')
            __append('>')
            __append('</script>')
            __append('\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f29f40197f0> name=None at 7f29f4019710> -> __attrs_139818164132608
            __attrs_139818164132608 = _static_139818164131824

            # <script ... (20:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append(' src="static/js/jquery.metadata.js"')
            __append('>')
            __append('</script>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f29f4019d30> name=None at 7f29f4019c50> -> __attrs_139818164133336
            __attrs_139818164133336 = _static_139818164133168

            # <script ... (21:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append(' src="static/js/jquery.tablesorter.min.js"')
            __append('>')
            __append('</script>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f29f412c1d0> name=None at 7f29f412ca20> -> __attrs_139818165259680
            __attrs_139818165259680 = _static_139818165256656

            # <script ... (22:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append(' src="static/js/jquery.tablesorter.widgets.min.js"')
            __append('>')
            __append('</script>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f29f412cb70> name=None at 7f29f412c048> -> __attrs_139818165259568
            __attrs_139818165259568 = _static_139818165259120

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

            # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165258616
            __attrs_139818165258616 = _static_139818165914032

            # <body ... (36:0)
            # --------------------------------------------------------
            __append('<body')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7f29f412c358> name=None at 7f29f412c4e0> -> __attrs_139818164444520
            __attrs_139818164444520 = _static_139818165257048

            # <div ... (37:4)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="navbar navbar-inverse navbar-static-top"')
            __append(' style="margin-bottom:0; border-bottom:1px solid #000;"')
            __append('>')
            __append('\n        ')

            # <Static value=<_ast.Dict object at 0x7f29f40651d0> name=None at 7f29f4065160> -> __attrs_139818164442672
            __attrs_139818164442672 = _static_139818164441552

            # <div ... (38:8)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="container"')
            __append('>')
            __append('\n            ')

            # <Static value=<_ast.Dict object at 0x7f29f40655c0> name=None at 7f29f4065588> -> __attrs_139818164441608
            __attrs_139818164441608 = _static_139818164442560

            # <ul ... (39:12)
            # --------------------------------------------------------
            __append('<ul')
            __append(' class="nav navbar-nav pull-left"')
            __append('>')
            __append('\n                ')

            # <Static value=<_ast.Dict object at 0x7f29f4065f60> name=None at 7f29f4065e48> -> __attrs_139818164443904
            __attrs_139818164443904 = _static_139818164445024

            # <li ... (40:16)
            # --------------------------------------------------------
            __append('<li')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7f29f510e5c0> at 7f29f5904e48> -> __default_139818164443960
            __default_139818164443960 = False

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'get_started')}" (40:27)> braces_required=True translation=False at 7f29f4065dd8> -> __attr_class
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

            # <Static value=<_ast.Dict object at 0x7f29f4065ac8> name=None at 7f29f40659b0> -> __attrs_139818164650392
            __attrs_139818164650392 = _static_139818164443848

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

            # <Static value=<_ast.Dict object at 0x7f29f4053470> name=None at 7f29f4098630> -> __attrs_139818164369448
            __attrs_139818164369448 = _static_139818164368496

            # <li ... (43:16)
            # --------------------------------------------------------
            __append('<li')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7f29f510e5c0> at 7f29f5904e48> -> __default_139818164369000
            __default_139818164369000 = False

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'ships')}" (43:27)> braces_required=True translation=False at 7f29f4053710> -> __attr_class
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

            # <Static value=<_ast.Dict object at 0x7f29f40537f0> name=None at 7f29f4053588> -> __attrs_139818164369896
            __attrs_139818164369896 = _static_139818164369392

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

            # <Static value=<_ast.Dict object at 0x7f29f4053e80> name=None at 7f29f4053ef0> -> __attrs_139818164367544
            __attrs_139818164367544 = _static_139818164371072

            # <li ... (46:16)
            # --------------------------------------------------------
            __append('<li')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7f29f510e5c0> at 7f29f5904e48> -> __default_139818164368216
            __default_139818164368216 = False

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'code_reference')}" (46:27)> braces_required=True translation=False at 7f29f4053400> -> __attr_class
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

            # <Static value=<_ast.Dict object at 0x7f29f4053240> name=None at 7f29f4053278> -> __attrs_139818164335728
            __attrs_139818164335728 = _static_139818164367936

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

            # <Static value=<_ast.Dict object at 0x7f29f404b2e8> name=None at 7f29f404b128> -> __attrs_139818164337968
            __attrs_139818164337968 = _static_139818164335336

            # <ul ... (50:12)
            # --------------------------------------------------------
            __append('<ul')
            __append(' class="nav navbar-nav pull-right"')
            __append('>')
            __append('\n                ')

            # <Static value=<_ast.Dict object at 0x7f29f404bb38> name=None at 7f29f404bc88> -> __attrs_139818164336624
            __attrs_139818164336624 = _static_139818164337464

            # <li ... (51:16)
            # --------------------------------------------------------
            __append('<li')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7f29f510e5c0> at 7f29f5904e48> -> __default_139818164337072
            __default_139818164337072 = False

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'translations')}" (51:27)> braces_required=True translation=False at 7f29f404bba8> -> __attr_class
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

            # <Static value=<_ast.Dict object at 0x7f29f404bef0> name=None at 7f29f404bf28> -> __attrs_139818164338584
            __attrs_139818164338584 = _static_139818164338416

            # <a ... (52:20)
            # --------------------------------------------------------
            __append('<a')
            __append(' href="translations.html"')
            __append('>')

            # <Static value=<_ast.Dict object at 0x7f29f404b278> name=None at 7f29f404b208> -> __attrs_139818164618632
            __attrs_139818164618632 = _static_139818164335224

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

            # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164621264
            __attrs_139818164621264 = _static_139818165914032

            # <li ... (54:16)
            # --------------------------------------------------------
            __append('<li')
            __append('>')
            __append('\n                    ')

            # <Static value=<_ast.Dict object at 0x7f29f4090b70> name=None at 7f29f4090208> -> __attrs_139818164618072
            __attrs_139818164618072 = _static_139818164620144

            # <a ... (55:20)
            # --------------------------------------------------------
            __append('<a')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7f29f510e5c0> at 7f29f5904e48> -> __default_139818164617960
            __default_139818164617960 = False

            # <Interpolation value=<Substitution "${metadata['dev_thread_url']}" (55:29)> braces_required=True translation=False at 7f29f4090518> -> __attr_href
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

            # <Static value=<_ast.Dict object at 0x7f29f4090a90> name=None at 7f29f4090048> -> __attrs_139818164620704
            __attrs_139818164620704 = _static_139818164619920

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

            # <Static value=<_ast.Dict object at 0x7f29f4090cc0> name=None at 7f29f4090cf8> -> __attrs_139818164619080
            __attrs_139818164619080 = _static_139818164620480

            # <div ... (60:4)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="hero-unit subhead"')
            __append('>')
            __append('\n        ')

            # <Static value=<_ast.Dict object at 0x7f29f40b3518> name=None at 7f29f40b3400> -> __attrs_139818164763616
            __attrs_139818164763616 = _static_139818164761880

            # <script ... (61:8)
            # --------------------------------------------------------
            __append('<script')
            __append(' language="JavaScript"')
            __append('>')
            __append('\n        function random_img(){\n            var images=new Array("",\n                                 "");\n\n            var random_image=images[Math.floor(Math.random()*images.length)];\n            document.write(\'')

            # <Static value=<_ast.Dict object at 0x7f29f40b32b0> name=None at 7f29f40b3278> -> __attrs_139818164760984
            __attrs_139818164760984 = _static_139818164761264

            # <a ... (67:28)
            # --------------------------------------------------------
            __append('<a')
            __append(' href="ships.html#\' + random_image + \'"')
            __append('>')

            # <Static value=<_ast.Dict object at 0x7f29f40b3908> name=None at 7f29f40b3208> -> __attrs_139818164761656
            __attrs_139818164761656 = _static_139818164762888

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

            # <Static value=<_ast.Dict object at 0x7f29f40b3390> name=None at 7f29f40b3a20> -> __attrs_139818164762496
            __attrs_139818164762496 = _static_139818164761488

            # <div ... (71:8)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="container"')
            __append('>')
            __append('\n            ')

            # <Static value=<_ast.Dict object at 0x7f29f4082cc0> name=None at 7f29f40829e8> -> __attrs_139818164561232
            __attrs_139818164561232 = _static_139818164563136

            # <h1 ... (72:12)
            # --------------------------------------------------------
            __append('<h1')
            __append(' style="font-size:48px; padding-top:30px;"')
            __append('>')
            __append('Squid Ate FISH')
            __append('</h1>')
            __append('\n            ')

            # <Static value=<_ast.Dict object at 0x7f29f40824e0> name=None at 7f29f4082860> -> __attrs_139818164562856
            __attrs_139818164562856 = _static_139818164561120

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

            # <Static value=<_ast.Dict object at 0x7f29f4082048> name=None at 7f29f4082588> -> __attrs_139818164560840
            __attrs_139818164560840 = _static_139818164559944

            # <div ... (79:4)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="container"')
            __append('>')
            __append('\n        ')
            if (__slot_body is None):
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164776296
                __attrs_139818164776296 = _static_139818165914032

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

            # <Static value=<_ast.Dict object at 0x7f29f40b6fd0> name=None at 7f29f40b6400> -> __attrs_139818164773048
            __attrs_139818164773048 = _static_139818164776912

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

            # <Static value=<_ast.Dict object at 0x7f29f407f400> name=None at 7f29f407f668> -> __attrs_139818164548104
            __attrs_139818164548104 = _static_139818164548608

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