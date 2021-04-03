# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/templates/header.pynml'
__tokens = {0: ('// define the newgrf\ngrf {\n\tgrfid: "\\41\\4E\\02\\01";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESCRIPTION);\n\tversion: ${repo_vars.repo_version};\n\tmin_compatible_version: 1455;\n\tparam 0 {\n        param_reset_construction_costs {\n            type:    bool;\n            name:    string(STR_PARAM_RESET_CONSTRUCTION_COSTS);\n            desc:    string(STR_PARAM_RESET_CONSTRUCTION_COSTS_DESC);\n            bit: 0;\n            def_value: 1;\n        }\n    }\n\tparam 1 {\n        param_adjust_ship_speed {\n            type:    int;\n            name:    string(STR_PARAM_ADJUST_SHIP_SPEEDS);\n            min_value: 0;\n            max_value: 2;\n            def_value: 1;\n            names: {\n                0: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_0);\n                1: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_1);\n                2: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_2);\n            };\n        }\n    }\n\tparam 2 {\n\t\tparam_roster {\n\t\t\tname: string(STR_PARAM_ROSTER);\n\t\t\tdesc: string(STR_PARAM_ROSTER_DESC);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ${len(registered_rosters)-1};\n\t\t\tnames: {', 1, 0), 128: ('repo_vars.repo_version', 6, 12), 1054: ('len(registered_rosters)-1', 36, 16), 1129: ('registered_rosters', 38, 35), 1170: ('${roster.numeric_id - 1}: string(STR_PARAM_ROSTER_OPTION_${roster.numeric_id - 1});', 39, 20), 1172: ('roster.numeric_id - 1', 39, 22), 1229: ('roster.numeric_id - 1', 39, 79), 1279: ('};\n\t\t}\n\t}\n}\n\n\nbasecost {\n \tPR_RUNNING_SHIP: 2;\n \tPR_BUILD_VEHICLE_SHIP: 2;\n}\n\nif (param_reset_construction_costs) {\n    basecost {\n \t    PR_BUILD_CANAL: -3;\n \t    PR_CLEAR_CANAL: -4;\n        PR_BUILD_AQUEDUCT: -2;\n        PR_CLEAR_AQUEDUCT: -4;\n        PR_BUILD_LOCK: -1;\n        PR_CLEAR_LOCK: -2;\n    }\n}\n\n// sort order\nsort(FEAT_SHIPS, ${[ship.numeric_id for ship in ships]});', 41, 3), 1620: ('[ship.numeric_id for ship in ships]', 64, 19)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

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

            # <Interpolation value=<Substitution '// define the newgrf\ngrf {\n\tgrfid: "\\41\\4E\\02\\01";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESCRIPTION);\n\tversion: ${repo_vars.repo_version};\n\tmin_compatible_version: 1455;\n\tparam 0 {\n        param_reset_construction_costs {\n            type:    bool;\n            name:    string(STR_PARAM_RESET_CONSTRUCTION_COSTS);\n            desc:    string(STR_PARAM_RESET_CONSTRUCTION_COSTS_DESC);\n            bit: 0;\n            def_value: 1;\n        }\n    }\n\tparam 1 {\n        param_adjust_ship_speed {\n            type:    int;\n            name:    string(STR_PARAM_ADJUST_SHIP_SPEEDS);\n            min_value: 0;\n            max_value: 2;\n            def_value: 1;\n            names: {\n                0: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_0);\n                1: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_1);\n                2: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_2);\n            };\n        }\n    }\n\tparam 2 {\n\t\tparam_roster {\n\t\t\tname: string(STR_PARAM_ROSTER);\n\t\t\tdesc: string(STR_PARAM_ROSTER_DESC);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ${len(registered_rosters)-1};\n\t\t\tnames: {\n\t\t\t    ' (1:0)> braces_required=True translation=False at 7f29f418d4e0> -> __content_139818181960344
            __token = 0
            __token = 128
            __content_139818181960344 = _lookup_attr(getitem('repo_vars'), 'repo_version')
            __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
            __token = 1054
            __content_139818181960344_1052 = (len(getitem('registered_rosters')) - 1)
            __content_139818181960344_1052 = __quote(__content_139818181960344_1052, '\x00', '&#0;', None, False)
            __content_139818181960344 = ('%s%s%s%s%s' % ('// define the newgrf\ngrf {\n\tgrfid: "\\41\\4E\\02\\01";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESCRIPTION);\n\tversion: ', (__content_139818181960344 if (__content_139818181960344 is not None) else ''), ';\n\tmin_compatible_version: 1455;\n\tparam 0 {\n        param_reset_construction_costs {\n            type:    bool;\n            name:    string(STR_PARAM_RESET_CONSTRUCTION_COSTS);\n            desc:    string(STR_PARAM_RESET_CONSTRUCTION_COSTS_DESC);\n            bit: 0;\n            def_value: 1;\n        }\n    }\n\tparam 1 {\n        param_adjust_ship_speed {\n            type:    int;\n            name:    string(STR_PARAM_ADJUST_SHIP_SPEEDS);\n            min_value: 0;\n            max_value: 2;\n            def_value: 1;\n            names: {\n                0: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_0);\n                1: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_1);\n                2: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_2);\n            };\n        }\n    }\n\tparam 2 {\n\t\tparam_roster {\n\t\t\tname: string(STR_PARAM_ROSTER);\n\t\t\tdesc: string(STR_PARAM_ROSTER_DESC);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ', (__content_139818181960344_1052 if (__content_139818181960344_1052 is not None) else ''), ';\n\t\t\tnames: {\n\t\t\t    ', ))
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
            __backup_roster_139818190930664 = get('roster', __marker)

            # <Value 'registered_rosters' (38:35)> -> __iterator
            __token = 1129
            __iterator = getitem('registered_rosters')
            (__iterator, ____index_139818165655088, ) = getitem('repeat')('roster', __iterator)
            econtext['roster'] = None
            for __item in __iterator:
                econtext['roster'] = __item

                # <Interpolation value=<Substitution '\n                    ${roster.numeric_id - 1}: string(STR_PARAM_ROSTER_OPTION_${roster.numeric_id - 1});\n\t\t\t    ' (38:55)> braces_required=True translation=False at 7f29f418d668> -> __content_139818181960344
                __token = 1170
                __token = 1172
                __content_139818181960344 = (_lookup_attr(getitem('roster'), 'numeric_id') - 1)
                __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                __token = 1229
                __content_139818181960344_1227 = (_lookup_attr(getitem('roster'), 'numeric_id') - 1)
                __content_139818181960344_1227 = __quote(__content_139818181960344_1227, '\x00', '&#0;', None, False)
                __content_139818181960344 = ('%s%s%s%s%s' % ('\n                    ', (__content_139818181960344 if (__content_139818181960344 is not None) else ''), ': string(STR_PARAM_ROSTER_OPTION_', (__content_139818181960344_1227 if (__content_139818181960344_1227 is not None) else ''), ');\n\t\t\t    ', ))
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
                ____index_139818165655088 -= 1
                if (____index_139818165655088 > 0):
                    __append('')
            if (__backup_roster_139818190930664 is __marker):
                del econtext['roster']
            else:
                econtext['roster'] = __backup_roster_139818190930664

            # <Interpolation value=<Substitution '\n\t\t\t};\n\t\t}\n\t}\n}\n\n\nbasecost {\n \tPR_RUNNING_SHIP: 2;\n \tPR_BUILD_VEHICLE_SHIP: 2;\n}\n\nif (param_reset_construction_costs) {\n    basecost {\n \t    PR_BUILD_CANAL: -3;\n \t    PR_CLEAR_CANAL: -4;\n        PR_BUILD_AQUEDUCT: -2;\n        PR_CLEAR_AQUEDUCT: -4;\n        PR_BUILD_LOCK: -1;\n        PR_CLEAR_LOCK: -2;\n    }\n}\n\n// sort order\nsort(FEAT_SHIPS, ${[ship.numeric_id for ship in ships]});\n' (40:21)> braces_required=True translation=False at 7f29f418d470> -> __content_139818181960344
            __token = 1279
            __token = 1620
            __content_139818181960344 = [_lookup_attr(getitem('ship'), 'numeric_id') for econtext['ship'] in getitem('ships')]
            __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
            __content_139818181960344 = ('%s%s%s' % ('\n\t\t\t};\n\t\t}\n\t}\n}\n\n\nbasecost {\n \tPR_RUNNING_SHIP: 2;\n \tPR_BUILD_VEHICLE_SHIP: 2;\n}\n\nif (param_reset_construction_costs) {\n    basecost {\n \t    PR_BUILD_CANAL: -3;\n \t    PR_CLEAR_CANAL: -4;\n        PR_BUILD_AQUEDUCT: -2;\n        PR_CLEAR_AQUEDUCT: -4;\n        PR_BUILD_LOCK: -1;\n        PR_CLEAR_LOCK: -2;\n    }\n}\n\n// sort order\nsort(FEAT_SHIPS, ', (__content_139818181960344 if (__content_139818181960344 is not None) else ''), ');\n', ))
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
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }