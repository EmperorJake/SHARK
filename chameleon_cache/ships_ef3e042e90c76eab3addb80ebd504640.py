# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/docs_templates/ships.pt'
__tokens = {127: ('${len(ships)} ships for OpenTTD', 5, 12), 129: ('len(ships)', 5, 14), 215: ('registered_rosters', 7, 36), 256: ('${doc_helper.get_roster_name(repeat.roster.index)}', 8, 20), 258: ('doc_helper.get_roster_name(repeat.roster.index)', 8, 22), 308: ('${doc_helper.get_roster_name(repeat.roster.index)}', 8, 72), 310: ('doc_helper.get_roster_name(repeat.roster.index)', 8, 74), 379: ('${len(roster.buy_menu_sort_order)} Ships', 9, 15), 381: ('len(roster.buy_menu_sort_order)', 9, 17), 848: ('ships', 20, 55), 911: ('ship.id in roster.buy_menu_sort_order', 21, 55), 1020: ('${ship.get_name_substr()} ${base_lang_strings[ship.get_str_name_suffix()]}', 23, 36), 1022: ('ship.get_name_substr()', 23, 38), 1048: ('base_lang_strings[ship.get_str_name_suffix()]', 23, 64), 1151: ('${ship.intro_date}', 24, 51), 1153: ('ship.intro_date', 24, 53), 1211: ('${base_lang_strings[ship.get_str_type_info()]}', 25, 36), 1213: ('base_lang_strings[ship.get_str_type_info()]', 25, 38), 1299: ('${int(ship.speed)} mph', 26, 36), 1301: ('int(ship.speed)', 26, 38), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.py26 import lookup_attr as _lookup_attr

_static_139818164158304 = {'class': 'number', }
_static_139818165181912 = {'class': 'number', }
_static_139818165179448 = {'class': 'table table-striped tablesorter', }
_static_139818164079976 = {'id': '${doc_helper.get_roster_name(repeat.roster.index)}', }
_static_139818164079528 = {'class': 'span12', }
_static_139818165914032 = {}
_static_139818164078408 = 'load:main_template.pt'

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
            __backup_macroname_139818164339080 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f29f400c748> name=None at 7f29f400c208> -> __value
            __value = _static_139818164078408
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164078968
                __attrs_139818164078968 = _static_139818165914032

                # <div ... (2:0)
                # --------------------------------------------------------
                __append('<div')
                __append('>')
                __append('\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f29f400cba8> name=None at 7f29f400cb70> -> __attrs_139818165283192
                __attrs_139818165283192 = _static_139818164079528

                # <div ... (4:4)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="span12"')
                __append('>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164544568
                __attrs_139818164544568 = _static_139818165914032

                # <h2 ... (5:8)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')

                # <Interpolation value=<Substitution '${len(ships)} ships for OpenTTD' (5:12)> braces_required=True translation=False at 7f29f407eeb8> -> __content_139818181960344
                __token = 127
                __token = 129
                __content_139818181960344 = len(getitem('ships'))
                __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                __content_139818181960344 = ('%s%s' % ((__content_139818181960344 if (__content_139818181960344 is not None) else ''), ' ships for OpenTTD', ))
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
                __append('</h2>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164547312
                __attrs_139818164547312 = _static_139818165914032

                # <hr ... (6:8)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n        ')
                __backup_roster_139818164546360 = get('roster', __marker)

                # <Value 'registered_rosters' (7:36)> -> __iterator
                __token = 215
                __iterator = getitem('registered_rosters')
                (__iterator, ____index_139818165077664, ) = getitem('repeat')('roster', __iterator)
                econtext['roster'] = None
                for __item in __iterator:
                    econtext['roster'] = __item
                    __append('\n            ')

                    # <Static value=<_ast.Dict object at 0x7f29f400cd68> name=None at 7f29f400cd30> -> __attrs_139818165178440
                    __attrs_139818165178440 = _static_139818164079976

                    # <h3 ... (8:12)
                    # --------------------------------------------------------
                    __append('<h3')

                    # <Builtin id='False' ctx=<_ast.Load object at 0x7f29f510e5c0> at 7f29f418d470> -> __default_139818164080368
                    __default_139818164080368 = False

                    # <Interpolation value=<Substitution '${doc_helper.get_roster_name(repeat.roster.index)}' (8:20)> braces_required=True translation=False at 7f29f400ceb8> -> __attr_id
                    __token = 256
                    __token = 258
                    __attr_id = _lookup_attr(getitem('doc_helper'), 'get_roster_name')(_lookup_attr(_lookup_attr(getitem('repeat'), 'roster'), 'index'))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, False)
                    __attr_id = __attr_id
                    if (__attr_id is None):
                        pass
                    else:
                        if (__attr_id is False):
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

                    # <Interpolation value=<Substitution '${doc_helper.get_roster_name(repeat.roster.index)}' (8:72)> braces_required=True translation=False at 7f29f4119128> -> __content_139818181960344
                    __token = 308
                    __token = 310
                    __content_139818181960344 = _lookup_attr(getitem('doc_helper'), 'get_roster_name')(_lookup_attr(_lookup_attr(getitem('repeat'), 'roster'), 'index'))
                    __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                    __content_139818181960344 = __content_139818181960344
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
                    __append('</h3>')
                    __append('\n            ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165179000
                    __attrs_139818165179000 = _static_139818165914032

                    # <p ... (9:12)
                    # --------------------------------------------------------
                    __append('<p')
                    __append('>')

                    # <Interpolation value=<Substitution '${len(roster.buy_menu_sort_order)} Ships' (9:15)> braces_required=True translation=False at 7f29f4119358> -> __content_139818181960344
                    __token = 379
                    __token = 381
                    __content_139818181960344 = len(_lookup_attr(getitem('roster'), 'buy_menu_sort_order'))
                    __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                    __content_139818181960344 = ('%s%s' % ((__content_139818181960344 if (__content_139818181960344 is not None) else ''), ' Ships', ))
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
                    __append('</p>')
                    __append('\n            ')

                    # <Static value=<_ast.Dict object at 0x7f29f4119438> name=None at 7f29f4119400> -> __attrs_139818165179952
                    __attrs_139818165179952 = _static_139818165179448

                    # <table ... (10:12)
                    # --------------------------------------------------------
                    __append('<table')
                    __append(' class="table table-striped tablesorter"')
                    __append('>')
                    __append('\n                ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165180456
                    __attrs_139818165180456 = _static_139818165914032

                    # <thead ... (11:16)
                    # --------------------------------------------------------
                    __append('<thead')
                    __append('>')
                    __append('\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165180960
                    __attrs_139818165180960 = _static_139818165914032

                    # <tr ... (12:20)
                    # --------------------------------------------------------
                    __append('<tr')
                    __append('>')
                    __append('\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165181464
                    __attrs_139818165181464 = _static_139818165914032

                    # <th ... (13:24)
                    # --------------------------------------------------------
                    __append('<th')
                    __append('>')
                    __append('Ship Name')
                    __append('</th>')
                    __append('\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f29f4119dd8> name=None at 7f29f4119da0> -> __attrs_139818165182416
                    __attrs_139818165182416 = _static_139818165181912

                    # <th ... (14:24)
                    # --------------------------------------------------------
                    __append('<th')
                    __append(' class="number"')
                    __append('>')
                    __append('Intro Date')
                    __append('</th>')
                    __append('\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164154888
                    __attrs_139818164154888 = _static_139818165914032

                    # <th ... (15:24)
                    # --------------------------------------------------------
                    __append('<th')
                    __append('>')
                    __append('Extra Info')
                    __append('</th>')
                    __append('\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164155392
                    __attrs_139818164155392 = _static_139818165914032

                    # <th ... (16:24)
                    # --------------------------------------------------------
                    __append('<th')
                    __append('>')
                    __append('Speed')
                    __append('</th>')
                    __append('\n                    ')
                    __append('</tr>')
                    __append('\n                ')
                    __append('</thead>')
                    __append('\n                ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164155896
                    __attrs_139818164155896 = _static_139818165914032

                    # <tbody ... (19:16)
                    # --------------------------------------------------------
                    __append('<tbody')
                    __append('>')
                    __append('\n                    ')
                    __backup_ship_139818165263776 = get('ship', __marker)

                    # <Value 'ships' (20:55)> -> __iterator
                    __token = 848
                    __iterator = getitem('ships')
                    (__iterator, ____index_139818164156512, ) = getitem('repeat')('ship', __iterator)
                    econtext['ship'] = None
                    for __item in __iterator:
                        econtext['ship'] = __item
                        __append('\n                        ')

                        # <Value 'ship.id in roster.buy_menu_sort_order' (21:55)> -> __condition
                        __token = 911
                        __condition = (_lookup_attr(getitem('ship'), 'id') in _lookup_attr(getitem('roster'), 'buy_menu_sort_order'))
                        if __condition:
                            __append('\n                            ')

                            # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164157296
                            __attrs_139818164157296 = _static_139818165914032

                            # <tr ... (22:28)
                            # --------------------------------------------------------
                            __append('<tr')
                            __append('>')
                            __append('\n                                ')

                            # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164157800
                            __attrs_139818164157800 = _static_139818165914032

                            # <td ... (23:32)
                            # --------------------------------------------------------
                            __append('<td')
                            __append('>')

                            # <Interpolation value=<Substitution '${ship.get_name_substr()} ${base_lang_strings[ship.get_str_name_suffix()]}' (23:36)> braces_required=True translation=False at 7f29f401fe48> -> __content_139818181960344
                            __token = 1020
                            __token = 1022
                            __content_139818181960344 = _lookup_attr(getitem('ship'), 'get_name_substr')()
                            __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                            __token = 1048
                            __content_139818181960344_1046 = getitem('base_lang_strings')[_lookup_attr(getitem('ship'), 'get_str_name_suffix')()]
                            __content_139818181960344_1046 = __quote(__content_139818181960344_1046, '\x00', '&#0;', None, False)
                            __content_139818181960344 = ('%s%s%s' % ((__content_139818181960344 if (__content_139818181960344 is not None) else ''), ' ', (__content_139818181960344_1046 if (__content_139818181960344_1046 is not None) else ''), ))
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
                            __append('</td>')
                            __append('\n                                ')

                            # <Static value=<_ast.Dict object at 0x7f29f401ff60> name=None at 7f29f401ff28> -> __attrs_139818164130200
                            __attrs_139818164130200 = _static_139818164158304

                            # <td ... (24:32)
                            # --------------------------------------------------------
                            __append('<td')
                            __append(' class="number"')
                            __append('>')

                            # <Interpolation value=<Substitution '${ship.intro_date}' (24:51)> braces_required=True translation=False at 7f29f4019278> -> __content_139818181960344
                            __token = 1151
                            __token = 1153
                            __content_139818181960344 = _lookup_attr(getitem('ship'), 'intro_date')
                            __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                            __content_139818181960344 = __content_139818181960344
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
                            __append('</td>')
                            __append('\n                                ')

                            # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164130760
                            __attrs_139818164130760 = _static_139818165914032

                            # <td ... (25:32)
                            # --------------------------------------------------------
                            __append('<td')
                            __append('>')

                            # <Interpolation value=<Substitution '${base_lang_strings[ship.get_str_type_info()]}' (25:36)> braces_required=True translation=False at 7f29f40194a8> -> __content_139818181960344
                            __token = 1211
                            __token = 1213
                            __content_139818181960344 = getitem('base_lang_strings')[_lookup_attr(getitem('ship'), 'get_str_type_info')()]
                            __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                            __content_139818181960344 = __content_139818181960344
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
                            __append('</td>')
                            __append('\n                                ')

                            # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164131320
                            __attrs_139818164131320 = _static_139818165914032

                            # <td ... (26:32)
                            # --------------------------------------------------------
                            __append('<td')
                            __append('>')

                            # <Interpolation value=<Substitution '${int(ship.speed)} mph' (26:36)> braces_required=True translation=False at 7f29f40196d8> -> __content_139818181960344
                            __token = 1299
                            __token = 1301
                            __content_139818181960344 = int(_lookup_attr(getitem('ship'), 'speed'))
                            __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                            __content_139818181960344 = ('%s%s' % ((__content_139818181960344 if (__content_139818181960344 is not None) else ''), ' mph', ))
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
                            __append('</td>')
                            __append('\n                            ')
                            __append('</tr>')
                            __append('\n                        ')
                        __append('\n                    ')
                        ____index_139818164156512 -= 1
                        if (____index_139818164156512 > 0):
                            __append('')
                    if (__backup_ship_139818165263776 is __marker):
                        del econtext['ship']
                    else:
                        econtext['ship'] = __backup_ship_139818165263776
                    __append('\n                ')
                    __append('</tbody>')
                    __append('\n            ')
                    __append('</table>')
                    __append('\n        ')
                    ____index_139818165077664 -= 1
                    if (____index_139818165077664 > 0):
                        __append('')
                if (__backup_roster_139818164546360 is __marker):
                    del econtext['roster']
                else:
                    econtext['roster'] = __backup_roster_139818164546360
                __append('\n    ')
                __append('</div>')
                __append('\n\n')
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
            if (__backup_macroname_139818164339080 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139818164339080
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }