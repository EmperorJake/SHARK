# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/docs_templates/main_template.pt'
__tokens = {1742: ("${doc_helper.get_active_nav(doc_name, 'get_started')}", 40, 27), 1744: ("doc_helper.get_active_nav(doc_name, 'get_started')", 40, 29), 1910: ("${doc_helper.get_active_nav(doc_name, 'ships')}", 43, 27), 1912: ("doc_helper.get_active_nav(doc_name, 'ships')", 43, 29), 2060: ("${doc_helper.get_active_nav(doc_name, 'code_reference')}", 46, 27), 2062: ("doc_helper.get_active_nav(doc_name, 'code_reference')", 46, 29), 2306: ("${doc_helper.get_active_nav(doc_name, 'translations')}", 51, 27), 2308: ("doc_helper.get_active_nav(doc_name, 'translations')", 51, 29), 2545: ("${metadata['dev_thread_url']}", 55, 29), 2547: ("metadata['dev_thread_url']", 55, 31)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_139628048580848 = {'version': '1.0', 'encoding': 'iso-8859-1', }
_static_139628048315952 = {'style': 'margin-top:30px; text-align:center; color:#999; padding:5px; background-color:#eee; border-top:solid 1px #ddd; box-shadow: inset 0px 1px 1px #ddd', }
_static_139628048198960 = {'class': 'container', }
_static_139628048197448 = {'class': 'lead', }
_static_139628048195880 = {'style': 'font-size:48px; padding-top:30px;', }
_static_139628048301472 = {'class': 'container', }
_static_139628048300520 = {'class': 'pull-right', 'style': 'margin-top:-30px; margin-bottom:0;', 'src': "static/img/industries/'+ random_image +'.png", }
_static_139628048298896 = {'href': "ships.html#' + random_image + '", }
_static_139628048298280 = {'language': 'JavaScript', }
_static_139628048116704 = {'class': 'hero-unit subhead', }
_static_139628048116648 = {'class': 'icon-comment icon-white', }
_static_139628048115472 = {'href': "${metadata['dev_thread_url']}", }
_static_139628049588008 = {'class': 'icon-globe icon-white', }
_static_139628049585040 = {'href': 'translations.html', }
_static_139628049586608 = {'class': "${doc_helper.get_active_nav(doc_name, 'translations')}", }
_static_139628049585544 = {'class': 'nav navbar-nav pull-right', }
_static_139628049436856 = {'href': 'code_reference.html', }
_static_139628049438480 = {'class': "${doc_helper.get_active_nav(doc_name, 'code_reference')}", }
_static_139628049439768 = {'href': 'ships.html', }
_static_139628049438200 = {'class': "${doc_helper.get_active_nav(doc_name, 'ships')}", }
_static_139628049473264 = {'href': 'get_started.html', }
_static_139628049471192 = {'class': "${doc_helper.get_active_nav(doc_name, 'get_started')}", }
_static_139628049469960 = {'class': 'nav navbar-nav pull-left', }
_static_139628049510240 = {'class': 'container', }
_static_139628049507776 = {'class': 'navbar navbar-inverse navbar-static-top', 'style': 'margin-bottom:0; border-bottom:1px solid #000;', }
_static_139628049508840 = {'type': 'text/javascript', }
_static_139628049509960 = {'type': 'text/javascript', 'src': 'static/js/jquery.tablesorter.widgets.min.js', }
_static_139628049643840 = {'type': 'text/javascript', 'src': 'static/js/jquery.tablesorter.min.js', }
_static_139628049643448 = {'type': 'text/javascript', 'src': 'static/js/jquery.metadata.js', }
_static_139628049641992 = {'type': 'text/javascript', 'src': 'static/js/jquery-1.9.1.min.js', }
_static_139628048592680 = {'rel': 'stylesheet', 'href': 'static/font-awesome/css/font-awesome.min.css', }
_static_139628048590888 = {'type': 'text/css', 'href': 'static/css/style.css', 'rel': 'stylesheet', }
_static_139628048589824 = {'type': 'text/css', 'href': 'static/css/bootstrap-responsive.min.css', 'rel': 'stylesheet', }
_static_139628048507288 = {'type': 'text/css', 'href': 'static/css/bootstrap.min.css', 'rel': 'stylesheet', }
_static_139628048509416 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0', }
_static_139628048508632 = {'http-equiv': 'Content-Type', 'content': 'text/html; charset=iso-8859-1', }
_static_139628050453112 = {}
_static_139628048428448 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'en', }

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

            # <Static value=<_ast.Dict object at 0x7efdb03a2da0> name=None at 7efdb03a2dd8> -> __attrs_139628048428952
            __attrs_139628048428952 = _static_139628048428448

            # <html ... (4:0)
            # --------------------------------------------------------
            __append('<html')
            __append(' xmlns="http://www.w3.org/1999/xhtml"')
            __append(' lang="en"')
            __append('>')
            __append('\n')

            # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048508352
            __attrs_139628048508352 = _static_139628050453112

            # <head ... (5:0)
            # --------------------------------------------------------
            __append('<head')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048508128
            __attrs_139628048508128 = _static_139628050453112

            # <title ... (6:4)
            # --------------------------------------------------------
            __append('<title')
            __append(' >')
            __append('Squid Ate FISH')
            __append('</title>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7efdb03b66d8> name=None at 7efdb03b65f8> -> __attrs_139628048509640
            __attrs_139628048509640 = _static_139628048508632

            # <meta ... (7:4)
            # --------------------------------------------------------
            __append('<meta')
            __append(' http-equiv="Content-Type"')
            __append(' content="text/html; charset=iso-8859-1"')
            __append(' />')
            __append('\n\n    ')

            # <Static value=<_ast.Dict object at 0x7efdb03b69e8> name=None at 7efdb03b6b70> -> __attrs_139628048510536
            __attrs_139628048510536 = _static_139628048509416

            # <meta ... (9:4)
            # --------------------------------------------------------
            __append('<meta')
            __append(' name="viewport"')
            __append(' content="width=device-width, initial-scale=1.0"')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7efdb03b6198> name=None at 7efdb03b6f60> -> __attrs_139628048589208
            __attrs_139628048589208 = _static_139628048507288

            # <link ... (10:4)
            # --------------------------------------------------------
            __append('<link')
            __append(' type="text/css"')
            __append(' href="static/css/bootstrap.min.css"')
            __append(' rel="stylesheet"')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7efdb03ca400> name=None at 7efdb03ca0f0> -> __attrs_139628048590160
            __attrs_139628048590160 = _static_139628048589824

            # <link ... (11:4)
            # --------------------------------------------------------
            __append('<link')
            __append(' type="text/css"')
            __append(' href="static/css/bootstrap-responsive.min.css"')
            __append(' rel="stylesheet"')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7efdb03ca828> name=None at 7efdb03ca710> -> __attrs_139628048592120
            __attrs_139628048592120 = _static_139628048590888

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

            # <Static value=<_ast.Dict object at 0x7efdb03caf28> name=None at 7efdb03cadd8> -> __attrs_139628049641544
            __attrs_139628049641544 = _static_139628048592680

            # <link ... (15:4)
            # --------------------------------------------------------
            __append('<link')
            __append(' rel="stylesheet"')
            __append(' href="static/font-awesome/css/font-awesome.min.css"')
            __append(' />')
            __append('\n    ')
            __append('<!--/Font Awesome-->')
            __append('\n\n    ')

            # <Static value=<_ast.Dict object at 0x7efdb04cb208> name=None at 7efdb04cb240> -> __attrs_139628049642888
            __attrs_139628049642888 = _static_139628049641992

            # <script ... (18:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append(' src="static/js/jquery-1.9.1.min.js"')
            __append('>')
            __append('</script>')
            __append('\n\n    ')

            # <Static value=<_ast.Dict object at 0x7efdb04cb7b8> name=None at 7efdb04cb5f8> -> __attrs_139628049644848
            __attrs_139628049644848 = _static_139628049643448

            # <script ... (20:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append(' src="static/js/jquery.metadata.js"')
            __append('>')
            __append('</script>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7efdb04cb940> name=None at 7efdb04cbb38> -> __attrs_139628049645408
            __attrs_139628049645408 = _static_139628049643840

            # <script ... (21:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append(' src="static/js/jquery.tablesorter.min.js"')
            __append('>')
            __append('</script>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7efdb04aae48> name=None at 7efdb04aae10> -> __attrs_139628049509680
            __attrs_139628049509680 = _static_139628049509960

            # <script ... (22:4)
            # --------------------------------------------------------
            __append('<script')
            __append(' type="text/javascript"')
            __append(' src="static/js/jquery.tablesorter.widgets.min.js"')
            __append('>')
            __append('</script>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7efdb04aa9e8> name=None at 7efdb04aaa58> -> __attrs_139628049509288
            __attrs_139628049509288 = _static_139628049508840

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

            # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049508336
            __attrs_139628049508336 = _static_139628050453112

            # <body ... (36:0)
            # --------------------------------------------------------
            __append('<body')
            __append('>')
            __append('\n    ')

            # <Static value=<_ast.Dict object at 0x7efdb04aa5c0> name=None at 7efdb04aa5f8> -> __attrs_139628049507216
            __attrs_139628049507216 = _static_139628049507776

            # <div ... (37:4)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="navbar navbar-inverse navbar-static-top"')
            __append(' style="margin-bottom:0; border-bottom:1px solid #000;"')
            __append('>')
            __append('\n        ')

            # <Static value=<_ast.Dict object at 0x7efdb04aaf60> name=None at 7efdb04aaf28> -> __attrs_139628049471360
            __attrs_139628049471360 = _static_139628049510240

            # <div ... (38:8)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="container"')
            __append('>')
            __append('\n            ')

            # <Static value=<_ast.Dict object at 0x7efdb04a1208> name=None at 7efdb04a12b0> -> __attrs_139628049470296
            __attrs_139628049470296 = _static_139628049469960

            # <ul ... (39:12)
            # --------------------------------------------------------
            __append('<ul')
            __append(' class="nav navbar-nav pull-left"')
            __append('>')
            __append('\n                ')

            # <Static value=<_ast.Dict object at 0x7efdb04a16d8> name=None at 7efdb04a1588> -> __attrs_139628049471752
            __attrs_139628049471752 = _static_139628049471192

            # <li ... (40:16)
            # --------------------------------------------------------
            __append('<li')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7efdb14d64e0> at 7efdb03c8b00> -> __default_139628049472424
            __default_139628049472424 = False

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'get_started')}" (40:27)> braces_required=True translation=False at 7efdb04a1be0> -> __attr_class
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

            # <Static value=<_ast.Dict object at 0x7efdb04a1ef0> name=None at 7efdb04a1e48> -> __attrs_139628049440552
            __attrs_139628049440552 = _static_139628049473264

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

            # <Static value=<_ast.Dict object at 0x7efdb04995f8> name=None at 7efdb0499198> -> __attrs_139628049439376
            __attrs_139628049439376 = _static_139628049438200

            # <li ... (43:16)
            # --------------------------------------------------------
            __append('<li')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7efdb14d64e0> at 7efdb03c8b00> -> __default_139628049439208
            __default_139628049439208 = False

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'ships')}" (43:27)> braces_required=True translation=False at 7efdb0499dd8> -> __attr_class
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

            # <Static value=<_ast.Dict object at 0x7efdb0499c18> name=None at 7efdb0499cf8> -> __attrs_139628049438760
            __attrs_139628049438760 = _static_139628049439768

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

            # <Static value=<_ast.Dict object at 0x7efdb0499710> name=None at 7efdb0499780> -> __attrs_139628049437472
            __attrs_139628049437472 = _static_139628049438480

            # <li ... (46:16)
            # --------------------------------------------------------
            __append('<li')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7efdb14d64e0> at 7efdb03c8b00> -> __default_139628049438088
            __default_139628049438088 = False

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'code_reference')}" (46:27)> braces_required=True translation=False at 7efdb04995c0> -> __attr_class
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

            # <Static value=<_ast.Dict object at 0x7efdb04990b8> name=None at 7efdb0499470> -> __attrs_139628049584928
            __attrs_139628049584928 = _static_139628049436856

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

            # <Static value=<_ast.Dict object at 0x7efdb04bd588> name=None at 7efdb04bd4a8> -> __attrs_139628049584256
            __attrs_139628049584256 = _static_139628049585544

            # <ul ... (50:12)
            # --------------------------------------------------------
            __append('<ul')
            __append(' class="nav navbar-nav pull-right"')
            __append('>')
            __append('\n                ')

            # <Static value=<_ast.Dict object at 0x7efdb04bd9b0> name=None at 7efdb04bdb70> -> __attrs_139628049585936
            __attrs_139628049585936 = _static_139628049586608

            # <li ... (51:16)
            # --------------------------------------------------------
            __append('<li')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7efdb14d64e0> at 7efdb03c8b00> -> __default_139628049585432
            __default_139628049585432 = False

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'translations')}" (51:27)> braces_required=True translation=False at 7efdb04bd5c0> -> __attr_class
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

            # <Static value=<_ast.Dict object at 0x7efdb04bd390> name=None at 7efdb04bd438> -> __attrs_139628049587784
            __attrs_139628049587784 = _static_139628049585040

            # <a ... (52:20)
            # --------------------------------------------------------
            __append('<a')
            __append(' href="translations.html"')
            __append('>')

            # <Static value=<_ast.Dict object at 0x7efdb04bdf28> name=None at 7efdb04bdf60> -> __attrs_139628048114408
            __attrs_139628048114408 = _static_139628049588008

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

            # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048116480
            __attrs_139628048116480 = _static_139628050453112

            # <li ... (54:16)
            # --------------------------------------------------------
            __append('<li')
            __append('>')
            __append('\n                    ')

            # <Static value=<_ast.Dict object at 0x7efdb0356710> name=None at 7efdb03565f8> -> __attrs_139628048116088
            __attrs_139628048116088 = _static_139628048115472

            # <a ... (55:20)
            # --------------------------------------------------------
            __append('<a')

            # <Builtin id='False' ctx=<_ast.Load object at 0x7efdb14d64e0> at 7efdb03c8b00> -> __default_139628048114688
            __default_139628048114688 = False

            # <Interpolation value=<Substitution "${metadata['dev_thread_url']}" (55:29)> braces_required=True translation=False at 7efdb0356588> -> __attr_href
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

            # <Static value=<_ast.Dict object at 0x7efdb0356ba8> name=None at 7efdb03569e8> -> __attrs_139628048117096
            __attrs_139628048117096 = _static_139628048116648

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

            # <Static value=<_ast.Dict object at 0x7efdb0356be0> name=None at 7efdb0356cc0> -> __attrs_139628048117544
            __attrs_139628048117544 = _static_139628048116704

            # <div ... (60:4)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="hero-unit subhead"')
            __append('>')
            __append('\n        ')

            # <Static value=<_ast.Dict object at 0x7efdb0383128> name=None at 7efdb03830f0> -> __attrs_139628048298952
            __attrs_139628048298952 = _static_139628048298280

            # <script ... (61:8)
            # --------------------------------------------------------
            __append('<script')
            __append(' language="JavaScript"')
            __append('>')
            __append('\n        function random_img(){\n            var images=new Array("",\n                                 "");\n\n            var random_image=images[Math.floor(Math.random()*images.length)];\n            document.write(\'')

            # <Static value=<_ast.Dict object at 0x7efdb0383390> name=None at 7efdb03834e0> -> __attrs_139628048299344
            __attrs_139628048299344 = _static_139628048298896

            # <a ... (67:28)
            # --------------------------------------------------------
            __append('<a')
            __append(' href="ships.html#\' + random_image + \'"')
            __append('>')

            # <Static value=<_ast.Dict object at 0x7efdb03839e8> name=None at 7efdb03838d0> -> __attrs_139628048301360
            __attrs_139628048301360 = _static_139628048300520

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

            # <Static value=<_ast.Dict object at 0x7efdb0383da0> name=None at 7efdb0383cc0> -> __attrs_139628048300968
            __attrs_139628048300968 = _static_139628048301472

            # <div ... (71:8)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="container"')
            __append('>')
            __append('\n            ')

            # <Static value=<_ast.Dict object at 0x7efdb036a128> name=None at 7efdb036a0f0> -> __attrs_139628048195768
            __attrs_139628048195768 = _static_139628048195880

            # <h1 ... (72:12)
            # --------------------------------------------------------
            __append('<h1')
            __append(' style="font-size:48px; padding-top:30px;"')
            __append('>')
            __append('Squid Ate FISH')
            __append('</h1>')
            __append('\n            ')

            # <Static value=<_ast.Dict object at 0x7efdb036a748> name=None at 7efdb036a6a0> -> __attrs_139628048198176
            __attrs_139628048198176 = _static_139628048197448

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

            # <Static value=<_ast.Dict object at 0x7efdb036ad30> name=None at 7efdb036aba8> -> __attrs_139628048199464
            __attrs_139628048199464 = _static_139628048198960

            # <div ... (79:4)
            # --------------------------------------------------------
            __append('<div')
            __append(' class="container"')
            __append('>')
            __append('\n        ')
            if (__slot_body is None):
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048315392
                __attrs_139628048315392 = _static_139628050453112

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

            # <Static value=<_ast.Dict object at 0x7efdb0387630> name=None at 7efdb0387278> -> __attrs_139628048316960
            __attrs_139628048316960 = _static_139628048315952

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

            # <Static value=<_ast.Dict object at 0x7efdb03c80f0> name=None at 7efdb03c87b8> -> __attrs_139628048581128
            __attrs_139628048581128 = _static_139628048580848

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