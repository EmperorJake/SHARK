# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/SHARK/src/docs_templates/main_template.pt'

__tokens = {1781: ("${doc_helper.get_active_nav(doc_name, 'get_started')}", 40, 27), 1783: ("doc_helper.get_active_nav(doc_name, 'get_started')", 40, 29), 1952: ("${doc_helper.get_active_nav(doc_name, 'ships')}", 43, 27), 1954: ("doc_helper.get_active_nav(doc_name, 'ships')", 43, 29), 2105: ("${doc_helper.get_active_nav(doc_name, 'code_reference')}", 46, 27), 2107: ("doc_helper.get_active_nav(doc_name, 'code_reference')", 46, 29), 2356: ("${doc_helper.get_active_nav(doc_name, 'translations')}", 51, 27), 2358: ("doc_helper.get_active_nav(doc_name, 'translations')", 51, 29), 2599: ("${metadata['dev_thread_url']}", 55, 29), 2601: ("metadata['dev_thread_url']", 55, 31)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140188662864336 = {'version': '1.0', 'encoding': 'iso-8859-1', }
_static_140188662454208 = {'style': 'margin-top:30px; text-align:center; color:#999; padding:5px; background-color:#eee; border-top:solid 1px #ddd; box-shadow: inset 0px 1px 1px #ddd', }
_static_140188662990496 = {'class': 'container', }
_static_140188662990640 = {'class': 'lead', }
_static_140188662990352 = {'style': 'font-size:48px; padding-top:30px;', }
_static_140188663567360 = {'class': 'container', }
_static_140188663568464 = {'class': 'pull-right', 'style': 'margin-top:-30px; margin-bottom:0;', 'src': "static/img/industries/'+ random_image +'.png", }
_static_140188663568608 = {'href': "ships.html#' + random_image + '", }
_static_140188661995888 = {'language': 'JavaScript', }
_static_140188661517088 = {'class': 'hero-unit subhead', }
_static_140188661995600 = {'class': 'icon-comment icon-white', }
_static_140188663698048 = {'href': "${metadata['dev_thread_url']}", }
_static_140188663700880 = {'class': 'icon-globe icon-white', }
_static_140188661518240 = {'href': 'translations.html', }
_static_140188661517040 = {'class': "${doc_helper.get_active_nav(doc_name, 'translations')}", }
_static_140188661515936 = {'class': 'nav navbar-nav pull-right', }
_static_140188664014400 = {'href': 'code_reference.html', }
_static_140188664016800 = {'class': "${doc_helper.get_active_nav(doc_name, 'code_reference')}", }
_static_140188664013392 = {'href': 'ships.html', }
_static_140188663575504 = {'class': "${doc_helper.get_active_nav(doc_name, 'ships')}", }
_static_140188663576752 = {'href': 'get_started.html', }
_static_140188663574592 = {'class': "${doc_helper.get_active_nav(doc_name, 'get_started')}", }
_static_140188663201696 = {'class': 'nav navbar-nav pull-left', }
_static_140188663200736 = {'class': 'container', }
_static_140188661450496 = {'class': 'navbar navbar-inverse navbar-static-top', 'style': 'margin-bottom:0; border-bottom:1px solid #000;', }
_static_140188661450448 = {'type': 'text/javascript', }
_static_140188663227632 = {'type': 'text/javascript', 'src': 'static/js/jquery.tablesorter.widgets.min.js', }
_static_140188663227248 = {'type': 'text/javascript', 'src': 'static/js/jquery.tablesorter.min.js', }
_static_140188663229312 = {'type': 'text/javascript', 'src': 'static/js/jquery.metadata.js', }
_static_140188662332240 = {'type': 'text/javascript', 'src': 'static/js/jquery-1.9.1.min.js', }
_static_140188662332960 = {'rel': 'stylesheet', 'href': 'static/font-awesome/css/font-awesome.min.css', }
_static_140188662330560 = {'type': 'text/css', 'href': 'static/css/style.css', 'rel': 'stylesheet', }
_static_140188664081280 = {'type': 'text/css', 'href': 'static/css/bootstrap-responsive.min.css', 'rel': 'stylesheet', }
_static_140188664081232 = {'type': 'text/css', 'href': 'static/css/bootstrap.min.css', 'rel': 'stylesheet', }
_static_140188664080608 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0', }
_static_140188662782704 = {'http-equiv': 'Content-Type', 'content': 'text/html; charset=iso-8859-1', }
_static_140188662325648 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'en', }
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

            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662328288
            __attrs_140188662328288 = _static_140188664645808
            __append('\r\n<!DOCTYPE html>\r\n')

            # <Static value=<_ast.Dict object at 0x7f80376b6190> name=None at 7f80376b6b80> -> __attrs_140188662781168
            __attrs_140188662781168 = _static_140188662325648

            # <html ... (4:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" lang="en">\r\n')

            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662783472
            __attrs_140188662783472 = _static_140188664645808

            # <head ... (5:0)
            # --------------------------------------------------------
            __append('<head>\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662783088
            __attrs_140188662783088 = _static_140188664645808

            # <title ... (6:4)
            # --------------------------------------------------------
            __append('<title >Squid Ate FISH</title>\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f8037725af0> name=None at 7f8037725a30> -> __attrs_140188662781648
            __attrs_140188662781648 = _static_140188662782704

            # <meta ... (7:4)
            # --------------------------------------------------------
            __append('<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />\r\n\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f80378628e0> name=None at 7f8037862310> -> __attrs_140188664082096
            __attrs_140188664082096 = _static_140188664080608

            # <meta ... (9:4)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f8037862b50> name=None at 7f8037862e20> -> __attrs_140188664082288
            __attrs_140188664082288 = _static_140188664081232

            # <link ... (10:4)
            # --------------------------------------------------------
            __append('<link type="text/css" href="static/css/bootstrap.min.css" rel="stylesheet">\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f8037862b80> name=None at 7f80378625b0> -> __attrs_140188662332432
            __attrs_140188662332432 = _static_140188664081280

            # <link ... (11:4)
            # --------------------------------------------------------
            __append('<link type="text/css" href="static/css/bootstrap-responsive.min.css" rel="stylesheet">\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f80376b74c0> name=None at 7f80376b7310> -> __attrs_140188662329984
            __attrs_140188662329984 = _static_140188662330560

            # <link ... (12:4)
            # --------------------------------------------------------
            __append('<link type="text/css" href="static/css/style.css" rel="stylesheet">\r\n\r\n    <!--Font Awesome-->\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f80376b7e20> name=None at 7f80376b7850> -> __attrs_140188662332384
            __attrs_140188662332384 = _static_140188662332960

            # <link ... (15:4)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" href="static/font-awesome/css/font-awesome.min.css" />\r\n    <!--/Font Awesome-->\r\n\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f80376b7b50> name=None at 7f80376b72b0> -> __attrs_140188663230128
            __attrs_140188663230128 = _static_140188662332240

            # <script ... (18:4)
            # --------------------------------------------------------
            __append('<script type="text/javascript" src="static/js/jquery-1.9.1.min.js"></script>\r\n\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f8037792b80> name=None at 7f8037792940> -> __attrs_140188663228304
            __attrs_140188663228304 = _static_140188663229312

            # <script ... (20:4)
            # --------------------------------------------------------
            __append('<script type="text/javascript" src="static/js/jquery.metadata.js"></script>\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f8037792370> name=None at 7f8037792ac0> -> __attrs_140188663229216
            __attrs_140188663229216 = _static_140188663227248

            # <script ... (21:4)
            # --------------------------------------------------------
            __append('<script type="text/javascript" src="static/js/jquery.tablesorter.min.js"></script>\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f80377924f0> name=None at 7f8037792850> -> __attrs_140188661449632
            __attrs_140188661449632 = _static_140188663227632

            # <script ... (22:4)
            # --------------------------------------------------------
            __append('<script type="text/javascript" src="static/js/jquery.tablesorter.widgets.min.js"></script>\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f80375e06d0> name=None at 7f80375e0160> -> __attrs_140188661448768
            __attrs_140188661448768 = _static_140188661450448

            # <script ... (23:4)
            # --------------------------------------------------------
            __append('<script type="text/javascript">\r\n        $(document).ready(function(){\r\n            $(\'.tablesorter\').tablesorter({\r\n                textExtraction: function(node){\r\n                            var cell_value = $(node).text();\r\n                            var sort_value = $(node).data(\'value\');\r\n                    return (sort_value != undefined) ? sort_value : cell_value;\r\n                 },\r\n            })\r\n        })\r\n    </script>\r\n</head>\r\n\r\n')

            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188661450304
            __attrs_140188661450304 = _static_140188664645808

            # <body ... (36:0)
            # --------------------------------------------------------
            __append('<body>\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f80375e0700> name=None at 7f80375e0730> -> __attrs_140188663200640
            __attrs_140188663200640 = _static_140188661450496

            # <div ... (37:4)
            # --------------------------------------------------------
            __append('<div class="navbar navbar-inverse navbar-static-top" style="margin-bottom:0; border-bottom:1px solid #000;">\r\n        ')

            # <Static value=<_ast.Dict object at 0x7f803778bbe0> name=None at 7f803778b520> -> __attrs_140188663201648
            __attrs_140188663201648 = _static_140188663200736

            # <div ... (38:8)
            # --------------------------------------------------------
            __append('<div class="container">\r\n            ')

            # <Static value=<_ast.Dict object at 0x7f803778bfa0> name=None at 7f803778bd30> -> __attrs_140188663200256
            __attrs_140188663200256 = _static_140188663201696

            # <ul ... (39:12)
            # --------------------------------------------------------
            __append('<ul class="nav navbar-nav pull-left">\r\n                ')

            # <Static value=<_ast.Dict object at 0x7f80377e7040> name=None at 7f80377e7070> -> __attrs_140188663576176
            __attrs_140188663576176 = _static_140188663574592

            # <li ... (40:16)
            # --------------------------------------------------------
            __append('<li')

            # <Symbol value=<DEFAULT> at 7f80381860a0> -> __default_140188663576512
            __default_140188663576512 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'get_started')}" (40:27)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f80377e7c10> -> __attr_class
            __token = 1781
            __token = 1783
            __attr_class = _lookup_attr(getitem('doc_helper'), 'get_active_nav')(getitem('doc_name'), 'get_started')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = __attr_class
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is _DEFAULT_MARKER):
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
            __append('>\r\n                    ')

            # <Static value=<_ast.Dict object at 0x7f80377e78b0> name=None at 7f80377e75b0> -> __attrs_140188663577328
            __attrs_140188663577328 = _static_140188663576752

            # <a ... (41:20)
            # --------------------------------------------------------
            __append('<a href="get_started.html">Get Started</a>\r\n                </li>\r\n                ')

            # <Static value=<_ast.Dict object at 0x7f80377e73d0> name=None at 7f80377e7760> -> __attrs_140188663575936
            __attrs_140188663575936 = _static_140188663575504

            # <li ... (43:16)
            # --------------------------------------------------------
            __append('<li')

            # <Symbol value=<DEFAULT> at 7f80381860a0> -> __default_140188663577712
            __default_140188663577712 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'ships')}" (43:27)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f80377e7d30> -> __attr_class
            __token = 1952
            __token = 1954
            __attr_class = _lookup_attr(getitem('doc_helper'), 'get_active_nav')(getitem('doc_name'), 'ships')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = __attr_class
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is _DEFAULT_MARKER):
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
            __append('>\r\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8037852250> name=None at 7f8037852fd0> -> __attrs_140188664013680
            __attrs_140188664013680 = _static_140188664013392

            # <a ... (44:20)
            # --------------------------------------------------------
            __append('<a href="ships.html">Ships</a>\r\n                </li>\r\n                ')

            # <Static value=<_ast.Dict object at 0x7f8037852fa0> name=None at 7f8037852e50> -> __attrs_140188664013296
            __attrs_140188664013296 = _static_140188664016800

            # <li ... (46:16)
            # --------------------------------------------------------
            __append('<li')

            # <Symbol value=<DEFAULT> at 7f80381860a0> -> __default_140188664016272
            __default_140188664016272 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'code_reference')}" (46:27)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f8037852970> -> __attr_class
            __token = 2105
            __token = 2107
            __attr_class = _lookup_attr(getitem('doc_helper'), 'get_active_nav')(getitem('doc_name'), 'code_reference')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = __attr_class
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is _DEFAULT_MARKER):
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
            __append('>\r\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8037852640> name=None at 7f80378528e0> -> __attrs_140188661516176
            __attrs_140188661516176 = _static_140188664014400

            # <a ... (47:20)
            # --------------------------------------------------------
            __append('<a href="code_reference.html">Code Reference</a>\r\n                </li>\r\n            </ul>\r\n            ')

            # <Static value=<_ast.Dict object at 0x7f80375f06a0> name=None at 7f80375f01f0> -> __attrs_140188661515216
            __attrs_140188661515216 = _static_140188661515936

            # <ul ... (50:12)
            # --------------------------------------------------------
            __append('<ul class="nav navbar-nav pull-right">\r\n                ')

            # <Static value=<_ast.Dict object at 0x7f80375f0af0> name=None at 7f80375f0970> -> __attrs_140188661516752
            __attrs_140188661516752 = _static_140188661517040

            # <li ... (51:16)
            # --------------------------------------------------------
            __append('<li')

            # <Symbol value=<DEFAULT> at 7f80381860a0> -> __default_140188661515072
            __default_140188661515072 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "${doc_helper.get_active_nav(doc_name, 'translations')}" (51:27)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f80375f0a30> -> __attr_class
            __token = 2356
            __token = 2358
            __attr_class = _lookup_attr(getitem('doc_helper'), 'get_active_nav')(getitem('doc_name'), 'translations')
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = __attr_class
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is _DEFAULT_MARKER):
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
            __append('>\r\n                    ')

            # <Static value=<_ast.Dict object at 0x7f80375f0fa0> name=None at 7f80375f0b50> -> __attrs_140188663700352
            __attrs_140188663700352 = _static_140188661518240

            # <a ... (52:20)
            # --------------------------------------------------------
            __append('<a href="translations.html">')

            # <Static value=<_ast.Dict object at 0x7f8037805d90> name=None at 7f8037805670> -> __attrs_140188663699488
            __attrs_140188663699488 = _static_140188663700880

            # <i ... (52:48)
            # --------------------------------------------------------
            __append('<i class="icon-globe icon-white"></i> Help Translate FISH</a>\r\n                </li>\r\n                ')

            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663698192
            __attrs_140188663698192 = _static_140188664645808

            # <li ... (54:16)
            # --------------------------------------------------------
            __append('<li>\r\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8037805280> name=None at 7f8037805e20> -> __attrs_140188661994496
            __attrs_140188661994496 = _static_140188663698048

            # <a ... (55:20)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7f80381860a0> -> __default_140188663697760
            __default_140188663697760 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "${metadata['dev_thread_url']}" (55:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f8037805bb0> -> __attr_href
            __token = 2599
            __token = 2601
            __attr_href = getitem('metadata')['dev_thread_url']
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = __attr_href
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is _DEFAULT_MARKER):
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

            # <Static value=<_ast.Dict object at 0x7f8037665850> name=None at 7f80376653d0> -> __attrs_140188661995936
            __attrs_140188661995936 = _static_140188661995600

            # <i ... (55:60)
            # --------------------------------------------------------
            __append('<i class="icon-comment icon-white"></i> Discuss at TT-Forums.net</a>\r\n                </li>\r\n            </ul>\r\n        </div>\r\n    </div>\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f80375f0b20> name=None at 7f80375f0c10> -> __attrs_140188661994592
            __attrs_140188661994592 = _static_140188661517088

            # <div ... (60:4)
            # --------------------------------------------------------
            __append('<div class="hero-unit subhead">\r\n        ')

            # <Static value=<_ast.Dict object at 0x7f8037665970> name=None at 7f8037665c10> -> __attrs_140188661995792
            __attrs_140188661995792 = _static_140188661995888

            # <script ... (61:8)
            # --------------------------------------------------------
            __append('<script language="JavaScript">\r\n        function random_img(){\r\n            var images=new Array("",\r\n                                 "");\r\n\r\n            var random_image=images[Math.floor(Math.random()*images.length)];\r\n            document.write(\'')

            # <Static value=<_ast.Dict object at 0x7f80377e58e0> name=None at 7f80377e52e0> -> __attrs_140188663567984
            __attrs_140188663567984 = _static_140188663568608

            # <a ... (67:28)
            # --------------------------------------------------------
            __append('<a href="ships.html#\' + random_image + \'">')

            # <Static value=<_ast.Dict object at 0x7f80377e5850> name=None at 7f80377e5970> -> __attrs_140188663569856
            __attrs_140188663569856 = _static_140188663568464

            # <img ... (67:70)
            # --------------------------------------------------------
            __append('<img class="pull-right" style="margin-top:-30px; margin-bottom:0;" src="static/img/industries/\'+ random_image +\'.png"></a>\')\r\n        }\r\n        random_img()\r\n        </script>\r\n        ')

            # <Static value=<_ast.Dict object at 0x7f80377e5400> name=None at 7f80377e5940> -> __attrs_140188662989056
            __attrs_140188662989056 = _static_140188663567360

            # <div ... (71:8)
            # --------------------------------------------------------
            __append('<div class="container">\r\n            ')

            # <Static value=<_ast.Dict object at 0x7f8037758610> name=None at 7f8037758640> -> __attrs_140188662989104
            __attrs_140188662989104 = _static_140188662990352

            # <h1 ... (72:12)
            # --------------------------------------------------------
            __append('<h1 style="font-size:48px; padding-top:30px;">Squid Ate FISH</h1>\r\n            ')

            # <Static value=<_ast.Dict object at 0x7f8037758730> name=None at 7f8037758eb0> -> __attrs_140188662992848
            __attrs_140188662992848 = _static_140188662990640

            # <p ... (73:12)
            # --------------------------------------------------------
            __append('<p class="lead">New Ships for OpenTTD</p>\r\n        </div>\r\n    </div>\r\n    ')
            if (__slot_opt_page_header is None):

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662990880
                __attrs_140188662990880 = _static_140188664645808
                __append('\r\n        \r\n    ')
            else:
                __slot_opt_page_header(__stream, econtext.copy(), rcontext)
            __append('\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f80377586a0> name=None at 7f80377586d0> -> __attrs_140188662453296
            __attrs_140188662453296 = _static_140188662990496

            # <div ... (79:4)
            # --------------------------------------------------------
            __append('<div class="container">\r\n        ')
            if (__slot_body is None):

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662453584
                __attrs_140188662453584 = _static_140188664645808
                __append('\r\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662455936
                __attrs_140188662455936 = _static_140188664645808

                # <p ... (81:12)
                # --------------------------------------------------------
                __append('<p>Ooooops - there is no content for some reason. Something has probably gone nuts in the build. </p>\r\n        ')
            else:
                __slot_body(__stream, econtext.copy(), rcontext)
            __append('\r\n    </div>\r\n    ')

            # <Static value=<_ast.Dict object at 0x7f80376d57c0> name=None at 7f80376d5400> -> __attrs_140188662454928
            __attrs_140188662454928 = _static_140188662454208

            # <div ... (84:4)
            # --------------------------------------------------------
            __append('<div style="margin-top:30px; text-align:center; color:#999; padding:5px; background-color:#eee; border-top:solid 1px #ddd; box-shadow: inset 0px 1px 1px #ddd">\r\n        Squid Ate FISH, with thanks to all who helped\r\n    </div>\r\n</body>\r\n</html>\r\n')
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

            # <Static value=<_ast.Dict object at 0x7f80377399d0> name=None at 7f80377390a0> -> __attrs_140188662328384
            __attrs_140188662328384 = _static_140188662864336

            # <?xml ... (1:0)
            # --------------------------------------------------------
            __append('<?xml version="1.0" encoding="iso-8859-1"?>\r\n')
            __token = None
            render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render': render, }