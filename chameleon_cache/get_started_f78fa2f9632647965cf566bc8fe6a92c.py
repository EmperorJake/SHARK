# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/SHARK/src/docs_templates/get_started.pt'

__tokens = {855: ("Intro dates ${metadata['dates'][0]}-${metadata['dates'][1]}", 16, 59), 869: ("metadata['dates'][0]", 16, 73), 893: ("metadata['dates'][1]", 16, 97), 3077: ("${metadata['repo_url']}", 46, 67), 3079: ("metadata['repo_url']", 46, 69), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140188662441008 = {'href': 'changelog.html', }
_static_140188662331712 = {'class': 'lead', }
_static_140188662332288 = {'id': 'fish-changes', }
_static_140188663569568 = {'class': 'btn btn-large btn-default', 'href': 'code_reference.html', }
_static_140188661388816 = {'class': 'btn btn-large btn-primary', 'href': 'ships.html', }
_static_140188661391312 = {'class': 'lead', }
_static_140188661390976 = {'id': 'what-next', }
_static_140188662633136 = {'class': 'lead', }
_static_140188664092800 = {'id': 'setting-up', }
_static_140188662899280 = {'class': 'btn btn-default btn-block', 'href': "${metadata['repo_url']}", }
_static_140188662899520 = {'href': 'code_reference.html', }
_static_140188661971408 = {'class': 'col-sm-4', }
_static_140188661972032 = {'class': 'btn btn-info btn-block', 'href': 'http://bundles.openttdcoop.org/fish/releases/LATEST/', }
_static_140188661971648 = {'href': 'http://wiki.openttd.org/Newgrf#Manual_install', }
_static_140188661548944 = {'class': 'col-sm-4', }
_static_140188663377584 = {'class': 'btn btn-primary btn-block', 'href': 'http://wiki.openttd.org/Content_downloading', }
_static_140188662342992 = {'class': 'col-sm-4', }
_static_140188662345392 = {'class': 'row', }
_static_140188662343952 = {'class': 'lead', }
_static_140188663215440 = {'id': 'download-fish', }
_static_140188663216784 = {'class': 'fa fa-check-circle', }
_static_140188660932128 = {'class': 'fa fa-check-circle', }
_static_140188660929296 = {'class': 'fa fa-check-circle', }
_static_140188663599936 = {'class': 'fa fa-check-circle', }
_static_140188663601520 = {'class': 'fa fa-check-circle', }
_static_140188662639776 = {'class': 'fa fa-check-circle', }
_static_140188662637712 = {'class': 'fa fa-check-circle', }
_static_140188664080032 = {'class': 'fa fa-check-circle', }
_static_140188664081184 = {'class': 'list-inline', }
_static_140188661516416 = {'class': 'page-header', }
_static_140188661515552 = {'class': 'col-md-9', }
_static_140188661517040 = {'href': '#fish-changes', }
_static_140188662992512 = {'class': 'list-group-item', }
_static_140188662992848 = {'href': '#what-next', }
_static_140188662992176 = {'class': 'list-group-item', }
_static_140188663700784 = {'href': '#setting-up', }
_static_140188663697760 = {'class': 'list-group-item', }
_static_140188663700976 = {'href': '#download-fish', }
_static_140188661995552 = {'class': 'list-group-item', }
_static_140188661997328 = {'class': 'list-group', 'style': 'margin-top:35px;', }
_static_140188661993728 = {'class': 'col-md-3', }
_static_140188663199344 = {'class': 'row', }
_static_140188663200688 = 'load:main_template.pt'
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

            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663198960
            __attrs_140188663198960 = _static_140188664645808
            __backup_macroname_140188664101440 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f803778bbb0> name=None at 7f803778b6a0> -> __value
            __value = _static_140188663200688
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663200496
                __attrs_140188663200496 = _static_140188664645808
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f803778b670> name=None at 7f803778b4c0> -> __attrs_140188663199680
                __attrs_140188663199680 = _static_140188663199344

                # <div ... (3:4)
                # --------------------------------------------------------
                __append('<div class="row">\n        ')

                # <Static value=<_ast.Dict object at 0x7f8037665100> name=None at 7f80376653d0> -> __attrs_140188661997472
                __attrs_140188661997472 = _static_140188661993728

                # <div ... (4:8)
                # --------------------------------------------------------
                __append('<div class="col-md-3">\n            ')

                # <Static value=<_ast.Dict object at 0x7f8037665f10> name=None at 7f8037665f70> -> __attrs_140188661994640
                __attrs_140188661994640 = _static_140188661997328

                # <ul ... (5:12)
                # --------------------------------------------------------
                __append('<ul class="list-group" style="margin-top:35px;">\n                ')

                # <Static value=<_ast.Dict object at 0x7f8037665820> name=None at 7f8037665340> -> __attrs_140188663697904
                __attrs_140188663697904 = _static_140188661995552

                # <li ... (6:16)
                # --------------------------------------------------------
                __append('<li class="list-group-item">')

                # <Static value=<_ast.Dict object at 0x7f8037805df0> name=None at 7f8037805400> -> __attrs_140188663698864
                __attrs_140188663698864 = _static_140188663700976

                # <a ... (6:44)
                # --------------------------------------------------------
                __append('<a href="#download-fish">Download Squid Ate FISH</a></li>\n                ')

                # <Static value=<_ast.Dict object at 0x7f8037805160> name=None at 7f8037805730> -> __attrs_140188663699584
                __attrs_140188663699584 = _static_140188663697760

                # <li ... (7:16)
                # --------------------------------------------------------
                __append('<li class="list-group-item">')

                # <Static value=<_ast.Dict object at 0x7f8037805d30> name=None at 7f8037805700> -> __attrs_140188662991072
                __attrs_140188662991072 = _static_140188663700784

                # <a ... (7:44)
                # --------------------------------------------------------
                __append('<a href="#setting-up">Setting up a Game with Squid Ate FISH</a></li>\n                ')

                # <Static value=<_ast.Dict object at 0x7f8037758d30> name=None at 7f8037758610> -> __attrs_140188662989200
                __attrs_140188662989200 = _static_140188662992176

                # <li ... (8:16)
                # --------------------------------------------------------
                __append('<li class="list-group-item">')

                # <Static value=<_ast.Dict object at 0x7f8037758fd0> name=None at 7f8037758a00> -> __attrs_140188662992128
                __attrs_140188662992128 = _static_140188662992848

                # <a ... (8:44)
                # --------------------------------------------------------
                __append('<a href="#what-next">What Next?</a></li>\n                ')

                # <Static value=<_ast.Dict object at 0x7f8037758e80> name=None at 7f8037758f10> -> __attrs_140188662991840
                __attrs_140188662991840 = _static_140188662992512

                # <li ... (9:16)
                # --------------------------------------------------------
                __append('<li class="list-group-item">')

                # <Static value=<_ast.Dict object at 0x7f80375f0af0> name=None at 7f80375f0310> -> __attrs_140188661515120
                __attrs_140188661515120 = _static_140188661517040

                # <a ... (9:44)
                # --------------------------------------------------------
                __append('<a href="#fish-changes">Squid Ate FISH Changes</a></li>\n            </ul>\n        </div>\n        ')

                # <Static value=<_ast.Dict object at 0x7f80375f0520> name=None at 7f80377585e0> -> __attrs_140188661517712
                __attrs_140188661517712 = _static_140188661515552

                # <div ... (12:8)
                # --------------------------------------------------------
                __append('<div class="col-md-9">\n            ')

                # <Static value=<_ast.Dict object at 0x7f80375f0880> name=None at 7f80375f0a60> -> __attrs_140188661516080
                __attrs_140188661516080 = _static_140188661516416

                # <div ... (13:12)
                # --------------------------------------------------------
                __append('<div class="page-header">\n                ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664080080
                __attrs_140188664080080 = _static_140188664645808

                # <h2 ... (14:16)
                # --------------------------------------------------------
                __append('<h2>Get Started</h2>\n                ')

                # <Static value=<_ast.Dict object at 0x7f8037862b20> name=None at 7f80378624f0> -> __attrs_140188664080848
                __attrs_140188664080848 = _static_140188664081184

                # <ul ... (15:16)
                # --------------------------------------------------------
                __append('<ul class="list-inline">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664081760
                __attrs_140188664081760 = _static_140188664645808

                # <li ... (16:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<_ast.Dict object at 0x7f80378626a0> name=None at 7f8037862670> -> __attrs_140188664082144
                __attrs_140188664082144 = _static_140188664080032

                # <i ... (16:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i>')

                # <Interpolation value=<Substitution " Intro dates ${metadata['dates'][0]}-${metadata['dates'][1]}" (16:58)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f8037862190> -> __content_140188669528304
                __token = 855
                __token = 869
                __content_140188669528304 = getitem('metadata')['dates'][0]
                __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
                __token = 893
                __content_140188669528304_891 = getitem('metadata')['dates'][1]
                __content_140188669528304_891 = __quote(__content_140188669528304_891, '\x00', '&#0;', None, None)
                __content_140188669528304 = ('%s%s%s%s' % (' Intro dates ', (__content_140188669528304 if (__content_140188669528304 is not None) else ''), '-', (__content_140188669528304_891 if (__content_140188669528304_891 is not None) else ''), ))
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
                __append('</li>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662637568
                __attrs_140188662637568 = _static_140188664645808

                # <li ... (17:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<_ast.Dict object at 0x7f8037702490> name=None at 7f8037702640> -> __attrs_140188662637280
                __attrs_140188662637280 = _static_140188662637712

                # <i ... (17:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> Wide range of ship types and capacities</li>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662639968
                __attrs_140188662639968 = _static_140188664645808

                # <li ... (18:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<_ast.Dict object at 0x7f8037702ca0> name=None at 7f8037702b80> -> __attrs_140188662718224
                __attrs_140188662718224 = _static_140188662639776

                # <i ... (18:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> Compatible with all known cargos</li>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663600608
                __attrs_140188663600608 = _static_140188664645808

                # <li ... (19:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<_ast.Dict object at 0x7f80377ed970> name=None at 7f80377ed910> -> __attrs_140188663601760
                __attrs_140188663601760 = _static_140188663601520

                # <i ... (19:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> Supports 2 company colours</li>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663602288
                __attrs_140188663602288 = _static_140188664645808

                # <li ... (20:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<_ast.Dict object at 0x7f80377ed340> name=None at 7f80377ed310> -> __attrs_140188663601856
                __attrs_140188663601856 = _static_140188663599936

                # <i ... (20:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> Autorefit support</li>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188660931024
                __attrs_140188660931024 = _static_140188664645808

                # <li ... (21:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<_ast.Dict object at 0x7f8037561310> name=None at 7f8037561610> -> __attrs_140188660931648
                __attrs_140188660931648 = _static_140188660929296

                # <i ... (21:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> Parameter for ship speed</li>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188660932224
                __attrs_140188660932224 = _static_140188664645808

                # <li ... (22:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<_ast.Dict object at 0x7f8037561e20> name=None at 7f8037561970> -> __attrs_140188660929968
                __attrs_140188660929968 = _static_140188660932128

                # <i ... (22:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> Parameter for canal construction costs</li>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663217600
                __attrs_140188663217600 = _static_140188664645808

                # <li ... (23:20)
                # --------------------------------------------------------
                __append('<li>')

                # <Static value=<_ast.Dict object at 0x7f803778fa90> name=None at 7f803778f370> -> __attrs_140188663214336
                __attrs_140188663214336 = _static_140188663216784

                # <i ... (23:24)
                # --------------------------------------------------------
                __append('<i class="fa fa-check-circle"></i> GPL v2 license</li>\n                </ul>\n            </div>\n            ')

                # <Static value=<_ast.Dict object at 0x7f803778f550> name=None at 7f803778fb20> -> __attrs_140188663216736
                __attrs_140188663216736 = _static_140188663215440

                # <div ... (26:12)
                # --------------------------------------------------------
                __append('<div id="download-fish">\n                ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662344048
                __attrs_140188662344048 = _static_140188664645808

                # <h2 ... (27:16)
                # --------------------------------------------------------
                __append('<h2>1. Download Squid Ate FISH</h2>\n                ')

                # <Static value=<_ast.Dict object at 0x7f80376ba910> name=None at 7f80376ba3a0> -> __attrs_140188662342608
                __attrs_140188662342608 = _static_140188662343952

                # <p ... (28:16)
                # --------------------------------------------------------
                __append('<p class="lead">\n                    Squid Ate FISH is available from the content service in OpenTTD, as a zip for manual installation,\n                    or as a source checkout for compiling locally (requires mercurial and various python dependencies).\n                </p>\n                ')

                # <Static value=<_ast.Dict object at 0x7f80376baeb0> name=None at 7f80376bac70> -> __attrs_140188662341792
                __attrs_140188662341792 = _static_140188662345392

                # <div ... (32:16)
                # --------------------------------------------------------
                __append('<div class="row">\n                    ')

                # <Static value=<_ast.Dict object at 0x7f80376ba550> name=None at 7f80376bad90> -> __attrs_140188663376384
                __attrs_140188663376384 = _static_140188662342992

                # <div ... (33:20)
                # --------------------------------------------------------
                __append('<div class="col-sm-4">\n                        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663373984
                __attrs_140188663373984 = _static_140188664645808

                # <h3 ... (34:24)
                # --------------------------------------------------------
                __append('<h3>Download in OpenTTD</h3>\n                        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663373936
                __attrs_140188663373936 = _static_140188664645808

                # <p ... (35:24)
                # --------------------------------------------------------
                __append('<p>')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663377536
                __attrs_140188663377536 = _static_140188664645808

                # <strong ... (35:27)
                # --------------------------------------------------------
                __append('<strong>Easiest</strong>: get Squid Ate FISH from the OpenTTD content service.</p>\n                        ')

                # <Static value=<_ast.Dict object at 0x7f80377b6eb0> name=None at 7f80377b6400> -> __attrs_140188661548848
                __attrs_140188661548848 = _static_140188663377584

                # <a ... (36:24)
                # --------------------------------------------------------
                __append('<a class="btn btn-primary btn-block" href="http://wiki.openttd.org/Content_downloading">Instructions</a>\n                    </div>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f80375f8790> name=None at 7f80375f8580> -> __attrs_140188661548272
                __attrs_140188661548272 = _static_140188661548944

                # <div ... (38:20)
                # --------------------------------------------------------
                __append('<div class="col-sm-4">\n                        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188661548464
                __attrs_140188661548464 = _static_140188664645808

                # <h3 ... (39:24)
                # --------------------------------------------------------
                __append('<h3>Download Zip</h3>\n                        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188661547888
                __attrs_140188661547888 = _static_140188664645808

                # <p ... (40:24)
                # --------------------------------------------------------
                __append('<p>Get the latest Squid Ate FISH release for ')

                # <Static value=<_ast.Dict object at 0x7f803765fac0> name=None at 7f803765f880> -> __attrs_140188661969872
                __attrs_140188661969872 = _static_140188661971648

                # <a ... (40:69)
                # --------------------------------------------------------
                __append('<a href="http://wiki.openttd.org/Newgrf#Manual_install">manual install</a>.</p>\n                        ')

                # <Static value=<_ast.Dict object at 0x7f803765fc40> name=None at 7f803765f820> -> __attrs_140188661970112
                __attrs_140188661970112 = _static_140188661972032

                # <a ... (41:24)
                # --------------------------------------------------------
                __append('<a class="btn btn-info btn-block" href="http://bundles.openttdcoop.org/fish/releases/LATEST/">Download Squid Ate FISH</a>\n                    </div>\n                    ')

                # <Static value=<_ast.Dict object at 0x7f803765f9d0> name=None at 7f803765fd00> -> __attrs_140188661971504
                __attrs_140188661971504 = _static_140188661971408

                # <div ... (43:20)
                # --------------------------------------------------------
                __append('<div class="col-sm-4">\n                        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662901632
                __attrs_140188662901632 = _static_140188664645808

                # <h3 ... (44:24)
                # --------------------------------------------------------
                __append('<h3>Download Source</h3>\n                        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662901920
                __attrs_140188662901920 = _static_140188664645808

                # <p ... (45:24)
                # --------------------------------------------------------
                __append('<p>Checkout source code and ')

                # <Static value=<_ast.Dict object at 0x7f8037742340> name=None at 7f80377424f0> -> __attrs_140188662899904
                __attrs_140188662899904 = _static_140188662899520

                # <a ... (45:52)
                # --------------------------------------------------------
                __append('<a href="code_reference.html">compile your own Squid Ate FISH</a>.</p>\n                        ')

                # <Static value=<_ast.Dict object at 0x7f8037742250> name=None at 7f8037742820> -> __attrs_140188664093424
                __attrs_140188664093424 = _static_140188662899280

                # <a ... (46:24)
                # --------------------------------------------------------
                __append('<a class="btn btn-default btn-block"')

                # <Symbol value=<DEFAULT> at 7f80381860a0> -> __default_140188664090880
                __default_140188664090880 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution "${metadata['repo_url']}" (46:67)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f8037742bb0> -> __attr_href
                __token = 3077
                __token = 3079
                __attr_href = getitem('metadata')['repo_url']
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
                __append('>Squid Ate FISH Source Repo</a>\n                    </div>\n                </div>\n            </div>\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664091264
                __attrs_140188664091264 = _static_140188664645808

                # <br ... (50:12)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664091696
                __attrs_140188664091696 = _static_140188664645808

                # <hr ... (51:12)
                # --------------------------------------------------------
                __append('<hr />\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664091360
                __attrs_140188664091360 = _static_140188664645808

                # <br ... (52:12)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<_ast.Dict object at 0x7f8037865880> name=None at 7f80378651c0> -> __attrs_140188664092128
                __attrs_140188664092128 = _static_140188664092800

                # <div ... (53:12)
                # --------------------------------------------------------
                __append('<div id="setting-up">\n                ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662632896
                __attrs_140188662632896 = _static_140188664645808

                # <h2 ... (54:16)
                # --------------------------------------------------------
                __append('<h2>2. Setting Up a Game with Squid Ate FISH</h2>\n                ')

                # <Static value=<_ast.Dict object at 0x7f80377012b0> name=None at 7f8037701ca0> -> __attrs_140188662632512
                __attrs_140188662632512 = _static_140188662633136

                # <p ... (55:16)
                # --------------------------------------------------------
                __append('<p class="lead">\n                    A few things to know before setting up a Squid Ate FISH game...\n                </p>\n                UNFINISHED - PARAMETERS ETC\n            </div>\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662635536
                __attrs_140188662635536 = _static_140188664645808

                # <br ... (60:12)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662634672
                __attrs_140188662634672 = _static_140188664645808

                # <hr ... (61:12)
                # --------------------------------------------------------
                __append('<hr />\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662634192
                __attrs_140188662634192 = _static_140188664645808

                # <br ... (62:12)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<_ast.Dict object at 0x7f80375d1e80> name=None at 7f80375d1dc0> -> __attrs_140188661388672
                __attrs_140188661388672 = _static_140188661390976

                # <div ... (63:12)
                # --------------------------------------------------------
                __append('<div id="what-next">\n                ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188661390400
                __attrs_140188661390400 = _static_140188664645808

                # <h2 ... (64:16)
                # --------------------------------------------------------
                __append('<h2>3. What Next?</h2>\n\n                ')

                # <Static value=<_ast.Dict object at 0x7f80375d1fd0> name=None at 7f80375d1190> -> __attrs_140188661389344
                __attrs_140188661389344 = _static_140188661391312

                # <p ... (66:16)
                # --------------------------------------------------------
                __append('<p class="lead">Find out more about Squid Ate FISH.  Or try it out in OpenTTD!</p>\n                ')

                # <Static value=<_ast.Dict object at 0x7f80375d1610> name=None at 7f80375d1550> -> __attrs_140188663569424
                __attrs_140188663569424 = _static_140188661388816

                # <a ... (67:16)
                # --------------------------------------------------------
                __append('<a class="btn btn-large btn-primary" href="ships.html">List of Ships</a>\n                ')

                # <Static value=<_ast.Dict object at 0x7f80377e5ca0> name=None at 7f80377e5370> -> __attrs_140188663566976
                __attrs_140188663566976 = _static_140188663569568

                # <a ... (68:16)
                # --------------------------------------------------------
                __append('<a class="btn btn-large btn-default" href="code_reference.html">Code Reference</a>\n            </div>\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663567408
                __attrs_140188663567408 = _static_140188664645808

                # <hr ... (70:12)
                # --------------------------------------------------------
                __append('<hr />\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662330368
                __attrs_140188662330368 = _static_140188664645808

                # <br ... (71:12)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<_ast.Dict object at 0x7f80376b7b80> name=None at 7f80376b7e80> -> __attrs_140188662333296
                __attrs_140188662333296 = _static_140188662332288

                # <div ... (72:12)
                # --------------------------------------------------------
                __append('<div id="fish-changes">\n                ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662332384
                __attrs_140188662332384 = _static_140188664645808

                # <h2 ... (73:16)
                # --------------------------------------------------------
                __append('<h2>4. Changes in Squid Ate FISH</h2>\n                ')

                # <Static value=<_ast.Dict object at 0x7f80376b7940> name=None at 7f80376b7bb0> -> __attrs_140188662332144
                __attrs_140188662332144 = _static_140188662331712

                # <p ... (74:16)
                # --------------------------------------------------------
                __append('<p class="lead">Squid Ate FISH is updated and improved quite often.</p>\n                ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662441968
                __attrs_140188662441968 = _static_140188664645808

                # <p ... (75:16)
                # --------------------------------------------------------
                __append('<p>The ')

                # <Static value=<_ast.Dict object at 0x7f80376d2430> name=None at 7f80376d2f40> -> __attrs_140188662442832
                __attrs_140188662442832 = _static_140188662441008

                # <a ... (75:23)
                # --------------------------------------------------------
                __append('<a href="changelog.html">')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662441728
                __attrs_140188662441728 = _static_140188664645808

                # <strong ... (75:48)
                # --------------------------------------------------------
                __append('<strong>Squid Ate FISH changelog</strong></a> keeps track of changes, including new features, bug fixes and updates to translations.</p>\n            </div>\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662443600
                __attrs_140188662443600 = _static_140188664645808

                # <br ... (77:12)
                # --------------------------------------------------------
                __append('<br />\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662442784
                __attrs_140188662442784 = _static_140188664645808

                # <br ... (78:12)
                # --------------------------------------------------------
                __append('<br />\n        </div>\n    </div>\n    ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188661927744
                __attrs_140188661927744 = _static_140188664645808

                # <br ... (81:4)
                # --------------------------------------------------------
                __append('<br />\n    ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188661927120
                __attrs_140188661927120 = _static_140188664645808

                # <br ... (82:4)
                # --------------------------------------------------------
                __append('<br />\n')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'load:main_template.pt' (1:36)> -> __macro
            __token = 36
            __macro = 'main_template.pt'
            __macro = __loader(__macro)
            __token = 36
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140188664101440 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140188664101440
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }