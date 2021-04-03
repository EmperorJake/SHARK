# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/docs_templates/get_started.pt'
__tokens = {855: ("Intro dates ${metadata['dates'][0]}-${metadata['dates'][1]}", 16, 59), 869: ("metadata['dates'][0]", 16, 73), 893: ("metadata['dates'][1]", 16, 97), 3077: ("${metadata['repo_url']}", 46, 67), 3079: ("metadata['repo_url']", 46, 69), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque

_static_139818165462688 = {'href': 'changelog.html', }
_static_139818164787128 = {'class': 'lead', }
_static_139818164788640 = {'id': 'fish-changes', }
_static_139818164786624 = {'class': 'btn btn-large btn-default', 'href': 'code_reference.html', }
_static_139818164111288 = {'class': 'btn btn-large btn-primary', 'href': 'ships.html', }
_static_139818164111904 = {'class': 'lead', }
_static_139818164109720 = {'id': 'what-next', }
_static_139818165326848 = {'class': 'lead', }
_static_139818165328360 = {'id': 'setting-up', }
_static_139818165791544 = {'class': 'btn btn-default btn-block', 'href': "${metadata['repo_url']}", }
_static_139818165789920 = {'href': 'code_reference.html', }
_static_139818164773384 = {'class': 'col-sm-4', }
_static_139818164772936 = {'class': 'btn btn-info btn-block', 'href': 'http://bundles.openttdcoop.org/fish/releases/LATEST/', }
_static_139818164763840 = {'href': 'http://wiki.openttd.org/Newgrf#Manual_install', }
_static_139818164762440 = {'class': 'col-sm-4', }
_static_139818164764400 = {'class': 'btn btn-primary btn-block', 'href': 'http://wiki.openttd.org/Content_downloading', }
_static_139818164548832 = {'class': 'col-sm-4', }
_static_139818164549728 = {'class': 'row', }
_static_139818164079752 = {'class': 'lead', }
_static_139818164077568 = {'id': 'download-fish', }
_static_139818164079976 = {'class': 'fa fa-check-circle', }
_static_139818164619752 = {'class': 'fa fa-check-circle', }
_static_139818164617904 = {'class': 'fa fa-check-circle', }
_static_139818164617456 = {'class': 'fa fa-check-circle', }
_static_139818164560168 = {'class': 'fa fa-check-circle', }
_static_139818164560672 = {'class': 'fa fa-check-circle', }
_static_139818165258504 = {'class': 'fa fa-check-circle', }
_static_139818165257496 = {'class': 'fa fa-check-circle', }
_static_139818165256376 = {'class': 'list-inline', }
_static_139818165914032 = {}
_static_139818164443624 = {'class': 'page-header', }
_static_139818164444184 = {'class': 'col-md-9', }
_static_139818164442224 = {'href': '#fish-changes', }
_static_139818164444352 = {'class': 'list-group-item', }
_static_139818164351664 = {'href': '#what-next', }
_static_139818164335280 = {'class': 'list-group-item', }
_static_139818164336176 = {'href': '#setting-up', }
_static_139818164336960 = {'class': 'list-group-item', }
_static_139818164337464 = {'href': '#download-fish', }
_static_139818164132440 = {'class': 'list-group-item', }
_static_139818164132272 = {'class': 'list-group', 'style': 'margin-top:35px;', }
_static_139818164130312 = {'class': 'col-md-3', }
_static_139818164131544 = {'class': 'row', }
_static_139818164368496 = 'load:main_template.pt'

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
            __backup_macroname_139818164523080 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f29f4053470> name=None at 7f29f40530f0> -> __value
            __value = _static_139818164368496
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f29f40196d8> name=None at 7f29f4019940> -> __attrs_139818164132608
                __attrs_139818164132608 = _static_139818164131544

                # <div ... (3:4)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="row"')
                __append('>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f29f4019208> name=None at 7f29f4019048> -> __attrs_139818164131432
                __attrs_139818164131432 = _static_139818164130312

                # <div ... (4:8)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-md-3"')
                __append('>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f40199b0> name=None at 7f29f40192b0> -> __attrs_139818164131824
                __attrs_139818164131824 = _static_139818164132272

                # <ul ... (5:12)
                # --------------------------------------------------------
                __append('<ul')
                __append(' class="list-group"')
                __append(' style="margin-top:35px;"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f4019a58> name=None at 7f29f4019898> -> __attrs_139818164130872
                __attrs_139818164130872 = _static_139818164132440

                # <li ... (6:16)
                # --------------------------------------------------------
                __append('<li')
                __append(' class="list-group-item"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f404bb38> name=None at 7f29f404bc88> -> __attrs_139818164338584
                __attrs_139818164338584 = _static_139818164337464

                # <a ... (6:44)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="#download-fish"')
                __append('>')
                __append('Download Squid Ate FISH')
                __append('</a>')
                __append('</li>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f404b940> name=None at 7f29f404bf60> -> __attrs_139818164338136
                __attrs_139818164338136 = _static_139818164336960

                # <li ... (7:16)
                # --------------------------------------------------------
                __append('<li')
                __append(' class="list-group-item"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f404b630> name=None at 7f29f404b828> -> __attrs_139818164336008
                __attrs_139818164336008 = _static_139818164336176

                # <a ... (7:44)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="#setting-up"')
                __append('>')
                __append('Setting up a Game with Squid Ate FISH')
                __append('</a>')
                __append('</li>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f404b2b0> name=None at 7f29f404bcf8> -> __attrs_139818164338304
                __attrs_139818164338304 = _static_139818164335280

                # <li ... (8:16)
                # --------------------------------------------------------
                __append('<li')
                __append(' class="list-group-item"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f404f2b0> name=None at 7f29f404bda0> -> __attrs_139818164906192
                __attrs_139818164906192 = _static_139818164351664

                # <a ... (8:44)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="#what-next"')
                __append('>')
                __append('What Next?')
                __append('</a>')
                __append('</li>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f4065cc0> name=None at 7f29f40658d0> -> __attrs_139818164444968
                __attrs_139818164444968 = _static_139818164444352

                # <li ... (9:16)
                # --------------------------------------------------------
                __append('<li')
                __append(' class="list-group-item"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f4065470> name=None at 7f29f4065668> -> __attrs_139818164442280
                __attrs_139818164442280 = _static_139818164442224

                # <a ... (9:44)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="#fish-changes"')
                __append('>')
                __append('Squid Ate FISH Changes')
                __append('</a>')
                __append('</li>')
                __append('\n            ')
                __append('</ul>')
                __append('\n        ')
                __append('</div>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f29f4065c18> name=None at 7f29f4065f60> -> __attrs_139818164441776
                __attrs_139818164441776 = _static_139818164444184

                # <div ... (12:8)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-md-9"')
                __append('>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f40659e8> name=None at 7f29f4065208> -> __attrs_139818164442336
                __attrs_139818164442336 = _static_139818164443624

                # <div ... (13:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="page-header"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164444576
                __attrs_139818164444576 = _static_139818165914032

                # <h2 ... (14:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('Get Started')
                __append('</h2>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f412c0b8> name=None at 7f29f412c208> -> __attrs_139818165259120
                __attrs_139818165259120 = _static_139818165256376

                # <ul ... (15:16)
                # --------------------------------------------------------
                __append('<ul')
                __append(' class="list-inline"')
                __append('>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165257048
                __attrs_139818165257048 = _static_139818165914032

                # <li ... (16:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f412c518> name=None at 7f29f412c550> -> __attrs_139818165260240
                __attrs_139818165260240 = _static_139818165257496

                # <i ... (16:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')

                # <Interpolation value=<Substitution " Intro dates ${metadata['dates'][0]}-${metadata['dates'][1]}" (16:58)> braces_required=True translation=False at 7f29f412c5c0> -> __content_139818181960344
                __token = 855
                __token = 869
                __content_139818181960344 = getitem('metadata')['dates'][0]
                __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                __token = 893
                __content_139818181960344_891 = getitem('metadata')['dates'][1]
                __content_139818181960344_891 = __quote(__content_139818181960344_891, '\x00', '&#0;', None, False)
                __content_139818181960344 = ('%s%s%s%s' % (' Intro dates ', (__content_139818181960344 if (__content_139818181960344 is not None) else ''), '-', (__content_139818181960344_891 if (__content_139818181960344_891 is not None) else ''), ))
                if (__content_139818181960344 is None):
                    pass
                else:
                    if (__content_139818181960344 is False):
                        __content_139818181960344 = None
                    else:
                        __tt = type(__content_139818181960344)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139818181960344 = str(__content_139818181960344)
                        else:
                            if (__tt is bytes):
                                __content_139818181960344 = decode(__content_139818181960344)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139818181960344 = __content_139818181960344.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139818181960344)
                                        __content_139818181960344 = (str(__content_139818181960344) if (__content_139818181960344 is __converted) else __converted)
                                    else:
                                        __content_139818181960344 = __content_139818181960344()
                if (__content_139818181960344 is not None):
                    __append(__content_139818181960344)
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165258952
                __attrs_139818165258952 = _static_139818165914032

                # <li ... (17:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f412c908> name=None at 7f29f412c128> -> __attrs_139818164560616
                __attrs_139818164560616 = _static_139818165258504

                # <i ... (17:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Wide range of ship types and capacities')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164562296
                __attrs_139818164562296 = _static_139818165914032

                # <li ... (18:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f4082320> name=None at 7f29f4082358> -> __attrs_139818164562856
                __attrs_139818164562856 = _static_139818164560672

                # <i ... (18:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Compatible with all known cargos')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164563304
                __attrs_139818164563304 = _static_139818165914032

                # <li ... (19:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f4082128> name=None at 7f29f4082cc0> -> __attrs_139818164621152
                __attrs_139818164621152 = _static_139818164560168

                # <i ... (19:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Supports 2 company colours')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164617848
                __attrs_139818164617848 = _static_139818165914032

                # <li ... (20:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f40900f0> name=None at 7f29f4090898> -> __attrs_139818164618688
                __attrs_139818164618688 = _static_139818164617456

                # <i ... (20:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Autorefit support')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164621096
                __attrs_139818164621096 = _static_139818165914032

                # <li ... (21:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f40902b0> name=None at 7f29f40906a0> -> __attrs_139818164619360
                __attrs_139818164619360 = _static_139818164617904

                # <i ... (21:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Parameter for ship speed')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164620032
                __attrs_139818164620032 = _static_139818165914032

                # <li ... (22:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f40909e8> name=None at 7f29f4090d68> -> __attrs_139818164077064
                __attrs_139818164077064 = _static_139818164619752

                # <i ... (22:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Parameter for canal construction costs')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164080032
                __attrs_139818164080032 = _static_139818165914032

                # <li ... (23:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f400cd68> name=None at 7f29f400c4e0> -> __attrs_139818164077904
                __attrs_139818164077904 = _static_139818164079976

                # <i ... (23:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' GPL v2 license')
                __append('</li>')
                __append('\n                ')
                __append('</ul>')
                __append('\n            ')
                __append('</div>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f400c400> name=None at 7f29f400c358> -> __attrs_139818164080368
                __attrs_139818164080368 = _static_139818164077568

                # <div ... (26:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' id="download-fish"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164079080
                __attrs_139818164079080 = _static_139818165914032

                # <h2 ... (27:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('1. Download Squid Ate FISH')
                __append('</h2>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f400cc88> name=None at 7f29f400ce48> -> __attrs_139818164076784
                __attrs_139818164076784 = _static_139818164079752

                # <p ... (28:16)
                # --------------------------------------------------------
                __append('<p')
                __append(' class="lead"')
                __append('>')
                __append('\n                    Squid Ate FISH is available from the content service in OpenTTD, as a zip for manual installation,\n                    or as a source checkout for compiling locally (requires mercurial and various python dependencies).\n                ')
                __append('</p>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f407f860> name=None at 7f29f407f7b8> -> __attrs_139818164548216
                __attrs_139818164548216 = _static_139818164549728

                # <div ... (32:16)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="row"')
                __append('>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f29f407f4e0> name=None at 7f29f407f5f8> -> __attrs_139818164551240
                __attrs_139818164551240 = _static_139818164548832

                # <div ... (33:20)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-sm-4"')
                __append('>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164547992
                __attrs_139818164547992 = _static_139818165914032

                # <h3 ... (34:24)
                # --------------------------------------------------------
                __append('<h3')
                __append('>')
                __append('Download in OpenTTD')
                __append('</h3>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164550064
                __attrs_139818164550064 = _static_139818165914032

                # <p ... (35:24)
                # --------------------------------------------------------
                __append('<p')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164761096
                __attrs_139818164761096 = _static_139818165914032

                # <strong ... (35:27)
                # --------------------------------------------------------
                __append('<strong')
                __append('>')
                __append('Easiest')
                __append('</strong>')
                __append(': get Squid Ate FISH from the OpenTTD content service.')
                __append('</p>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f29f40b3ef0> name=None at 7f29f40b3cf8> -> __attrs_139818164760648
                __attrs_139818164760648 = _static_139818164764400

                # <a ... (36:24)
                # --------------------------------------------------------
                __append('<a')
                __append(' class="btn btn-primary btn-block"')
                __append(' href="http://wiki.openttd.org/Content_downloading"')
                __append('>')
                __append('Instructions')
                __append('</a>')
                __append('\n                    ')
                __append('</div>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f29f40b3748> name=None at 7f29f40b3b38> -> __attrs_139818164763560
                __attrs_139818164763560 = _static_139818164762440

                # <div ... (38:20)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-sm-4"')
                __append('>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164761992
                __attrs_139818164761992 = _static_139818165914032

                # <h3 ... (39:24)
                # --------------------------------------------------------
                __append('<h3')
                __append('>')
                __append('Download Zip')
                __append('</h3>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164760816
                __attrs_139818164760816 = _static_139818165914032

                # <p ... (40:24)
                # --------------------------------------------------------
                __append('<p')
                __append('>')
                __append('Get the latest Squid Ate FISH release for ')

                # <Static value=<_ast.Dict object at 0x7f29f40b3cc0> name=None at 7f29f40b3438> -> __attrs_139818164776520
                __attrs_139818164776520 = _static_139818164763840

                # <a ... (40:69)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="http://wiki.openttd.org/Newgrf#Manual_install"')
                __append('>')
                __append('manual install')
                __append('</a>')
                __append('.')
                __append('</p>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f29f40b6048> name=None at 7f29f40b6748> -> __attrs_139818164773888
                __attrs_139818164773888 = _static_139818164772936

                # <a ... (41:24)
                # --------------------------------------------------------
                __append('<a')
                __append(' class="btn btn-info btn-block"')
                __append(' href="http://bundles.openttdcoop.org/fish/releases/LATEST/"')
                __append('>')
                __append('Download Squid Ate FISH')
                __append('</a>')
                __append('\n                    ')
                __append('</div>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f29f40b6208> name=None at 7f29f40b6588> -> __attrs_139818164773552
                __attrs_139818164773552 = _static_139818164773384

                # <div ... (43:20)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-sm-4"')
                __append('>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164776464
                __attrs_139818164776464 = _static_139818165914032

                # <h3 ... (44:24)
                # --------------------------------------------------------
                __append('<h3')
                __append('>')
                __append('Download Source')
                __append('</h3>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164775512
                __attrs_139818164775512 = _static_139818165914032

                # <p ... (45:24)
                # --------------------------------------------------------
                __append('<p')
                __append('>')
                __append('Checkout source code and ')

                # <Static value=<_ast.Dict object at 0x7f29f41ae4e0> name=None at 7f29f41ae5f8> -> __attrs_139818165791488
                __attrs_139818165791488 = _static_139818165789920

                # <a ... (45:52)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="code_reference.html"')
                __append('>')
                __append('compile your own Squid Ate FISH')
                __append('</a>')
                __append('.')
                __append('</p>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f29f41aeb38> name=None at 7f29f41ae6d8> -> __attrs_139818165791992
                __attrs_139818165791992 = _static_139818165791544

                # <a ... (46:24)
                # --------------------------------------------------------
                __append('<a')
                __append(' class="btn btn-default btn-block"')

                # <Builtin id='False' ctx=<_ast.Load object at 0x7f29f510e5c0> at 7f29f4053c88> -> __default_139818165790760
                __default_139818165790760 = False

                # <Interpolation value=<Substitution "${metadata['repo_url']}" (46:67)> braces_required=True translation=False at 7f29f41aefd0> -> __attr_href
                __token = 3077
                __token = 3079
                __attr_href = getitem('metadata')['repo_url']
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
                __append('Squid Ate FISH Source Repo')
                __append('</a>')
                __append('\n                    ')
                __append('</div>')
                __append('\n                ')
                __append('</div>')
                __append('\n            ')
                __append('</div>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165326176
                __attrs_139818165326176 = _static_139818165914032

                # <br ... (50:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165328248
                __attrs_139818165328248 = _static_139818165914032

                # <hr ... (51:12)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165327240
                __attrs_139818165327240 = _static_139818165914032

                # <br ... (52:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f413d9e8> name=None at 7f29f413da58> -> __attrs_139818165329536
                __attrs_139818165329536 = _static_139818165328360

                # <div ... (53:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' id="setting-up"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165327184
                __attrs_139818165327184 = _static_139818165914032

                # <h2 ... (54:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('2. Setting Up a Game with Squid Ate FISH')
                __append('</h2>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f413d400> name=None at 7f29f413d860> -> __attrs_139818165328808
                __attrs_139818165328808 = _static_139818165326848

                # <p ... (55:16)
                # --------------------------------------------------------
                __append('<p')
                __append(' class="lead"')
                __append('>')
                __append('\n                    A few things to know before setting up a Squid Ate FISH game...\n                ')
                __append('</p>')
                __append('\n                UNFINISHED - PARAMETERS ETC\n            ')
                __append('</div>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165328416
                __attrs_139818165328416 = _static_139818165914032

                # <br ... (60:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165327576
                __attrs_139818165327576 = _static_139818165914032

                # <hr ... (61:12)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164111848
                __attrs_139818164111848 = _static_139818165914032

                # <br ... (62:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f4014198> name=None at 7f29f4014278> -> __attrs_139818164109440
                __attrs_139818164109440 = _static_139818164109720

                # <div ... (63:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' id="what-next"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164112184
                __attrs_139818164112184 = _static_139818165914032

                # <h2 ... (64:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('3. What Next?')
                __append('</h2>')
                __append('\n\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f4014a20> name=None at 7f29f4014860> -> __attrs_139818164112912
                __attrs_139818164112912 = _static_139818164111904

                # <p ... (66:16)
                # --------------------------------------------------------
                __append('<p')
                __append(' class="lead"')
                __append('>')
                __append('Find out more about Squid Ate FISH.  Or try it out in OpenTTD!')
                __append('</p>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f40147b8> name=None at 7f29f4014cc0> -> __attrs_139818164111568
                __attrs_139818164111568 = _static_139818164111288

                # <a ... (67:16)
                # --------------------------------------------------------
                __append('<a')
                __append(' class="btn btn-large btn-primary"')
                __append(' href="ships.html"')
                __append('>')
                __append('List of Ships')
                __append('</a>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f40b95c0> name=None at 7f29f40b9898> -> __attrs_139818164786120
                __attrs_139818164786120 = _static_139818164786624

                # <a ... (68:16)
                # --------------------------------------------------------
                __append('<a')
                __append(' class="btn btn-large btn-default"')
                __append(' href="code_reference.html"')
                __append('>')
                __append('Code Reference')
                __append('</a>')
                __append('\n            ')
                __append('</div>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164786680
                __attrs_139818164786680 = _static_139818165914032

                # <hr ... (70:12)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164787576
                __attrs_139818164787576 = _static_139818165914032

                # <br ... (71:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f40b9da0> name=None at 7f29f40b9b70> -> __attrs_139818164788976
                __attrs_139818164788976 = _static_139818164788640

                # <div ... (72:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' id="fish-changes"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164785224
                __attrs_139818164785224 = _static_139818165914032

                # <h2 ... (73:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('4. Changes in Squid Ate FISH')
                __append('</h2>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f40b97b8> name=None at 7f29f40b9390> -> __attrs_139818165461288
                __attrs_139818165461288 = _static_139818164787128

                # <p ... (74:16)
                # --------------------------------------------------------
                __append('<p')
                __append(' class="lead"')
                __append('>')
                __append('Squid Ate FISH is updated and improved quite often.')
                __append('</p>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165462632
                __attrs_139818165462632 = _static_139818165914032

                # <p ... (75:16)
                # --------------------------------------------------------
                __append('<p')
                __append('>')
                __append('The ')

                # <Static value=<_ast.Dict object at 0x7f29f415e6a0> name=None at 7f29f415e4e0> -> __attrs_139818165461568
                __attrs_139818165461568 = _static_139818165462688

                # <a ... (75:23)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="changelog.html"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165464760
                __attrs_139818165464760 = _static_139818165914032

                # <strong ... (75:48)
                # --------------------------------------------------------
                __append('<strong')
                __append('>')
                __append('Squid Ate FISH changelog')
                __append('</strong>')
                __append('</a>')
                __append(' keeps track of changes, including new features, bug fixes and updates to translations.')
                __append('</p>')
                __append('\n            ')
                __append('</div>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165464312
                __attrs_139818165464312 = _static_139818165914032

                # <br ... (77:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165462520
                __attrs_139818165462520 = _static_139818165914032

                # <br ... (78:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n        ')
                __append('</div>')
                __append('\n    ')
                __append('</div>')
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165463696
                __attrs_139818165463696 = _static_139818165914032

                # <br ... (81:4)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165462352
                __attrs_139818165462352 = _static_139818165914032

                # <br ... (82:4)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'load:main_template.pt' (1:36)> -> __macro
            __token = 36
            __macro = 'main_template.pt'
            __macro = __loader(__macro)
            __token = 36
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_139818164523080 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139818164523080
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }