# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/SHARK/src/docs_templates/ships.pt'

__tokens = {127: ('${len(ships)} ships for OpenTTD', 5, 12), 129: ('len(ships)', 5, 14), 215: ('registered_rosters', 7, 36), 256: ('${doc_helper.get_roster_name(repeat.roster.index)}', 8, 20), 258: ('doc_helper.get_roster_name(repeat.roster.index)', 8, 22), 308: ('${doc_helper.get_roster_name(repeat.roster.index)}', 8, 72), 310: ('doc_helper.get_roster_name(repeat.roster.index)', 8, 74), 379: ('${len(roster.buy_menu_sort_order)} Ships', 9, 15), 381: ('len(roster.buy_menu_sort_order)', 9, 17), 848: ('ships', 20, 55), 911: ('ship.id in roster.buy_menu_sort_order', 21, 55), 1020: ('${ship.get_name_substr()} ${base_lang_strings[ship.get_str_name_suffix()]}', 23, 36), 1022: ('ship.get_name_substr()', 23, 38), 1048: ('base_lang_strings[ship.get_str_name_suffix()]', 23, 64), 1151: ('${ship.intro_date}', 24, 51), 1153: ('ship.intro_date', 24, 53), 1211: ('${base_lang_strings[ship.get_str_type_info()]}', 25, 36), 1213: ('base_lang_strings[ship.get_str_type_info()]', 25, 38), 1299: ('${int(ship.speed)} mph', 26, 36), 1301: ('int(ship.speed)', 26, 38), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.utils import lookup_attr as _lookup_attr
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140188664081904 = {'class': 'number', }
_static_140188662327280 = {'class': 'number', }
_static_140188661452560 = {'class': 'table table-striped tablesorter', }
_static_140188663200592 = {'id': '${doc_helper.get_roster_name(repeat.roster.index)}', }
_static_140188664014688 = {'class': 'span12', }
_static_140188662862032 = 'load:main_template.pt'
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

            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664013152
            __attrs_140188664013152 = _static_140188664645808
            __backup_macroname_140188663354240 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f80377390d0> name=None at 7f8037739e50> -> __value
            __value = _static_140188662862032
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664014352
                __attrs_140188664014352 = _static_140188664645808

                # <div ... (2:0)
                # --------------------------------------------------------
                __append('<div>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8037852760> name=None at 7f8037852af0> -> __attrs_140188664016272
                __attrs_140188664016272 = _static_140188664014688

                # <div ... (4:4)
                # --------------------------------------------------------
                __append('<div class="span12">\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663199440
                __attrs_140188663199440 = _static_140188664645808

                # <h2 ... (5:8)
                # --------------------------------------------------------
                __append('<h2>')

                # <Interpolation value=<Substitution '${len(ships)} ships for OpenTTD' (5:12)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f803778b0a0> -> __content_140188669528304
                __token = 127
                __token = 129
                __content_140188669528304 = len(getitem('ships'))
                __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
                __content_140188669528304 = ('%s%s' % ((__content_140188669528304 if (__content_140188669528304 is not None) else ''), ' ships for OpenTTD', ))
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
                __append('</h2>\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663199488
                __attrs_140188663199488 = _static_140188664645808

                # <hr ... (6:8)
                # --------------------------------------------------------
                __append('<hr />\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663198624
                __attrs_140188663198624 = _static_140188664645808
                __backup_roster_140188662861936 = get('roster', __marker)

                # <Value 'registered_rosters' (7:36)> -> __iterator
                __token = 215
                __iterator = getitem('registered_rosters')
                (__iterator, ____index_140188663201744, ) = getitem('repeat')('roster', __iterator)
                econtext['roster'] = None
                for __item in __iterator:
                    econtext['roster'] = __item
                    __append('\n            ')

                    # <Static value=<_ast.Dict object at 0x7f803778bb50> name=None at 7f803778b970> -> __attrs_140188663201072
                    __attrs_140188663201072 = _static_140188663200592

                    # <h3 ... (8:12)
                    # --------------------------------------------------------
                    __append('<h3')

                    # <Symbol value=<DEFAULT> at 7f80381860a0> -> __default_140188663201360
                    __default_140188663201360 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${doc_helper.get_roster_name(repeat.roster.index)}' (8:20)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f803778bf10> -> __attr_id
                    __token = 256
                    __token = 258
                    __attr_id = _lookup_attr(getitem('doc_helper'), 'get_roster_name')(_lookup_attr(_lookup_attr(getitem('repeat'), 'roster'), 'index'))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_id = __attr_id
                    if (__attr_id is None):
                        pass
                    else:
                        if (__attr_id is _DEFAULT_MARKER):
                            __attr_id = None
                        else:
                            __tt = type(__attr_id)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_id = str(__attr_id)
                            else:
                                if (__tt is bytes):
                                    __attr_id = decode(__attr_id)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_id = __attr_id.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_id)
                                            __attr_id = (str(__attr_id) if (__attr_id is __converted) else __converted)
                                        else:
                                            __attr_id = __attr_id()
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append('>')

                    # <Interpolation value=<Substitution '${doc_helper.get_roster_name(repeat.roster.index)}' (8:72)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f803778bdc0> -> __content_140188669528304
                    __token = 308
                    __token = 310
                    __content_140188669528304 = _lookup_attr(getitem('doc_helper'), 'get_roster_name')(_lookup_attr(_lookup_attr(getitem('repeat'), 'roster'), 'index'))
                    __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
                    __content_140188669528304 = __content_140188669528304
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
                    __append('</h3>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188661451360
                    __attrs_140188661451360 = _static_140188664645808

                    # <p ... (9:12)
                    # --------------------------------------------------------
                    __append('<p>')

                    # <Interpolation value=<Substitution '${len(roster.buy_menu_sort_order)} Ships' (9:15)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f80375e01f0> -> __content_140188669528304
                    __token = 379
                    __token = 381
                    __content_140188669528304 = len(_lookup_attr(getitem('roster'), 'buy_menu_sort_order'))
                    __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
                    __content_140188669528304 = ('%s%s' % ((__content_140188669528304 if (__content_140188669528304 is not None) else ''), ' Ships', ))
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
                    __append('</p>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f80375e0f10> name=None at 7f80375e0490> -> __attrs_140188661450736
                    __attrs_140188661450736 = _static_140188661452560

                    # <table ... (10:12)
                    # --------------------------------------------------------
                    __append('<table class="table table-striped tablesorter">\n                ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188661452464
                    __attrs_140188661452464 = _static_140188664645808

                    # <thead ... (11:16)
                    # --------------------------------------------------------
                    __append('<thead>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662326944
                    __attrs_140188662326944 = _static_140188664645808

                    # <tr ... (12:20)
                    # --------------------------------------------------------
                    __append('<tr>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662326464
                    __attrs_140188662326464 = _static_140188664645808

                    # <th ... (13:24)
                    # --------------------------------------------------------
                    __append('<th>Ship Name</th>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f80376b67f0> name=None at 7f80376b6d60> -> __attrs_140188662328864
                    __attrs_140188662328864 = _static_140188662327280

                    # <th ... (14:24)
                    # --------------------------------------------------------
                    __append('<th class="number">Intro Date</th>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662328192
                    __attrs_140188662328192 = _static_140188664645808

                    # <th ... (15:24)
                    # --------------------------------------------------------
                    __append('<th>Extra Info</th>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662780544
                    __attrs_140188662780544 = _static_140188664645808

                    # <th ... (16:24)
                    # --------------------------------------------------------
                    __append('<th>Speed</th>\n                    </tr>\n                </thead>\n                ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662780976
                    __attrs_140188662780976 = _static_140188664645808

                    # <tbody ... (19:16)
                    # --------------------------------------------------------
                    __append('<tbody>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662782752
                    __attrs_140188662782752 = _static_140188664645808
                    __backup_ship_140188663198144 = get('ship', __marker)

                    # <Value 'ships' (20:55)> -> __iterator
                    __token = 848
                    __iterator = getitem('ships')
                    (__iterator, ____index_140188662781024, ) = getitem('repeat')('ship', __iterator)
                    econtext['ship'] = None
                    for __item in __iterator:
                        econtext['ship'] = __item
                        __append('\n                        ')

                        # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662781888
                        __attrs_140188662781888 = _static_140188664645808

                        # <Value 'ship.id in roster.buy_menu_sort_order' (21:55)> -> __condition
                        __token = 911
                        __condition = (_lookup_attr(getitem('ship'), 'id') in _lookup_attr(getitem('roster'), 'buy_menu_sort_order'))
                        if __condition:
                            __append('\n                            ')

                            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664080992
                            __attrs_140188664080992 = _static_140188664645808

                            # <tr ... (22:28)
                            # --------------------------------------------------------
                            __append('<tr>\n                                ')

                            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664078400
                            __attrs_140188664078400 = _static_140188664645808

                            # <td ... (23:32)
                            # --------------------------------------------------------
                            __append('<td>')

                            # <Interpolation value=<Substitution '${ship.get_name_substr()} ${base_lang_strings[ship.get_str_name_suffix()]}' (23:36)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f8037862ca0> -> __content_140188669528304
                            __token = 1020
                            __token = 1022
                            __content_140188669528304 = _lookup_attr(getitem('ship'), 'get_name_substr')()
                            __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
                            __token = 1048
                            __content_140188669528304_1046 = getitem('base_lang_strings')[_lookup_attr(getitem('ship'), 'get_str_name_suffix')()]
                            __content_140188669528304_1046 = __quote(__content_140188669528304_1046, '\x00', '&#0;', None, None)
                            __content_140188669528304 = ('%s%s%s' % ((__content_140188669528304 if (__content_140188669528304 is not None) else ''), ' ', (__content_140188669528304_1046 if (__content_140188669528304_1046 is not None) else ''), ))
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
                            __append('</td>\n                                ')

                            # <Static value=<_ast.Dict object at 0x7f8037862df0> name=None at 7f8037862610> -> __attrs_140188662714816
                            __attrs_140188662714816 = _static_140188664081904

                            # <td ... (24:32)
                            # --------------------------------------------------------
                            __append('<td class="number">')

                            # <Interpolation value=<Substitution '${ship.intro_date}' (24:51)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f80376c5c40> -> __content_140188669528304
                            __token = 1151
                            __token = 1153
                            __content_140188669528304 = _lookup_attr(getitem('ship'), 'intro_date')
                            __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
                            __content_140188669528304 = __content_140188669528304
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
                            __append('</td>\n                                ')

                            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664081712
                            __attrs_140188664081712 = _static_140188664645808

                            # <td ... (25:32)
                            # --------------------------------------------------------
                            __append('<td>')

                            # <Interpolation value=<Substitution '${base_lang_strings[ship.get_str_type_info()]}' (25:36)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f80378622e0> -> __content_140188669528304
                            __token = 1211
                            __token = 1213
                            __content_140188669528304 = getitem('base_lang_strings')[_lookup_attr(getitem('ship'), 'get_str_type_info')()]
                            __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
                            __content_140188669528304 = __content_140188669528304
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
                            __append('</td>\n                                ')

                            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664079504
                            __attrs_140188664079504 = _static_140188664645808

                            # <td ... (26:32)
                            # --------------------------------------------------------
                            __append('<td>')

                            # <Interpolation value=<Substitution '${int(ship.speed)} mph' (26:36)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f8037862760> -> __content_140188669528304
                            __token = 1299
                            __token = 1301
                            __content_140188669528304 = int(_lookup_attr(getitem('ship'), 'speed'))
                            __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
                            __content_140188669528304 = ('%s%s' % ((__content_140188669528304 if (__content_140188669528304 is not None) else ''), ' mph', ))
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
                            __append('</td>\n                            </tr>\n                        ')
                        __append('\n                    ')
                        ____index_140188662781024 -= 1
                        if (____index_140188662781024 > 0):
                            __append('')
                    if (__backup_ship_140188663198144 is __marker):
                        del econtext['ship']
                    else:
                        econtext['ship'] = __backup_ship_140188663198144
                    __append('\n                </tbody>\n            </table>\n        ')
                    ____index_140188663201744 -= 1
                    if (____index_140188663201744 > 0):
                        __append('')
                if (__backup_roster_140188662861936 is __marker):
                    del econtext['roster']
                else:
                    econtext['roster'] = __backup_roster_140188662861936
                __append('\n    </div>\n\n</div>')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'load:main_template.pt' (1:36)> -> __macro
            __token = 36
            __macro = 'main_template.pt'
            __macro = __loader(__macro)
            __token = 36
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140188663354240 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140188663354240
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }