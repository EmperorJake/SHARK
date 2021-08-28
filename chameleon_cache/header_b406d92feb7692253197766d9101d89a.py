# -*- coding: utf-8 -*-
__filename = '/mnt/c/Users/Jakob/Games/GitHub/SHARK/src/templates/header.pynml'

__tokens = {0: ('// define the newgrf\ngrf {\n\tgrfid: "\\41\\4E\\02\\01";\n//\tgrfid: "\\4A\\44\\BB\\B1";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESCRIPTION);\n\tversion: ${repo_vars.repo_version};\n\tmin_compatible_version: 1702;\n\tparam 0 {\n        param_reset_construction_costs {\n            type:    bool;\n            name:    string(STR_PARAM_RESET_CONSTRUCTION_COSTS);\n            desc:    string(STR_PARAM_RESET_CONSTRUCTION_COSTS_DESC);\n            bit: 0;\n            def_value: 1;\n        }\n    }\n\tparam 1 {\n        param_adjust_ship_speed {\n            type:    int;\n            name:    string(STR_PARAM_ADJUST_SHIP_SPEEDS);\n            min_value: 0;\n            max_value: 2;\n            def_value: 1;\n            names: {\n                0: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_0);\n                1: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_1);\n                2: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_2);\n            };\n        }\n    }\n\tparam 2 {\n\t\tparam_roster {\n\t\t\tname: string(STR_PARAM_ROSTER);\n\t\t\tdesc: string(STR_PARAM_ROSTER_DESC);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ${len(registered_rosters)-1};\n\t\t\tnames: {', 1, 0), 154: ('repo_vars.repo_version', 7, 12), 1080: ('len(registered_rosters)-1', 37, 16), 1155: ('registered_rosters', 39, 35), 1196: ('${roster.numeric_id - 1}: string(STR_PARAM_ROSTER_OPTION_${roster.numeric_id - 1});', 40, 20), 1198: ('roster.numeric_id - 1', 40, 22), 1255: ('roster.numeric_id - 1', 40, 79), 1305: ('};\n\t\t}\n\t}\n}\n\n\nbasecost {\n \tPR_RUNNING_SHIP: 2;\n \tPR_BUILD_VEHICLE_SHIP: 2;\n}\n\nif (param_reset_construction_costs) {\n    basecost {\n \t    PR_BUILD_CANAL: -3;\n \t    PR_CLEAR_CANAL: -4;\n        PR_BUILD_AQUEDUCT: -2;\n        PR_CLEAR_AQUEDUCT: -4;\n        PR_BUILD_LOCK: -1;\n        PR_CLEAR_LOCK: -2;\n    }\n}\n\n// sort order\nsort(FEAT_SHIPS, ${[ship.numeric_id for ship in ships]});', 42, 3), 1646: ('[ship.numeric_id for ship in ships]', 65, 19)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

_static_139736649140784 = {}

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

            # <Interpolation value=<Substitution '// define the newgrf\ngrf {\n\tgrfid: "\\41\\4E\\02\\01";\n//\tgrfid: "\\4A\\44\\BB\\B1";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESCRIPTION);\n\tversion: ${repo_vars.repo_version};\n\tmin_compatible_version: 1702;\n\tparam 0 {\n        param_reset_construction_costs {\n            type:    bool;\n            name:    string(STR_PARAM_RESET_CONSTRUCTION_COSTS);\n            desc:    string(STR_PARAM_RESET_CONSTRUCTION_COSTS_DESC);\n            bit: 0;\n            def_value: 1;\n        }\n    }\n\tparam 1 {\n        param_adjust_ship_speed {\n            type:    int;\n            name:    string(STR_PARAM_ADJUST_SHIP_SPEEDS);\n            min_value: 0;\n            max_value: 2;\n            def_value: 1;\n            names: {\n                0: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_0);\n                1: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_1);\n                2: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_2);\n            };\n        }\n    }\n\tparam 2 {\n\t\tparam_roster {\n\t\t\tname: string(STR_PARAM_ROSTER);\n\t\t\tdesc: string(STR_PARAM_ROSTER_DESC);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ${len(registered_rosters)-1};\n\t\t\tnames: {\n\t\t\t    ' (1:0)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f16f94be4f0> -> __content_139736654094960
            __token = 0
            __token = 154
            __content_139736654094960 = _lookup_attr(getitem('repo_vars'), 'repo_version')
            __content_139736654094960 = __quote(__content_139736654094960, '\x00', '&#0;', None, None)
            __token = 1080
            __content_139736654094960_1078 = (len(getitem('registered_rosters')) - 1)
            __content_139736654094960_1078 = __quote(__content_139736654094960_1078, '\x00', '&#0;', None, None)
            __content_139736654094960 = ('%s%s%s%s%s' % ('// define the newgrf\ngrf {\n\tgrfid: "\\41\\4E\\02\\01";\n//\tgrfid: "\\4A\\44\\BB\\B1";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESCRIPTION);\n\tversion: ', (__content_139736654094960 if (__content_139736654094960 is not None) else ''), ';\n\tmin_compatible_version: 1702;\n\tparam 0 {\n        param_reset_construction_costs {\n            type:    bool;\n            name:    string(STR_PARAM_RESET_CONSTRUCTION_COSTS);\n            desc:    string(STR_PARAM_RESET_CONSTRUCTION_COSTS_DESC);\n            bit: 0;\n            def_value: 1;\n        }\n    }\n\tparam 1 {\n        param_adjust_ship_speed {\n            type:    int;\n            name:    string(STR_PARAM_ADJUST_SHIP_SPEEDS);\n            min_value: 0;\n            max_value: 2;\n            def_value: 1;\n            names: {\n                0: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_0);\n                1: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_1);\n                2: string(STR_PARAM_ADJUST_SHIP_SPEEDS_OPTION_2);\n            };\n        }\n    }\n\tparam 2 {\n\t\tparam_roster {\n\t\t\tname: string(STR_PARAM_ROSTER);\n\t\t\tdesc: string(STR_PARAM_ROSTER_DESC);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ', (__content_139736654094960_1078 if (__content_139736654094960_1078 is not None) else ''), ';\n\t\t\tnames: {\n\t\t\t    ', ))
            if (__content_139736654094960 is None):
                pass
            else:
                if (__content_139736654094960 is None):
                    __content_139736654094960 = None
                else:
                    __tt = type(__content_139736654094960)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139736654094960 = str(__content_139736654094960)
                    else:
                        if (__tt is bytes):
                            __content_139736654094960 = decode(__content_139736654094960)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139736654094960 = __content_139736654094960.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139736654094960)
                                    __content_139736654094960 = (str(__content_139736654094960) if (__content_139736654094960 is __converted) else __converted)
                                else:
                                    __content_139736654094960 = __content_139736654094960()
            if (__content_139736654094960 is not None):
                __append(__content_139736654094960)

            # <Static value=<_ast.Dict object at 0x7f16f9558a30> name=None at 7f16f9558970> -> __attrs_139736648509280
            __attrs_139736648509280 = _static_139736649140784
            __backup_roster_139736660706592 = get('roster', __marker)

            # <Value 'registered_rosters' (39:35)> -> __iterator
            __token = 1155
            __iterator = getitem('registered_rosters')
            (__iterator, ____index_139736648509520, ) = getitem('repeat')('roster', __iterator)
            econtext['roster'] = None
            for __item in __iterator:
                econtext['roster'] = __item

                # <Interpolation value=<Substitution '\n                    ${roster.numeric_id - 1}: string(STR_PARAM_ROSTER_OPTION_${roster.numeric_id - 1});\n\t\t\t    ' (39:55)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f16f94be9a0> -> __content_139736654094960
                __token = 1196
                __token = 1198
                __content_139736654094960 = (_lookup_attr(getitem('roster'), 'numeric_id') - 1)
                __content_139736654094960 = __quote(__content_139736654094960, '\x00', '&#0;', None, None)
                __token = 1255
                __content_139736654094960_1253 = (_lookup_attr(getitem('roster'), 'numeric_id') - 1)
                __content_139736654094960_1253 = __quote(__content_139736654094960_1253, '\x00', '&#0;', None, None)
                __content_139736654094960 = ('%s%s%s%s%s' % ('\n                    ', (__content_139736654094960 if (__content_139736654094960 is not None) else ''), ': string(STR_PARAM_ROSTER_OPTION_', (__content_139736654094960_1253 if (__content_139736654094960_1253 is not None) else ''), ');\n\t\t\t    ', ))
                if (__content_139736654094960 is None):
                    pass
                else:
                    if (__content_139736654094960 is None):
                        __content_139736654094960 = None
                    else:
                        __tt = type(__content_139736654094960)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_139736654094960 = str(__content_139736654094960)
                        else:
                            if (__tt is bytes):
                                __content_139736654094960 = decode(__content_139736654094960)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_139736654094960 = __content_139736654094960.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_139736654094960)
                                        __content_139736654094960 = (str(__content_139736654094960) if (__content_139736654094960 is __converted) else __converted)
                                    else:
                                        __content_139736654094960 = __content_139736654094960()
                if (__content_139736654094960 is not None):
                    __append(__content_139736654094960)
                ____index_139736648509520 -= 1
                if (____index_139736648509520 > 0):
                    __append('')
            if (__backup_roster_139736660706592 is __marker):
                del econtext['roster']
            else:
                econtext['roster'] = __backup_roster_139736660706592

            # <Interpolation value=<Substitution '\n\t\t\t};\n\t\t}\n\t}\n}\n\n\nbasecost {\n \tPR_RUNNING_SHIP: 2;\n \tPR_BUILD_VEHICLE_SHIP: 2;\n}\n\nif (param_reset_construction_costs) {\n    basecost {\n \t    PR_BUILD_CANAL: -3;\n \t    PR_CLEAR_CANAL: -4;\n        PR_BUILD_AQUEDUCT: -2;\n        PR_CLEAR_AQUEDUCT: -4;\n        PR_BUILD_LOCK: -1;\n        PR_CLEAR_LOCK: -2;\n    }\n}\n\n// sort order\nsort(FEAT_SHIPS, ${[ship.numeric_id for ship in ships]});\n' (41:21)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f16f94be550> -> __content_139736654094960
            __token = 1305
            __token = 1646
            __content_139736654094960 = [_lookup_attr(getitem('ship'), 'numeric_id') for econtext['ship'] in getitem('ships')]
            __content_139736654094960 = __quote(__content_139736654094960, '\x00', '&#0;', None, None)
            __content_139736654094960 = ('%s%s%s' % ('\n\t\t\t};\n\t\t}\n\t}\n}\n\n\nbasecost {\n \tPR_RUNNING_SHIP: 2;\n \tPR_BUILD_VEHICLE_SHIP: 2;\n}\n\nif (param_reset_construction_costs) {\n    basecost {\n \t    PR_BUILD_CANAL: -3;\n \t    PR_CLEAR_CANAL: -4;\n        PR_BUILD_AQUEDUCT: -2;\n        PR_CLEAR_AQUEDUCT: -4;\n        PR_BUILD_LOCK: -1;\n        PR_CLEAR_LOCK: -2;\n    }\n}\n\n// sort order\nsort(FEAT_SHIPS, ', (__content_139736654094960 if (__content_139736654094960 is not None) else ''), ');\n', ))
            if (__content_139736654094960 is None):
                pass
            else:
                if (__content_139736654094960 is None):
                    __content_139736654094960 = None
                else:
                    __tt = type(__content_139736654094960)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_139736654094960 = str(__content_139736654094960)
                    else:
                        if (__tt is bytes):
                            __content_139736654094960 = decode(__content_139736654094960)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_139736654094960 = __content_139736654094960.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_139736654094960)
                                    __content_139736654094960 = (str(__content_139736654094960) if (__content_139736654094960 is __converted) else __converted)
                                else:
                                    __content_139736654094960 = __content_139736654094960()
            if (__content_139736654094960 is not None):
                __append(__content_139736654094960)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }