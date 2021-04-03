# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/templates/ship_properties.pynml'
__tokens = {0: ('// -- some switches are common to all vehicles so included with properties -- //\n\n// -- dibble about with purchase menu capacity to handle various cargo-specific capacity issues (cargo might be missing etc) -- //\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_purchase_cargo_capacity, cargo_type_in_veh) {', 1, 0), 241: ('ship.id', 4, 28), 400: ("ship.str_type_info.lower()=='trawler'", 6, 29), 448: ('FISH: return ${ship.capacity_fish_holds};\n        PASS: return ${ship.capacity_pax};', 7, 8), 463: ('ship.capacity_fish_holds', 7, 23), 513: ('ship.capacity_pax', 8, 23), 557: ("return ${ship.default_cargo_capacity};\n}\n\n// -- smoke -- //\nswitch (FEAT_SHIPS, SELF, ${ship.id}_create_visual_effect, ${ship.get_expression_for_effects()}) {\n    return ${len(ship.effects)};\n}\n\n\n// -- props -- //\nitem(FEAT_SHIPS, ${ship.id}, ${ship.numeric_id}) {\n    property {\n        name:                           ${ship.get_name()};\n        climates_available:             NO_CLIMATE; // nml constant\n        sound_effect:                   ${('SOUND_SHIP_HORN','SOUND_FERRY_HORN')[ship.default_cargo=='PASS']};\n        effect_spawn_model:             ${ship.effect_spawn_model};\n        introduction_date:              date(${ship.intro_date},01,01); // ship just supplies intro year - openttd randomises intro dates a bit anyway\n        cargo_capacity:                 ${ship.default_cargo_capacity};\n        sprite_id:                      SPRITE_ID_NEW_SHIP; //enable new graphics - nml constant\n        speed:                          ${ship.speed}mph;\n        ocean_speed_fraction:           ${ship.ocean_speed};\n        canal_speed_fraction:           ${ship.canal_speed};\n        cost_factor:                    ${ship.buy_cost};\n        running_cost_factor:            ${ship.running_cost};\n        refit_cost:                     0; // leave at 0 for refitting without defining cb\n        is_refittable:                  1;\n        refittable_cargo_classes:       bitmask(${ship.refittable_classes});\n        non_refittable_cargo_classes:   bitmask(); // don't set non-refittable classes, increases likelihood of breaking cargo support\n        cargo_allow_refit:              [${ship.get_label_refits_allowed()}];\n        cargo_disallow_refit:           [${ship.get_label_refits_disallowed()}];\n        default_cargo_type:             ${ship.default_cargo};\n        loading_speed:                  ${ship.loading_speed};\n        cargo_age_period:               ${ship.cargo_age_period};\n        misc_flags:                     bitmask(SHIP_FLAG_2CC, SHIP_FLAG_AUTOREFIT); // nml constants\n        model_life:                     ${ship.adjusted_model_life};\n        retire_early:                   ${ship.vehicle_life - 4}; // magic from Eddi\n        reliability_decay:              20; // default value\n        vehicle_life:                   ${ship.vehicle_life};\n    }\n    graphics {\n        speed:                          ${ship.id}_switch_speed_varies_with_load_amount;\n        purchase_speed:                 ${ship.id}_switch_purchase_speed;\n        cargo_capacity:                 ${ship.id}_switch_cargo_capacity;\n        purchase_cargo_capacity:        ${ship.id}_switch_purchase_cargo_capacity;\n        additional_text:                ${ship.get_buy_menu_string()};\n        cargo_subtype_text:             ${ship.id}_switch_cargo_subtype_text;\n        default:                        ${ship.id}_switch_graphics;\n        purchase:                       ${ship.id}_sg_purchase;\n        create_effect:                  ${ship.id}_create_visual_effect;\n    }\n}\n\nif (${ship.get_expression_for_rosters()}) {\n    item(FEAT_SHIPS, ${ship.id}, ${ship.numeric_id}) {\n        property {\n            climates_available:             ALL_CLIMATES;\n        }\n    }\n}\n\n// -- end ${ship.title} --", 10, 4), 566: ('ship.default_cargo_capacity', 10, 13), 645: ('ship.id', 14, 28), 678: ('ship.get_expression_for_effects()', 14, 61), 729: ('len(ship.effects)', 15, 13), 790: ('ship.id', 20, 19), 802: ('ship.numeric_id', 20, 31), 879: ('ship.get_name()', 22, 42), 1007: ("('SOUND_SHIP_HORN','SOUND_FERRY_HORN')[ship.default_cargo=='PASS']", 24, 42), 1118: ('ship.effect_spawn_model', 25, 42), 1191: ('ship.intro_date', 26, 47), 1337: ('ship.default_cargo_capacity', 27, 42), 1506: ('ship.speed', 29, 42), 1564: ('ship.ocean_speed', 30, 42), 1625: ('ship.canal_speed', 31, 42), 1686: ('ship.buy_cost', 32, 42), 1744: ('ship.running_cost', 33, 42), 1948: ('ship.refittable_classes', 36, 50), 2153: ('ship.get_label_refits_allowed()', 38, 43), 2231: ('ship.get_label_refits_disallowed()', 39, 43), 2311: ('ship.default_cargo', 40, 42), 2374: ('ship.loading_speed', 41, 42), 2437: ('ship.cargo_age_period', 42, 42), 2605: ('ship.adjusted_model_life', 44, 42), 2674: ('ship.vehicle_life - 4', 45, 42), 2820: ('ship.vehicle_life', 47, 42), 2903: ('ship.id', 50, 42), 2992: ('ship.id', 51, 42), 3066: ('ship.id', 52, 42), 3140: ('ship.id', 53, 42), 3223: ('ship.get_buy_menu_string()', 54, 42), 3294: ('ship.id', 55, 42), 3372: ('ship.id', 56, 42), 3440: ('ship.id', 57, 42), 3504: ('ship.id', 58, 42), 3550: ('ship.get_expression_for_rosters()', 62, 6), 3611: ('ship.id', 63, 23), 3623: ('ship.numeric_id', 63, 35), 3751: ('ship.title', 70, 12)}

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

            # <Interpolation value=<Substitution '// -- some switches are common to all vehicles so included with properties -- //\n\n// -- dibble about with purchase menu capacity to handle various cargo-specific capacity issues (cargo might be missing etc) -- //\nswitch (FEAT_SHIPS, SELF, ${ship.id}_switch_purchase_cargo_capacity, cargo_type_in_veh) {\n    ' (1:0)> braces_required=True translation=False at 7f29f4098588> -> __content_139818181960344
            __token = 0
            __token = 241
            __content_139818181960344 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
            __content_139818181960344 = ('%s%s%s' % ('// -- some switches are common to all vehicles so included with properties -- //\n\n// -- dibble about with purchase menu capacity to handle various cargo-specific capacity issues (cargo might be missing etc) -- //\nswitch (FEAT_SHIPS, SELF, ', (__content_139818181960344 if (__content_139818181960344 is not None) else ''), '_switch_purchase_cargo_capacity, cargo_type_in_veh) {\n    ', ))
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
            __append('\n    ')

            # <Value "ship.str_type_info.lower()=='trawler'" (6:29)> -> __condition
            __token = 400
            __condition = (_lookup_attr(_lookup_attr(getitem('ship'), 'str_type_info'), 'lower')() == 'trawler')
            if __condition:

                # <Interpolation value=<Substitution '\n        FISH: return ${ship.capacity_fish_holds};\n        PASS: return ${ship.capacity_pax};\n    ' (6:68)> braces_required=True translation=False at 7f29f4187048> -> __content_139818181960344
                __token = 448
                __token = 463
                __content_139818181960344 = _lookup_attr(getitem('ship'), 'capacity_fish_holds')
                __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
                __token = 513
                __content_139818181960344_511 = _lookup_attr(getitem('ship'), 'capacity_pax')
                __content_139818181960344_511 = __quote(__content_139818181960344_511, '\x00', '&#0;', None, False)
                __content_139818181960344 = ('%s%s%s%s%s' % ('\n        FISH: return ', (__content_139818181960344 if (__content_139818181960344 is not None) else ''), ';\n        PASS: return ', (__content_139818181960344_511 if (__content_139818181960344_511 is not None) else ''), ';\n    ', ))
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

            # <Interpolation value=<Substitution "\n    return ${ship.default_cargo_capacity};\n}\n\n// -- smoke -- //\nswitch (FEAT_SHIPS, SELF, ${ship.id}_create_visual_effect, ${ship.get_expression_for_effects()}) {\n    return ${len(ship.effects)};\n}\n\n\n// -- props -- //\nitem(FEAT_SHIPS, ${ship.id}, ${ship.numeric_id}) {\n    property {\n        name:                           ${ship.get_name()};\n        climates_available:             NO_CLIMATE; // nml constant\n        sound_effect:                   ${('SOUND_SHIP_HORN','SOUND_FERRY_HORN')[ship.default_cargo=='PASS']};\n        effect_spawn_model:             ${ship.effect_spawn_model};\n        introduction_date:              date(${ship.intro_date},01,01); // ship just supplies intro year - openttd randomises intro dates a bit anyway\n        cargo_capacity:                 ${ship.default_cargo_capacity};\n        sprite_id:                      SPRITE_ID_NEW_SHIP; //enable new graphics - nml constant\n        speed:                          ${ship.speed}mph;\n        ocean_speed_fraction:           ${ship.ocean_speed};\n        canal_speed_fraction:           ${ship.canal_speed};\n        cost_factor:                    ${ship.buy_cost};\n        running_cost_factor:            ${ship.running_cost};\n        refit_cost:                     0; // leave at 0 for refitting without defining cb\n        is_refittable:                  1;\n        refittable_cargo_classes:       bitmask(${ship.refittable_classes});\n        non_refittable_cargo_classes:   bitmask(); // don't set non-refittable classes, increases likelihood of breaking cargo support\n        cargo_allow_refit:              [${ship.get_label_refits_allowed()}];\n        cargo_disallow_refit:           [${ship.get_label_refits_disallowed()}];\n        default_cargo_type:             ${ship.default_cargo};\n        loading_speed:                  ${ship.loading_speed};\n        cargo_age_period:               ${ship.cargo_age_period};\n        misc_flags:                     bitmask(SHIP_FLAG_2CC, SHIP_FLAG_AUTOREFIT); // nml constants\n        model_life:                     ${ship.adjusted_model_life};\n        retire_early:                   ${ship.vehicle_life - 4}; // magic from Eddi\n        reliability_decay:              20; // default value\n        vehicle_life:                   ${ship.vehicle_life};\n    }\n    graphics {\n        speed:                          ${ship.id}_switch_speed_varies_with_load_amount;\n        purchase_speed:                 ${ship.id}_switch_purchase_speed;\n        cargo_capacity:                 ${ship.id}_switch_cargo_capacity;\n        purchase_cargo_capacity:        ${ship.id}_switch_purchase_cargo_capacity;\n        additional_text:                ${ship.get_buy_menu_string()};\n        cargo_subtype_text:             ${ship.id}_switch_cargo_subtype_text;\n        default:                        ${ship.id}_switch_graphics;\n        purchase:                       ${ship.id}_sg_purchase;\n        create_effect:                  ${ship.id}_create_visual_effect;\n    }\n}\n\nif (${ship.get_expression_for_rosters()}) {\n    item(FEAT_SHIPS, ${ship.id}, ${ship.numeric_id}) {\n        property {\n            climates_available:             ALL_CLIMATES;\n        }\n    }\n}\n\n// -- end ${ship.title} -- " (9:19)> braces_required=True translation=False at 7f29f4098518> -> __content_139818181960344
            __token = 557
            __token = 566
            __content_139818181960344 = _lookup_attr(getitem('ship'), 'default_cargo_capacity')
            __content_139818181960344 = __quote(__content_139818181960344, '\x00', '&#0;', None, False)
            __token = 645
            __content_139818181960344_643 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_643 = __quote(__content_139818181960344_643, '\x00', '&#0;', None, False)
            __token = 678
            __content_139818181960344_676 = _lookup_attr(getitem('ship'), 'get_expression_for_effects')()
            __content_139818181960344_676 = __quote(__content_139818181960344_676, '\x00', '&#0;', None, False)
            __token = 729
            __content_139818181960344_727 = len(_lookup_attr(getitem('ship'), 'effects'))
            __content_139818181960344_727 = __quote(__content_139818181960344_727, '\x00', '&#0;', None, False)
            __token = 790
            __content_139818181960344_788 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_788 = __quote(__content_139818181960344_788, '\x00', '&#0;', None, False)
            __token = 802
            __content_139818181960344_800 = _lookup_attr(getitem('ship'), 'numeric_id')
            __content_139818181960344_800 = __quote(__content_139818181960344_800, '\x00', '&#0;', None, False)
            __token = 879
            __content_139818181960344_877 = _lookup_attr(getitem('ship'), 'get_name')()
            __content_139818181960344_877 = __quote(__content_139818181960344_877, '\x00', '&#0;', None, False)
            __token = 1007
            __content_139818181960344_1005 = ('SOUND_SHIP_HORN', 'SOUND_FERRY_HORN', )[(_lookup_attr(getitem('ship'), 'default_cargo') == 'PASS')]
            __content_139818181960344_1005 = __quote(__content_139818181960344_1005, '\x00', '&#0;', None, False)
            __token = 1118
            __content_139818181960344_1116 = _lookup_attr(getitem('ship'), 'effect_spawn_model')
            __content_139818181960344_1116 = __quote(__content_139818181960344_1116, '\x00', '&#0;', None, False)
            __token = 1191
            __content_139818181960344_1189 = _lookup_attr(getitem('ship'), 'intro_date')
            __content_139818181960344_1189 = __quote(__content_139818181960344_1189, '\x00', '&#0;', None, False)
            __token = 1337
            __content_139818181960344_1335 = _lookup_attr(getitem('ship'), 'default_cargo_capacity')
            __content_139818181960344_1335 = __quote(__content_139818181960344_1335, '\x00', '&#0;', None, False)
            __token = 1506
            __content_139818181960344_1504 = _lookup_attr(getitem('ship'), 'speed')
            __content_139818181960344_1504 = __quote(__content_139818181960344_1504, '\x00', '&#0;', None, False)
            __token = 1564
            __content_139818181960344_1562 = _lookup_attr(getitem('ship'), 'ocean_speed')
            __content_139818181960344_1562 = __quote(__content_139818181960344_1562, '\x00', '&#0;', None, False)
            __token = 1625
            __content_139818181960344_1623 = _lookup_attr(getitem('ship'), 'canal_speed')
            __content_139818181960344_1623 = __quote(__content_139818181960344_1623, '\x00', '&#0;', None, False)
            __token = 1686
            __content_139818181960344_1684 = _lookup_attr(getitem('ship'), 'buy_cost')
            __content_139818181960344_1684 = __quote(__content_139818181960344_1684, '\x00', '&#0;', None, False)
            __token = 1744
            __content_139818181960344_1742 = _lookup_attr(getitem('ship'), 'running_cost')
            __content_139818181960344_1742 = __quote(__content_139818181960344_1742, '\x00', '&#0;', None, False)
            __token = 1948
            __content_139818181960344_1946 = _lookup_attr(getitem('ship'), 'refittable_classes')
            __content_139818181960344_1946 = __quote(__content_139818181960344_1946, '\x00', '&#0;', None, False)
            __token = 2153
            __content_139818181960344_2151 = _lookup_attr(getitem('ship'), 'get_label_refits_allowed')()
            __content_139818181960344_2151 = __quote(__content_139818181960344_2151, '\x00', '&#0;', None, False)
            __token = 2231
            __content_139818181960344_2229 = _lookup_attr(getitem('ship'), 'get_label_refits_disallowed')()
            __content_139818181960344_2229 = __quote(__content_139818181960344_2229, '\x00', '&#0;', None, False)
            __token = 2311
            __content_139818181960344_2309 = _lookup_attr(getitem('ship'), 'default_cargo')
            __content_139818181960344_2309 = __quote(__content_139818181960344_2309, '\x00', '&#0;', None, False)
            __token = 2374
            __content_139818181960344_2372 = _lookup_attr(getitem('ship'), 'loading_speed')
            __content_139818181960344_2372 = __quote(__content_139818181960344_2372, '\x00', '&#0;', None, False)
            __token = 2437
            __content_139818181960344_2435 = _lookup_attr(getitem('ship'), 'cargo_age_period')
            __content_139818181960344_2435 = __quote(__content_139818181960344_2435, '\x00', '&#0;', None, False)
            __token = 2605
            __content_139818181960344_2603 = _lookup_attr(getitem('ship'), 'adjusted_model_life')
            __content_139818181960344_2603 = __quote(__content_139818181960344_2603, '\x00', '&#0;', None, False)
            __token = 2674
            __content_139818181960344_2672 = (_lookup_attr(getitem('ship'), 'vehicle_life') - 4)
            __content_139818181960344_2672 = __quote(__content_139818181960344_2672, '\x00', '&#0;', None, False)
            __token = 2820
            __content_139818181960344_2818 = _lookup_attr(getitem('ship'), 'vehicle_life')
            __content_139818181960344_2818 = __quote(__content_139818181960344_2818, '\x00', '&#0;', None, False)
            __token = 2903
            __content_139818181960344_2901 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2901 = __quote(__content_139818181960344_2901, '\x00', '&#0;', None, False)
            __token = 2992
            __content_139818181960344_2990 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_2990 = __quote(__content_139818181960344_2990, '\x00', '&#0;', None, False)
            __token = 3066
            __content_139818181960344_3064 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3064 = __quote(__content_139818181960344_3064, '\x00', '&#0;', None, False)
            __token = 3140
            __content_139818181960344_3138 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3138 = __quote(__content_139818181960344_3138, '\x00', '&#0;', None, False)
            __token = 3223
            __content_139818181960344_3221 = _lookup_attr(getitem('ship'), 'get_buy_menu_string')()
            __content_139818181960344_3221 = __quote(__content_139818181960344_3221, '\x00', '&#0;', None, False)
            __token = 3294
            __content_139818181960344_3292 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3292 = __quote(__content_139818181960344_3292, '\x00', '&#0;', None, False)
            __token = 3372
            __content_139818181960344_3370 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3370 = __quote(__content_139818181960344_3370, '\x00', '&#0;', None, False)
            __token = 3440
            __content_139818181960344_3438 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3438 = __quote(__content_139818181960344_3438, '\x00', '&#0;', None, False)
            __token = 3504
            __content_139818181960344_3502 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3502 = __quote(__content_139818181960344_3502, '\x00', '&#0;', None, False)
            __token = 3550
            __content_139818181960344_3548 = _lookup_attr(getitem('ship'), 'get_expression_for_rosters')()
            __content_139818181960344_3548 = __quote(__content_139818181960344_3548, '\x00', '&#0;', None, False)
            __token = 3611
            __content_139818181960344_3609 = _lookup_attr(getitem('ship'), 'id')
            __content_139818181960344_3609 = __quote(__content_139818181960344_3609, '\x00', '&#0;', None, False)
            __token = 3623
            __content_139818181960344_3621 = _lookup_attr(getitem('ship'), 'numeric_id')
            __content_139818181960344_3621 = __quote(__content_139818181960344_3621, '\x00', '&#0;', None, False)
            __token = 3751
            __content_139818181960344_3749 = _lookup_attr(getitem('ship'), 'title')
            __content_139818181960344_3749 = __quote(__content_139818181960344_3749, '\x00', '&#0;', None, False)
            __content_139818181960344 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    return ', (__content_139818181960344 if (__content_139818181960344 is not None) else ''), ';\n}\n\n// -- smoke -- //\nswitch (FEAT_SHIPS, SELF, ', (__content_139818181960344_643 if (__content_139818181960344_643 is not None) else ''), '_create_visual_effect, ', (__content_139818181960344_676 if (__content_139818181960344_676 is not None) else ''), ') {\n    return ', (__content_139818181960344_727 if (__content_139818181960344_727 is not None) else ''), ';\n}\n\n\n// -- props -- //\nitem(FEAT_SHIPS, ', (__content_139818181960344_788 if (__content_139818181960344_788 is not None) else ''), ', ', (__content_139818181960344_800 if (__content_139818181960344_800 is not None) else ''), ') {\n    property {\n        name:                           ', (__content_139818181960344_877 if (__content_139818181960344_877 is not None) else ''), ';\n        climates_available:             NO_CLIMATE; // nml constant\n        sound_effect:                   ', (__content_139818181960344_1005 if (__content_139818181960344_1005 is not None) else ''), ';\n        effect_spawn_model:             ', (__content_139818181960344_1116 if (__content_139818181960344_1116 is not None) else ''), ';\n        introduction_date:              date(', (__content_139818181960344_1189 if (__content_139818181960344_1189 is not None) else ''), ',01,01); // ship just supplies intro year - openttd randomises intro dates a bit anyway\n        cargo_capacity:                 ', (__content_139818181960344_1335 if (__content_139818181960344_1335 is not None) else ''), ';\n        sprite_id:                      SPRITE_ID_NEW_SHIP; //enable new graphics - nml constant\n        speed:                          ', (__content_139818181960344_1504 if (__content_139818181960344_1504 is not None) else ''), 'mph;\n        ocean_speed_fraction:           ', (__content_139818181960344_1562 if (__content_139818181960344_1562 is not None) else ''), ';\n        canal_speed_fraction:           ', (__content_139818181960344_1623 if (__content_139818181960344_1623 is not None) else ''), ';\n        cost_factor:                    ', (__content_139818181960344_1684 if (__content_139818181960344_1684 is not None) else ''), ';\n        running_cost_factor:            ', (__content_139818181960344_1742 if (__content_139818181960344_1742 is not None) else ''), ';\n        refit_cost:                     0; // leave at 0 for refitting without defining cb\n        is_refittable:                  1;\n        refittable_cargo_classes:       bitmask(', (__content_139818181960344_1946 if (__content_139818181960344_1946 is not None) else ''), ");\n        non_refittable_cargo_classes:   bitmask(); // don't set non-refittable classes, increases likelihood of breaking cargo support\n        cargo_allow_refit:              [", (__content_139818181960344_2151 if (__content_139818181960344_2151 is not None) else ''), '];\n        cargo_disallow_refit:           [', (__content_139818181960344_2229 if (__content_139818181960344_2229 is not None) else ''), '];\n        default_cargo_type:             ', (__content_139818181960344_2309 if (__content_139818181960344_2309 is not None) else ''), ';\n        loading_speed:                  ', (__content_139818181960344_2372 if (__content_139818181960344_2372 is not None) else ''), ';\n        cargo_age_period:               ', (__content_139818181960344_2435 if (__content_139818181960344_2435 is not None) else ''), ';\n        misc_flags:                     bitmask(SHIP_FLAG_2CC, SHIP_FLAG_AUTOREFIT); // nml constants\n        model_life:                     ', (__content_139818181960344_2603 if (__content_139818181960344_2603 is not None) else ''), ';\n        retire_early:                   ', (__content_139818181960344_2672 if (__content_139818181960344_2672 is not None) else ''), '; // magic from Eddi\n        reliability_decay:              20; // default value\n        vehicle_life:                   ', (__content_139818181960344_2818 if (__content_139818181960344_2818 is not None) else ''), ';\n    }\n    graphics {\n        speed:                          ', (__content_139818181960344_2901 if (__content_139818181960344_2901 is not None) else ''), '_switch_speed_varies_with_load_amount;\n        purchase_speed:                 ', (__content_139818181960344_2990 if (__content_139818181960344_2990 is not None) else ''), '_switch_purchase_speed;\n        cargo_capacity:                 ', (__content_139818181960344_3064 if (__content_139818181960344_3064 is not None) else ''), '_switch_cargo_capacity;\n        purchase_cargo_capacity:        ', (__content_139818181960344_3138 if (__content_139818181960344_3138 is not None) else ''), '_switch_purchase_cargo_capacity;\n        additional_text:                ', (__content_139818181960344_3221 if (__content_139818181960344_3221 is not None) else ''), ';\n        cargo_subtype_text:             ', (__content_139818181960344_3292 if (__content_139818181960344_3292 is not None) else ''), '_switch_cargo_subtype_text;\n        default:                        ', (__content_139818181960344_3370 if (__content_139818181960344_3370 is not None) else ''), '_switch_graphics;\n        purchase:                       ', (__content_139818181960344_3438 if (__content_139818181960344_3438 is not None) else ''), '_sg_purchase;\n        create_effect:                  ', (__content_139818181960344_3502 if (__content_139818181960344_3502 is not None) else ''), '_create_visual_effect;\n    }\n}\n\nif (', (__content_139818181960344_3548 if (__content_139818181960344_3548 is not None) else ''), ') {\n    item(FEAT_SHIPS, ', (__content_139818181960344_3609 if (__content_139818181960344_3609 is not None) else ''), ', ', (__content_139818181960344_3621 if (__content_139818181960344_3621 is not None) else ''), ') {\n        property {\n            climates_available:             ALL_CLIMATES;\n        }\n    }\n}\n\n// -- end ', (__content_139818181960344_3749 if (__content_139818181960344_3749 is not None) else ''), ' -- ', ))
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
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }