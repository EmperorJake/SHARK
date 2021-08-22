# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/SHARK/src/docs_templates/code_reference.pt'

__tokens = {157: ('${len(ships)} ships', 5, 11), 159: ('len(ships)', 5, 13), 237: ('doc_helper.get_ships_by_subclass()', 7, 41), 333: ('doc_helper.get_props_to_print_in_code_reference(subclass)', 8, 59), 413: ('${subclass.__name__}', 9, 20), 415: ('subclass.__name__', 9, 22), 482: ('${subclass.__doc__}', 10, 19), 484: ('subclass.__doc__', 10, 21), 720: ('props_to_print[subclass]', 14, 51), 833: ('${prop}', 15, 86), 835: ('prop', 15, 88), 1022: ('doc_helper.get_ships_by_subclass()[subclass]', 20, 48), 1163: ('props_to_print[subclass]', 22, 61), 1230: ('${props_to_print[ship][prop_name]}', 23, 40), 1232: ('props_to_print[ship][prop_name]', 23, 42), 1372: ('dir(ship)', 25, 57), 2016: ('sorted(ships, key=doc_helper.get_base_numeric_id)', 45, 46), 2121: ('${vehicle.numeric_id}', 47, 28), 2123: ('vehicle.numeric_id', 47, 30), 2176: ('${vehicle.id}', 48, 28), 2178: ('vehicle.id', 48, 30), 2223: ('${vehicle.title}', 49, 28), 2225: ('vehicle.title', 49, 30), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.utils import lookup_attr as _lookup_attr

_static_140188661517664 = {'class': 'table table-striped table-condensed table-bordered', }
_static_140188664014016 = {'style': 'background-color:#eee; vertical-align:top', }
_static_140188663576416 = {'style': 'font-size:84%;', 'class': 'table table-striped table-condensed table-bordered', }
_static_140188664081280 = {'class': 'span12', }
_static_140188664081520 = 'load:main_template.pt'
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

            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664080320
            __attrs_140188664080320 = _static_140188664645808
            __backup_macroname_140188661574464 = get('macroname', __marker)

            # <Static value=<_ast.Constant object at 0x7f8037862c70> name=None at 7f8037862670> -> __value
            __value = _static_140188664081520
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664078736
                __attrs_140188664078736 = _static_140188664645808

                # <div ... (2:0)
                # --------------------------------------------------------
                __append('<div>\n    ')

                # <Static value=<_ast.Dict object at 0x7f8037862b80> name=None at 7f8037862490> -> __attrs_140188662333008
                __attrs_140188662333008 = _static_140188664081280

                # <div ... (3:4)
                # --------------------------------------------------------
                __append('<div class="span12">\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662331520
                __attrs_140188662331520 = _static_140188664645808

                # <h2 ... (4:8)
                # --------------------------------------------------------
                __append('<h2>Code Reference</h2>\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662331856
                __attrs_140188662331856 = _static_140188664645808

                # <p ... (5:8)
                # --------------------------------------------------------
                __append('<p>')

                # <Interpolation value=<Substitution '${len(ships)} ships' (5:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f80376b7df0> -> __content_140188669528304
                __token = 157
                __token = 159
                __content_140188669528304 = len(getitem('ships'))
                __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
                __content_140188669528304 = ('%s%s' % ((__content_140188669528304 if (__content_140188669528304 is not None) else ''), ' ships', ))
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
                __append('</p>\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662333248
                __attrs_140188662333248 = _static_140188664645808

                # <hr ... (6:8)
                # --------------------------------------------------------
                __append('<hr />\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188662330320
                __attrs_140188662330320 = _static_140188664645808
                __backup_subclass_140188661924048 = get('subclass', __marker)

                # <Value 'doc_helper.get_ships_by_subclass()' (7:41)> -> __iterator
                __token = 237
                __iterator = _lookup_attr(getitem('doc_helper'), 'get_ships_by_subclass')()
                (__iterator, ____index_140188662329456, ) = getitem('repeat')('subclass', __iterator)
                econtext['subclass'] = None
                for __item in __iterator:
                    econtext['subclass'] = __item
                    __append('\n            ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663228448
                    __attrs_140188663228448 = _static_140188664645808
                    __backup_props_to_print_140188663216208 = get('props_to_print', __marker)

                    # <Value 'doc_helper.get_props_to_print_in_code_reference(subclass)' (8:59)> -> __value
                    __token = 333
                    __value = _lookup_attr(getitem('doc_helper'), 'get_props_to_print_in_code_reference')(getitem('subclass'))
                    econtext['props_to_print'] = __value
                    __append('\n                ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663227440
                    __attrs_140188663227440 = _static_140188664645808

                    # <h4 ... (9:16)
                    # --------------------------------------------------------
                    __append('<h4>')

                    # <Interpolation value=<Substitution '${subclass.__name__} ' (9:20)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f8037792d90> -> __content_140188669528304
                    __token = 413
                    __token = 415
                    __content_140188669528304 = _lookup_attr(getitem('subclass'), '__name__')
                    __content_140188669528304 = __quote(__content_140188669528304, '\x00', '&#0;', None, None)
                    __content_140188669528304 = ('%s%s' % ((__content_140188669528304 if (__content_140188669528304 is not None) else ''), ' ', ))
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

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663227776
                    __attrs_140188663227776 = _static_140188664645808

                    # <small ... (9:41)
                    # --------------------------------------------------------
                    __append('<small>Subclass</small></h4>\n                ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663227872
                    __attrs_140188663227872 = _static_140188664645808

                    # <p ... (10:16)
                    # --------------------------------------------------------
                    __append('<p>')

                    # <Interpolation value=<Substitution '${subclass.__doc__}' (10:19)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f8037792a30> -> __content_140188669528304
                    __token = 482
                    __token = 484
                    __content_140188669528304 = _lookup_attr(getitem('subclass'), '__doc__')
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
                    __append('</p>\n                ')

                    # <Static value=<_ast.Dict object at 0x7f80377e7760> name=None at 7f80377e70d0> -> __attrs_140188663575792
                    __attrs_140188663575792 = _static_140188663576416

                    # <table ... (11:16)
                    # --------------------------------------------------------
                    __append('<table style="font-size:84%;" class="table table-striped table-condensed table-bordered">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663576896
                    __attrs_140188663576896 = _static_140188664645808

                    # <thead ... (12:20)
                    # --------------------------------------------------------
                    __append('<thead>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663578096
                    __attrs_140188663578096 = _static_140188664645808

                    # <tr ... (13:24)
                    # --------------------------------------------------------
                    __append('<tr>\n                           ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663576224
                    __attrs_140188663576224 = _static_140188664645808
                    __backup_prop_140188662328336 = get('prop', __marker)

                    # <Value 'props_to_print[subclass]' (14:51)> -> __iterator
                    __token = 720
                    __iterator = getitem('props_to_print')[getitem('subclass')]
                    (__iterator, ____index_140188664014832, ) = getitem('repeat')('prop', __iterator)
                    econtext['prop'] = None
                    for __item in __iterator:
                        econtext['prop'] = __item
                        __append('\n                                ')

                        # <Static value=<_ast.Dict object at 0x7f80378524c0> name=None at 7f8037852460> -> __attrs_140188664013152
                        __attrs_140188664013152 = _static_140188664014016

                        # <th ... (15:32)
                        # --------------------------------------------------------
                        __append('<th style="background-color:#eee; vertical-align:top">')

                        # <Interpolation value=<Substitution '${prop}' (15:86)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f8037852400> -> __content_140188669528304
                        __token = 833
                        __token = 835
                        __content_140188669528304 = getitem('prop')
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
                        __append('</th>\n                            ')
                        ____index_140188664014832 -= 1
                        if (____index_140188664014832 > 0):
                            __append('')
                    if (__backup_prop_140188662328336 is __marker):
                        del econtext['prop']
                    else:
                        econtext['prop'] = __backup_prop_140188662328336
                    __append('\n                        </tr>\n                    </thead>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664015456
                    __attrs_140188664015456 = _static_140188664645808

                    # <tbody ... (19:20)
                    # --------------------------------------------------------
                    __append('<tbody>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664013968
                    __attrs_140188664013968 = _static_140188664645808
                    __backup_ship_140188662716400 = get('ship', __marker)

                    # <Value 'doc_helper.get_ships_by_subclass()[subclass]' (20:48)> -> __iterator
                    __token = 1022
                    __iterator = _lookup_attr(getitem('doc_helper'), 'get_ships_by_subclass')()[getitem('subclass')]
                    (__iterator, ____index_140188664016560, ) = getitem('repeat')('ship', __iterator)
                    econtext['ship'] = None
                    for __item in __iterator:
                        econtext['ship'] = __item
                        __append('\n                            ')

                        # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663568224
                        __attrs_140188663568224 = _static_140188664645808

                        # <tr ... (21:28)
                        # --------------------------------------------------------
                        __append('<tr>\n                                ')

                        # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663569520
                        __attrs_140188663569520 = _static_140188664645808
                        __backup_prop_name_140188662327760 = get('prop_name', __marker)

                        # <Value 'props_to_print[subclass]' (22:61)> -> __iterator
                        __token = 1163
                        __iterator = getitem('props_to_print')[getitem('subclass')]
                        (__iterator, ____index_140188663567936, ) = getitem('repeat')('prop_name', __iterator)
                        econtext['prop_name'] = None
                        for __item in __iterator:
                            econtext['prop_name'] = __item
                            __append('\n                                    ')

                            # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663570336
                            __attrs_140188663570336 = _static_140188664645808

                            # <td ... (23:36)
                            # --------------------------------------------------------
                            __append('<td>')

                            # <Interpolation value=<Substitution '${props_to_print[ship][prop_name]}' (23:40)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f80377e5940> -> __content_140188669528304
                            __token = 1230
                            __token = 1232
                            __content_140188669528304 = getitem('props_to_print')[getitem('ship')][getitem('prop_name')]
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
                            ____index_140188663567936 -= 1
                            if (____index_140188663567936 > 0):
                                __append('')
                        if (__backup_prop_name_140188662327760 is __marker):
                            del econtext['prop_name']
                        else:
                            econtext['prop_name'] = __backup_prop_name_140188662327760
                        __append('\n                                ')

                        # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663567168
                        __attrs_140188663567168 = _static_140188664645808
                        __backup_prop_140188662522496 = get('prop', __marker)

                        # <Value 'dir(ship)' (25:57)> -> __iterator
                        __token = 1372
                        __iterator = get('dir', dir)(getitem('ship'))
                        (__iterator, ____index_140188661516656, ) = getitem('repeat')('prop', __iterator)
                        econtext['prop'] = None
                        for __item in __iterator:
                            econtext['prop'] = __item
                            __append('\n                                    \n                                ')
                            ____index_140188661516656 -= 1
                            if (____index_140188661516656 > 0):
                                __append('')
                        if (__backup_prop_140188662522496 is __marker):
                            del econtext['prop']
                        else:
                            econtext['prop'] = __backup_prop_140188662522496
                        __append('\n                            </tr>\n                        ')
                        ____index_140188664016560 -= 1
                        if (____index_140188664016560 > 0):
                            __append('')
                    if (__backup_ship_140188662716400 is __marker):
                        del econtext['ship']
                    else:
                        econtext['ship'] = __backup_ship_140188662716400
                    __append('\n                    </tbody>\n                </table>\n                ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188664014640
                    __attrs_140188664014640 = _static_140188664645808

                    # <br ... (32:16)
                    # --------------------------------------------------------
                    __append('<br />\n            ')
                    if (__backup_props_to_print_140188663216208 is __marker):
                        del econtext['props_to_print']
                    else:
                        econtext['props_to_print'] = __backup_props_to_print_140188663216208
                    __append('\n        ')
                    ____index_140188662329456 -= 1
                    if (____index_140188662329456 > 0):
                        __append('')
                if (__backup_subclass_140188661924048 is __marker):
                    del econtext['subclass']
                else:
                    econtext['subclass'] = __backup_subclass_140188661924048
                __append('\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663228832
                __attrs_140188663228832 = _static_140188664645808

                # <hr ... (36:8)
                # --------------------------------------------------------
                __append('<hr />\n        ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188661517232
                __attrs_140188661517232 = _static_140188664645808

                # <h3 ... (37:8)
                # --------------------------------------------------------
                __append('<h3>Numeric IDs</h3>\n        ')

                # <Static value=<_ast.Dict object at 0x7f80375f0d60> name=None at 7f80375f0100> -> __attrs_140188661515504
                __attrs_140188661515504 = _static_140188661517664

                # <table ... (38:8)
                # --------------------------------------------------------
                __append('<table class="table table-striped table-condensed table-bordered">\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188661518144
                __attrs_140188661518144 = _static_140188664645808

                # <thead ... (39:12)
                # --------------------------------------------------------
                __append('<thead>\n                ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663697904
                __attrs_140188663697904 = _static_140188664645808

                # <th ... (40:16)
                # --------------------------------------------------------
                __append('<th>Numeric ID</th>\n                ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663699920
                __attrs_140188663699920 = _static_140188664645808

                # <th ... (41:16)
                # --------------------------------------------------------
                __append('<th>ID</th>\n                ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663699440
                __attrs_140188663699440 = _static_140188664645808

                # <th ... (42:16)
                # --------------------------------------------------------
                __append('<th>Title</th>\n            </thead>\n            ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663700304
                __attrs_140188663700304 = _static_140188664645808

                # <tbody ... (44:12)
                # --------------------------------------------------------
                __append('<tbody>\n                ')

                # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663700352
                __attrs_140188663700352 = _static_140188664645808
                __backup_vehicle_140188661925872 = get('vehicle', __marker)

                # <Value 'sorted(ships, key=doc_helper.get_base_numeric_id)' (45:46)> -> __iterator
                __token = 2016
                __iterator = get('sorted', sorted)(getitem('ships'), key=_lookup_attr(getitem('doc_helper'), 'get_base_numeric_id'))
                (__iterator, ____index_140188663697664, ) = getitem('repeat')('vehicle', __iterator)
                econtext['vehicle'] = None
                for __item in __iterator:
                    econtext['vehicle'] = __item
                    __append('\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663198480
                    __attrs_140188663198480 = _static_140188664645808

                    # <tr ... (46:20)
                    # --------------------------------------------------------
                    __append('<tr>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663198192
                    __attrs_140188663198192 = _static_140188664645808

                    # <td ... (47:24)
                    # --------------------------------------------------------
                    __append('<td>')

                    # <Interpolation value=<Substitution '${vehicle.numeric_id}' (47:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f803778b340> -> __content_140188669528304
                    __token = 2121
                    __token = 2123
                    __content_140188669528304 = _lookup_attr(getitem('vehicle'), 'numeric_id')
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
                    __append('</td>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663199248
                    __attrs_140188663199248 = _static_140188664645808

                    # <td ... (48:24)
                    # --------------------------------------------------------
                    __append('<td>')

                    # <Interpolation value=<Substitution '${vehicle.id}' (48:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f803778bbe0> -> __content_140188669528304
                    __token = 2176
                    __token = 2178
                    __content_140188669528304 = _lookup_attr(getitem('vehicle'), 'id')
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
                    __append('</td>\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f80378ec8b0> name=None at 7f80378ec2e0> -> __attrs_140188663198864
                    __attrs_140188663198864 = _static_140188664645808

                    # <td ... (49:24)
                    # --------------------------------------------------------
                    __append('<td>')

                    # <Interpolation value=<Substitution '${vehicle.title}' (49:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f803778b2b0> -> __content_140188669528304
                    __token = 2223
                    __token = 2225
                    __content_140188669528304 = _lookup_attr(getitem('vehicle'), 'title')
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
                    __append('</td>\n                    </tr>\n                ')
                    ____index_140188663697664 -= 1
                    if (____index_140188663697664 > 0):
                        __append('')
                if (__backup_vehicle_140188661925872 is __marker):
                    del econtext['vehicle']
                else:
                    econtext['vehicle'] = __backup_vehicle_140188661925872
                __append('\n            </tbody>\n        </table>\n    </div>\n\n</div>')
            _slots = econtext['__slot_body'] = _deque((__fill_body, ))

            # <Value 'load:main_template.pt' (1:36)> -> __macro
            __token = 36
            __macro = 'main_template.pt'
            __macro = __loader(__macro)
            __token = 36
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140188661574464 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140188661574464
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }