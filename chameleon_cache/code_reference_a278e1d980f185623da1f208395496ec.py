# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/docs_templates/code_reference.pt'
__tokens = {157: ('${len(ships)} ships', 5, 11), 159: ('len(ships)', 5, 13), 237: ('doc_helper.get_ships_by_subclass()', 7, 41), 333: ('doc_helper.get_props_to_print_in_code_reference(subclass)', 8, 59), 413: ('${subclass.__name__}', 9, 20), 415: ('subclass.__name__', 9, 22), 482: ('${subclass.__doc__}', 10, 19), 484: ('subclass.__doc__', 10, 21), 720: ('props_to_print[subclass]', 14, 51), 833: ('${prop}', 15, 86), 835: ('prop', 15, 88), 1022: ('doc_helper.get_ships_by_subclass()[subclass]', 20, 48), 1163: ('props_to_print[subclass]', 22, 61), 1230: ('${props_to_print[ship][prop_name]}', 23, 40), 1232: ('props_to_print[ship][prop_name]', 23, 42), 1372: ('dir(ship)', 25, 57), 2016: ('sorted(ships, key=doc_helper.get_base_numeric_id)', 45, 46), 2121: ('${vehicle.numeric_id}', 47, 28), 2123: ('vehicle.numeric_id', 47, 30), 2176: ('${vehicle.id}', 48, 28), 2178: ('vehicle.id', 48, 30), 2223: ('${vehicle.title}', 49, 28), 2225: ('vehicle.title', 49, 30), 36: ('load:main_template.pt', 1, 36), 36: ('load:main_template.pt', 1, 36)}

from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.py26 import lookup_attr as _lookup_attr

_static_139818164334944 = {'class': 'table table-striped table-condensed table-bordered', }
_static_139818164371184 = {'style': 'background-color:#eee; vertical-align:top', }
_static_139818164131880 = {'style': 'font-size:84%;', 'class': 'table table-striped table-condensed table-bordered', }
_static_139818164078352 = {'class': 'span12', }
_static_139818165914032 = {}
_static_139818164077736 = 'load:main_template.pt'

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
            __backup_macroname_139818165428040 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f29f400c4a8> name=None at 7f29f400cfd0> -> __value
            __value = _static_139818164077736
            econtext['macroname'] = __value

            def __fill_body(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164080200
                __attrs_139818164080200 = _static_139818165914032

                # <div ... (2:0)
                # --------------------------------------------------------
                __append('<div')
                __append('>')
                __append('\n    ')

                # <Static value=<_ast.Dict object at 0x7f29f400c710> name=None at 7f29f400c908> -> __attrs_139818164079808
                __attrs_139818164079808 = _static_139818164078352

                # <div ... (3:4)
                # --------------------------------------------------------
                __append('<div')
                __append(' class="span12"')
                __append('>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164077176
                __attrs_139818164077176 = _static_139818165914032

                # <h2 ... (4:8)
                # --------------------------------------------------------
                __append('<h2')
                __append('>')
                __append('Code Reference')
                __append('</h2>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164076672
                __attrs_139818164076672 = _static_139818165914032

                # <p ... (5:8)
                # --------------------------------------------------------
                __append('<p')
                __append('>')

                # <Interpolation value=<Substitution '${len(ships)} ships' (5:11)> braces_required=True translation=False at 7f29f400c630> -> __content_139818181960344
                __token = 157
                __token = 159
                __content_139818181960344 = len(getitem('ships'))
                __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                __content_139818181960344 = ('%s%s' % ((__content_139818181960344 if (__content_139818181960344 is not None) else ''), ' ships', ))
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
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164077512
                __attrs_139818164077512 = _static_139818165914032

                # <hr ... (6:8)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n        ')
                __backup_subclass_139818164420680 = get('subclass', __marker)

                # <Value 'doc_helper.get_ships_by_subclass()' (7:41)> -> __iterator
                __token = 237
                __iterator = _lookup_attr(getitem('doc_helper'), 'get_ships_by_subclass')()
                (__iterator, ____index_139818164080424, ) = getitem('repeat')('subclass', __iterator)
                econtext['subclass'] = None
                for __item in __iterator:
                    econtext['subclass'] = __item
                    __append('\n            ')
                    __backup_props_to_print_139818164561848 = get('props_to_print', __marker)

                    # <Value 'doc_helper.get_props_to_print_in_code_reference(subclass)' (8:59)> -> __value
                    __token = 333
                    __value = _lookup_attr(getitem('doc_helper'), 'get_props_to_print_in_code_reference')(getitem('subclass'))
                    econtext['props_to_print'] = __value
                    __append('\n                ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164130368
                    __attrs_139818164130368 = _static_139818165914032

                    # <h4 ... (9:16)
                    # --------------------------------------------------------
                    __append('<h4')
                    __append('>')

                    # <Interpolation value=<Substitution '${subclass.__name__} ' (9:20)> braces_required=True translation=False at 7f29f40191d0> -> __content_139818181960344
                    __token = 413
                    __token = 415
                    __content_139818181960344 = _lookup_attr(getitem('subclass'), '__name__')
                    __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                    __content_139818181960344 = ('%s%s' % ((__content_139818181960344 if (__content_139818181960344 is not None) else ''), ' ', ))
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

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164131208
                    __attrs_139818164131208 = _static_139818165914032

                    # <small ... (9:41)
                    # --------------------------------------------------------
                    __append('<small')
                    __append('>')
                    __append('Subclass')
                    __append('</small>')
                    __append('</h4>')
                    __append('\n                ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164130984
                    __attrs_139818164130984 = _static_139818165914032

                    # <p ... (10:16)
                    # --------------------------------------------------------
                    __append('<p')
                    __append('>')

                    # <Interpolation value=<Substitution '${subclass.__doc__}' (10:19)> braces_required=True translation=False at 7f29f4019b70> -> __content_139818181960344
                    __token = 482
                    __token = 484
                    __content_139818181960344 = _lookup_attr(getitem('subclass'), '__doc__')
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
                    __append('</p>')
                    __append('\n                ')

                    # <Static value=<_ast.Dict object at 0x7f29f4019828> name=None at 7f29f4019a90> -> __attrs_139818164133616
                    __attrs_139818164133616 = _static_139818164131880

                    # <table ... (11:16)
                    # --------------------------------------------------------
                    __append('<table')
                    __append(' style="font-size:84%;"')
                    __append(' class="table table-striped table-condensed table-bordered"')
                    __append('>')
                    __append('\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164133504
                    __attrs_139818164133504 = _static_139818165914032

                    # <thead ... (12:20)
                    # --------------------------------------------------------
                    __append('<thead')
                    __append('>')
                    __append('\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164906136
                    __attrs_139818164906136 = _static_139818165914032

                    # <tr ... (13:24)
                    # --------------------------------------------------------
                    __append('<tr')
                    __append('>')
                    __append('\n                           ')
                    __backup_prop_139818164013768 = get('prop', __marker)

                    # <Value 'props_to_print[subclass]' (14:51)> -> __iterator
                    __token = 720
                    __iterator = getitem('props_to_print')[getitem('subclass')]
                    (__iterator, ____index_139818164650840, ) = getitem('repeat')('prop', __iterator)
                    econtext['prop'] = None
                    for __item in __iterator:
                        econtext['prop'] = __item
                        __append('\n                                ')

                        # <Static value=<_ast.Dict object at 0x7f29f4053ef0> name=None at 7f29f40985c0> -> __attrs_139818164368608
                        __attrs_139818164368608 = _static_139818164371184

                        # <th ... (15:32)
                        # --------------------------------------------------------
                        __append('<th')
                        __append(' style="background-color:#eee; vertical-align:top"')
                        __append('>')

                        # <Interpolation value=<Substitution '${prop}' (15:86)> braces_required=True translation=False at 7f29f40533c8> -> __content_139818181960344
                        __token = 833
                        __token = 835
                        __content_139818181960344 = getitem('prop')
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
                        __append('</th>')
                        __append('\n                            ')
                        ____index_139818164650840 -= 1
                        if (____index_139818164650840 > 0):
                            __append('')
                    if (__backup_prop_139818164013768 is __marker):
                        del econtext['prop']
                    else:
                        econtext['prop'] = __backup_prop_139818164013768
                    __append('\n                        ')
                    __append('</tr>')
                    __append('\n                    ')
                    __append('</thead>')
                    __append('\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164367600
                    __attrs_139818164367600 = _static_139818165914032

                    # <tbody ... (19:20)
                    # --------------------------------------------------------
                    __append('<tbody')
                    __append('>')
                    __append('\n                        ')
                    __backup_ship_139818164504168 = get('ship', __marker)

                    # <Value 'doc_helper.get_ships_by_subclass()[subclass]' (20:48)> -> __iterator
                    __token = 1022
                    __iterator = _lookup_attr(getitem('doc_helper'), 'get_ships_by_subclass')()[getitem('subclass')]
                    (__iterator, ____index_139818164369728, ) = getitem('repeat')('ship', __iterator)
                    econtext['ship'] = None
                    for __item in __iterator:
                        econtext['ship'] = __item
                        __append('\n                            ')

                        # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164369224
                        __attrs_139818164369224 = _static_139818165914032

                        # <tr ... (21:28)
                        # --------------------------------------------------------
                        __append('<tr')
                        __append('>')
                        __append('\n                                ')
                        __backup_prop_name_139818164335616 = get('prop_name', __marker)

                        # <Value 'props_to_print[subclass]' (22:61)> -> __iterator
                        __token = 1163
                        __iterator = getitem('props_to_print')[getitem('subclass')]
                        (__iterator, ____index_139818164370120, ) = getitem('repeat')('prop_name', __iterator)
                        econtext['prop_name'] = None
                        for __item in __iterator:
                            econtext['prop_name'] = __item
                            __append('\n                                    ')

                            # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164368664
                            __attrs_139818164368664 = _static_139818165914032

                            # <td ... (23:36)
                            # --------------------------------------------------------
                            __append('<td')
                            __append('>')

                            # <Interpolation value=<Substitution '${props_to_print[ship][prop_name]}' (23:40)> braces_required=True translation=False at 7f29f4053048> -> __content_139818181960344
                            __token = 1230
                            __token = 1232
                            __content_139818181960344 = getitem('props_to_print')[getitem('ship')][getitem('prop_name')]
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
                            ____index_139818164370120 -= 1
                            if (____index_139818164370120 > 0):
                                __append('')
                        if (__backup_prop_name_139818164335616 is __marker):
                            del econtext['prop_name']
                        else:
                            econtext['prop_name'] = __backup_prop_name_139818164335616
                        __append('\n                                ')
                        __backup_prop_139818164560448 = get('prop', __marker)

                        # <Value 'dir(ship)' (25:57)> -> __iterator
                        __token = 1372
                        __iterator = get('dir', dir)(getitem('ship'))
                        (__iterator, ____index_139818164368160, ) = getitem('repeat')('prop', __iterator)
                        econtext['prop'] = None
                        for __item in __iterator:
                            econtext['prop'] = __item
                            __append('\n                                    ')
                            __append('\n                                ')
                            ____index_139818164368160 -= 1
                            if (____index_139818164368160 > 0):
                                __append('')
                        if (__backup_prop_139818164560448 is __marker):
                            del econtext['prop']
                        else:
                            econtext['prop'] = __backup_prop_139818164560448
                        __append('\n                            ')
                        __append('</tr>')
                        __append('\n                        ')
                        ____index_139818164369728 -= 1
                        if (____index_139818164369728 > 0):
                            __append('')
                    if (__backup_ship_139818164504168 is __marker):
                        del econtext['ship']
                    else:
                        econtext['ship'] = __backup_ship_139818164504168
                    __append('\n                    ')
                    __append('</tbody>')
                    __append('\n                ')
                    __append('</table>')
                    __append('\n                ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164370344
                    __attrs_139818164370344 = _static_139818165914032

                    # <br ... (32:16)
                    # --------------------------------------------------------
                    __append('<br')
                    __append(' />')
                    __append('\n            ')
                    if (__backup_props_to_print_139818164561848 is __marker):
                        del econtext['props_to_print']
                    else:
                        econtext['props_to_print'] = __backup_props_to_print_139818164561848
                    __append('\n        ')
                    ____index_139818164080424 -= 1
                    if (____index_139818164080424 > 0):
                        __append('')
                if (__backup_subclass_139818164420680 is __marker):
                    del econtext['subclass']
                else:
                    econtext['subclass'] = __backup_subclass_139818164420680
                __append('\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164130872
                __attrs_139818164130872 = _static_139818165914032

                # <hr ... (36:8)
                # --------------------------------------------------------
                __append('<hr')
                __append(' />')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164337576
                __attrs_139818164337576 = _static_139818165914032

                # <h3 ... (37:8)
                # --------------------------------------------------------
                __append('<h3')
                __append('>')
                __append('Numeric IDs')
                __append('</h3>')
                __append('\n        ')

                # <Static value=<_ast.Dict object at 0x7f29f404b160> name=None at 7f29f404bfd0> -> __attrs_139818164337296
                __attrs_139818164337296 = _static_139818164334944

                # <table ... (38:8)
                # --------------------------------------------------------
                __append('<table')
                __append(' class="table table-striped table-condensed table-bordered"')
                __append('>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164337128
                __attrs_139818164337128 = _static_139818165914032

                # <thead ... (39:12)
                # --------------------------------------------------------
                __append('<thead')
                __append('>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164336568
                __attrs_139818164336568 = _static_139818165914032

                # <th ... (40:16)
                # --------------------------------------------------------
                __append('<th')
                __append('>')
                __append('Numeric ID')
                __append('</th>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818165079456
                __attrs_139818165079456 = _static_139818165914032

                # <th ... (41:16)
                # --------------------------------------------------------
                __append('<th')
                __append('>')
                __append('ID')
                __append('</th>')
                __append('\n                ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164336904
                __attrs_139818164336904 = _static_139818165914032

                # <th ... (42:16)
                # --------------------------------------------------------
                __append('<th')
                __append('>')
                __append('Title')
                __append('</th>')
                __append('\n            ')
                __append('</thead>')
                __append('\n            ')

                # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164444408
                __attrs_139818164444408 = _static_139818165914032

                # <tbody ... (44:12)
                # --------------------------------------------------------
                __append('<tbody')
                __append('>')
                __append('\n                ')
                __backup_vehicle_139818164562688 = get('vehicle', __marker)

                # <Value 'sorted(ships, key=doc_helper.get_base_numeric_id)' (45:46)> -> __iterator
                __token = 2016
                __iterator = get('sorted', sorted)(getitem('ships'), key=_lookup_attr(getitem('doc_helper'), 'get_base_numeric_id'))
                (__iterator, ____index_139818164443568, ) = getitem('repeat')('vehicle', __iterator)
                econtext['vehicle'] = None
                for __item in __iterator:
                    econtext['vehicle'] = __item
                    __append('\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164442616
                    __attrs_139818164442616 = _static_139818165914032

                    # <tr ... (46:20)
                    # --------------------------------------------------------
                    __append('<tr')
                    __append('>')
                    __append('\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164444968
                    __attrs_139818164444968 = _static_139818165914032

                    # <td ... (47:24)
                    # --------------------------------------------------------
                    __append('<td')
                    __append('>')

                    # <Interpolation value=<Substitution '${vehicle.numeric_id}' (47:28)> braces_required=True translation=False at 7f29f4065c18> -> __content_139818181960344
                    __token = 2121
                    __token = 2123
                    __content_139818181960344 = _lookup_attr(getitem('vehicle'), 'numeric_id')
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
                    __append('\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164441608
                    __attrs_139818164441608 = _static_139818165914032

                    # <td ... (48:24)
                    # --------------------------------------------------------
                    __append('<td')
                    __append('>')

                    # <Interpolation value=<Substitution '${vehicle.id}' (48:28)> braces_required=True translation=False at 7f29f4065668> -> __content_139818181960344
                    __token = 2176
                    __token = 2178
                    __content_139818181960344 = _lookup_attr(getitem('vehicle'), 'id')
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
                    __append('\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f29f41cc9b0> name=None at 7f29f41ccc88> -> __attrs_139818164442392
                    __attrs_139818164442392 = _static_139818165914032

                    # <td ... (49:24)
                    # --------------------------------------------------------
                    __append('<td')
                    __append('>')

                    # <Interpolation value=<Substitution '${vehicle.title}' (49:28)> braces_required=True translation=False at 7f29f40651d0> -> __content_139818181960344
                    __token = 2223
                    __token = 2225
                    __content_139818181960344 = _lookup_attr(getitem('vehicle'), 'title')
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
                    __append('\n                    ')
                    __append('</tr>')
                    __append('\n                ')
                    ____index_139818164443568 -= 1
                    if (____index_139818164443568 > 0):
                        __append('')
                if (__backup_vehicle_139818164562688 is __marker):
                    del econtext['vehicle']
                else:
                    econtext['vehicle'] = __backup_vehicle_139818164562688
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
            if (__backup_macroname_139818165428040 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_139818165428040
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }