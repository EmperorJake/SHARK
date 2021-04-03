# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/shark/src/docs_templates/changelog.pt'
__tokens = {}

from sys import exc_info as _exc_info

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
            __append("Changelog\n=========\n\n-----\n2.0.3\n-----\n\n*Translations*\n\n- translator credits: http://bundles.openttdcoop.org/fish/push/LATEST/credits.txt\n\n\n-----\n2.0.2\n-----\n\n*Fixes*\n\n- Little Cumbrae Freighter and Frisco Bay Freighter sometimes hidden due to incorrect setting of replacement_id property\n\n*Language Updates*\n\n- italian\n- translator credits: http://bundles.openttdcoop.org/fish/push/LATEST/credits.txt\n\n*Docs*\n\n- update to Bootstrap 3 framework\n- include Font Awesome for resolution-independent icons\n\n-----\n2.0.1\n-----\n\n*Language Updates*\n\n- Polish\n- Italian\n- German\n\n*Codechanges*\n\n- compile now uses python 3 not python 2\n- compile now requires nml 0.4.0 or newer\n- refactored compile scripts, keeping pyflakes happy, and not relying on weird magic related to python imports\n\n-----\n2.0.0\n-----\n\n*Changes / Features*\n\n- it's 2.0.0 (Squid Ate FISH)\n\n*Fixes*\n\n- sorted out spritesheets for hovercraft, now correctly positioned and not clipping\n- fixed a bug with Fish Island trawler being 1px too high when loaded\n\n\n-------------------\nRelease Candidate 9\n-------------------\n\n*Changes / Features*\n\n- Provence Edibles Tanker\n- Sprites by Pikka for Nanaimo and Pegwell hovercraft (known to need some tweaks)\n- First ships available 1860 (instead of 1870) to match Iron Horse and Road Hog\n\n*Language Updates*\n\n- Afrikaans (telanus)\n- Catalan (juanjo)\n- Croatian (Voyager1)\n- Dutch (Alberth)\n- Finnish (Arexander)\n- French (Arikover)\n- Korean KR (kevin)\n- Portugese (vesgo)\n- Russian (aantano)\n- Scots Gaelic (GunChleoc)\n- Spanish (SilverSurferZzZ)\n\n-------------------\nRelease Candidate 8\n-------------------\n\n*Changes / Features*\n\n- Adjust costs for some of the smaller ships\n- Improved sprites for Eddystone Tanker\n\n-------------------\nRelease Candidate 7\n-------------------\n\n*Fixes*\n\n- Cap max ship speed to 79mph at compile time (to prevent overflow to negative)\n- Some buy / run costs were wrong\n\n-------------------\nRelease Candidate 6\n-------------------\n\n*Fixes*\n\n- Removed red pixel on Little Cumbrae Freighter\n- Remove unwanted space between ship names and type string\n\n-------------------\nRelease Candidate 5\n-------------------\n\n*Fixes*\n\n- Nanaimo 70 hovercraft speed was too high, causing it to travel too slowly (speed values above 79mph overflow to negative)\n\n-------------------\nRelease Candidate 4\n-------------------\n\n*Features*\n\n- smoke for most ships, requires OpenTTD nightly version r26747 or newer\n\n*Fixes*\n\n- lighting was wrong on Cadiz Freighter, also fixed offsets\n- offsets for Fastnet Paddle Steamer, Altamira Freighter, Little Cumbrae Freighter, Hopetown Tanker\n\n*Language Updates*\n\n- Dutch (Alberth)\n\n-------------------\nRelease Candidate 3\n-------------------\n\n*Features*\n\n- correct-sized sprites for Cadiz Freighter\n\n*Fixes*\n\n- offsets for Frisco Bay Freighter\n\n\n-------------------\nRelease Candidate 2\n-------------------\n\n*Fixes*\n\n- Hovercraft now have proper names\n- Castle Point Steamer: fixed offsets, added wake sprites, removed bad pixel\n\n*Language Updates*\n\n- Catalan (juanjo)\n- Scots Gaelic (GunChleoc)\n\n\n-------------------\nRelease Candidate 1\n-------------------\n\n*New Features / Changes*\n\n- remove parameter for turning Sea / River ships on / off\n- introduce Rosters (work in progress): choose one set of ships from a range of options\n- only one roster available in 0.1: This Sceptred Isle, a British-ish set of ships\n- some ships removed\n- some new ships added\n- river ships no longer have a speed penalty on open sea, for gameplay balance\n- adjust speeds, capacities and intro dates for gameplay balance\n- remove some confusing graphic variations\n- remove smoke from all ships, present in alphas as a test only, may return in future\n\n*Language Updates*\n\n- Afrikaans (telanus)\n- Catalan (juanjo)\n- Croatian (Voyager1)\n- Dutch (foobar)\n- Finnish (Arexander)\n- French (Arikover)\n- Korean KR (kevin, konlee0518)\n- German (Planetmaker)\n- Polish (ciekma)\n- Russian (George)\n- Scots Gaelic (GunChleoc)\n- Spanish (SilverSurferZzZ)\n\n\n-------\nAlpha 5\n-------\n\n*New Features / Changes*\n\n- cargo aging bonus for livestock cargo when using Livestock ship  (50% of normal cargo decay rate)\n\n*Language Updates*\n\n- Croatian (Voyager1)\n- German (Planetmaker)\n- Spanish (SilverSurferZzZ)\n\n-------\nAlpha 4\n-------\n\n*New Features / Changes*\n\n- rebalanced Mount Blaze cat, reducing some stats overkill\n- Enoshima Ferry now river capable\n- Autorefit info in buy menu\n\n*Fixes*\n\n- correct buy menu sprites for Saint Marie Barge Tug\n\n*Language Updates*\n\n- Russian (George)\n- Spanish (SilverSurferZzZ)\n\n-------\nAlpha 3\n-------\n\n*New Features / Changes*\n\n- updated sprites for Little Cumbrae Freighter, including generation 2 variant from 1920 (Coxx)\n\n*Fixes*\n\n- correct offsets and provide missing sprites for Saint Marie Barge Tug\n\n*Language Updates*\n\n- Croatian (Voyager1)\n- Dutch (Alberth)\n- Finnish (juzza1)\n- Hungarian (zaza)\n- Norwegian (Trond)\n- Russion (George)\n- Spanish (SilverSurferZzZ)\n\n-------\nAlpha 2\n-------\n\n**Not savegame compatible with Alpha 1 (ship IDs changed).**\n\n*New Features / Changes*\n\n- create two groups of ships: Sea Ships and River Boats, which can be turned on/off by parameter\n- provide a basic group of river boats (unfinished)\n    - most river boats have reduced performance at sea\n    - added Geneva and Constance (large freight barges) and Dieze Container Carrier (offsets known to be wrong)\n- Saint Marie tug now 200t capacity (offsets known to be wrong)\n- introduce Cadiz and Meteor freighters and shuffle other freighter dates and capacities for gameplay balance\n- reduce canal / river speed of the faster sea freighters for gameplay balance\n- Barletta Paddle Steamer now available from 1870, not 1878\n\n*Fixes*\n\n- Grindavik Reefer\n    - improved sprites (DanMacK)\n    - spritesheet missing rows\n    - removed flashing pixels\n- remove white pixel from Little Cumbrae Freigher\n\n*Language Updates*\n\n- Hungarian (zaza)\n- Norwegian (Trond)\n\n-------\nAlpha 1\n-------\n\nFirst release for testing\n")
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }