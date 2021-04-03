# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/docs_templates/get_started.pt'
__tokens = {855: ("Intro dates ${metadata['dates'][0]}-${metadata['dates'][1]}", 16, 59), 869: ("metadata['dates'][0]", 16, 73), 893: ("metadata['dates'][1]", 16, 97), 3077: ("${metadata['repo_url']}", 46, 67), 3079: ("metadata['repo_url']", 46, 69), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque

_static_139628048935792 = {'href': 'changelog.html', }
_static_139628049030560 = {'class': 'lead', }
_static_139628049029496 = {'id': 'fish-changes', }
_static_139628049027480 = {'class': 'btn btn-large btn-default', 'href': 'code_reference.html', }
_static_139628049012720 = {'class': 'btn btn-large btn-primary', 'href': 'ships.html', }
_static_139628049011992 = {'class': 'lead', }
_static_139628048895952 = {'id': 'what-next', }
_static_139628048893320 = {'class': 'lead', }
_static_139628049727272 = {'id': 'setting-up', }
_static_139628049723632 = {'class': 'btn btn-default btn-block', 'href': "${metadata['repo_url']}", }
_static_139628049825240 = {'href': 'code_reference.html', }
_static_139628049822160 = {'class': 'col-sm-4', }
_static_139628049866256 = {'class': 'btn btn-info btn-block', 'href': 'http://bundles.openttdcoop.org/fish/releases/LATEST/', }
_static_139628049865192 = {'href': 'http://wiki.openttd.org/Newgrf#Manual_install', }
_static_139628049863680 = {'class': 'col-sm-4', }
_static_139628048591336 = {'class': 'btn btn-primary btn-block', 'href': 'http://wiki.openttd.org/Content_downloading', }
_static_139628048315000 = {'class': 'col-sm-4', }
_static_139628048316568 = {'class': 'row', }
_static_139628048314440 = {'class': 'lead', }
_static_139628048274992 = {'id': 'download-fish', }
_static_139628048276168 = {'class': 'fa fa-check-circle', }
_static_139628048273592 = {'class': 'fa fa-check-circle', }
_static_139628049471584 = {'class': 'fa fa-check-circle', }
_static_139628049472760 = {'class': 'fa fa-check-circle', }
_static_139628049470744 = {'class': 'fa fa-check-circle', }
_static_139628049585152 = {'class': 'fa fa-check-circle', }
_static_139628049585208 = {'class': 'fa fa-check-circle', }
_static_139628049586720 = {'class': 'fa fa-check-circle', }
_static_139628048198344 = {'class': 'list-inline', }
_static_139628050453112 = {}
_static_139628048195880 = {'class': 'page-header', }
_static_139628048198456 = {'class': 'col-md-9', }
_static_139628048014696 = {'href': '#fish-changes', }
_static_139628048012624 = {'class': 'list-group-item', }
_static_139628048012176 = {'href': '#what-next', }
_static_139628048011392 = {'class': 'list-group-item', }
_static_139628048012400 = {'href': '#setting-up', }
_static_139628048428952 = {'class': 'list-group-item', }
_static_139628048427720 = {'href': '#download-fish', }
_static_139628048428392 = {'class': 'list-group-item', }
_static_139628048582136 = {'class': 'list-group', 'style': 'margin-top:35px;', }
_static_139628048582808 = {'class': 'col-md-3', }
_static_139628048300184 = {'class': 'row', }
_static_139628048302032 = 'load:main_template.pt'

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
            __backup_macroname_139628048211144 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7efdb0383fd0> name=None at 7efdb03833c8> -> __value
            __value = _static_139628048302032
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7efdb0383898> name=None at 7efdb0383470> -> __attrs_139628048298504
                __attrs_139628048298504 = _static_139628048300184

                # <div ... (3:4)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="row"')
                __append('>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7efdb03c8898> name=None at 7efdb03c8438> -> __attrs_139628048581744
                __attrs_139628048581744 = _static_139628048582808

                # <div ... (4:8)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-md-3"')
                __append('>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7efdb03c85f8> name=None at 7efdb03c83c8> -> __attrs_139628048427664
                __attrs_139628048427664 = _static_139628048582136

                # <ul ... (5:12)
                # --------------------------------------------------------
                __append('<ul')
                __append(' class="list-group"')
                __append(' style="margin-top:35px;"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb03a2d68> name=None at 7efdb03a2c18> -> __attrs_139628048428616
                __attrs_139628048428616 = _static_139628048428392

                # <li ... (6:16)
                # --------------------------------------------------------
                __append('<li')
                __append(' class="list-group-item"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb03a2ac8> name=None at 7efdb03a2588> -> __attrs_139628048427832
                __attrs_139628048427832 = _static_139628048427720

                # <a ... (6:44)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="#download-fish"')
                __append('>')
                __append('Download Squid Ate FISH')
                __append('</a>')
                __append('</li>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb03a2f98> name=None at 7efdb03a2a58> -> __attrs_139628048012064
                __attrs_139628048012064 = _static_139628048428952

                # <li ... (7:16)
                # --------------------------------------------------------
                __append('<li')
                __append(' class="list-group-item"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb033d470> name=None at 7efdb033d3c8> -> __attrs_139628048013408
                __attrs_139628048013408 = _static_139628048012400

                # <a ... (7:44)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="#setting-up"')
                __append('>')
                __append('Setting up a Game with Squid Ate FISH')
                __append('</a>')
                __append('</li>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb033d080> name=None at 7efdb033dba8> -> __attrs_139628048014640
                __attrs_139628048014640 = _static_139628048011392

                # <li ... (8:16)
                # --------------------------------------------------------
                __append('<li')
                __append(' class="list-group-item"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb033d390> name=None at 7efdb033d438> -> __attrs_139628048013184
                __attrs_139628048013184 = _static_139628048012176

                # <a ... (8:44)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="#what-next"')
                __append('>')
                __append('What Next?')
                __append('</a>')
                __append('</li>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb033d550> name=None at 7efdb033d518> -> __attrs_139628048013856
                __attrs_139628048013856 = _static_139628048012624

                # <li ... (9:16)
                # --------------------------------------------------------
                __append('<li')
                __append(' class="list-group-item"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb033dd68> name=None at 7efdb033def0> -> __attrs_139628048197448
                __attrs_139628048197448 = _static_139628048014696

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

                # <Static value=<_ast.Dict object at 0x7efdb036ab38> name=None at 7efdb036a9b0> -> __attrs_139628048197784
                __attrs_139628048197784 = _static_139628048198456

                # <div ... (12:8)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-md-9"')
                __append('>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7efdb036a128> name=None at 7efdb036a198> -> __attrs_139628048197672
                __attrs_139628048197672 = _static_139628048195880

                # <div ... (13:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="page-header"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048199408
                __attrs_139628048199408 = _static_139628050453112

                # <h2 ... (14:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('Get Started')
                __append('</h2>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb036aac8> name=None at 7efdb036a7b8> -> __attrs_139628048196552
                __attrs_139628048196552 = _static_139628048198344

                # <ul ... (15:16)
                # --------------------------------------------------------
                __append('<ul')
                __append(' class="list-inline"')
                __append('>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049584648
                __attrs_139628049584648 = _static_139628050453112

                # <li ... (16:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb04bda20> name=None at 7efdb04bd780> -> __attrs_139628049586384
                __attrs_139628049586384 = _static_139628049586720

                # <i ... (16:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')

                # <Interpolation value=<Substitution " Intro dates ${metadata['dates'][0]}-${metadata['dates'][1]}" (16:58)> braces_required=True translation=False at 7efdb04bd828> -> __content_139628066513336
                __token = 855
                __token = 869
                __content_139628066513336 = getitem('metadata')['dates'][0]
                __content_139628066513336 = __quote(__content_139628066513336, '\x00', '&#0;', None, False)
                __token = 893
                __content_139628066513336_891 = getitem('metadata')['dates'][1]
                __content_139628066513336_891 = __quote(__content_139628066513336_891, '\x00', '&#0;', None, False)
                __content_139628066513336 = ('%s%s%s%s' % (' Intro dates ', (__content_139628066513336 if (__content_139628066513336 is not None) else ''), '-', (__content_139628066513336_891 if (__content_139628066513336_891 is not None) else ''), ))
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
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049587784
                __attrs_139628049587784 = _static_139628050453112

                # <li ... (17:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb04bd438> name=None at 7efdb04bd940> -> __attrs_139628049585936
                __attrs_139628049585936 = _static_139628049585208

                # <i ... (17:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Wide range of ship types and capacities')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049584872
                __attrs_139628049584872 = _static_139628050453112

                # <li ... (18:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb04bd400> name=None at 7efdb04bd0f0> -> __attrs_139628049584424
                __attrs_139628049584424 = _static_139628049585152

                # <i ... (18:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Compatible with all known cargos')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049472088
                __attrs_139628049472088 = _static_139628050453112

                # <li ... (19:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb04a1518> name=None at 7efdb04a1dd8> -> __attrs_139628049470464
                __attrs_139628049470464 = _static_139628049470744

                # <i ... (19:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Supports 2 company colours')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049472872
                __attrs_139628049472872 = _static_139628050453112

                # <li ... (20:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb04a1cf8> name=None at 7efdb04a1b00> -> __attrs_139628049471528
                __attrs_139628049471528 = _static_139628049472760

                # <i ... (20:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Autorefit support')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049470184
                __attrs_139628049470184 = _static_139628050453112

                # <li ... (21:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb04a1860> name=None at 7efdb04a1c50> -> __attrs_139628049470296
                __attrs_139628049470296 = _static_139628049471584

                # <i ... (21:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Parameter for ship speed')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048273816
                __attrs_139628048273816 = _static_139628050453112

                # <li ... (22:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb037d0b8> name=None at 7efdb037d048> -> __attrs_139628048275216
                __attrs_139628048275216 = _static_139628048273592

                # <i ... (22:24)
                # --------------------------------------------------------
                __append('<i')
                __append(' class="fa fa-check-circle"')
                __append('>')
                __append('</i>')
                __append(' Parameter for canal construction costs')
                __append('</li>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048276392
                __attrs_139628048276392 = _static_139628050453112

                # <li ... (23:20)
                # --------------------------------------------------------
                __append('<li')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb037dac8> name=None at 7efdb037dc50> -> __attrs_139628048275664
                __attrs_139628048275664 = _static_139628048276168

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

                # <Static value=<_ast.Dict object at 0x7efdb037d630> name=None at 7efdb037d358> -> __attrs_139628048273760
                __attrs_139628048273760 = _static_139628048274992

                # <div ... (26:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' id="download-fish"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048277064
                __attrs_139628048277064 = _static_139628050453112

                # <h2 ... (27:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('1. Download Squid Ate FISH')
                __append('</h2>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb0387048> name=None at 7efdb0387780> -> __attrs_139628048316512
                __attrs_139628048316512 = _static_139628048314440

                # <p ... (28:16)
                # --------------------------------------------------------
                __append('<p')
                __append(' class="lead"')
                __append('>')
                __append('\n                    Squid Ate FISH is available from the content service in OpenTTD, as a zip for manual installation,\n                    or as a source checkout for compiling locally (requires mercurial and various python dependencies).\n                ')
                __append('</p>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb0387898> name=None at 7efdb0387eb8> -> __attrs_139628048317576
                __attrs_139628048317576 = _static_139628048316568

                # <div ... (32:16)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="row"')
                __append('>')
                __append('\n                    ')

                # <Static value=<_ast.Dict object at 0x7efdb0387278> name=None at 7efdb0387d30> -> __attrs_139628048318024
                __attrs_139628048318024 = _static_139628048315000

                # <div ... (33:20)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-sm-4"')
                __append('>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048318304
                __attrs_139628048318304 = _static_139628050453112

                # <h3 ... (34:24)
                # --------------------------------------------------------
                __append('<h3')
                __append('>')
                __append('Download in OpenTTD')
                __append('</h3>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048316120
                __attrs_139628048316120 = _static_139628050453112

                # <p ... (35:24)
                # --------------------------------------------------------
                __append('<p')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048592064
                __attrs_139628048592064 = _static_139628050453112

                # <strong ... (35:27)
                # --------------------------------------------------------
                __append('<strong')
                __append('>')
                __append('Easiest')
                __append('</strong>')
                __append(': get Squid Ate FISH from the OpenTTD content service.')
                __append('</p>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7efdb03ca9e8> name=None at 7efdb03cab70> -> __attrs_139628049863008
                __attrs_139628049863008 = _static_139628048591336

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

                # <Static value=<_ast.Dict object at 0x7efdb0501400> name=None at 7efdb05012e8> -> __attrs_139628049863904
                __attrs_139628049863904 = _static_139628049863680

                # <div ... (38:20)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-sm-4"')
                __append('>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049864688
                __attrs_139628049864688 = _static_139628050453112

                # <h3 ... (39:24)
                # --------------------------------------------------------
                __append('<h3')
                __append('>')
                __append('Download Zip')
                __append('</h3>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049864912
                __attrs_139628049864912 = _static_139628050453112

                # <p ... (40:24)
                # --------------------------------------------------------
                __append('<p')
                __append('>')
                __append('Get the latest Squid Ate FISH release for ')

                # <Static value=<_ast.Dict object at 0x7efdb05019e8> name=None at 7efdb0501a20> -> __attrs_139628049865976
                __attrs_139628049865976 = _static_139628049865192

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

                # <Static value=<_ast.Dict object at 0x7efdb0501e10> name=None at 7efdb0501da0> -> __attrs_139628049821992
                __attrs_139628049821992 = _static_139628049866256

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

                # <Static value=<_ast.Dict object at 0x7efdb04f71d0> name=None at 7efdb04f7278> -> __attrs_139628049822888
                __attrs_139628049822888 = _static_139628049822160

                # <div ... (43:20)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="col-sm-4"')
                __append('>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049823448
                __attrs_139628049823448 = _static_139628050453112

                # <h3 ... (44:24)
                # --------------------------------------------------------
                __append('<h3')
                __append('>')
                __append('Download Source')
                __append('</h3>')
                __append('\n                        ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049824400
                __attrs_139628049824400 = _static_139628050453112

                # <p ... (45:24)
                # --------------------------------------------------------
                __append('<p')
                __append('>')
                __append('Checkout source code and ')

                # <Static value=<_ast.Dict object at 0x7efdb04f7dd8> name=None at 7efdb04f7c88> -> __attrs_139628049825632
                __attrs_139628049825632 = _static_139628049825240

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

                # <Static value=<_ast.Dict object at 0x7efdb04df0f0> name=None at 7efdb04df0b8> -> __attrs_139628049725424
                __attrs_139628049725424 = _static_139628049723632

                # <a ... (46:24)
                # --------------------------------------------------------
                __append('<a')
                __append(' class="btn btn-default btn-block"')

                # <Builtin id='False' ctx=<_ast.Load object at 0x7efdb14d64e0> at 7efdb04cb7b8> -> __default_139628049724864
                __default_139628049724864 = False

                # <Interpolation value=<Substitution "${metadata['repo_url']}" (46:67)> braces_required=True translation=False at 7efdb04df5f8> -> __attr_href
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

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049725648
                __attrs_139628049725648 = _static_139628050453112

                # <br ... (50:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049726320
                __attrs_139628049726320 = _static_139628050453112

                # <hr ... (51:12)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049726768
                __attrs_139628049726768 = _static_139628050453112

                # <br ... (52:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7efdb04dff28> name=None at 7efdb04dfeb8> -> __attrs_139628048892592
                __attrs_139628048892592 = _static_139628049727272

                # <div ... (53:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' id="setting-up"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048892816
                __attrs_139628048892816 = _static_139628050453112

                # <h2 ... (54:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('2. Setting Up a Game with Squid Ate FISH')
                __append('</h2>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb0414588> name=None at 7efdb04144a8> -> __attrs_139628048893712
                __attrs_139628048893712 = _static_139628048893320

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

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048894272
                __attrs_139628048894272 = _static_139628050453112

                # <br ... (60:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048895000
                __attrs_139628048895000 = _static_139628050453112

                # <hr ... (61:12)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048895616
                __attrs_139628048895616 = _static_139628050453112

                # <br ... (62:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7efdb0414fd0> name=None at 7efdb0414dd8> -> __attrs_139628049010816
                __attrs_139628049010816 = _static_139628048895952

                # <div ... (63:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' id="what-next"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049011544
                __attrs_139628049011544 = _static_139628050453112

                # <h2 ... (64:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('3. What Next?')
                __append('</h2>')
                __append('\n\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb0431518> name=None at 7efdb04314a8> -> __attrs_139628049012048
                __attrs_139628049012048 = _static_139628049011992

                # <p ... (66:16)
                # --------------------------------------------------------
                __append('<p')
                __append(' class="lead"')
                __append('>')
                __append('Find out more about Squid Ate FISH.  Or try it out in OpenTTD!')
                __append('</p>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb04317f0> name=None at 7efdb0431898> -> __attrs_139628049014456
                __attrs_139628049014456 = _static_139628049012720

                # <a ... (67:16)
                # --------------------------------------------------------
                __append('<a')
                __append(' class="btn btn-large btn-primary"')
                __append(' href="ships.html"')
                __append('>')
                __append('List of Ships')
                __append('</a>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb0435198> name=None at 7efdb04351d0> -> __attrs_139628049028208
                __attrs_139628049028208 = _static_139628049027480

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

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049028656
                __attrs_139628049028656 = _static_139628050453112

                # <hr ... (70:12)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049028768
                __attrs_139628049028768 = _static_139628050453112

                # <br ... (71:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7efdb0435978> name=None at 7efdb0435780> -> __attrs_139628049030056
                __attrs_139628049030056 = _static_139628049029496

                # <div ... (72:12)
                # --------------------------------------------------------
                __append('<div')
                __append(' id="fish-changes"')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628049030112
                __attrs_139628049030112 = _static_139628050453112

                # <h2 ... (73:16)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('4. Changes in Squid Ate FISH')
                __append('</h2>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb0435da0> name=None at 7efdb0435f28> -> __attrs_139628048681896
                __attrs_139628048681896 = _static_139628049030560

                # <p ... (74:16)
                # --------------------------------------------------------
                __append('<p')
                __append(' class="lead"')
                __append('>')
                __append('Squid Ate FISH is updated and improved quite often.')
                __append('</p>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048682344
                __attrs_139628048682344 = _static_139628050453112

                # <p ... (75:16)
                # --------------------------------------------------------
                __append('<p')
                __append('>')
                __append('The ')

                # <Static value=<_ast.Dict object at 0x7efdb041eb70> name=None at 7efdb041eb00> -> __attrs_139628048933552
                __attrs_139628048933552 = _static_139628048935792

                # <a ... (75:23)
                # --------------------------------------------------------
                __append('<a')
                __append(' href="changelog.html"')
                __append('>')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048933944
                __attrs_139628048933944 = _static_139628050453112

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

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048934336
                __attrs_139628048934336 = _static_139628050453112

                # <br ... (77:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048934616
                __attrs_139628048934616 = _static_139628050453112

                # <br ... (78:12)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n        ')
                __append('</div>')
                __append('\n    ')
                __append('</div>')
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048935120
                __attrs_139628048935120 = _static_139628050453112

                # <br ... (81:4)
                # --------------------------------------------------------
                __append('<br')
                __append(' />')
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7efdb0591278> name=None at 7efdb0591400> -> __attrs_139628048935232
                __attrs_139628048935232 = _static_139628050453112

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
            if (__backup_macroname_139628048211144 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139628048211144
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }