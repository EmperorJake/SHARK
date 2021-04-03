# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/fish1672/src/docs_templates/code_reference.pt'
__tokens = {157: ('${len(ships)} ships', 5, 11), 159: ('len(ships)', 5, 13), 237: ('doc_helper.get_ships_by_subclass()', 7, 41), 333: ('doc_helper.get_props_to_print_in_code_reference(subclass)', 8, 59), 413: ('${subclass.__name__}', 9, 20), 415: ('subclass.__name__', 9, 22), 482: ('${subclass.__doc__}', 10, 19), 484: ('subclass.__doc__', 10, 21), 720: ('props_to_print[subclass]', 14, 51), 833: ('${prop}', 15, 86), 835: ('prop', 15, 88), 1022: ('doc_helper.get_ships_by_subclass()[subclass]', 20, 48), 1163: ('props_to_print[subclass]', 22, 61), 1230: ('${props_to_print[ship][prop_name]}', 23, 40), 1232: ('props_to_print[ship][prop_name]', 23, 42), 1372: ('dir(ship)', 25, 57), 2016: ('sorted(ships, key=doc_helper.get_base_numeric_id)', 45, 46), 2121: ('${vehicle.numeric_id}', 47, 28), 2123: ('vehicle.numeric_id', 47, 30), 2176: ('${vehicle.id}', 48, 28), 2178: ('vehicle.id', 48, 30), 2223: ('${vehicle.title}', 49, 28), 2225: ('vehicle.title', 49, 30), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.py26 import lookup_attr as _lookup_attr

_static_139865821331864 = {'class': 'table table-striped table-condensed table-bordered', }
_static_139865820387592 = {'style': 'background-color:#eee; vertical-align:top', }
_static_139865821428536 = {'style': 'font-size:84%;', 'class': 'table table-striped table-condensed table-bordered', }
_static_139865820509632 = {'class': 'span12', }
_static_139865822210704 = {}
_static_139865820626392 = 'load:main_template.pt'

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
            __backup_macroname_139865820958152 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f350c8dfdd8> name=None at 7f350c8dff60> -> __value
            __value = _static_139865820626392
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820510864
                __attrs_139865820510864 = _static_139865822210704

                # <div ... (2:0)
                # --------------------------------------------------------
                __append('<div')
                __append('>')
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f350c8c35c0> name=None at 7f350c8c3400> -> __attrs_139865820511144
                __attrs_139865820511144 = _static_139865820509632

                # <div ... (3:4)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="span12"')
                __append('>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820511480
                __attrs_139865820511480 = _static_139865822210704

                # <h2 ... (4:8)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('Code Reference')
                __append('</h2>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820510024
                __attrs_139865820510024 = _static_139865822210704

                # <p ... (5:8)
                # --------------------------------------------------------
                __append('<p')
                __append('>')

                # <Interpolation value=<Substitution '${len(ships)} ships' (5:11)> braces_required=True translation=False at 7f350c8c30b8> -> __content_139865838111856
                __token = 157
                __token = 159
                __content_139865838111856 = len(getitem('ships'))
                __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
                __content_139865838111856 = ('%s%s' % ((__content_139865838111856 if (__content_139865838111856 is not None) else ''), ' ships', ))
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
                __append('</p>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820508456
                __attrs_139865820508456 = _static_139865822210704

                # <hr ... (6:8)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n        ')
                __backup_subclass_139865821090648 = get('subclass', __marker)

                # <Value 'doc_helper.get_ships_by_subclass()' (7:41)> -> __iterator
                __token = 237
                __iterator = _lookup_attr(getitem('doc_helper'), 'get_ships_by_subclass')()
                (__iterator, ____index_139865820508512, ) = getitem('repeat')('subclass', __iterator)
                econtext['subclass'] = None
                for __item in __iterator:
                    econtext['subclass'] = __item
                    __append('\n            ')
                    __backup_props_to_print_139865821892000 = get('props_to_print', __marker)

                    # <Value 'doc_helper.get_props_to_print_in_code_reference(subclass)' (8:59)> -> __value
                    __token = 333
                    __value = _lookup_attr(getitem('doc_helper'), 'get_props_to_print_in_code_reference')(getitem('subclass'))
                    econtext['props_to_print'] = __value
                    __append('\n                ')

                    # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821428424
                    __attrs_139865821428424 = _static_139865822210704

                    # <h4 ... (9:16)
                    # --------------------------------------------------------
                    __append('<h4')
                    __append('>')

                    # <Interpolation value=<Substitution '${subclass.__name__} ' (9:20)> braces_required=True translation=False at 7f350c9a3400> -> __content_139865838111856
                    __token = 413
                    __token = 415
                    __content_139865838111856 = _lookup_attr(getitem('subclass'), '__name__')
                    __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
                    __content_139865838111856 = ('%s%s' % ((__content_139865838111856 if (__content_139865838111856 is not None) else ''), ' ', ))
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

                    # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821429320
                    __attrs_139865821429320 = _static_139865822210704

                    # <small ... (9:41)
                    # --------------------------------------------------------
                    __append('<small')
                    __append('>')
                    __append('Subclass')
                    __append('</small>')
                    __append('</h4>')
                    __append('\n                ')

                    # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821427472
                    __attrs_139865821427472 = _static_139865822210704

                    # <p ... (10:16)
                    # --------------------------------------------------------
                    __append('<p')
                    __append('>')

                    # <Interpolation value=<Substitution '${subclass.__doc__}' (10:19)> braces_required=True translation=False at 7f350c9a3828> -> __content_139865838111856
                    __token = 482
                    __token = 484
                    __content_139865838111856 = _lookup_attr(getitem('subclass'), '__doc__')
                    __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
                    __content_139865838111856 = __content_139865838111856
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
                    __append('</p>')
                    __append('\n                ')

                    # <Static value=<_ast.Dict object at 0x7f350c9a3b38> name=None at 7f350c9a3b00> -> __attrs_139865821426240
                    __attrs_139865821426240 = _static_139865821428536

                    # <table ... (11:16)
                    # --------------------------------------------------------
                    __append('<table')
                    __append(' style="font-size:84%;"')
                    __append(' class="table table-striped table-condensed table-bordered"')
                    __append('>')
                    __append('\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821426296
                    __attrs_139865821426296 = _static_139865822210704

                    # <thead ... (12:20)
                    # --------------------------------------------------------
                    __append('<thead')
                    __append('>')
                    __append('\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820387872
                    __attrs_139865820387872 = _static_139865822210704

                    # <tr ... (13:24)
                    # --------------------------------------------------------
                    __append('<tr')
                    __append('>')
                    __append('\n                           ')
                    __backup_prop_139865821425848 = get('prop', __marker)

                    # <Value 'props_to_print[subclass]' (14:51)> -> __iterator
                    __token = 720
                    __iterator = getitem('props_to_print')[getitem('subclass')]
                    (__iterator, ____index_139865820388376, ) = getitem('repeat')('prop', __iterator)
                    econtext['prop'] = None
                    for __item in __iterator:
                        econtext['prop'] = __item
                        __append('\n                                ')

                        # <Static value=<_ast.Dict object at 0x7f350c8a5908> name=None at 7f350c8a58d0> -> __attrs_139865820386864
                        __attrs_139865820386864 = _static_139865820387592

                        # <th ... (15:32)
                        # --------------------------------------------------------
                        __append('<th')
                        __append(' style="background-color:#eee; vertical-align:top"')
                        __append('>')

                        # <Interpolation value=<Substitution '${prop}' (15:86)> braces_required=True translation=False at 7f350c8a5a90> -> __content_139865838111856
                        __token = 833
                        __token = 835
                        __content_139865838111856 = getitem('prop')
                        __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
                        __content_139865838111856 = __content_139865838111856
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
                        __append('</th>')
                        __append('\n                            ')
                        ____index_139865820388376 -= 1
                        if (____index_139865820388376 > 0):
                            __append('')
                    if (__backup_prop_139865821425848 is __marker):
                        del econtext['prop']
                    else:
                        econtext['prop'] = __backup_prop_139865821425848
                    __append('\n                        ')
                    __append('</tr>')
                    __append('\n                    ')
                    __append('</thead>')
                    __append('\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820385968
                    __attrs_139865820385968 = _static_139865822210704

                    # <tbody ... (19:20)
                    # --------------------------------------------------------
                    __append('<tbody')
                    __append('>')
                    __append('\n                        ')
                    __backup_ship_139865820387312 = get('ship', __marker)

                    # <Value 'doc_helper.get_ships_by_subclass()[subclass]' (20:48)> -> __iterator
                    __token = 1022
                    __iterator = _lookup_attr(getitem('doc_helper'), 'get_ships_by_subclass')()[getitem('subclass')]
                    (__iterator, ____index_139865820387928, ) = getitem('repeat')('ship', __iterator)
                    econtext['ship'] = None
                    for __item in __iterator:
                        econtext['ship'] = __item
                        __append('\n                            ')

                        # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821334776
                        __attrs_139865821334776 = _static_139865822210704

                        # <tr ... (21:28)
                        # --------------------------------------------------------
                        __append('<tr')
                        __append('>')
                        __append('\n                                ')
                        __backup_prop_name_139865820572976 = get('prop_name', __marker)

                        # <Value 'props_to_print[subclass]' (22:61)> -> __iterator
                        __token = 1163
                        __iterator = getitem('props_to_print')[getitem('subclass')]
                        (__iterator, ____index_139865821335336, ) = getitem('repeat')('prop_name', __iterator)
                        econtext['prop_name'] = None
                        for __item in __iterator:
                            econtext['prop_name'] = __item
                            __append('\n                                    ')

                            # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821333096
                            __attrs_139865821333096 = _static_139865822210704

                            # <td ... (23:36)
                            # --------------------------------------------------------
                            __append('<td')
                            __append('>')

                            # <Interpolation value=<Substitution '${props_to_print[ship][prop_name]}' (23:40)> braces_required=True translation=False at 7f350c98c128> -> __content_139865838111856
                            __token = 1230
                            __token = 1232
                            __content_139865838111856 = getitem('props_to_print')[getitem('ship')][getitem('prop_name')]
                            __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
                            __content_139865838111856 = __content_139865838111856
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
                            __append('</td>')
                            __append('\n                                ')
                            ____index_139865821335336 -= 1
                            if (____index_139865821335336 > 0):
                                __append('')
                        if (__backup_prop_name_139865820572976 is __marker):
                            del econtext['prop_name']
                        else:
                            econtext['prop_name'] = __backup_prop_name_139865820572976
                        __append('\n                                ')
                        __backup_prop_139865820774640 = get('prop', __marker)

                        # <Value 'dir(ship)' (25:57)> -> __iterator
                        __token = 1372
                        __iterator = get('dir', dir)(getitem('ship'))
                        (__iterator, ____index_139865821333600, ) = getitem('repeat')('prop', __iterator)
                        econtext['prop'] = None
                        for __item in __iterator:
                            econtext['prop'] = __item
                            __append('\n                                    ')
                            __append('\n                                ')
                            ____index_139865821333600 -= 1
                            if (____index_139865821333600 > 0):
                                __append('')
                        if (__backup_prop_139865820774640 is __marker):
                            del econtext['prop']
                        else:
                            econtext['prop'] = __backup_prop_139865820774640
                        __append('\n                            ')
                        __append('</tr>')
                        __append('\n                        ')
                        ____index_139865820387928 -= 1
                        if (____index_139865820387928 > 0):
                            __append('')
                    if (__backup_ship_139865820387312 is __marker):
                        del econtext['ship']
                    else:
                        econtext['ship'] = __backup_ship_139865820387312
                    __append('\n                    ')
                    __append('</tbody>')
                    __append('\n                ')
                    __append('</table>')
                    __append('\n                ')

                    # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821334496
                    __attrs_139865821334496 = _static_139865822210704

                    # <br ... (32:16)
                    # --------------------------------------------------------
                    __append('<br')
                    __append(' />')
                    __append('\n            ')
                    if (__backup_props_to_print_139865821892000 is __marker):
                        del econtext['props_to_print']
                    else:
                        econtext['props_to_print'] = __backup_props_to_print_139865821892000
                    __append('\n        ')
                    ____index_139865820508512 -= 1
                    if (____index_139865820508512 > 0):
                        __append('')
                if (__backup_subclass_139865821090648 is __marker):
                    del econtext['subclass']
                else:
                    econtext['subclass'] = __backup_subclass_139865821090648
                __append('\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820508904
                __attrs_139865820508904 = _static_139865822210704

                # <hr ... (36:8)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821333880
                __attrs_139865821333880 = _static_139865822210704

                # <h3 ... (37:8)
                # --------------------------------------------------------
                __append('<h3')
                __append('>')
                __append('Numeric IDs')
                __append('</h3>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f350c98c198> name=None at 7f350c98c278> -> __attrs_139865821335112
                __attrs_139865821335112 = _static_139865821331864

                # <table ... (38:8)
                # --------------------------------------------------------
                __append('<table')
                __append(' class="table table-striped table-condensed table-bordered"')
                __append('>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821333320
                __attrs_139865821333320 = _static_139865822210704

                # <thead ... (39:12)
                # --------------------------------------------------------
                __append('<thead')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820777944
                __attrs_139865820777944 = _static_139865822210704

                # <th ... (40:16)
                # --------------------------------------------------------
                __append('<th')
                __append('>')
                __append('Numeric ID')
                __append('</th>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821405928
                __attrs_139865821405928 = _static_139865822210704

                # <th ... (41:16)
                # --------------------------------------------------------
                __append('<th')
                __append('>')
                __append('ID')
                __append('</th>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821409120
                __attrs_139865821409120 = _static_139865822210704

                # <th ... (42:16)
                # --------------------------------------------------------
                __append('<th')
                __append('>')
                __append('Title')
                __append('</th>')
                __append('\n            ')
                __append('</thead>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821406992
                __attrs_139865821406992 = _static_139865822210704

                # <tbody ... (44:12)
                # --------------------------------------------------------
                __append('<tbody')
                __append('>')
                __append('\n                ')
                __backup_vehicle_139865821406880 = get('vehicle', __marker)

                # <Value 'sorted(ships, key=doc_helper.get_base_numeric_id)' (45:46)> -> __iterator
                __token = 2016
                __iterator = get('sorted', sorted)(getitem('ships'), key=_lookup_attr(getitem('doc_helper'), 'get_base_numeric_id'))
                (__iterator, ____index_139865821405872, ) = getitem('repeat')('vehicle', __iterator)
                econtext['vehicle'] = None
                for __item in __iterator:
                    econtext['vehicle'] = __item
                    __append('\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821408952
                    __attrs_139865821408952 = _static_139865822210704

                    # <tr ... (46:20)
                    # --------------------------------------------------------
                    __append('<tr')
                    __append('>')
                    __append('\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865821407888
                    __attrs_139865821407888 = _static_139865822210704

                    # <td ... (47:24)
                    # --------------------------------------------------------
                    __append('<td')
                    __append('>')

                    # <Interpolation value=<Substitution '${vehicle.numeric_id}' (47:28)> braces_required=True translation=False at 7f350c99ea58> -> __content_139865838111856
                    __token = 2121
                    __token = 2123
                    __content_139865838111856 = _lookup_attr(getitem('vehicle'), 'numeric_id')
                    __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
                    __content_139865838111856 = __content_139865838111856
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
                    __append('</td>')
                    __append('\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820295240
                    __attrs_139865820295240 = _static_139865822210704

                    # <td ... (48:24)
                    # --------------------------------------------------------
                    __append('<td')
                    __append('>')

                    # <Interpolation value=<Substitution '${vehicle.id}' (48:28)> braces_required=True translation=False at 7f350c88f320> -> __content_139865838111856
                    __token = 2176
                    __token = 2178
                    __content_139865838111856 = _lookup_attr(getitem('vehicle'), 'id')
                    __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
                    __content_139865838111856 = __content_139865838111856
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
                    __append('</td>')
                    __append('\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f350ca62a90> name=None at 7f350ca62748> -> __attrs_139865820296304
                    __attrs_139865820296304 = _static_139865822210704

                    # <td ... (49:24)
                    # --------------------------------------------------------
                    __append('<td')
                    __append('>')

                    # <Interpolation value=<Substitution '${vehicle.title}' (49:28)> braces_required=True translation=False at 7f350c88f588> -> __content_139865838111856
                    __token = 2223
                    __token = 2225
                    __content_139865838111856 = _lookup_attr(getitem('vehicle'), 'title')
                    __content_139865838111856 = __quote(__content_139865838111856, '\x00', '&#0;', None, False)
                    __content_139865838111856 = __content_139865838111856
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
                    __append('</td>')
                    __append('\n                    ')
                    __append('</tr>')
                    __append('\n                ')
                    ____index_139865821405872 -= 1
                    if (____index_139865821405872 > 0):
                        __append('')
                if (__backup_vehicle_139865821406880 is __marker):
                    del econtext['vehicle']
                else:
                    econtext['vehicle'] = __backup_vehicle_139865821406880
                __append('\n            ')
                __append('</tbody>')
                __append('\n        ')
                __append('</table>')
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
            if (__backup_macroname_139865820958152 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139865820958152
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }