# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/fish1672/src/docs_templates/get_started.pt'
__tokens = {855: ("Intro dates ${metadata['dates'][0]}-${metadata['dates'][1]}", 16, 59), 869: ("metadata['dates'][0]", 16, 73), 893: ("metadata['dates'][1]", 16, 97), 3077: ("${metadata['repo_url']}", 46, 67), 3079: ("metadata['repo_url']", 46, 69), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque

_static_139865819840752 = {'href': 'changelog.html', }
_static_139865819882496 = {'class': 'lead', }
_static_139865819884120 = {'id': 'fish-changes', }
_static_139865819882608 = {'class': 'btn btn-large btn-default', 'href': 'code_reference.html', }
_static_139865819864424 = {'class': 'btn btn-large btn-primary', 'href': 'ships.html', }
_static_139865819862744 = {'class': 'lead', }
_static_139865819862128 = {'id': 'what-next', }
_static_139865821484704 = {'class': 'lead', }
_static_139865821484872 = {'id': 'setting-up', }
_static_139865819164800 = {'class': 'btn btn-default btn-block', 'href': "${metadata['repo_url']}", }
_static_139865819168720 = {'href': 'code_reference.html', }
_static_139865821393584 = {'class': 'col-sm-4', }
_static_139865821395656 = {'class': 'btn btn-info btn-block', 'href': 'http://bundles.openttdcoop.org/fish/releases/LATEST/', }
_static_139865821396440 = {'href': 'http://wiki.openttd.org/Newgrf#Manual_install', }
_static_139865820297368 = {'class': 'col-sm-4', }
_static_139865820298544 = {'class': 'btn btn-primary btn-block', 'href': 'http://wiki.openttd.org/Content_downloading', }
_static_139865820705904 = {'class': 'col-sm-4', }
_static_139865820705624 = {'class': 'row', }
_static_139865820706576 = {'class': 'lead', }
_static_139865820706240 = {'id': 'download-fish', }
_static_139865821518312 = {'class': 'fa fa-check-circle', }
_static_139865821517360 = {'class': 'fa fa-check-circle', }
_static_139865821516128 = {'class': 'fa fa-check-circle', }
_static_139865820573824 = {'class': 'fa fa-check-circle', }
_static_139865820465752 = {'class': 'fa fa-check-circle', }
_static_139865820463568 = {'class': 'fa fa-check-circle', }
_static_139865820464520 = {'class': 'fa fa-check-circle', }
_static_139865820510192 = {'class': 'fa fa-check-circle', }
_static_139865820508848 = {'class': 'list-inline', }
_static_139865822210704 = {}
_static_139865820510696 = {'class': 'page-header', }
_static_139865821331528 = {'class': 'col-md-9', }
_static_139865821333320 = {'href': '#fish-changes', }
_static_139865821333040 = {'class': 'list-group-item', }
_static_139865821334272 = {'href': '#what-next', }
_static_139865821335224 = {'class': 'list-group-item', }
_static_139865821406824 = {'href': '#setting-up', }
_static_139865821407776 = {'class': 'list-group-item', }
_static_139865821406152 = {'href': '#download-fish', }
_static_139865821406488 = {'class': 'list-group-item', }
_static_139865820626280 = {'class': 'list-group', 'style': 'margin-top:35px;', }
_static_139865821427920 = {'class': 'col-md-3', }
_static_139865821428704 = {'class': 'row', }
_static_139865821426184 = 'load:main_template.pt'

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
            __backup_macroname_139865822043080 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f350c9a3208> name=None at 7f350c9a3ba8> -> __value
            __value = _static_139865821426184
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f350c9a3be0> name=None at 7f350c9a3a20> -> __attrs_139865821426128
                __attrs_139865821426128 = _static_139865821428704

                # <div ... (3:4)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="row"')
                __append('>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f350c9a38d0> name=None at 7f350c9a3a90> -> __attrs_139865821428312
                __attrs_139865821428312 = _static_139865821427920

                # <div ... (4:8)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-md-3"')
                __append('>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350c8dfd68> name=None at 7f350c8dfba8> -> __attrs_139865821406040
                __attrs_139865821406040 = _static_139865820626280

                # <ul ... (5:12)
                # --------------------------------------------------------
                __append('<ul')
                __append(' class="list-group"')
                __append(' style="margin-top:35px;"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350c99e518> name=None at 7f350c99ea58> -> __attrs_139865821406712
                __attrs_139865821406712 = _static_139865821406488

                # <li ... (6:16)
                # --------------------------------------------------------
                __append('<li')
                __append(' class="list-group-item"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350c99e3c8> name=None at 7f350c99ecc0> -> __attrs_139865821407944
                __attrs_139865821407944 = _static_139865821406152

                # <a ... (6:44)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="#download-fish"')
                __append('>')
                __append('Download Squid Ate FISH')
                __append('</a>')
                __append('</li>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350c99ea20> name=None at 7f350c99ec50> -> __attrs_139865821405648
                __attrs_139865821405648 = _static_139865821407776

                # <li ... (7:16)
                # --------------------------------------------------------
                __append('<li')
                __append(' class="list-group-item"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350c99e668> name=None at 7f350c99e780> -> __attrs_139865821409008
                __attrs_139865821409008 = _static_139865821406824

                # <a ... (7:44)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="#setting-up"')
                __append('>')
                __append('Setting up a Game with Squid Ate FISH')
                __append('</a>')
                __append('</li>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350c98ceb8> name=None at 7f350c98cda0> -> __attrs_139865821335168
                __attrs_139865821335168 = _static_139865821335224

                # <li ... (8:16)
                # --------------------------------------------------------
                __append('<li')
                __append(' class="list-group-item"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350c98cb00> name=None at 7f350c98c588> -> __attrs_139865821335336
                __attrs_139865821335336 = _static_139865821334272

                # <a ... (8:44)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="#what-next"')
                __append('>')
                __append('What Next?')
                __append('</a>')
                __append('</li>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350c98c630> name=None at 7f350c98c0b8> -> __attrs_139865821334384
                __attrs_139865821334384 = _static_139865821333040

                # <li ... (9:16)
                # --------------------------------------------------------
                __append('<li')
                __append(' class="list-group-item"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350c98c748> name=None at 7f350c98c390> -> __attrs_139865821331864
                __attrs_139865821331864 = _static_139865821333320

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

                # <Static value=<_ast.Dict object at 0x7f350c98c048> name=None at 7f350c98c9e8> -> __attrs_139865820509240
                __attrs_139865820509240 = _static_139865821331528

                # <div ... (12:8)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-md-9"')
                __append('>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350c8c39e8> name=None at 7f350c8c3e48> -> __attrs_139865820508288
                __attrs_139865820508288 = _static_139865820510696

                # <div ... (13:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="page-header"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820510304
                __attrs_139865820510304 = _static_139865822210704

                # <h2 ... (14:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('Get Started')
                __append('</h2>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350c8c32b0> name=None at 7f350c8c36a0> -> __attrs_139865820508624
                __attrs_139865820508624 = _static_139865820508848

                # <ul ... (15:16)
                # --------------------------------------------------------
                __append('<ul')
                __append(' class="list-inline"')
                __append('>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820509464
                __attrs_139865820509464 = _static_139865822210704

                # <li ... (16:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350c8c37f0> name=None at 7f350c8c3278> -> __attrs_139865820509744
                __attrs_139865820509744 = _static_139865820510192

                # <i ... (16:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')

                # <Interpolation value=<Substitution " Intro dates ${metadata['dates'][0]}-${metadata['dates'][1]}" (16:58)> braces_required=True translation=False at 7f350c8b8630> -> __content_139865838111856
                __token = 855
                __token = 869
                __content_139865838111856 = getitem('metadata')['dates'][0]
                __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
                __token = 893
                __content_139865838111856_891 = getitem('metadata')['dates'][1]
                __content_139865838111856_891 = __quote(__content_139865838111856_891, '\x00', '&#0;', None, False)
                __content_139865838111856 = ('%s%s%s%s' % (' Intro dates ', (__content_139865838111856 if (__content_139865838111856 is not None) else ''), '-', (__content_139865838111856_891 if (__content_139865838111856_891 is not None) else ''), ))
                if (__content_139865838111856 is None):
                    pass
                else:
                    if (__content_139865838111856 is False):
                        __content_139865838111856 = None
                    else:
                        __tt = type(__content_139865838111856)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139865838111856 = str(__content_139865838111856)
                        else:
                            if (__tt is bytes):
                                __content_139865838111856 = decode(__content_139865838111856)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139865838111856 = __content_139865838111856.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139865838111856)
                                        __content_139865838111856 = (str(__content_139865838111856) if (__content_139865838111856 is __converted) else __converted)
                                    else:
                                        __content_139865838111856 = __content_139865838111856()
                if (__content_139865838111856 is not None):
                    __append(__content_139865838111856)
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820464296
                __attrs_139865820464296 = _static_139865822210704

                # <li ... (17:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350c8b8588> name=None at 7f350c8b8cc0> -> __attrs_139865820465584
                __attrs_139865820465584 = _static_139865820464520

                # <i ... (17:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Wide range of ship types and capacities')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820465360
                __attrs_139865820465360 = _static_139865822210704

                # <li ... (18:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350c8b81d0> name=None at 7f350c8b8c50> -> __attrs_139865820465416
                __attrs_139865820465416 = _static_139865820463568

                # <i ... (18:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Compatible with all known cargos')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820463344
                __attrs_139865820463344 = _static_139865822210704

                # <li ... (19:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350c8b8a58> name=None at 7f350c8b85c0> -> __attrs_139865820573936
                __attrs_139865820573936 = _static_139865820465752

                # <i ... (19:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Supports 2 company colours')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820575504
                __attrs_139865820575504 = _static_139865822210704

                # <li ... (20:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350c8d3080> name=None at 7f350c8d3828> -> __attrs_139865820576512
                __attrs_139865820576512 = _static_139865820573824

                # <i ... (20:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Autorefit support')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821519264
                __attrs_139865821519264 = _static_139865822210704

                # <li ... (21:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350c9b9160> name=None at 7f350c9b9588> -> __attrs_139865821519208
                __attrs_139865821519208 = _static_139865821516128

                # <i ... (21:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Parameter for ship speed')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821519544
                __attrs_139865821519544 = _static_139865822210704

                # <li ... (22:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350c9b9630> name=None at 7f350c9b9668> -> __attrs_139865821516744
                __attrs_139865821516744 = _static_139865821517360

                # <i ... (22:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Parameter for canal construction costs')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821518760
                __attrs_139865821518760 = _static_139865822210704

                # <li ... (23:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350c9b99e8> name=None at 7f350c9b97f0> -> __attrs_139865821516072
                __attrs_139865821516072 = _static_139865821518312

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

                # <Static value=<_ast.Dict object at 0x7f350c8f35c0> name=None at 7f350c8f3c50> -> __attrs_139865820706520
                __attrs_139865820706520 = _static_139865820706240

                # <div ... (26:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' id="download-fish"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820706632
                __attrs_139865820706632 = _static_139865822210704

                # <h2 ... (27:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('1. Download Squid Ate FISH')
                __append('</h2>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350c8f3710> name=None at 7f350c8f33c8> -> __attrs_139865820705792
                __attrs_139865820705792 = _static_139865820706576

                # <p ... (28:16)
                # --------------------------------------------------------
                __append('<p')
                __append(' class="lead"')
                __append('>')
                __append('\n                    Squid Ate FISH is available from the content service in OpenTTD, as a zip for manual installation,\n                    or as a source checkout for compiling locally (requires mercurial and various python dependencies).\n                ')
                __append('</p>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350c8f3358> name=None at 7f350c8f3940> -> __attrs_139865820705400
                __attrs_139865820705400 = _static_139865820705624

                # <div ... (32:16)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="row"')
                __append('>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7f350c8f3470> name=None at 7f350c8f3518> -> __attrs_139865821090984
                __attrs_139865821090984 = _static_139865820705904

                # <div ... (33:20)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-sm-4"')
                __append('>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821093784
                __attrs_139865821093784 = _static_139865822210704

                # <h3 ... (34:24)
                # --------------------------------------------------------
                __append('<h3')
                __append('>')
                __append('Download in OpenTTD')
                __append('</h3>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820296584
                __attrs_139865820296584 = _static_139865822210704

                # <p ... (35:24)
                # --------------------------------------------------------
                __append('<p')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820296696
                __attrs_139865820296696 = _static_139865822210704

                # <strong ... (35:27)
                # --------------------------------------------------------
                __append('<strong')
                __append('>')
                __append('Easiest')
                __append('</strong>')
                __append(': get Squid Ate FISH from the OpenTTD content service.')
                __append('</p>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f350c88fd30> name=None at 7f350c88ff28> -> __attrs_139865820297536
                __attrs_139865820297536 = _static_139865820298544

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

                # <Static value=<_ast.Dict object at 0x7f350c88f898> name=None at 7f350c88ff98> -> __attrs_139865820297200
                __attrs_139865820297200 = _static_139865820297368

                # <div ... (38:20)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-sm-4"')
                __append('>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821394032
                __attrs_139865821394032 = _static_139865822210704

                # <h3 ... (39:24)
                # --------------------------------------------------------
                __append('<h3')
                __append('>')
                __append('Download Zip')
                __append('</h3>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821396608
                __attrs_139865821396608 = _static_139865822210704

                # <p ... (40:24)
                # --------------------------------------------------------
                __append('<p')
                __append('>')
                __append('Get the latest Squid Ate FISH release for ')

                # <Static value=<_ast.Dict object at 0x7f350c99bdd8> name=None at 7f350c99bd30> -> __attrs_139865821396160
                __attrs_139865821396160 = _static_139865821396440

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

                # <Static value=<_ast.Dict object at 0x7f350c99bac8> name=None at 7f350c99bf60> -> __attrs_139865821395712
                __attrs_139865821395712 = _static_139865821395656

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

                # <Static value=<_ast.Dict object at 0x7f350c99b2b0> name=None at 7f350c99b390> -> __attrs_139865821393136
                __attrs_139865821393136 = _static_139865821393584

                # <div ... (43:20)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-sm-4"')
                __append('>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819167992
                __attrs_139865819167992 = _static_139865822210704

                # <h3 ... (44:24)
                # --------------------------------------------------------
                __append('<h3')
                __append('>')
                __append('Download Source')
                __append('</h3>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819167208
                __attrs_139865819167208 = _static_139865822210704

                # <p ... (45:24)
                # --------------------------------------------------------
                __append('<p')
                __append('>')
                __append('Checkout source code and ')

                # <Static value=<_ast.Dict object at 0x7f350c77bfd0> name=None at 7f350c77bcc0> -> __attrs_139865819166984
                __attrs_139865819166984 = _static_139865819168720

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

                # <Static value=<_ast.Dict object at 0x7f350c77b080> name=None at 7f350c77b390> -> __attrs_139865819166424
                __attrs_139865819166424 = _static_139865819164800

                # <a ... (46:24)
                # --------------------------------------------------------
                __append('<a')
                __append(' class="btn btn-default btn-block"')

                # <Builtin id='False' ctx=<_ast.Load object at 0x7f350d97df98> at 7f350c9a35c0> -> __default_139865819165192
                __default_139865819165192 = False

                # <Interpolation value=<Substitution "${metadata['repo_url']}" (46:67)> braces_required=True translation=False at 7f350c77b438> -> __attr_href
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

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819166088
                __attrs_139865819166088 = _static_139865822210704

                # <br ... (50:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819166704
                __attrs_139865819166704 = _static_139865822210704

                # <hr ... (51:12)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821483864
                __attrs_139865821483864 = _static_139865822210704

                # <br ... (52:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350c9b1748> name=None at 7f350c9b11d0> -> __attrs_139865821483640
                __attrs_139865821483640 = _static_139865821484872

                # <div ... (53:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' id="setting-up"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821483808
                __attrs_139865821483808 = _static_139865822210704

                # <h2 ... (54:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('2. Setting Up a Game with Squid Ate FISH')
                __append('</h2>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350c9b16a0> name=None at 7f350c9b18d0> -> __attrs_139865821483528
                __attrs_139865821483528 = _static_139865821484704

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

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821486384
                __attrs_139865821486384 = _static_139865822210704

                # <br ... (60:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821483360
                __attrs_139865821483360 = _static_139865822210704

                # <hr ... (61:12)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821486608
                __attrs_139865821486608 = _static_139865822210704

                # <br ... (62:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350c825470> name=None at 7f350c8254a8> -> __attrs_139865819862968
                __attrs_139865819862968 = _static_139865819862128

                # <div ... (63:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' id="what-next"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819861848
                __attrs_139865819861848 = _static_139865822210704

                # <h2 ... (64:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('3. What Next?')
                __append('</h2>')
                __append('\n\n                ')

                # <Static value=<_ast.Dict object at 0x7f350c8256d8> name=None at 7f350c8259b0> -> __attrs_139865819862016
                __attrs_139865819862016 = _static_139865819862744

                # <p ... (66:16)
                # --------------------------------------------------------
                __append('<p')
                __append(' class="lead"')
                __append('>')
                __append('Find out more about Squid Ate FISH.  Or try it out in OpenTTD!')
                __append('</p>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350c825d68> name=None at 7f350c825ba8> -> __attrs_139865819864200
                __attrs_139865819864200 = _static_139865819864424

                # <a ... (67:16)
                # --------------------------------------------------------
                __append('<a')
                __append(' class="btn btn-large btn-primary"')
                __append(' href="ships.html"')
                __append('>')
                __append('List of Ships')
                __append('</a>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350c82a470> name=None at 7f350c825908> -> __attrs_139865819881768
                __attrs_139865819881768 = _static_139865819882608

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

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819883896
                __attrs_139865819883896 = _static_139865822210704

                # <hr ... (70:12)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819882104
                __attrs_139865819882104 = _static_139865822210704

                # <br ... (71:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350c82aa58> name=None at 7f350c82af28> -> __attrs_139865819884288
                __attrs_139865819884288 = _static_139865819884120

                # <div ... (72:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' id="fish-changes"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819884008
                __attrs_139865819884008 = _static_139865822210704

                # <h2 ... (73:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('4. Changes in Squid Ate FISH')
                __append('</h2>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350c82a400> name=None at 7f350c82a630> -> __attrs_139865819883672
                __attrs_139865819883672 = _static_139865819882496

                # <p ... (74:16)
                # --------------------------------------------------------
                __append('<p')
                __append(' class="lead"')
                __append('>')
                __append('Squid Ate FISH is updated and improved quite often.')
                __append('</p>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819842656
                __attrs_139865819842656 = _static_139865822210704

                # <p ... (75:16)
                # --------------------------------------------------------
                __append('<p')
                __append('>')
                __append('The ')

                # <Static value=<_ast.Dict object at 0x7f350c8200f0> name=None at 7f350c8209e8> -> __attrs_139865819841592
                __attrs_139865819841592 = _static_139865819840752

                # <a ... (75:23)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="changelog.html"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819842320
                __attrs_139865819842320 = _static_139865822210704

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

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819843664
                __attrs_139865819843664 = _static_139865822210704

                # <br ... (77:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819843608
                __attrs_139865819843608 = _static_139865822210704

                # <br ... (78:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n        ')
                __append('</div>')
                __append('\n    ')
                __append('</div>')
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819844392
                __attrs_139865819844392 = _static_139865822210704

                # <br ... (81:4)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865819842264
                __attrs_139865819842264 = _static_139865822210704

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
            if (__backup_macroname_139865822043080 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139865822043080
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }